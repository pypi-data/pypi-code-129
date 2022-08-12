import numpy as np
from taurex.model import ForwardModel
from taurex.model import SimpleForwardModel
# from .simplemodel import SimpleForwardModel
from taurex.core import fitparam
from taurex.util.math import *
from taurex_2d.util.math import *
from taurex.constants import *
from taurex.log import Logger

class Transmission2DModel(SimpleForwardModel, ForwardModel):
    """
    Model using 2D information. This model should be used with a 2D pressure and temperature profiles (see :class:`~taurex.data.profiles.pressure.pressure2Dprofile.Pressure2DProfile`, :class:`~taurex.data.profiles.temperature.temperature2D.Temperature2D`).
    2D gases may also be used, in which case you should set the chemistry to be
    :class:`~taurex.data.profiles.chemistry.chemistry2D.Chemistry2D`.

    Parameters
    ----------
    planet: :obj:`Planet` or :obj:`None`
        Planet object created or None to use the default planet (Jupiter)

    nslices : int
        Number of slices between day and night, each covering an angle of beta/(nslices-2), plus the day and the night slices

    beta : float
        Transition angle (in degrees) between day and night (with a linear interpolation between -beta/2 and beta/2)

    p_iso : float
        Pression threshold over which temperature is considered isothermal
    """
    def __init__(self,
                 planet=None,
                 star=None,
                 pressure_profile=None,
                 temperature_profile=None,
                 chemistry=None,
                 nlayers=100,
                 atm_min_pressure=1e-4,
                 atm_max_pressure=1e6,
                 z_discretization=True,
                 nslices = 20,
                 beta = 30,
                 p_iso = 1e3
                 ):

        Logger.__init__(self, self.__class__.__name__)
        if beta == 0 and nslices > 2:
            self.warning("beta = 0 so we will only use 2 slices (for day and for night")
            nslices = 2
        if nslices < 2:
            self.warning("Minimum number of slices is 2, for day and night (given %d)"%nslices)
            nslices = 2
        if nslices == 2 and beta != 0:
            self.warning("Number of slices is 2, but beta is not zero. Setting beta to zero")
            beta = 0

        self._nslices = int(nslices)
        self.z_discretization = z_discretization
        """Use altitude to choose vertical points. If false, use pressure (original TauREx behavior)."""

        self._beta = beta # cover the whole angle
        self._p_iso = p_iso
        super().__init__(self.__class__.__name__, planet,
                         star,
                         pressure_profile,
                         temperature_profile,
                         chemistry,
                         nlayers,
                         atm_min_pressure,
                         atm_max_pressure)

    @property
    def alpha(self):
        return 0 if (self._beta == 0) else self._beta/(self._nslices-2)  # angle of slices in the transition, so do not count day and night slices

    @fitparam(param_name='nslices',param_latex='$N_{slices}$',default_fit=False,default_bounds=[2, 100])
    def nslices(self):
        """Transition angle between day and night"""
        return self._nslices

    @nslices.setter
    def nslices(self,value):
        self._nslices = value
        self._pressure_profile.nslices = value
        self._temperature_profile.nslices = value

    @fitparam(param_name='beta',param_latex=r'$\beta$',default_fit=False,default_bounds=[0.0,90.0])
    def beta(self):
        """Transition angle between day and night"""
        return self._beta

    @beta.setter
    def beta(self,value):
        self._beta = value
        self._pressure_profile.beta = value
        self._temperature_profile.beta = value

    @fitparam(param_name='p_iso',param_latex='$P_{iso}$',default_mode='log',default_fit=False,default_bounds=[0.1,1.0])
    def p_iso(self):
        """Pressure threshold over which temperature is considered isothermal"""
        return self._p_iso

    @p_iso.setter
    def p_iso(self,value):
        self._p_iso = value
        self._pressure_profile.p_iso = value
        self._temperature_profile.p_iso = value
        self.chemistry.p_iso = value

    def _compute_inital_mu(self):
        # af: TODO get rid of this?
        from taurex_2d.data.profiles.chemistry import Chemistry2D, Gas2D
        tc = Chemistry2D()
        tc.addGas(Gas2D('H2O'))
        self._inital_mu = tc

    def _setup_defaults(self,nlayers,atm_min_pressure,atm_max_pressure):
        if self._pressure_profile is None:
            from taurex_2d.data.profiles.pressure import Pressure2DProfile
            self.info('No pressure profile defined, using simple pressure profile with')
            self.info('parameters nlayers: %s, atm_pressure_range=(%s,%s)',nlayers,atm_min_pressure,atm_max_pressure)
            self._pressure_profile = Pressure2DProfile(nlayers,atm_min_pressure,atm_max_pressure)

        if self._planet is None:
            from taurex.data import Planet
            self.warning('No planet defined, using Jupiter as planet')
            self._planet = Planet()

        if self._temperature_profile is None:
            from taurex_2d.data.profiles.temperature import Temperature2D
            self.warning('No temperature profile defined: using default 2D profile with Tday=1500K, Tnight=300K')
            self._temperature_profile = Temperature2D()

        # Get model attributes and copy them to pressure and temperature profiles
        self.p_iso = self.p_iso
        self.beta = self.beta
        self.nslices = self.nslices

        if self._chemistry is None:
            from taurex_2d.data.profiles.chemistry import Chemistry2D,Gas2D
            tc = Chemistry2D()
            self.warning('No gas profile set, using constant profile with H2O and CH4')
            tc.addGas(Gas2D('H2O',mix_ratio=1e-5))
            tc.addGas(Gas2D('CH4',mix_ratio=1e-6))
            self._chemistry = tc

        if self._star is None:
            from taurex.data.stellar import BlackbodyStar
            self.warning('No star, using the Sun')
            self._star = BlackbodyStar()

    def initialize_profiles(self):
        self.info('Computing pressure profile')

        self.pressure.compute_pressure_profile(self.nslices, self.beta)

        self._temperature_profile.initialize_profile(self._planet,
                    self.pressure.nLayers,
                    self.pressure.profile)

        #Initialize the atmosphere with a constant gas profile
        if self._initialized is False:
            self._inital_mu.initialize_chemistry(self.pressure.nLayers,
                                                self.temperatureProfile,self.pressureProfile,
                                                None, self)
            # self._inital_mu.muProfile = np.zeros((self.nslices,self._nlayers))
            self.compute_altitude_gravity_scaleheight_profile_P(self._inital_mu.muProfile)
            self._initialized=True

        #Now initialize the gas profile using pressure grid
        self._chemistry.initialize_chemistry(self.pressure.nLayers,
                                                self.temperatureProfile,self.pressureProfile,
                                                self.altitude_profile)

        #Compute gravity scale height
        self.compute_altitude_gravity_scaleheight_profile_P()

        self.generate_polar_grid()

        if hasattr(self.pressure, "custom_pressure"):
            print("custom pressure")
        else:
            self.interpolate_profiles_polar_coordinates()
            self.compute_pressure()

        #Now initialize the gas profile using altitude grid
        self._chemistry.initialize_chemistry(self.pressure.nLayers,
                                                self.temperatureProfile,self.pressureProfile,
                                                self.altitude_profile)

    def compute_altitude_gravity_scaleheight_profile_P(self,mu_profile=None):
        """
        Compute z, H and g coordinates on (alpha, P) grid
        """
        from taurex.constants import KBOLTZ
        if mu_profile is None:
            mu_profile=self._chemistry.muProfile

        # build the altitude profile from the bottom up
        nlayers = self.pressure.nLayers
        H = np.zeros((self.nslices, nlayers))
        g = np.zeros((self.nslices, nlayers))
        z = np.zeros((self.nslices, nlayers+1))

        g[:,0] = self._planet.gravity # surface gravity (0th layer)
        H[:,0] = (KBOLTZ*self.temperatureProfile[:,0])/(mu_profile[:,0]*g[:,0]) # scaleheight at the surface (0th layer)

        for i in range(1, nlayers+1):
            deltaz = (-1.)*H[:, i-1]*np.log(self.pressure.pressure_profile_levels[i]/self.pressure.pressure_profile_levels[i-1])
            z[:,i] = z[:,i-1] + deltaz # altitude at the i-th layer

            if i == nlayers:
                break
            with np.errstate(over='ignore'):
                g[:,i] = self._planet.gravity_at_height(z[:,i]) # gravity at the i-th layer
            with np.errstate(divide='ignore'):
                H[:,i] = (KBOLTZ*self.temperatureProfile[:,i])/(mu_profile[:,i]*g[:,i])

        self.altitude_P = z
        self.scaleheight_P = H
        self.gravity_P = g

    def generate_polar_grid(self,mu_profile=None):
        """
        Take day side as the new 'polar' (alpha, z) coordinate system
        """
        if self.z_discretization:
            self.altitude_profile = np.linspace(0,self.altitude_P.max(), self.nLayers+1)
        else:
            self.altitude_profile = self.altitude_P[int(self.altitude_P.argmax() / (self.nLayers+1))]
        self.dz = np.diff(self.altitudeProfile)
        self.altitude_layers = self.altitude_profile[:-1] + self.dz/2 # middle of layers
        # copy day side scaleheight and gravity (useless?)
        self.scaleheight_profile = self.scaleheight_P[-1]
        self.gravity_profile = self.gravity_P[-1]

    def interpolate_profiles_polar_coordinates(self):
        """
            Interpolate P,T profiles into the polar grid (alpha, z).
            This function rewrites on top of the old P,T profiles but
            makes a copy renamed pressure_P and temperature_P beforehand
        """
        self.temperature_P=np.concatenate([self.temperatureProfile, self.temperatureProfile[:, -1:]], axis=1)

        for a in range(self.nslices):
            pressure_a = np.zeros((self.nLayers+1))
            pressure_a[-1] = self.pressure.pressure_profile_levels[-1]
            pressure_a = np.zeros((self.nLayers+1))

            alt_max = self.altitude_layers.searchsorted(self.altitude_P[a,:].max(), side='left')
            pressure_a[alt_max:] = self.pressure.pressure_profile_levels[-1] # outside of origin boundaries, just copy last value
            self.temperatureProfile[a, alt_max:] = self.temperature_P[a,-1] # outside of origin boundaries, just copy last value

            pressure_a[:alt_max] = interp1d(self.altitude_P[a, :], self.pressure.pressure_profile_levels[:], ykind='log')(self.altitude_layers[:alt_max])
            self.temperatureProfile[a, :alt_max] = interp1d(self.altitude_P[a, :], self.temperature_P[a, :], ykind='linear')(self.altitude_layers[:alt_max])

            # For every slice, get mid point (layer) pressure between levels computing geometric average between pressure at n and n+1 level
            self.pressure.profile[a] = pressure_a[:-1]



    def compute_pressure(self):
        mu_profile=self._chemistry.muProfile

        p_min = self.pressure.pressure_profile_levels.min()

        nlayers = self.pressure.nLayers
        H = np.zeros((self.nslices, nlayers))
        g = np.zeros((nlayers))

        ps = self.pressure.pressure_profile_levels[0] # surface pressure
        g[0] = self._planet.gravity # surface gravity (0th layer)
        H[:,0] = (KBOLTZ*self.temperatureProfile[:,0])/(mu_profile[:,0]*g[0]) # scaleheight at the surface (0th layer)
        dz = self.dz
        z = self.altitude_layers

        slices = np.where(self.pressureProfile[:,0] < 10*p_min)
        self.pressure.pressure_profile[slices,0] = ps * np.exp(-z[0]/H[slices,0])

        for i in range(1, nlayers):
            slices = np.where(self.pressureProfile[:,i] < 10*p_min)
            self.pressure.pressure_profile[slices,i] = self.pressure.pressure_profile[slices,i-1] * np.exp(-dz[i-1]/H[slices,i-1])

            if i == nlayers:
                break
            with np.errstate(over='ignore'):
                g[i] = self._planet.gravity_at_height(z[i]) # gravity at the i-th layer
            with np.errstate(divide='ignore'):
                H[:,i] = (KBOLTZ*self.temperatureProfile[:,i])/(mu_profile[:,i]*g[i])

    def compute_path_length(self, dz):
        dl = []
        self.points = []

        z0 = self._planet.fullRadius
        total_layers = self.nLayers

        z = self.altitudeProfile
        self.debug('Computing path_length: \n z=%s \n dz=%s', z, dz)

        for layer in range(total_layers):
            ## intersection of path with spheres of radius planet+layer+i
            altitude = self.z_path[layer]
            n_up_lay = z[layer+1:].shape[0] # nb of upper layers
            radii = np.zeros(2*n_up_lay + self.nslices-1)
            radii[:n_up_lay] = z[layer+1:]
            radii[n_up_lay:2*n_up_lay] = z[layer+1:]
            angles = np.zeros(radii.shape)
            for i in range(n_up_lay):
                angles[i] = math.acos(altitude/(z0 + radii[i]))*180/np.pi # day side
                angles[n_up_lay+i] = -angles[i] # night side

            ## intersection of path with slices between -beta and beta
            angles[2*n_up_lay:] = self.alpha*np.arange(self.nslices-1)-self.beta/2
            for i in range(self.nslices-1):
                radii[2*n_up_lay+i] = altitude/math.cos(np.pi/180*angles[2*n_up_lay+i]) - z0

            ## filter out circles that are larger than atmosphere and merge+sort
            atm_idx = np.where(radii <= z[-1])
            radii = radii[atm_idx]
            angles = angles[atm_idx]
            points = np.array((angles,radii)).T
            if (self.nslices % 2) != 0:
                points = np.concatenate((points, [[0, altitude-z0]])) # add mid point 90,altitude (at terminator) in case of odd number of slices (but should not happen)
            points = sorted(points,key=lambda x: x[0])

            ## computing path coordinates and length: (alpha, z, length)
            k = np.ndarray((max(0,(len(points)-1)),3),dtype = object)
            p = altitude**2
            for i in range(len(points)-1):
                a0 = points[i][0]
                a1 = points[i+1][0]
                r0 = points[i][1]
                r1 = points[i+1][1]
                if a0 < -self.beta/2:
                    a=0
                elif a0 >= self.beta/2:
                    a=self.nslices-1
                else:
                    a = int(math.floor((a0+self.beta/2)/self.alpha))+1 # slice after night side
                id_z = int(self.altitudeProfile.searchsorted(min(r0,r1),
                side='right')-1) # layer
                r0 = z0 + r0  # after search because of float rounding effect
                r1 = z0 + r1
                # handle rounding issues with substraction (mid point at 90 degrees)
                if r0 < altitude:
                    r0 = altitude
                if r1 < altitude:
                    r1 = altitude

                # dist = np.sqrt(r0**2 + r1**2 - 2*r0*r1*np.cos(np.pi/180*(a1-a0))) # polar distance is different from cartesian distance
                dist = np.abs(np.sqrt(r1**2 - p) - np.sqrt(r0**2 - p))
                k[i] = [a,id_z,dist]
            dl.append(k)
            self.points.append(points)

        return dl

    def path_integral(self, wngrid, return_contrib):
        z0 = self._planet.fullRadius
        z = self.altitudeProfile

        # Bottom of layer and weird gradient
        # dz = np.gradient(z[:-1])
        # self.z_path = z0 + z[:-1]

        # Middle of layer and dz is difference between two layers
        dz = np.diff(z)
        self.z_path = z0 + z[:-1] + dz/2.

        wngrid_size = wngrid.shape[0]
        density_profile = self.densityProfile
        total_layers = self.nLayers
        tau = np.zeros(shape=(total_layers, wngrid_size), dtype=np.float64)

        path_length = self.compute_path_length(dz)
        self.path_length = path_length

        for layer in range(total_layers):

            self.debug('Computing layer %s', layer)
            dl = path_length[layer]

            endK = len(dl)

            for contrib in self.contribution_list:
                if tau[layer].min() > 10:
                    break
                self.debug('Adding contribution from %s', contrib.name)
                contrib.contribute(self, 0, endK, layer, layer,
                                   density_profile, tau, path_length=dl)

        self.debug('tau %s %s', tau, tau.shape)

        absorption, tau = self.compute_absorption(tau, dz)
        return absorption, tau

    def compute_absorption(self, tau, dz):
        tau = np.exp(-tau)
        ap = self.altitude_layers[:, None]
        pradius = self._planet.fullRadius
        sradius = self._star.radius
        _dz = dz[:, None]

        integral = np.sum((pradius+ap)*(1.0-tau)*_dz*2.0, axis=0)
        return ((pradius**2.0) + integral)/(sradius**2), tau

    def write(self,output):
        transmission = super().write(output)

        transmission.write_scalar('beta',self.beta)
        transmission.write_scalar('nslices',self.nslices)
        transmission.write_scalar('p_iso',self.p_iso)
        transmission.write_array('mid_altitude', np.array(self.z_path))

        path = transmission.create_group('Path')

        for i in range(len(self.path_length)):
            path.write_array('path_ang_%d'%i, np.array(self.path_length[i],dtype=int)[:,0])
            path.write_array('path_rad_%d'%i, np.array(self.path_length[i],dtype=int)[:,1])
            path.write_array('path_len_%d'%i, np.array(self.path_length[i],dtype=float)[:,2])

        for i in range(len(self.points)):
            path.write_array('point_ang_%d'%i, np.array(self.points[i],dtype=float)[:,0])
            path.write_array('point_rad_%d'%i, np.array(self.points[i],dtype=float)[:,1])

        return transmission

    @classmethod
    def input_keywords(cls):
        return ['2d','transmission2d','transmission2D']


    BIBTEX_ENTRIES = [
        """
        @ARTICLE{falco2021toward,
        author = {{Falco}, Aur{\'e}lien and {Zingales}, Tiziano and {Pluriel}, William and {Leconte}, J{\'e}r{\'e}my},
        title = "{Toward a multidimensional analysis of transmission spectroscopy. I. Computation of transmission spectra using a 1D, 2D, or 3D atmosphere structure}",
        journal = {\aap},
        keywords = {planets and satellites: atmospheres, methods: numerical, techniques: spectroscopic, radiative transfer, planets and satellites: general, Astrophysics - Earth and Planetary Astrophysics},
        year = 2022,
        month = feb,
        volume = {658},
        eid = {A41},
        pages = {A41},
        doi = {10.1051/0004-6361/202141940},
        archivePrefix = {arXiv},
        eprint = {2110.11799},
        primaryClass = {astro-ph.EP},
        adsurl = {https://ui.adsabs.harvard.edu/abs/2022A&A...658A..41F},
        adsnote = {Provided by the SAO/NASA Astrophysics Data System}
        }
        """
    ]
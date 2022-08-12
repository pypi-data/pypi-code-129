from taurex.temperature import TemperatureProfile
import numpy as np
from taurex.core import fitparam

class Temperature2D(TemperatureProfile):
    """A 'two-dimensional' temperature profile with
    a temperature :py:attr:`day_temp` on the day side,
    a temperature :py:attr:`night_temp` on the night side,
    and a linear transition between day and night within the angle :py:attr:`~taurex.model.transmission2D.Transmission2DModel.beta`.
    A temperature :py:attr:`deep_temp` is also set in layers
    with a pressure higher than :py:attr:`~taurex.model.transmission2D.Transmission2DModel.p_iso`.
    :py:attr:`~taurex.model.transmission2D.Transmission2DModel.beta` and
    :py:attr:`~taurex.model.transmission2D.Transmission2DModel.p_iso` are
    inherited from the 2D model :class:`~taurex.model.transmission2D.Transmission2DModel`.

    Parameters
    ----------

    day_temp : float
        Temperature to set on day side

    night_temp : float
        Temperature to set on night side

    deep_temp : float
        Temperature to set in layers with pressure higher than p_iso (default is day temperature)
    """

    def __init__(self, day_temp=1500, night_temp=300, deep_temp=None):
        super().__init__('Temperature2D')

        self._day_temp = day_temp
        self._night_temp = night_temp
        self._deep_temp = deep_temp
        # The following variables must be set by the forward model
        self.nslices = None
        self.beta = None
        self.p_iso = None

    @property
    def alpha(self):
        return 0 if (self.beta == 0) else self.beta/(self.nslices-2)  # angle of slices in the transition, so do not count day and night slices

    @fitparam(param_name='Tday',param_latex='$T_{day}$',default_fit=False,default_bounds=[300.0, 2000.0])
    def dayTemperature(self):
        """Day temperature in Kelvin"""
        return self._day_temp

    @dayTemperature.setter
    def dayTemperature(self,value):
        self._day_temp = value

    @fitparam(param_name='Tnight',param_latex='$T_{night}$',default_fit=False,default_bounds=[300.0, 2000.0])
    def nightTemperature(self):
        """Night temperature in Kelvin"""
        return self._night_temp

    @nightTemperature.setter
    def nightTemperature(self,value):
        self._night_temp = value

    @fitparam(param_name='Tdeep',param_latex='$T_{deep}$',default_fit=False,default_bounds=[300.0, 2000.0])
    def deepTemperature(self):
        """deep temperature in Kelvin"""
        if self._deep_temp is None:
            self.warning("No deep temperature given. Using day temperature (%d)"%self._day_temp)
            return self._day_temp
        return self._deep_temp

    @deepTemperature.setter
    def deepTemperature(self,value):
        self._deep_temp = value

    def initialize_profile(self, planet=None, nlayers=100,
                           pressure_profile=None):
        super().initialize_profile(planet,nlayers,pressure_profile)
        all_temp = np.zeros((self.nslices, self.nlayers))
        angles = self.alpha*np.arange(self.nslices-2)-self.beta/2+self.alpha/2

        all_temp[0,:] = self.nightTemperature
        all_temp[-1,:] = self.dayTemperature

        # Interpolation between day and night
        if self.beta != 0:
            all_temp[1:-1,:] = self.nightTemperature + (self.dayTemperature - self.nightTemperature) * (angles[:,None] / self.beta + 1/2)

        # set isothermal temperature in layers with pressure larger than p_iso
        p_iso_ids = np.where(self.pressure_profile[0] > self.p_iso) # pressure profile is the same in all columns
        all_temp[:,p_iso_ids] = self.deepTemperature

        # set day and night temperature on first and last slice

        self.temp_profile = all_temp
        if hasattr(self, "custom_temperature"):
            self.temp_profile[:] =  self.custom_temperature


    @property
    def profile(self):
        """Returns an 2D temperature profile

        Returns: :obj:np.array(float)
            temperature profile
        """
        return self.temp_profile

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


    @classmethod
    def input_keywords(cls):
        return ['2d']

    def write(self,output):
        temperature = super().write(output)
        temperature.write_scalar('day_temp', self._day_temp)
        temperature.write_scalar('night_temp', self._night_temp)
        return temperature
import numpy as np
from taurex.pressure import PressureProfile
from .pressureprofile import SimplePressureProfile

class Pressure2DProfile(SimplePressureProfile, PressureProfile):
    """
    A pressure profile using 2 dimensions (see :class:`~taurex.model.transmission2D.Transmission2DModel`).
    Simply duplicates the 1D profile over the 2nd dimension.

    Parameters
    ----------
    nlayers : int
        Number of layers in atmosphere

    atm_min_pressure : float
        minimum pressure in Pascal (top of atmosphere)

    atm_max_pressure : float
        maximum pressure in Pascal (surface of planet)
    """

    def __init__(self, nlayers=100,
                 atm_min_pressure=1e-4,
                 atm_max_pressure=1e6):
        super().__init__(nlayers,atm_min_pressure,atm_max_pressure)
        # These variables should be defined by the forward model
        self.nslices = None
        self.beta = None

    def compute_pressure_profile(self, nslices, beta):
        """Sets up the pressure profile for the atmosphere model"""
        self.nslices = nslices
        self.beta = beta
        self.pressure_profile = np.zeros((self.nslices,self._nlayers))

        # set pressure profile of layer boundaries
        press_exp = np.linspace(np.log(self._atm_min_pressure), np.log(self._atm_max_pressure), self.nLevels)
        self.pressure_profile_levels =  np.exp(press_exp)[::-1]
        if hasattr(self, "custom_pressure_levels"):
            self.pressure_profile_levels =  self.custom_pressure_levels # set by user
        if hasattr(self, "custom_pressure"):
            self.pressure_profile[:] = self.custom_pressure # set by user
            return

        # get mid point pressure between levels (i.e. get layer pressure) computing geometric
        # average between pressure at n and n+1 level
        pressure_grid = np.power(10, np.log10(self.pressure_profile_levels)[:-1]+
                                         np.diff(np.log10(self.pressure_profile_levels))/2.)

        # In case of (P, alpha) coordinates, just copy pressure profile on every slice
        # This profile will be changed later into a polar (z, alpha) coordinate system
        self.pressure_profile[:] = pressure_grid

    @classmethod
    def input_keywords(cls):
        return ['2d', ]
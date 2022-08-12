from taurex.chemistry import TaurexChemistry as OriginalTaurexChemistry # Chemistry from main taurex code
import numpy as np
from taurex.cache import OpacityCache
from taurex.exceptions import InvalidModelException
from taurex.data.fittable import Fittable, derivedparam

class InvalidChemistryException(InvalidModelException):
    """
    Exception that is called when atmosphere mix is greater
    than unity
    """
    pass

class TaurexChemistry(OriginalTaurexChemistry):

    """
    Copy of the standard chemical model used in Taurex, which is also compatible with multi-dimensional models.
    This allows for the combination of different mixing profiles for each molecule.
    Lets take an example profile, we want an atmosphere with a constant mixing of ``H2O``
    but two layer mixing for ``CH4``.
    First we initialize our chemical model:

        >>> chemistry = TaurexChemistry()

    Then we can add our molecules using the :func:`addGas` method. Lets start
    with ``H2O``, since its a constant profile for all layers of the atmosphere
    we thus add
    the :class:`~taurex.data.profiles.chemistry.gas.constantgas.ConstantGas`
    object:

        >>> chemistry.addGas(ConstantGas('H2O',mix_ratio = 1e-4))

    Easy right? Now the same goes for ``CH4``, we can add the molecule into
    the chemical model by using the correct profile (in this case
    :class:`~taurex.data.profiles.chemistry.gas.twolayergas.TwoLayerGas`):

        >>> chemistry.addGas(TwoLayerGas('CH4',mix_ratio_surface=1e-4,
                                         mix_ratio_top=1e-8))

    Molecular profiles available are:
        * :class:`~taurex.data.profiles.chemistry.gas.constantgas.ConstantGas`
        * :class:`~taurex.data.profiles.chemistry.gas.twolayergas.TwoLayerGas`
        * :class:`~taurex.data.profiles.chemistry.gas.twolayergas.TwoPointGas`


    Parameters
    ----------

    fill_gases : str or :obj:`list`
        Either a single gas or list of gases to fill the atmosphere with

    ratio : float or :obj:`list`
        If a bunch of molecules are used to fill an atmosphere, whats the
        ratio between them?
        The first fill gas is considered the main one with others defined as
        ``molecule / main_molecule``


    """

    def __init__(self, fill_gases=['H2', 'He'], ratio=0.17567):
        OriginalTaurexChemistry.__init__(self, fill_gases=fill_gases, ratio=ratio)

        self.active_mixratio_profile = None
        self.inactive_mixratio_profile = None

        for derivedparam in self.find_derivedparams():

            get_func = derivedparam.fget
            param_name = get_func.param_name
            param_latex = get_func.param_latex
            compute = get_func.compute

            self.add_derived_param(param_name,
                                   param_latex,
                                   get_func,
                                   compute)
            break # small hack for to get 2D mu

    @derivedparam(param_name='mu', param_latex='$\mu$', compute=True)
    def mu(self):
        """
        Mean molecular weight at surface (amu)
        """

        from taurex.constants import AMU
        try:
            return self.muProfile.flatten()[0]/AMU
        except AttributeError:
            return np.nan


    def initialize_chemistry(self,nlayers,temperature_profile,pressure_profile,altitude_profile, model=None):
        """
        Initializes the chemical model and computes the all gas profiles
        and the mu profile for the forward model
        """
        self.info('Initializing chemistry model')

        mix_profile = []

        for gas in self._gases:
            gas.p_iso = self.p_iso
            if model is None:
                gas.initialize_profile(nlayers,temperature_profile,pressure_profile,altitude_profile)
            else:
                gas.initialize_profile(nlayers,temperature_profile,pressure_profile,altitude_profile, model)
            diss = gas.dissociatedMix(temperature_profile, pressure_profile, gas.mixProfile)
            if hasattr(gas, "custom_mix"):
                mix_profile.append(gas.custom_mix)
                continue
            mix_profile.append(diss)

        total_mix = sum(mix_profile)

        self.debug('Total mix output %s',total_mix)

        validity = np.any(total_mix> 1.0)

        self.debug('Is invalid? %s',validity)

        if validity:
            self.error('Greater than 1.0 chemistry profile detected')
            raise InvalidChemistryException

        mixratio_remainder = 1. - total_mix
        mixratio_remainder += np.zeros(shape=pressure_profile.shape)
        mix_profile = self.fill_atmosphere(mixratio_remainder) + mix_profile

        if len(mix_profile) > 0:
            self._mix_profile = np.stack(mix_profile)
        else:
            self._mix_profile = 0.0
        self.compute_mu_profile(pressure_profile)

    def compute_mu_profile(self, pressure_profile):
        self.mu_profile = np.zeros(shape=pressure_profile.shape)
        if self.mixProfile is not None:
            mix_profile = self.mixProfile
            for idx, gasname in enumerate(self.gases):
                self.mu_profile += mix_profile[idx] * \
                    self.get_molecular_mass(gasname)

    @classmethod
    def input_keywords(cls):
        return ['1d',]

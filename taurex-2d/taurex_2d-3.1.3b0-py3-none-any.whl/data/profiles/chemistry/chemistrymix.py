from .gas.gas2D import Gas2D
from taurex.chemistry import Chemistry # Chemistry from main taurex code
from .taurexchemistry import TaurexChemistry as Taurex2DChemistry # 2D-compatible version of taurex chemistry
from .taurexchemistry import InvalidChemistryException
import numpy as np
from taurex.util import *
from taurex.data.fittable import Fittable, derivedparam

class ChemistryMix(Taurex2DChemistry, Chemistry):
    """
    Chemical model in a 2D polar grid (see :class:`~taurex.model.transmission2D.Transmission2DModel`), including dissociation.
    Gases can also be computed based on the mix ratios of other gases.
    The dissociation of :math:`H_2` is taken into account by adding some :math:`H` in the mix.

    Compatible Molecular profiles available are:
        * :class:`~taurex_2d.data.profiles.chemistry.gas.gas2D.Gas2D`
        * :class:`~taurex_2d.data.profiles.chemistry.gas.gasratio.GasRatio`

    Parameters
    ----------

    fill_gases : str or obj:`list`
        Either a single gas or list of gases to fill the atmosphere with. Ignored when :math:`H_2` is defined by the user and dissociates.

    ratio : float or :obj:`list`
        If a bunch of molecules are used to fill an atmosphere, whats the ratio between them?
        The first fill gas is considered the main one with others defined as ``molecule / main_molecule``.
        Ignored if :math:`H_2` is defined by the user and dissociates.
    """
    def __init__(self,fill_gases=[],ratio=0.17567,H2_dissociation=False):
        self.p_iso = None
        self.H2_dissociation = H2_dissociation
        if self.H2_dissociation:
            fill_gases = ["H2", "H", "He"]
            ratio=[0,0]
        Taurex2DChemistry.__init__(self, fill_gases=fill_gases, ratio=ratio)

    def initialize_chemistry(self,nlayers,temperature_profile,pressure_profile,altitude_profile, model=None):
        """
        Initializes the chemical model and computes the all gas profiles
        and the mu profile for the forward model
        """
        self.info('Initializing chemistry model')

        mix_profile = []

        gases = {}
        for gas in self._fill_gases:
            gases[gas] = 0 # fill gases are listed first

        x_traces_solar = []
        for gas in self._gases:
            gas.p_iso = self.p_iso
            gas.initialize_profile(nlayers,temperature_profile,pressure_profile,altitude_profile, gases)
            diss = gas.dissociatedMix(temperature_profile, pressure_profile, gas.mixProfile)
            x_traces_solar.append(np.atleast_1d(gas.mixProfile).item(0))
            gases[gas.molecule] = diss

        total_mix = sum(gases.values())
        trace_mix_solar = sum(x_traces_solar)

        self.debug('Total mix output %s',total_mix)

        validity = np.any(total_mix> 1.0)

        self.debug('Is invalid? %s',validity)

        if validity:
            self.error('Greater than 1.0 chemistry profile detected')
            raise InvalidChemistryException

        mixratio_remainder = 1. - total_mix
        mixratio_remainder += np.zeros(shape=pressure_profile.shape)

        if self.H2_dissociation:
            ratio_HeH2 = self._fill_ratio[0]
            x_H2_solar = (1-trace_mix_solar)/(1+ratio_HeH2)
            gas_H2 = Gas2D("H2", mix_ratio = x_H2_solar, dissociation=True, alpha = 1., beta = 2.41e4, gamma = 6.5)
            gas_H2.initialize_profile(nlayers,temperature_profile,pressure_profile,altitude_profile, gases)
            diss = gas_H2.dissociatedMix(temperature_profile, pressure_profile, gas_H2.mixProfile)
            gases["H2"] = diss

            gases["H"] = 2*((1-total_mix-gases["H2"]*(1+ratio_HeH2))/(2+ratio_HeH2))
            gases["He"] = 1 - sum(gases.values())
        else:
            gases = self.fill_atmosphere(gases, mixratio_remainder)

        for gas, vmr in gases.items():
            if (vmr < -1e-14).any():
                self.error("Mix ratio of %s is negative (min() = %s)"%(gas, vmr.min()))
            mix_profile.append(vmr)

        if len(mix_profile) > 0:
            self._mix_profile = np.stack(mix_profile)
        else:
            self._mix_profile = 0.0
        if not np.isclose(sum(gases.values()),1).all():
            mean = np.mean(sum(gases.values()))
            if mean < 1:
                self.error("VMR total below 1 (mean=%s). Maybe you should add a fill gas?"%mean)
            else:
                self.error("VMR total above 1 (mean=%s). Too much gases?"%mean)
        self.compute_mu_profile(pressure_profile)

    def compute_mu_profile(self, pressure_profile):
        self.mu_profile = np.zeros(shape=pressure_profile.shape)
        if self.activeGasMixProfile is not None:
            for idx, gasname in enumerate(self.activeGases):
                self.mu_profile += self.activeGasMixProfile[idx] * \
                    get_molecular_weight(gasname)
        if self.inactiveGasMixProfile is not None:
            for idx, gasname in enumerate(self.inactiveGases):
                self.mu_profile += self.inactiveGasMixProfile[idx] * \
                    get_molecular_weight(gasname)

    def fill_atmosphere(self, gases, mixratio_remainder):
        if len(self._fill_gases) ==1:
            gases[self._fill_gases[0]] = mixratio_remainder
        elif len(self._fill_gases):
            main_molecule =  mixratio_remainder/(1. + sum(self._fill_ratio))
            gases[self._fill_gases[0]] = main_molecule
            for molecule,ratio in zip(self._fill_gases[1:],self._fill_ratio):
                second_molecule = ratio * main_molecule
                gases[molecule] = second_molecule
        return gases

    @classmethod
    def input_keywords(cls):
        return ['2d','2d-mix','dissociation','diss','2d-dissociation', 'mix']

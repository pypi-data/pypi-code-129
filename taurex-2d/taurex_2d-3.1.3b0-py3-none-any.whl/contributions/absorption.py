from taurex.contributions import Contribution
from .contribution import SimpleContribution
import numpy as np
from taurex.cache import OpacityCache

class AbsorptionContribution(SimpleContribution, Contribution):
    """
    Computes the contribution to the optical depth
    occuring from molecular absorption.
    """

    def __init__(self, exo_k=False):
        super().__init__('Absorption')
        self._opacity_cache = OpacityCache()
        self.exo_k = exo_k

    def prepare_each(self, model, wngrid):
        """
        Prepares each molecular opacity by weighting them
        by their mixing ratio in the atmosphere

        Parameters
        ----------
        model: :class:`~taurex.model.model.ForwardModel`
            Forward model

        wngrid: :obj:`array`
            Wavenumber grid

        Yields
        ------
        component: :obj:`tuple` of type (str, :obj:`array`)
            Name of molecule and weighted opacity

        """

        self.debug('Preparing model with %s', wngrid.shape)
        self._ngrid = wngrid.shape[0]
        sigma_xsec = np.zeros(shape=(model.pressureProfile.shape+wngrid.shape))

        # Get the opacity cache
        self._opacity_cache = OpacityCache()

        if self.exo_k:
            import exo_k as xk
            xk.Settings().set_mks(True)
            k_data=xk.Kdatabase(model.chemistry.activeGases, remove_zeros=True)
            self.gas_mix = xk.Gas_mix(k_database=k_data)

        # Loop through all active gases
        for gas in model.chemistry.activeGases:

            gas_object = next((x for x in model.chemistry._gases if x.molecule == gas), None)

            # Clear sigma array
            sigma_xsec[...] = 0.0

            # Get the mix ratio of the gas
            gas_mix = model.chemistry.get_gas_mix_profile(gas)
            self.info('Recomputing active gas %s opacity', gas)

            # Get the cross section object relating to the gas
            xsec = self._opacity_cache[gas]
            # Loop through the layers
            if (model.pressureProfile.ndim > 1):
                for idx_slice, tp_slice in enumerate(zip(model.temperatureProfile,
                                                         model.pressureProfile)):
                    temperature_slice, pressure_slice = tp_slice
                    self.debug('Got index,tp %s %s', idx_slice, tp_slice)
                    for idx_layer, tp in enumerate(zip(temperature_slice,
                                                    pressure_slice)):
                        self.debug('Got index,tp %s %s', idx_layer, tp)
                        temperature, pressure = tp

                        # Place into the array
                        if self.exo_k:
                            sigma_xsec[idx_slice,idx_layer] += \
                                self.gas_mix.cross_section(composition={gas:gas_mix[idx_slice,idx_layer]}, logp_array=np.log10(pressure), t_array=temperature, rayleigh=False)[0]
                            continue
                        sigma_xsec[idx_slice,idx_layer] += \
                            xsec.opacity(temperature, pressure, wngrid) * \
                            gas_mix[idx_slice,idx_layer]
            else:
                for idx_layer, tp in enumerate(zip(model.temperatureProfile,
                                                   model.pressureProfile)):
                    self.debug('Got index,tp %s %s', idx_layer, tp)
                    temperature, pressure = tp

                    # Place into the array
                    if self.exo_k:
                        sigma_xsec[idx_layer] += \
                            self.gas_mix.cross_section(composition={gas:gas_mix[idx_layer]}, logp_array=np.log10(pressure), t_array=temperature, rayleigh=False)[0]
                        continue
                    sigma_xsec[idx_layer] += \
                        xsec.opacity(temperature, pressure, wngrid) * \
                        gas_mix[idx_layer]

            # Temporarily assign to master cross-section
            self.sigma_xsec = sigma_xsec
            yield gas, sigma_xsec

    @property
    def sigma(self):
        """
        Returns the fused weighted cross-section
        of all active gases
        """
        return self.sigma_xsec

    @classmethod
    def input_keywords(self):
        return ['Absorption2D','Absorption2d','absorption2d',]
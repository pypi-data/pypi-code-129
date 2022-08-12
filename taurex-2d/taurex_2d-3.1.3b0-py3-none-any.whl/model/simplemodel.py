import numpy as np
from .model import ForwardModel
from taurex.util.util import clip_native_to_wngrid


class SimpleForwardModel(ForwardModel):
    # altitude, gravity and scale height profile
    def _compute_altitude_gravity_scaleheight_profile(self, mu_profile=None):
        """
        Computes altitude, gravity and scale height of the atmosphere.
        Only call after :func:`build` has been called at least once.

        Parameters
        ----------
        mu_profile, optional:
            Molecular weight profile at each layer

        """

        from taurex.constants import KBOLTZ
        if mu_profile is None:
            mu_profile = self._chemistry.muProfile

        # build the altitude profile from the bottom up
        nlayers = self.pressure.nLayers
        H = np.zeros(nlayers)
        g = np.zeros(nlayers)
        z = np.zeros(nlayers+1)

        # surface gravity (0th layer)
        g[0] = self._planet.gravity
        # scaleheight at the surface (0th layer)
        H[0] = (KBOLTZ*self.temperatureProfile[0])/(mu_profile[0]*g[0])

        for i in range(1, nlayers+1):
            deltaz = (-1.)*H[i-1]*np.log(
                self.pressure.pressure_profile_levels[i] /
                self.pressure.pressure_profile_levels[i-1])

            z[i] = z[i-1] + deltaz  # altitude at the i-th layer
            if i == nlayers:
                break
            with np.errstate(over='ignore'):
                # gravity at the i-th layer
                g[i] = self._planet.gravity_at_height(z[i])
                self.debug('G[%s] = %s', i, g[i])

            with np.errstate(divide='ignore'):
                H[i] = (KBOLTZ*self.temperatureProfile[i])/(mu_profile[i]*g[i])

        self.altitude_profile = z
        self.altitude_layers = z[:-1]
        self.scaleheight_profile = H
        self.gravity_profile = g

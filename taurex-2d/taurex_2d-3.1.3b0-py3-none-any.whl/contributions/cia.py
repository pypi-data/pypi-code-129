from taurex.contributions import Contribution
from taurex_2d.contributions.contribution import SimpleContribution
import numpy as np
import numba
from taurex.cache import CIACache


@numba.jit(nopython=True, nogil=True)
def contribute_cia_1D(startK, endK, density_offset, sigma, density, path, nlayers,
                   ngrid, layer, tau):
    for k in range(startK, endK):
        _path = path[k]
        _density = density[k+density_offset]
        # for mol in range(nmols):
        for wn in range(ngrid):
            tau[layer, wn] += sigma[k+layer, wn]*_path*_density*_density

@numba.njit(nogil=True)
def contribute_cia_2D(startK, endK, density_offset, sigma, density, angle, z, path, nlayers, ngrid, layer, tau):
    """
    Same as contribute_tau_1D but arrays have one more dimension and path contains coordinates.
    """
    for k in range(startK, endK):
        _angle = angle[k]
        _z = z[k]
        _path = path[k]
        _density = density[_angle, _z]
        for wn in range(ngrid):
        # for wn in numba.prange(ngrid):
            tau[layer, wn] += sigma[_angle, _z, wn]*_path*_density*_density

def contribute_cia(startK, endK, density_offset, sigma, density, path, nlayers,
                   ngrid, layer, tau):
    """
    Collisionally induced absorption integration function

    This has the form:

    .. math::

        \\tau_{\\lambda}(z) = \\int_{z_{0}}^{z_{1}}
            \\sigma(z') \\rho(z')^{2} dz',

    where :math:`z` is the layer, :math:`z_0` and :math:`z_1` are ``startK``
    and ``endK`` respectively. :math:`\\sigma` is the weighted
    cross-section ``sigma``. :math:`rho` is the ``density`` and
    :math:`dz'` is the integration path length ``path``


    Parameters
    ----------
    startK: int
        starting layer in integration

    endK: int
        last layer in integration

    density_offset: int
        Which part of the density profile to start from

    sigma: :obj:`array`
        cross-section

    density: array_like
        density profile of atmosphere

    path: array_like
        path-length or altitude gradient

    nlayers: int
        Total number of layers (unused)

    ngrid: int
        total number of grid points

    layer: int
        Which layer we currently on

    Returns
    -------
    tau : array_like
        optical depth (well almost you still need to do ``exp(-tau)`` yourself)

    """
    if (density.ndim > 1):
        angle = np.array(path, dtype=int)[:,0]
        z = np.array(path, dtype=int)[:,1]
        path_length = np.array(path, dtype=float)[:,2]
        contribute_cia_2D(startK, endK, density_offset,
                       sigma, density, angle, z, path_length, nlayers, ngrid, layer, tau)
    else:
        contribute_cia_1D(startK, endK, density_offset,
                       sigma, density, path, nlayers, ngrid, layer, tau)

class CIAContribution(SimpleContribution, Contribution):
    """
    Computes the contribution to the optical depth
    occuring from collisionally induced absorption.

    Parameters
    ----------
    cia_pairs: :obj:`list` of str
        list of molecule pairs of the form ``mol1-mol2``
        e.g. ``H2-He``
    """
    def __init__(self, cia_pairs=None):
        super().__init__('CIA')
        self._cia_pairs = cia_pairs

        self._cia_cache = CIACache()
        if self._cia_pairs is None:
            self._cia_pairs = []

    @property
    def ciaPairs(self):
        """
        Returns list of molecular pairs involved

        Returns
        -------
        :obj:`list` of str
        """

        return self._cia_pairs

    @ciaPairs.setter
    def ciaPairs(self, value):
        self._cia_pairs = value

    def contribute(self, model, start_layer, end_layer, density_offset, layer,
                   density, tau, path_length=None):
        if self._total_cia > 0:
            contribute_cia(start_layer, end_layer, density_offset,
                           self.sigma_xsec, density, path_length,
                           self._nlayers, self._ngrid,
                           layer, tau)

    def prepare_each(self, model, wngrid):
        """
        Computes and weighs cross-section for
        a single pair of molecules

        Parameters
        ----------
        model: :class:`~taurex.model.model.ForwardModel`
            Forward model

        wngrid: :obj:`array`
            Wavenumber grid


        Yields
        ------
        component: :obj:`tuple` of type (str, :obj:`array`)
            Molecular pair and the weighted cia opacity.

        """

        self._total_cia = len(self.ciaPairs)
        self._nlayers = model.nLayers
        self._ngrid = wngrid.shape[0]
        self.info('Computing CIA ')

        from taurex_2d.model import Transmission2DModel #to get right dimension later
        sigma_cia = np.zeros(shape=(model.pressureProfile.shape+wngrid.shape))

        chemistry = model.chemistry

        for pairName in self.ciaPairs:
            cia = self._cia_cache[pairName]
            sigma_cia[...] = 0.0

            cia_factor = chemistry.get_gas_mix_profile(cia.pairOne) * \
                chemistry.get_gas_mix_profile(cia.pairTwo)

            if (isinstance(model,Transmission2DModel)):
                for idx_slice, tp_slice in enumerate(zip(model.temperatureProfile, model.pressureProfile)):
                    temperature_slice, pressure_slice = tp_slice
                    self.debug('Got index,tp %s %s', idx_slice, tp_slice)
                    for idx_layer, tp in enumerate(zip(temperature_slice, pressure_slice)):
                        self.debug('Got index,tp %s %s', idx_layer, tp)
                        temperature, pressure = tp

                        _cia_xsec = cia.cia(temperature, wngrid)
                        sigma_cia[idx_slice,idx_layer] += _cia_xsec*cia_factor[idx_slice,idx_layer]
            else:
                for idx_layer, temperature in enumerate(model.temperatureProfile):
                    _cia_xsec = cia.cia(temperature, wngrid)
                    sigma_cia[idx_layer] += _cia_xsec*cia_factor[idx_layer]
            self.sigma_xsec = sigma_cia
            yield pairName, sigma_cia

    def write(self, output):
        contrib = super().write(output)
        if len(self.ciaPairs) > 0:
            contrib.write_string_array('cia_pairs', self.ciaPairs)
        return contrib

    @classmethod
    def input_keywords(self):
        return ['CIA2D']
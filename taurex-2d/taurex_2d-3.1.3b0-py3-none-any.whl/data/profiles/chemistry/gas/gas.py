from taurex.log import Logger
from taurex.core import Fittable
from taurex.output.writeable import Writeable
import numpy as np

wasp121b_coeffs = {
'H2':(1, 2.41, 6.5),
'H2O':(2, 4.83, 15.9),
'TiO':(1.6, 5.94, 23.0),
'VO':(1.5, 5.40, 23.8),
'H-':(0.6, -0.14, 7.7),
'Na':(0.6, 1.89, 12.2),
'K':(0.6, 1.28, 12.7),
}
wasp121b_deep_abundances_log = {
'H2':-0.1,
'H2O':-3.3,
'TiO':-7.1,
'VO':-9.2,
'H-':-8.3,
'Na':-5.5,
'K':-7.1,
}

class SimpleGas(Fittable, Logger, Writeable):
    """

    *Abstract Class*

    This class is a base for a single molecule or gas.
    Its used to describe how it mixes at each layer and combined
    with
    :class:`~taurex.data.profile.chemistry.taurexchemistry.TaurexChemistry`
    is used to build a chemical profile of the planets atmosphere.
    Requires implementation of:

    - func:`~mixProfile`


    Parameters
    -----------

    name :str
        Name used in logging

    molecule_name : str
        Name of molecule

    """

    def __init__(self, name, molecule_name, dissociation=False, alpha=None, beta=None, gamma=None):
        Logger.__init__(self, name)
        Fittable.__init__(self)
        self._molecule_name = molecule_name
        self.mix_profile = None
        self.dissociation = dissociation
        if dissociation:
            if alpha is None:
                alpha = wasp121b_coeffs[molecule_name][0]
                self.warning(f"{molecule_name} alpha = {alpha}")
            if beta is None:
                beta = wasp121b_coeffs[molecule_name][1]*1e4
                self.warning(f"{molecule_name} beta = {beta}")
            if gamma is None:
                gamma = wasp121b_coeffs[molecule_name][2]
                self.warning(f"{molecule_name} gamma = {gamma}")

            self.alpha = alpha
            self.beta = beta
            self.gamma = gamma

    @property
    def molecule(self):
        """
        Returns
        -------
        molecule_name: str
            Name of molecule
        """
        return self._molecule_name

    @property
    def mixProfile(self):
        """
        **Requires implementation**

        Should return mix profile of molecule/gas at each layer

        Returns
        -------
        mix: :obj:`array`
            Mix ratio for molecule at each layer

        """
        raise NotImplementedError

    def dissociatedMix(self, T, P, mix_ratio):
        """
        Parameters
        ----------
        T:

        P:

        Returns
        -------
        mix: :obj:`array`
            Mix ratio of a molecule after dissociation

        """
        if self.dissociation:
            scalar = False
            if T.ndim == 0:
                scalar = True
            T = np.asarray(T)
            # diss = np.ones(T.shape)
            diss = np.copy(mix_ratio)
            diss = (1. / np.power(1. / np.sqrt(mix_ratio)
                         + 1. / np.sqrt(np.power(10, self.beta / T - self.gamma)
                           * np.power(P*1e-5, self.alpha)), 2))
            if scalar:
                return np.squeeze(diss)
            return diss
        else:
            return mix_ratio

    def initialize_profile(self, nlayers=None, temperature_profile=None,
                           pressure_profile=None, altitude_profile=None, model=None):
        """
        Initializes and computes mix profile

        Parameters
        ----------
        nlayers: int
            Number of layers in atmosphere

        temperature_profile: :obj:`array`
            Temperature profile of atmosphere in K. Length must be
            equal to ``nlayers``

        pressure_profile: :obj:`array`
            Pressure profile of atmosphere in Pa. Length must be
            equal to ``nlayers``

        altitude_profile: :obj:`array`
            Altitude profile of atmosphere in m. Length must be
            equal to ``nlayers``

        """
        pass

    def write(self, output):
        """
        Writes class and arguments to file

        Parameters
        ----------
        output: :class:`~taurex.output.output.Output`

        """
        gas_entry = output.create_group(self.molecule)
        gas_entry.write_string('gas_type', self.__class__.__name__)
        gas_entry.write_string('molecule_name', self._molecule_name)
        if self.dissociation:
            gas_entry.write_string('alpha', self.alpha)
            gas_entry.write_string('beta', self.beta)
            gas_entry.write_string('gamma', self.gamma)
        return gas_entry

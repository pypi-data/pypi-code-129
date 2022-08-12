from taurex.chemistry import Chemistry # Chemistry from main taurex code
from .taurexchemistry import TaurexChemistry as Taurex2DChemistry # 2D-compatible version of taurex chemistry
from .taurexchemistry import InvalidChemistryException
import numpy as np
from taurex.util import *
from taurex.data.fittable import Fittable, derivedparam

class Chemistry2D(Taurex2DChemistry, Chemistry):
    """
    Chemical model in a 2D polar grid (see :class:`~taurex.model.transmission2D.Transmission2DModel`).
    Same behavior as 1D chemistry but adding an extra dimension.

    2D Molecular profiles available are:
        * :class:`~taurex_2d.data.profiles.chemistry.gas.gas2D.Gas2D`

    Parameters
    ----------

    fill_gases : str or obj:`list`
        Either a single gas or list of gases to fill the atmosphere with

    ratio : float or :obj:`list`
        If a bunch of molecules are used to fill an atmosphere, whats the ratio between them?
        The first fill gas is considered the main one with others defined as ``molecule / main_molecule``
    """
    def __init__(self,fill_gases=['H2','He'],ratio=0.17567):
        self.p_iso = None
        Taurex2DChemistry.__init__(self, fill_gases=fill_gases, ratio=ratio)

    @classmethod
    def input_keywords(cls):
        return ['2d-constant',]

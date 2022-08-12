"""_1232.py

CADMagnetsForLayer
"""


from mastapy.electric_machines import _1258
from mastapy._internal.python_net import python_net_import

_CAD_MAGNETS_FOR_LAYER = python_net_import('SMT.MastaAPI.ElectricMachines', 'CADMagnetsForLayer')


__docformat__ = 'restructuredtext en'
__all__ = ('CADMagnetsForLayer',)


class CADMagnetsForLayer(_1258.MagnetDesign):
    """CADMagnetsForLayer

    This is a mastapy class.
    """

    TYPE = _CAD_MAGNETS_FOR_LAYER

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CADMagnetsForLayer.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

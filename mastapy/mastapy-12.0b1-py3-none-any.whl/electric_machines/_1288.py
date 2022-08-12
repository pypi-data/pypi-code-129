"""_1288.py

WindingMaterialDatabase
"""


from mastapy.materials import _261
from mastapy.electric_machines import _1287
from mastapy._internal.python_net import python_net_import

_WINDING_MATERIAL_DATABASE = python_net_import('SMT.MastaAPI.ElectricMachines', 'WindingMaterialDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('WindingMaterialDatabase',)


class WindingMaterialDatabase(_261.MaterialDatabase['_1287.WindingMaterial']):
    """WindingMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _WINDING_MATERIAL_DATABASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WindingMaterialDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

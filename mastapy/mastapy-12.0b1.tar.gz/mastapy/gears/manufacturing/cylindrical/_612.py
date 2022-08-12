"""_612.py

CylindricalMeshManufacturingConfig
"""


from typing import List

from mastapy.gears.manufacturing.cylindrical.cutter_simulation import _721, _724, _725
from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import _1211
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MESH_MANUFACTURING_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'CylindricalMeshManufacturingConfig')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalMeshManufacturingConfig',)


class CylindricalMeshManufacturingConfig(_1211.GearMeshImplementationDetail):
    """CylindricalMeshManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MESH_MANUFACTURING_CONFIG

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalMeshManufacturingConfig.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_a_as_manufactured(self) -> 'List[_721.CutterSimulationCalc]':
        """List[CutterSimulationCalc]: 'GearAAsManufactured' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearAAsManufactured
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_b_as_manufactured(self) -> 'List[_721.CutterSimulationCalc]':
        """List[CutterSimulationCalc]: 'GearBAsManufactured' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBAsManufactured
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshed_gear_a_as_manufactured(self) -> 'List[_724.CylindricalManufacturedRealGearInMesh]':
        """List[CylindricalManufacturedRealGearInMesh]: 'MeshedGearAAsManufactured' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshedGearAAsManufactured
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshed_gear_a_as_manufactured_virtual(self) -> 'List[_725.CylindricalManufacturedVirtualGearInMesh]':
        """List[CylindricalManufacturedVirtualGearInMesh]: 'MeshedGearAAsManufacturedVirtual' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshedGearAAsManufacturedVirtual
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshed_gear_b_as_manufactured(self) -> 'List[_724.CylindricalManufacturedRealGearInMesh]':
        """List[CylindricalManufacturedRealGearInMesh]: 'MeshedGearBAsManufactured' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshedGearBAsManufactured
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshed_gear_b_as_manufactured_virtual(self) -> 'List[_725.CylindricalManufacturedVirtualGearInMesh]':
        """List[CylindricalManufacturedVirtualGearInMesh]: 'MeshedGearBAsManufacturedVirtual' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshedGearBAsManufacturedVirtual
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

"""_615.py

CylindricalSetManufacturingConfig
"""


from typing import List

from mastapy.gears.manufacturing.cylindrical import _602, _612
from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import _1217
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_SET_MANUFACTURING_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'CylindricalSetManufacturingConfig')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalSetManufacturingConfig',)


class CylindricalSetManufacturingConfig(_1217.GearSetImplementationDetail):
    """CylindricalSetManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_SET_MANUFACTURING_CONFIG

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalSetManufacturingConfig.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cylindrical_gear_manufacturing_configurations(self) -> 'List[_602.CylindricalGearManufacturingConfig]':
        """List[CylindricalGearManufacturingConfig]: 'CylindricalGearManufacturingConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearManufacturingConfigurations
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_mesh_manufacturing_configurations(self) -> 'List[_612.CylindricalMeshManufacturingConfig]':
        """List[CylindricalMeshManufacturingConfig]: 'CylindricalMeshManufacturingConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalMeshManufacturingConfigurations
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def duplicate(self) -> 'CylindricalSetManufacturingConfig':
        """ 'Duplicate' is the original name of this method.

        Returns:
            mastapy.gears.manufacturing.cylindrical.CylindricalSetManufacturingConfig
        """

        method_result = self.wrapped.Duplicate()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

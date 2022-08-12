"""_781.py

ConicalSetManufacturingConfig
"""


from typing import List

from mastapy._internal.implicit import enum_with_selected_value
from mastapy.gears.gear_designs.conical import _1145, _1146
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy.gears.manufacturing.bevel import _766, _775, _783
from mastapy._internal.python_net import python_net_import

_CONICAL_SET_MANUFACTURING_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalSetManufacturingConfig')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalSetManufacturingConfig',)


class ConicalSetManufacturingConfig(_783.ConicalSetMicroGeometryConfigBase):
    """ConicalSetManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_SET_MANUFACTURING_CONFIG

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalSetManufacturingConfig.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def machine_setting_calculation_method(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ConicalMachineSettingCalculationMethods':
        """enum_with_selected_value.EnumWithSelectedValue_ConicalMachineSettingCalculationMethods: 'MachineSettingCalculationMethod' is the original name of this property."""

        temp = self.wrapped.MachineSettingCalculationMethod
        value = enum_with_selected_value.EnumWithSelectedValue_ConicalMachineSettingCalculationMethods.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @machine_setting_calculation_method.setter
    def machine_setting_calculation_method(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ConicalMachineSettingCalculationMethods.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ConicalMachineSettingCalculationMethods.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.MachineSettingCalculationMethod = value

    @property
    def manufacture_method(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ConicalManufactureMethods':
        """enum_with_selected_value.EnumWithSelectedValue_ConicalManufactureMethods: 'ManufactureMethod' is the original name of this property."""

        temp = self.wrapped.ManufactureMethod
        value = enum_with_selected_value.EnumWithSelectedValue_ConicalManufactureMethods.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @manufacture_method.setter
    def manufacture_method(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ConicalManufactureMethods.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ConicalManufactureMethods.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ManufactureMethod = value

    @property
    def gear_manufacturing_configurations(self) -> 'List[_766.ConicalGearManufacturingConfig]':
        """List[ConicalGearManufacturingConfig]: 'GearManufacturingConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearManufacturingConfigurations
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshes(self) -> 'List[_775.ConicalMeshManufacturingConfig]':
        """List[ConicalMeshManufacturingConfig]: 'Meshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Meshes
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def duplicate(self) -> 'ConicalSetManufacturingConfig':
        """ 'Duplicate' is the original name of this method.

        Returns:
            mastapy.gears.manufacturing.bevel.ConicalSetManufacturingConfig
        """

        method_result = self.wrapped.Duplicate()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

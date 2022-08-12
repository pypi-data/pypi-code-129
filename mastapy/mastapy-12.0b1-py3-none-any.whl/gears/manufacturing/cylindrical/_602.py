"""_602.py

CylindricalGearManufacturingConfig
"""


from mastapy._internal.python_net import python_net_import
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import enum_with_selected_value, overridable
from mastapy.gears.manufacturing.cylindrical import _613, _614, _601
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.gear_designs.cylindrical import _1003, _1032
from mastapy._internal.cast_exception import CastException
from mastapy.gears.manufacturing.cylindrical.cutters import (
    _703, _697, _698, _699,
    _700, _702, _704, _705,
    _708
)
from mastapy.gears.manufacturing.cylindrical.cutter_simulation import (
    _729, _726, _734, _732,
    _723
)
from mastapy.gears.manufacturing.cylindrical.process_simulation import _629, _630, _631
from mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash import _1079
from mastapy.gears.analysis import _1207

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_CYLINDRICAL_GEAR_MANUFACTURING_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'CylindricalGearManufacturingConfig')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearManufacturingConfig',)


class CylindricalGearManufacturingConfig(_1207.GearImplementationDetail):
    """CylindricalGearManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MANUFACTURING_CONFIG

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearManufacturingConfig.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def finish_cutter_database_selector(self) -> 'str':
        """str: 'FinishCutterDatabaseSelector' is the original name of this property."""

        temp = self.wrapped.FinishCutterDatabaseSelector.SelectedItemName
        return temp

    @finish_cutter_database_selector.setter
    def finish_cutter_database_selector(self, value: 'str'):
        self.wrapped.FinishCutterDatabaseSelector.SetSelectedItem(str(value) if value else '')

    @property
    def finishing_method(self) -> 'enum_with_selected_value.EnumWithSelectedValue_CylindricalMftFinishingMethods':
        """enum_with_selected_value.EnumWithSelectedValue_CylindricalMftFinishingMethods: 'FinishingMethod' is the original name of this property."""

        temp = self.wrapped.FinishingMethod
        value = enum_with_selected_value.EnumWithSelectedValue_CylindricalMftFinishingMethods.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @finishing_method.setter
    def finishing_method(self, value: 'enum_with_selected_value.EnumWithSelectedValue_CylindricalMftFinishingMethods.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_CylindricalMftFinishingMethods.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.FinishingMethod = value

    @property
    def minimum_finish_cutter_gear_root_clearance_factor(self) -> 'float':
        """float: 'MinimumFinishCutterGearRootClearanceFactor' is the original name of this property."""

        temp = self.wrapped.MinimumFinishCutterGearRootClearanceFactor
        return temp

    @minimum_finish_cutter_gear_root_clearance_factor.setter
    def minimum_finish_cutter_gear_root_clearance_factor(self, value: 'float'):
        self.wrapped.MinimumFinishCutterGearRootClearanceFactor = float(value) if value else 0.0

    @property
    def number_of_points_for_reporting_main_profile_finish_stock(self) -> 'overridable.Overridable_int':
        """overridable.Overridable_int: 'NumberOfPointsForReportingMainProfileFinishStock' is the original name of this property."""

        temp = self.wrapped.NumberOfPointsForReportingMainProfileFinishStock
        return constructor.new_from_mastapy_type(overridable.Overridable_int)(temp) if temp is not None else None

    @number_of_points_for_reporting_main_profile_finish_stock.setter
    def number_of_points_for_reporting_main_profile_finish_stock(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0, is_overridden)
        self.wrapped.NumberOfPointsForReportingMainProfileFinishStock = value

    @property
    def rough_cutter_database_selector(self) -> 'str':
        """str: 'RoughCutterDatabaseSelector' is the original name of this property."""

        temp = self.wrapped.RoughCutterDatabaseSelector.SelectedItemName
        return temp

    @rough_cutter_database_selector.setter
    def rough_cutter_database_selector(self, value: 'str'):
        self.wrapped.RoughCutterDatabaseSelector.SetSelectedItem(str(value) if value else '')

    @property
    def roughing_method(self) -> 'enum_with_selected_value.EnumWithSelectedValue_CylindricalMftRoughingMethods':
        """enum_with_selected_value.EnumWithSelectedValue_CylindricalMftRoughingMethods: 'RoughingMethod' is the original name of this property."""

        temp = self.wrapped.RoughingMethod
        value = enum_with_selected_value.EnumWithSelectedValue_CylindricalMftRoughingMethods.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @roughing_method.setter
    def roughing_method(self, value: 'enum_with_selected_value.EnumWithSelectedValue_CylindricalMftRoughingMethods.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_CylindricalMftRoughingMethods.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.RoughingMethod = value

    @property
    def design(self) -> '_1003.CylindricalGearDesign':
        """CylindricalGearDesign: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design
        if _1003.CylindricalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast design to CylindricalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def finish_cutter(self) -> '_703.CylindricalGearRealCutterDesign':
        """CylindricalGearRealCutterDesign: 'FinishCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishCutter
        if _703.CylindricalGearRealCutterDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast finish_cutter to CylindricalGearRealCutterDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def finish_cutter_of_type_cylindrical_gear_form_grinding_wheel(self) -> '_697.CylindricalGearFormGrindingWheel':
        """CylindricalGearFormGrindingWheel: 'FinishCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishCutter
        if _697.CylindricalGearFormGrindingWheel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast finish_cutter to CylindricalGearFormGrindingWheel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def finish_cutter_of_type_cylindrical_gear_grinding_worm(self) -> '_698.CylindricalGearGrindingWorm':
        """CylindricalGearGrindingWorm: 'FinishCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishCutter
        if _698.CylindricalGearGrindingWorm.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast finish_cutter to CylindricalGearGrindingWorm. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def finish_cutter_of_type_cylindrical_gear_hob_design(self) -> '_699.CylindricalGearHobDesign':
        """CylindricalGearHobDesign: 'FinishCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishCutter
        if _699.CylindricalGearHobDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast finish_cutter to CylindricalGearHobDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def finish_cutter_of_type_cylindrical_gear_plunge_shaver(self) -> '_700.CylindricalGearPlungeShaver':
        """CylindricalGearPlungeShaver: 'FinishCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishCutter
        if _700.CylindricalGearPlungeShaver.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast finish_cutter to CylindricalGearPlungeShaver. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def finish_cutter_of_type_cylindrical_gear_rack_design(self) -> '_702.CylindricalGearRackDesign':
        """CylindricalGearRackDesign: 'FinishCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishCutter
        if _702.CylindricalGearRackDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast finish_cutter to CylindricalGearRackDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def finish_cutter_of_type_cylindrical_gear_shaper(self) -> '_704.CylindricalGearShaper':
        """CylindricalGearShaper: 'FinishCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishCutter
        if _704.CylindricalGearShaper.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast finish_cutter to CylindricalGearShaper. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def finish_cutter_of_type_cylindrical_gear_shaver(self) -> '_705.CylindricalGearShaver':
        """CylindricalGearShaver: 'FinishCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishCutter
        if _705.CylindricalGearShaver.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast finish_cutter to CylindricalGearShaver. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def finish_cutter_of_type_involute_cutter_design(self) -> '_708.InvoluteCutterDesign':
        """InvoluteCutterDesign: 'FinishCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishCutter
        if _708.InvoluteCutterDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast finish_cutter to InvoluteCutterDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def finish_cutter_simulation(self) -> '_729.GearCutterSimulation':
        """GearCutterSimulation: 'FinishCutterSimulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishCutterSimulation
        if _729.GearCutterSimulation.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast finish_cutter_simulation to GearCutterSimulation. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def finish_cutter_simulation_of_type_finish_cutter_simulation(self) -> '_726.FinishCutterSimulation':
        """FinishCutterSimulation: 'FinishCutterSimulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishCutterSimulation
        if _726.FinishCutterSimulation.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast finish_cutter_simulation to FinishCutterSimulation. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def finish_cutter_simulation_of_type_rough_cutter_simulation(self) -> '_734.RoughCutterSimulation':
        """RoughCutterSimulation: 'FinishCutterSimulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishCutterSimulation
        if _734.RoughCutterSimulation.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast finish_cutter_simulation to RoughCutterSimulation. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def finish_manufacturing_process_controls(self) -> '_732.ManufacturingProcessControls':
        """ManufacturingProcessControls: 'FinishManufacturingProcessControls' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishManufacturingProcessControls
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def finish_process_simulation(self) -> '_629.CutterProcessSimulation':
        """CutterProcessSimulation: 'FinishProcessSimulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishProcessSimulation
        if _629.CutterProcessSimulation.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast finish_process_simulation to CutterProcessSimulation. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def finish_process_simulation_of_type_form_wheel_grinding_process_simulation(self) -> '_630.FormWheelGrindingProcessSimulation':
        """FormWheelGrindingProcessSimulation: 'FinishProcessSimulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishProcessSimulation
        if _630.FormWheelGrindingProcessSimulation.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast finish_process_simulation to FormWheelGrindingProcessSimulation. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def finish_process_simulation_of_type_shaping_process_simulation(self) -> '_631.ShapingProcessSimulation':
        """ShapingProcessSimulation: 'FinishProcessSimulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishProcessSimulation
        if _631.ShapingProcessSimulation.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast finish_process_simulation to ShapingProcessSimulation. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def finish_stock_specification(self) -> '_1079.FinishStockSpecification':
        """FinishStockSpecification: 'FinishStockSpecification' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishStockSpecification
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def finished_gear_specification(self) -> '_723.CylindricalGearSpecification':
        """CylindricalGearSpecification: 'FinishedGearSpecification' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishedGearSpecification
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_blank(self) -> '_601.CylindricalGearBlank':
        """CylindricalGearBlank: 'GearBlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBlank
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rough_cutter(self) -> '_703.CylindricalGearRealCutterDesign':
        """CylindricalGearRealCutterDesign: 'RoughCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughCutter
        if _703.CylindricalGearRealCutterDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rough_cutter to CylindricalGearRealCutterDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rough_cutter_of_type_cylindrical_gear_form_grinding_wheel(self) -> '_697.CylindricalGearFormGrindingWheel':
        """CylindricalGearFormGrindingWheel: 'RoughCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughCutter
        if _697.CylindricalGearFormGrindingWheel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rough_cutter to CylindricalGearFormGrindingWheel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rough_cutter_of_type_cylindrical_gear_grinding_worm(self) -> '_698.CylindricalGearGrindingWorm':
        """CylindricalGearGrindingWorm: 'RoughCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughCutter
        if _698.CylindricalGearGrindingWorm.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rough_cutter to CylindricalGearGrindingWorm. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rough_cutter_of_type_cylindrical_gear_hob_design(self) -> '_699.CylindricalGearHobDesign':
        """CylindricalGearHobDesign: 'RoughCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughCutter
        if _699.CylindricalGearHobDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rough_cutter to CylindricalGearHobDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rough_cutter_of_type_cylindrical_gear_plunge_shaver(self) -> '_700.CylindricalGearPlungeShaver':
        """CylindricalGearPlungeShaver: 'RoughCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughCutter
        if _700.CylindricalGearPlungeShaver.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rough_cutter to CylindricalGearPlungeShaver. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rough_cutter_of_type_cylindrical_gear_rack_design(self) -> '_702.CylindricalGearRackDesign':
        """CylindricalGearRackDesign: 'RoughCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughCutter
        if _702.CylindricalGearRackDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rough_cutter to CylindricalGearRackDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rough_cutter_of_type_cylindrical_gear_shaper(self) -> '_704.CylindricalGearShaper':
        """CylindricalGearShaper: 'RoughCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughCutter
        if _704.CylindricalGearShaper.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rough_cutter to CylindricalGearShaper. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rough_cutter_of_type_cylindrical_gear_shaver(self) -> '_705.CylindricalGearShaver':
        """CylindricalGearShaver: 'RoughCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughCutter
        if _705.CylindricalGearShaver.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rough_cutter to CylindricalGearShaver. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rough_cutter_of_type_involute_cutter_design(self) -> '_708.InvoluteCutterDesign':
        """InvoluteCutterDesign: 'RoughCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughCutter
        if _708.InvoluteCutterDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rough_cutter to InvoluteCutterDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rough_cutter_simulation(self) -> '_729.GearCutterSimulation':
        """GearCutterSimulation: 'RoughCutterSimulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughCutterSimulation
        if _729.GearCutterSimulation.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rough_cutter_simulation to GearCutterSimulation. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rough_cutter_simulation_of_type_finish_cutter_simulation(self) -> '_726.FinishCutterSimulation':
        """FinishCutterSimulation: 'RoughCutterSimulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughCutterSimulation
        if _726.FinishCutterSimulation.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rough_cutter_simulation to FinishCutterSimulation. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rough_cutter_simulation_of_type_rough_cutter_simulation(self) -> '_734.RoughCutterSimulation':
        """RoughCutterSimulation: 'RoughCutterSimulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughCutterSimulation
        if _734.RoughCutterSimulation.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rough_cutter_simulation to RoughCutterSimulation. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rough_gear_specification(self) -> '_723.CylindricalGearSpecification':
        """CylindricalGearSpecification: 'RoughGearSpecification' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughGearSpecification
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rough_manufacturing_process_controls(self) -> '_732.ManufacturingProcessControls':
        """ManufacturingProcessControls: 'RoughManufacturingProcessControls' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughManufacturingProcessControls
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rough_process_simulation(self) -> '_629.CutterProcessSimulation':
        """CutterProcessSimulation: 'RoughProcessSimulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughProcessSimulation
        if _629.CutterProcessSimulation.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rough_process_simulation to CutterProcessSimulation. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rough_process_simulation_of_type_form_wheel_grinding_process_simulation(self) -> '_630.FormWheelGrindingProcessSimulation':
        """FormWheelGrindingProcessSimulation: 'RoughProcessSimulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughProcessSimulation
        if _630.FormWheelGrindingProcessSimulation.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rough_process_simulation to FormWheelGrindingProcessSimulation. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rough_process_simulation_of_type_shaping_process_simulation(self) -> '_631.ShapingProcessSimulation':
        """ShapingProcessSimulation: 'RoughProcessSimulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughProcessSimulation
        if _631.ShapingProcessSimulation.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rough_process_simulation to ShapingProcessSimulation. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def create_new_finish_cutter_compatible_with_gear_in_design_mode(self):
        """ 'CreateNewFinishCutterCompatibleWithGearInDesignMode' is the original name of this method."""

        self.wrapped.CreateNewFinishCutterCompatibleWithGearInDesignMode()

    def create_new_rough_cutter_compatible_with_gear_in_design_mode(self):
        """ 'CreateNewRoughCutterCompatibleWithGearInDesignMode' is the original name of this method."""

        self.wrapped.CreateNewRoughCutterCompatibleWithGearInDesignMode()

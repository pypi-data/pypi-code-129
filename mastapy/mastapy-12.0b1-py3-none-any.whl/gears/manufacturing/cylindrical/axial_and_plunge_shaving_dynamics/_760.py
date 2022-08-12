"""_760.py

ShavingDynamicsViewModel
"""


from typing import List, Generic, TypeVar

from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
    _739, _756, _742, _743,
    _748, _749, _751, _761,
    _755
)
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.gears.gear_designs.cylindrical import _1017, _1069
from mastapy.utility_gui.charts import (
    _1815, _1805, _1810, _1812
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.implicit import enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.python_net import python_net_import

_SHAVING_DYNAMICS_VIEW_MODEL = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics', 'ShavingDynamicsViewModel')


__docformat__ = 'restructuredtext en'
__all__ = ('ShavingDynamicsViewModel',)


T = TypeVar('T', bound='_755.ShavingDynamics')


class ShavingDynamicsViewModel(_761.ShavingDynamicsViewModelBase, Generic[T]):
    """ShavingDynamicsViewModel

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _SHAVING_DYNAMICS_VIEW_MODEL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShavingDynamicsViewModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_profile_range_calculation_source(self) -> '_739.ActiveProfileRangeCalculationSource':
        """ActiveProfileRangeCalculationSource: 'ActiveProfileRangeCalculationSource' is the original name of this property."""

        temp = self.wrapped.ActiveProfileRangeCalculationSource
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_739.ActiveProfileRangeCalculationSource)(value) if value is not None else None

    @active_profile_range_calculation_source.setter
    def active_profile_range_calculation_source(self, value: '_739.ActiveProfileRangeCalculationSource'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ActiveProfileRangeCalculationSource = value

    @property
    def chart_display_method(self) -> '_1017.CylindricalGearProfileMeasurementType':
        """CylindricalGearProfileMeasurementType: 'ChartDisplayMethod' is the original name of this property."""

        temp = self.wrapped.ChartDisplayMethod
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1017.CylindricalGearProfileMeasurementType)(value) if value is not None else None

    @chart_display_method.setter
    def chart_display_method(self, value: '_1017.CylindricalGearProfileMeasurementType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ChartDisplayMethod = value

    @property
    def redressing_chart(self) -> '_1815.TwoDChartDefinition':
        """TwoDChartDefinition: 'RedressingChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingChart
        if _1815.TwoDChartDefinition.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast redressing_chart to TwoDChartDefinition. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_measurement_method(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ThicknessType':
        """enum_with_selected_value.EnumWithSelectedValue_ThicknessType: 'SelectedMeasurementMethod' is the original name of this property."""

        temp = self.wrapped.SelectedMeasurementMethod
        value = enum_with_selected_value.EnumWithSelectedValue_ThicknessType.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @selected_measurement_method.setter
    def selected_measurement_method(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ThicknessType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ThicknessType.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.SelectedMeasurementMethod = value

    @property
    def shaver_tip_diameter_adjustment(self) -> 'float':
        """float: 'ShaverTipDiameterAdjustment' is the original name of this property."""

        temp = self.wrapped.ShaverTipDiameterAdjustment
        return temp

    @shaver_tip_diameter_adjustment.setter
    def shaver_tip_diameter_adjustment(self, value: 'float'):
        self.wrapped.ShaverTipDiameterAdjustment = float(value) if value else 0.0

    @property
    def use_shaver_from_database(self) -> 'bool':
        """bool: 'UseShaverFromDatabase' is the original name of this property."""

        temp = self.wrapped.UseShaverFromDatabase
        return temp

    @use_shaver_from_database.setter
    def use_shaver_from_database(self, value: 'bool'):
        self.wrapped.UseShaverFromDatabase = bool(value) if value else False

    @property
    def calculation(self) -> '_756.ShavingDynamicsCalculation[T]':
        """ShavingDynamicsCalculation[T]: 'Calculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Calculation
        if _756.ShavingDynamicsCalculation[T].TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast calculation to ShavingDynamicsCalculation[T]. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[T](temp) if temp is not None else None

    @property
    def calculation_of_type_conventional_shaving_dynamics_calculation_for_designed_gears(self) -> '_742.ConventionalShavingDynamicsCalculationForDesignedGears':
        """ConventionalShavingDynamicsCalculationForDesignedGears: 'Calculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Calculation
        if _742.ConventionalShavingDynamicsCalculationForDesignedGears.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast calculation to ConventionalShavingDynamicsCalculationForDesignedGears. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def calculation_of_type_conventional_shaving_dynamics_calculation_for_hobbed_gears(self) -> '_743.ConventionalShavingDynamicsCalculationForHobbedGears':
        """ConventionalShavingDynamicsCalculationForHobbedGears: 'Calculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Calculation
        if _743.ConventionalShavingDynamicsCalculationForHobbedGears.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast calculation to ConventionalShavingDynamicsCalculationForHobbedGears. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def calculation_of_type_plunge_shaving_dynamics_calculation_for_designed_gears(self) -> '_748.PlungeShavingDynamicsCalculationForDesignedGears':
        """PlungeShavingDynamicsCalculationForDesignedGears: 'Calculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Calculation
        if _748.PlungeShavingDynamicsCalculationForDesignedGears.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast calculation to PlungeShavingDynamicsCalculationForDesignedGears. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def calculation_of_type_plunge_shaving_dynamics_calculation_for_hobbed_gears(self) -> '_749.PlungeShavingDynamicsCalculationForHobbedGears':
        """PlungeShavingDynamicsCalculationForHobbedGears: 'Calculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Calculation
        if _749.PlungeShavingDynamicsCalculationForHobbedGears.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast calculation to PlungeShavingDynamicsCalculationForHobbedGears. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def redressing_settings(self) -> 'List[_751.RedressingSettings[T]]':
        """List[RedressingSettings[T]]: 'RedressingSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingSettings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def add_shaver_to_database(self):
        """ 'AddShaverToDatabase' is the original name of this method."""

        self.wrapped.AddShaverToDatabase()

    def calculate(self):
        """ 'Calculate' is the original name of this method."""

        self.wrapped.Calculate()

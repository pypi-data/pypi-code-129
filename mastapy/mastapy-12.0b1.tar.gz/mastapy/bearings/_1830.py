"""_1830.py

BearingSettingsItem
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.bearings import _1839, _1832, _1833
from mastapy._internal.implicit import enum_with_selected_value, overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.utility.databases import _1785
from mastapy._internal.python_net import python_net_import

_BEARING_SETTINGS_ITEM = python_net_import('SMT.MastaAPI.Bearings', 'BearingSettingsItem')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingSettingsItem',)


class BearingSettingsItem(_1785.NamedDatabaseItem):
    """BearingSettingsItem

    This is a mastapy class.
    """

    TYPE = _BEARING_SETTINGS_ITEM

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BearingSettingsItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def ball_bearing_weibull_reliability_slope(self) -> 'float':
        """float: 'BallBearingWeibullReliabilitySlope' is the original name of this property."""

        temp = self.wrapped.BallBearingWeibullReliabilitySlope
        return temp

    @ball_bearing_weibull_reliability_slope.setter
    def ball_bearing_weibull_reliability_slope(self, value: 'float'):
        self.wrapped.BallBearingWeibullReliabilitySlope = float(value) if value else 0.0

    @property
    def failure_probability_for_rating_life_percent(self) -> '_1839.RatingLife':
        """RatingLife: 'FailureProbabilityForRatingLifePercent' is the original name of this property."""

        temp = self.wrapped.FailureProbabilityForRatingLifePercent
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1839.RatingLife)(value) if value is not None else None

    @failure_probability_for_rating_life_percent.setter
    def failure_probability_for_rating_life_percent(self, value: '_1839.RatingLife'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.FailureProbabilityForRatingLifePercent = value

    @property
    def include_exponent_and_reduction_factors_in_isots162812008(self) -> '_1832.ExponentAndReductionFactorsInISO16281Calculation':
        """ExponentAndReductionFactorsInISO16281Calculation: 'IncludeExponentAndReductionFactorsInISOTS162812008' is the original name of this property."""

        temp = self.wrapped.IncludeExponentAndReductionFactorsInISOTS162812008
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1832.ExponentAndReductionFactorsInISO16281Calculation)(value) if value is not None else None

    @include_exponent_and_reduction_factors_in_isots162812008.setter
    def include_exponent_and_reduction_factors_in_isots162812008(self, value: '_1832.ExponentAndReductionFactorsInISO16281Calculation'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.IncludeExponentAndReductionFactorsInISOTS162812008 = value

    @property
    def lubricant_film_temperature_calculation_pressure_fed_grease_filled_bearings(self) -> 'enum_with_selected_value.EnumWithSelectedValue_FluidFilmTemperatureOptions':
        """enum_with_selected_value.EnumWithSelectedValue_FluidFilmTemperatureOptions: 'LubricantFilmTemperatureCalculationPressureFedGreaseFilledBearings' is the original name of this property."""

        temp = self.wrapped.LubricantFilmTemperatureCalculationPressureFedGreaseFilledBearings
        value = enum_with_selected_value.EnumWithSelectedValue_FluidFilmTemperatureOptions.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @lubricant_film_temperature_calculation_pressure_fed_grease_filled_bearings.setter
    def lubricant_film_temperature_calculation_pressure_fed_grease_filled_bearings(self, value: 'enum_with_selected_value.EnumWithSelectedValue_FluidFilmTemperatureOptions.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_FluidFilmTemperatureOptions.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LubricantFilmTemperatureCalculationPressureFedGreaseFilledBearings = value

    @property
    def lubricant_film_temperature_calculation_splashed_submerged_bearings(self) -> 'enum_with_selected_value.EnumWithSelectedValue_FluidFilmTemperatureOptions':
        """enum_with_selected_value.EnumWithSelectedValue_FluidFilmTemperatureOptions: 'LubricantFilmTemperatureCalculationSplashedSubmergedBearings' is the original name of this property."""

        temp = self.wrapped.LubricantFilmTemperatureCalculationSplashedSubmergedBearings
        value = enum_with_selected_value.EnumWithSelectedValue_FluidFilmTemperatureOptions.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @lubricant_film_temperature_calculation_splashed_submerged_bearings.setter
    def lubricant_film_temperature_calculation_splashed_submerged_bearings(self, value: 'enum_with_selected_value.EnumWithSelectedValue_FluidFilmTemperatureOptions.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_FluidFilmTemperatureOptions.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.LubricantFilmTemperatureCalculationSplashedSubmergedBearings = value

    @property
    def number_of_strips_for_roller_calculation(self) -> 'overridable.Overridable_int':
        """overridable.Overridable_int: 'NumberOfStripsForRollerCalculation' is the original name of this property."""

        temp = self.wrapped.NumberOfStripsForRollerCalculation
        return constructor.new_from_mastapy_type(overridable.Overridable_int)(temp) if temp is not None else None

    @number_of_strips_for_roller_calculation.setter
    def number_of_strips_for_roller_calculation(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0, is_overridden)
        self.wrapped.NumberOfStripsForRollerCalculation = value

    @property
    def roller_bearing_weibull_reliability_slope(self) -> 'float':
        """float: 'RollerBearingWeibullReliabilitySlope' is the original name of this property."""

        temp = self.wrapped.RollerBearingWeibullReliabilitySlope
        return temp

    @roller_bearing_weibull_reliability_slope.setter
    def roller_bearing_weibull_reliability_slope(self, value: 'float'):
        self.wrapped.RollerBearingWeibullReliabilitySlope = float(value) if value else 0.0

    @property
    def third_weibull_parameter(self) -> 'float':
        """float: 'ThirdWeibullParameter' is the original name of this property."""

        temp = self.wrapped.ThirdWeibullParameter
        return temp

    @third_weibull_parameter.setter
    def third_weibull_parameter(self, value: 'float'):
        self.wrapped.ThirdWeibullParameter = float(value) if value else 0.0

    @property
    def tolerance_used_for_diameter_warnings_and_database_filter(self) -> 'float':
        """float: 'ToleranceUsedForDiameterWarningsAndDatabaseFilter' is the original name of this property."""

        temp = self.wrapped.ToleranceUsedForDiameterWarningsAndDatabaseFilter
        return temp

    @tolerance_used_for_diameter_warnings_and_database_filter.setter
    def tolerance_used_for_diameter_warnings_and_database_filter(self, value: 'float'):
        self.wrapped.ToleranceUsedForDiameterWarningsAndDatabaseFilter = float(value) if value else 0.0

    @property
    def use_plain_journal_bearing_misalignment_factors(self) -> 'bool':
        """bool: 'UsePlainJournalBearingMisalignmentFactors' is the original name of this property."""

        temp = self.wrapped.UsePlainJournalBearingMisalignmentFactors
        return temp

    @use_plain_journal_bearing_misalignment_factors.setter
    def use_plain_journal_bearing_misalignment_factors(self, value: 'bool'):
        self.wrapped.UsePlainJournalBearingMisalignmentFactors = bool(value) if value else False

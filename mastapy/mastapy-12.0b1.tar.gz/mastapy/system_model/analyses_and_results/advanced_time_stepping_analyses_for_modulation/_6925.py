"""_6925.py

AdvancedTimeSteppingAnalysisForModulationOptions
"""


from mastapy.system_model.analyses_and_results.static_loads import (
    _6727, _6719, _6809, _6730,
    _6739, _6744, _6757, _6762,
    _6779, _6800, _6821, _6828,
    _6831, _6834, _6847, _6869,
    _6875, _6878, _6898, _6901
)
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results import _2623
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'AdvancedTimeSteppingAnalysisForModulationOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('AdvancedTimeSteppingAnalysisForModulationOptions',)


class AdvancedTimeSteppingAnalysisForModulationOptions(_0.APIBase):
    """AdvancedTimeSteppingAnalysisForModulationOptions

    This is a mastapy class.
    """

    TYPE = _ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION_OPTIONS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AdvancedTimeSteppingAnalysisForModulationOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def advanced_time_stepping_analysis_method(self) -> '_6727.AdvancedTimeSteppingAnalysisForModulationType':
        """AdvancedTimeSteppingAnalysisForModulationType: 'AdvancedTimeSteppingAnalysisMethod' is the original name of this property."""

        temp = self.wrapped.AdvancedTimeSteppingAnalysisMethod
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_6727.AdvancedTimeSteppingAnalysisForModulationType)(value) if value is not None else None

    @advanced_time_stepping_analysis_method.setter
    def advanced_time_stepping_analysis_method(self, value: '_6727.AdvancedTimeSteppingAnalysisForModulationType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.AdvancedTimeSteppingAnalysisMethod = value

    @property
    def include_time_offset_for_steady_state(self) -> 'bool':
        """bool: 'IncludeTimeOffsetForSteadyState' is the original name of this property."""

        temp = self.wrapped.IncludeTimeOffsetForSteadyState
        return temp

    @include_time_offset_for_steady_state.setter
    def include_time_offset_for_steady_state(self, value: 'bool'):
        self.wrapped.IncludeTimeOffsetForSteadyState = bool(value) if value else False

    @property
    def load_case_for_advanced_time_stepping_analysis_for_modulation_time_options_and_active_fe_parts(self) -> 'list_with_selected_item.ListWithSelectedItem_StaticLoadCase':
        """list_with_selected_item.ListWithSelectedItem_StaticLoadCase: 'LoadCaseForAdvancedTimeSteppingAnalysisForModulationTimeOptionsAndActiveFEParts' is the original name of this property."""

        temp = self.wrapped.LoadCaseForAdvancedTimeSteppingAnalysisForModulationTimeOptionsAndActiveFEParts
        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_StaticLoadCase)(temp) if temp is not None else None

    @load_case_for_advanced_time_stepping_analysis_for_modulation_time_options_and_active_fe_parts.setter
    def load_case_for_advanced_time_stepping_analysis_for_modulation_time_options_and_active_fe_parts(self, value: 'list_with_selected_item.ListWithSelectedItem_StaticLoadCase.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_StaticLoadCase.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_StaticLoadCase.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.LoadCaseForAdvancedTimeSteppingAnalysisForModulationTimeOptionsAndActiveFEParts = value

    @property
    def number_of_periods_for_advanced_time_stepping_analysis(self) -> 'float':
        """float: 'NumberOfPeriodsForAdvancedTimeSteppingAnalysis' is the original name of this property."""

        temp = self.wrapped.NumberOfPeriodsForAdvancedTimeSteppingAnalysis
        return temp

    @number_of_periods_for_advanced_time_stepping_analysis.setter
    def number_of_periods_for_advanced_time_stepping_analysis(self, value: 'float'):
        self.wrapped.NumberOfPeriodsForAdvancedTimeSteppingAnalysis = float(value) if value else 0.0

    @property
    def number_of_steps_for_advanced_time_stepping_analysis(self) -> 'int':
        """int: 'NumberOfStepsForAdvancedTimeSteppingAnalysis' is the original name of this property."""

        temp = self.wrapped.NumberOfStepsForAdvancedTimeSteppingAnalysis
        return temp

    @number_of_steps_for_advanced_time_stepping_analysis.setter
    def number_of_steps_for_advanced_time_stepping_analysis(self, value: 'int'):
        self.wrapped.NumberOfStepsForAdvancedTimeSteppingAnalysis = int(value) if value else 0

    @property
    def number_of_times_per_quasi_step(self) -> 'int':
        """int: 'NumberOfTimesPerQuasiStep' is the original name of this property."""

        temp = self.wrapped.NumberOfTimesPerQuasiStep
        return temp

    @number_of_times_per_quasi_step.setter
    def number_of_times_per_quasi_step(self, value: 'int'):
        self.wrapped.NumberOfTimesPerQuasiStep = int(value) if value else 0

    @property
    def tolerance_for_compatibility_of_atsam_and_te_periods_check(self) -> 'float':
        """float: 'ToleranceForCompatibilityOfATSAMAndTEPeriodsCheck' is the original name of this property."""

        temp = self.wrapped.ToleranceForCompatibilityOfATSAMAndTEPeriodsCheck
        return temp

    @tolerance_for_compatibility_of_atsam_and_te_periods_check.setter
    def tolerance_for_compatibility_of_atsam_and_te_periods_check(self, value: 'float'):
        self.wrapped.ToleranceForCompatibilityOfATSAMAndTEPeriodsCheck = float(value) if value else 0.0

    @property
    def use_this_load_case_for_load_case_for_advanced_time_stepping_analysis_for_modulation_time_options_and_active_fe_parts(self) -> 'bool':
        """bool: 'UseThisLoadCaseForLoadCaseForAdvancedTimeSteppingAnalysisForModulationTimeOptionsAndActiveFEParts' is the original name of this property."""

        temp = self.wrapped.UseThisLoadCaseForLoadCaseForAdvancedTimeSteppingAnalysisForModulationTimeOptionsAndActiveFEParts
        return temp

    @use_this_load_case_for_load_case_for_advanced_time_stepping_analysis_for_modulation_time_options_and_active_fe_parts.setter
    def use_this_load_case_for_load_case_for_advanced_time_stepping_analysis_for_modulation_time_options_and_active_fe_parts(self, value: 'bool'):
        self.wrapped.UseThisLoadCaseForLoadCaseForAdvancedTimeSteppingAnalysisForModulationTimeOptionsAndActiveFEParts = bool(value) if value else False

    @property
    def gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation(self) -> '_6809.GearSetLoadCase':
        """GearSetLoadCase: 'GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation
        if _6809.GearSetLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation to GearSetLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation_of_type_agma_gleason_conical_gear_set_load_case(self) -> '_6730.AGMAGleasonConicalGearSetLoadCase':
        """AGMAGleasonConicalGearSetLoadCase: 'GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation
        if _6730.AGMAGleasonConicalGearSetLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation to AGMAGleasonConicalGearSetLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation_of_type_bevel_differential_gear_set_load_case(self) -> '_6739.BevelDifferentialGearSetLoadCase':
        """BevelDifferentialGearSetLoadCase: 'GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation
        if _6739.BevelDifferentialGearSetLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation to BevelDifferentialGearSetLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation_of_type_bevel_gear_set_load_case(self) -> '_6744.BevelGearSetLoadCase':
        """BevelGearSetLoadCase: 'GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation
        if _6744.BevelGearSetLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation to BevelGearSetLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation_of_type_concept_gear_set_load_case(self) -> '_6757.ConceptGearSetLoadCase':
        """ConceptGearSetLoadCase: 'GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation
        if _6757.ConceptGearSetLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation to ConceptGearSetLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation_of_type_conical_gear_set_load_case(self) -> '_6762.ConicalGearSetLoadCase':
        """ConicalGearSetLoadCase: 'GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation
        if _6762.ConicalGearSetLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation to ConicalGearSetLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation_of_type_cylindrical_gear_set_load_case(self) -> '_6779.CylindricalGearSetLoadCase':
        """CylindricalGearSetLoadCase: 'GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation
        if _6779.CylindricalGearSetLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation to CylindricalGearSetLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation_of_type_face_gear_set_load_case(self) -> '_6800.FaceGearSetLoadCase':
        """FaceGearSetLoadCase: 'GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation
        if _6800.FaceGearSetLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation to FaceGearSetLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation_of_type_hypoid_gear_set_load_case(self) -> '_6821.HypoidGearSetLoadCase':
        """HypoidGearSetLoadCase: 'GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation
        if _6821.HypoidGearSetLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation to HypoidGearSetLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation_of_type_klingelnberg_cyclo_palloid_conical_gear_set_load_case(self) -> '_6828.KlingelnbergCycloPalloidConicalGearSetLoadCase':
        """KlingelnbergCycloPalloidConicalGearSetLoadCase: 'GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation
        if _6828.KlingelnbergCycloPalloidConicalGearSetLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation to KlingelnbergCycloPalloidConicalGearSetLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(self) -> '_6831.KlingelnbergCycloPalloidHypoidGearSetLoadCase':
        """KlingelnbergCycloPalloidHypoidGearSetLoadCase: 'GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation
        if _6831.KlingelnbergCycloPalloidHypoidGearSetLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation to KlingelnbergCycloPalloidHypoidGearSetLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(self) -> '_6834.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase':
        """KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase: 'GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation
        if _6834.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation to KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation_of_type_planetary_gear_set_load_case(self) -> '_6847.PlanetaryGearSetLoadCase':
        """PlanetaryGearSetLoadCase: 'GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation
        if _6847.PlanetaryGearSetLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation to PlanetaryGearSetLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation_of_type_spiral_bevel_gear_set_load_case(self) -> '_6869.SpiralBevelGearSetLoadCase':
        """SpiralBevelGearSetLoadCase: 'GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation
        if _6869.SpiralBevelGearSetLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation to SpiralBevelGearSetLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation_of_type_straight_bevel_diff_gear_set_load_case(self) -> '_6875.StraightBevelDiffGearSetLoadCase':
        """StraightBevelDiffGearSetLoadCase: 'GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation
        if _6875.StraightBevelDiffGearSetLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation to StraightBevelDiffGearSetLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation_of_type_straight_bevel_gear_set_load_case(self) -> '_6878.StraightBevelGearSetLoadCase':
        """StraightBevelGearSetLoadCase: 'GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation
        if _6878.StraightBevelGearSetLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation to StraightBevelGearSetLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation_of_type_worm_gear_set_load_case(self) -> '_6898.WormGearSetLoadCase':
        """WormGearSetLoadCase: 'GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation
        if _6898.WormGearSetLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation to WormGearSetLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation_of_type_zerol_bevel_gear_set_load_case(self) -> '_6901.ZerolBevelGearSetLoadCase':
        """ZerolBevelGearSetLoadCase: 'GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetLoadCaseWithinLoadCaseForAdvancedTimeSteppingAnalysisForModulation
        if _6901.ZerolBevelGearSetLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_load_case_within_load_case_for_advanced_time_stepping_analysis_for_modulation to ZerolBevelGearSetLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def time_options(self) -> '_2623.TimeOptions':
        """TimeOptions: 'TimeOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TimeOptions
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

"""_4467.py

RootAssemblyCompoundParametricStudyTool
"""


from typing import List

from mastapy.system_model.analyses_and_results.load_case_groups import (
    _5583, _5582, _5584, _5587,
    _5588, _5591, _5595
)
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4319, _4320, _4338
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2837
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4380
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'RootAssemblyCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyCompoundParametricStudyTool',)


class RootAssemblyCompoundParametricStudyTool(_4380.AssemblyCompoundParametricStudyTool):
    """RootAssemblyCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RootAssemblyCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def compound_load_case(self) -> '_5583.AbstractLoadCaseGroup':
        """AbstractLoadCaseGroup: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundLoadCase
        if _5583.AbstractLoadCaseGroup.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to AbstractLoadCaseGroup. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_load_case_of_type_abstract_design_state_load_case_group(self) -> '_5582.AbstractDesignStateLoadCaseGroup':
        """AbstractDesignStateLoadCaseGroup: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundLoadCase
        if _5582.AbstractDesignStateLoadCaseGroup.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to AbstractDesignStateLoadCaseGroup. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_load_case_of_type_abstract_static_load_case_group(self) -> '_5584.AbstractStaticLoadCaseGroup':
        """AbstractStaticLoadCaseGroup: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundLoadCase
        if _5584.AbstractStaticLoadCaseGroup.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to AbstractStaticLoadCaseGroup. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_load_case_of_type_design_state(self) -> '_5587.DesignState':
        """DesignState: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundLoadCase
        if _5587.DesignState.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to DesignState. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_load_case_of_type_duty_cycle(self) -> '_5588.DutyCycle':
        """DutyCycle: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundLoadCase
        if _5588.DutyCycle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to DutyCycle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_load_case_of_type_sub_group_in_single_design_state(self) -> '_5591.SubGroupInSingleDesignState':
        """SubGroupInSingleDesignState: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundLoadCase
        if _5591.SubGroupInSingleDesignState.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to SubGroupInSingleDesignState. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_load_case_of_type_time_series_load_case_group(self) -> '_5595.TimeSeriesLoadCaseGroup':
        """TimeSeriesLoadCaseGroup: 'CompoundLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundLoadCase
        if _5595.TimeSeriesLoadCaseGroup.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast compound_load_case to TimeSeriesLoadCaseGroup. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def parametric_analysis_options(self) -> '_4319.ParametricStudyToolOptions':
        """ParametricStudyToolOptions: 'ParametricAnalysisOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParametricAnalysisOptions
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def results_for_reporting(self) -> '_4320.ParametricStudyToolResultsForReporting':
        """ParametricStudyToolResultsForReporting: 'ResultsForReporting' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResultsForReporting
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def root_assembly_duty_cycle_results(self) -> '_2837.DutyCycleEfficiencyResults':
        """DutyCycleEfficiencyResults: 'RootAssemblyDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RootAssemblyDutyCycleResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4338.RootAssemblyParametricStudyTool]':
        """List[RootAssemblyParametricStudyTool]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4338.RootAssemblyParametricStudyTool]':
        """List[RootAssemblyParametricStudyTool]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

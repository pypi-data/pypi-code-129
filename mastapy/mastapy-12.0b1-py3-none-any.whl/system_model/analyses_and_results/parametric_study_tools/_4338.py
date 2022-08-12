"""_4338.py

RootAssemblyParametricStudyTool
"""


from typing import List

from mastapy.system_model.part_model import _2414
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4318, _4320, _4233
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2837
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'RootAssemblyParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyParametricStudyTool',)


class RootAssemblyParametricStudyTool(_4233.AssemblyParametricStudyTool):
    """RootAssemblyParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RootAssemblyParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2414.RootAssembly':
        """RootAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def parametric_study_tool_inputs(self) -> '_4318.ParametricStudyTool':
        """ParametricStudyTool: 'ParametricStudyToolInputs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParametricStudyToolInputs
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
    def root_assembly_duty_cycle_results(self) -> 'List[_2837.DutyCycleEfficiencyResults]':
        """List[DutyCycleEfficiencyResults]: 'RootAssemblyDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RootAssemblyDutyCycleResults
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

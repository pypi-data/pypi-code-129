"""_4377.py

AGMAGleasonConicalGearCompoundParametricStudyTool
"""


from typing import List

from mastapy.system_model.analyses_and_results.parametric_study_tools import _4231
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4405
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'AGMAGleasonConicalGearCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearCompoundParametricStudyTool',)


class AGMAGleasonConicalGearCompoundParametricStudyTool(_4405.ConicalGearCompoundParametricStudyTool):
    """AGMAGleasonConicalGearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_4231.AGMAGleasonConicalGearParametricStudyTool]':
        """List[AGMAGleasonConicalGearParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4231.AGMAGleasonConicalGearParametricStudyTool]':
        """List[AGMAGleasonConicalGearParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

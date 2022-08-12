"""_4418.py

CycloidalDiscCompoundParametricStudyTool
"""


from typing import List

from mastapy.system_model.part_model.cycloidal import _2508
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4271
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4374
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'CycloidalDiscCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscCompoundParametricStudyTool',)


class CycloidalDiscCompoundParametricStudyTool(_4374.AbstractShaftCompoundParametricStudyTool):
    """CycloidalDiscCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_COMPOUND_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CycloidalDiscCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2508.CycloidalDisc':
        """CycloidalDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4271.CycloidalDiscParametricStudyTool]':
        """List[CycloidalDiscParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4271.CycloidalDiscParametricStudyTool]':
        """List[CycloidalDiscParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

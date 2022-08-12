"""_4434.py

GuideDxfModelCompoundParametricStudyTool
"""


from typing import List

from mastapy.system_model.part_model import _2395
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4294
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4398
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'GuideDxfModelCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('GuideDxfModelCompoundParametricStudyTool',)


class GuideDxfModelCompoundParametricStudyTool(_4398.ComponentCompoundParametricStudyTool):
    """GuideDxfModelCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_COMPOUND_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GuideDxfModelCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2395.GuideDxfModel':
        """GuideDxfModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4294.GuideDxfModelParametricStudyTool]':
        """List[GuideDxfModelParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4294.GuideDxfModelParametricStudyTool]':
        """List[GuideDxfModelParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

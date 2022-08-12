"""_4975.py

GuideDxfModelCompoundModalAnalysisAtAStiffness
"""


from typing import List

from mastapy.system_model.part_model import _2395
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4846
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4939
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'GuideDxfModelCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('GuideDxfModelCompoundModalAnalysisAtAStiffness',)


class GuideDxfModelCompoundModalAnalysisAtAStiffness(_4939.ComponentCompoundModalAnalysisAtAStiffness):
    """GuideDxfModelCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GuideDxfModelCompoundModalAnalysisAtAStiffness.TYPE'):
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
    def component_analysis_cases_ready(self) -> 'List[_4846.GuideDxfModelModalAnalysisAtAStiffness]':
        """List[GuideDxfModelModalAnalysisAtAStiffness]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4846.GuideDxfModelModalAnalysisAtAStiffness]':
        """List[GuideDxfModelModalAnalysisAtAStiffness]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

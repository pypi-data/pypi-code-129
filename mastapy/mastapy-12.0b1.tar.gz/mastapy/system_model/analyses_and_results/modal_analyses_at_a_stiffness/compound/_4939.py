"""_4939.py

ComponentCompoundModalAnalysisAtAStiffness
"""


from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4809
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4993
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'ComponentCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('ComponentCompoundModalAnalysisAtAStiffness',)


class ComponentCompoundModalAnalysisAtAStiffness(_4993.PartCompoundModalAnalysisAtAStiffness):
    """ComponentCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ComponentCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_4809.ComponentModalAnalysisAtAStiffness]':
        """List[ComponentModalAnalysisAtAStiffness]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4809.ComponentModalAnalysisAtAStiffness]':
        """List[ComponentModalAnalysisAtAStiffness]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

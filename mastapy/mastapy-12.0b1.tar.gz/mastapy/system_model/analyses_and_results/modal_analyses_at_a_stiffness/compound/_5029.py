"""_5029.py

SynchroniserPartCompoundModalAnalysisAtAStiffness
"""


from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4900
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4953
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'SynchroniserPartCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserPartCompoundModalAnalysisAtAStiffness',)


class SynchroniserPartCompoundModalAnalysisAtAStiffness(_4953.CouplingHalfCompoundModalAnalysisAtAStiffness):
    """SynchroniserPartCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SynchroniserPartCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_4900.SynchroniserPartModalAnalysisAtAStiffness]':
        """List[SynchroniserPartModalAnalysisAtAStiffness]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4900.SynchroniserPartModalAnalysisAtAStiffness]':
        """List[SynchroniserPartModalAnalysisAtAStiffness]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

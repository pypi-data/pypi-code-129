"""_5293.py

UnbalancedMassCompoundModalAnalysisAtASpeed
"""


from typing import List

from mastapy.system_model.part_model import _2417
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5164
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5294
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'UnbalancedMassCompoundModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('UnbalancedMassCompoundModalAnalysisAtASpeed',)


class UnbalancedMassCompoundModalAnalysisAtASpeed(_5294.VirtualComponentCompoundModalAnalysisAtASpeed):
    """UnbalancedMassCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'UnbalancedMassCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2417.UnbalancedMass':
        """UnbalancedMass: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5164.UnbalancedMassModalAnalysisAtASpeed]':
        """List[UnbalancedMassModalAnalysisAtASpeed]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5164.UnbalancedMassModalAnalysisAtASpeed]':
        """List[UnbalancedMassModalAnalysisAtASpeed]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

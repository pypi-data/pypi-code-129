"""_3154.py

SpringDamperHalfCompoundSteadyStateSynchronousResponse
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2540
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3021
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import _3089
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound', 'SpringDamperHalfCompoundSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperHalfCompoundSteadyStateSynchronousResponse',)


class SpringDamperHalfCompoundSteadyStateSynchronousResponse(_3089.CouplingHalfCompoundSteadyStateSynchronousResponse):
    """SpringDamperHalfCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperHalfCompoundSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2540.SpringDamperHalf':
        """SpringDamperHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3021.SpringDamperHalfSteadyStateSynchronousResponse]':
        """List[SpringDamperHalfSteadyStateSynchronousResponse]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3021.SpringDamperHalfSteadyStateSynchronousResponse]':
        """List[SpringDamperHalfSteadyStateSynchronousResponse]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

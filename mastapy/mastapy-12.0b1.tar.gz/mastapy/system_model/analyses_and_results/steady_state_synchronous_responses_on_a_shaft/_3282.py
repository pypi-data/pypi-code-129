"""_3282.py

SpringDamperHalfSteadyStateSynchronousResponseOnAShaft
"""


from mastapy.system_model.part_model.couplings import _2540
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6871
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3217
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'SpringDamperHalfSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperHalfSteadyStateSynchronousResponseOnAShaft',)


class SpringDamperHalfSteadyStateSynchronousResponseOnAShaft(_3217.CouplingHalfSteadyStateSynchronousResponseOnAShaft):
    """SpringDamperHalfSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperHalfSteadyStateSynchronousResponseOnAShaft.TYPE'):
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
    def component_load_case(self) -> '_6871.SpringDamperHalfLoadCase':
        """SpringDamperHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

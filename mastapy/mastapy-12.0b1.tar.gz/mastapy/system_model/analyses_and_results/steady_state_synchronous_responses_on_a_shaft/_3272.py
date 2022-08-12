"""_3272.py

RollingRingSteadyStateSynchronousResponseOnAShaft
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2535
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6861
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3217
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'RollingRingSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingSteadyStateSynchronousResponseOnAShaft',)


class RollingRingSteadyStateSynchronousResponseOnAShaft(_3217.CouplingHalfSteadyStateSynchronousResponseOnAShaft):
    """RollingRingSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RollingRingSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2535.RollingRing':
        """RollingRing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6861.RollingRingLoadCase':
        """RollingRingLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[RollingRingSteadyStateSynchronousResponseOnAShaft]':
        """List[RollingRingSteadyStateSynchronousResponseOnAShaft]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

"""_3464.py

ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed
"""


from mastapy.system_model.connections_and_sockets.couplings import _2284
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6752
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3475
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed', 'ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed',)


class ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed(_3475.CouplingConnectionSteadyStateSynchronousResponseAtASpeed):
    """ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingConnectionSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2284.ConceptCouplingConnection':
        """ConceptCouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6752.ConceptCouplingConnectionLoadCase':
        """ConceptCouplingConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

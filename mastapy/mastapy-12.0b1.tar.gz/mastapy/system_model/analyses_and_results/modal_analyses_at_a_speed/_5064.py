"""_5064.py

ClutchConnectionModalAnalysisAtASpeed
"""


from mastapy.system_model.connections_and_sockets.couplings import _2282
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6747
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5080
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'ClutchConnectionModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchConnectionModalAnalysisAtASpeed',)


class ClutchConnectionModalAnalysisAtASpeed(_5080.CouplingConnectionModalAnalysisAtASpeed):
    """ClutchConnectionModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchConnectionModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2282.ClutchConnection':
        """ClutchConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6747.ClutchConnectionLoadCase':
        """ClutchConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

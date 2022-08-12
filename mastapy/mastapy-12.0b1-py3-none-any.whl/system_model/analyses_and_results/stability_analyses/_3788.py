"""_3788.py

RingPinsToDiscConnectionStabilityAnalysis
"""


from mastapy.system_model.connections_and_sockets.cycloidal import _2281
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6858
from mastapy.system_model.analyses_and_results.stability_analyses import _3763
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'RingPinsToDiscConnectionStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RingPinsToDiscConnectionStabilityAnalysis',)


class RingPinsToDiscConnectionStabilityAnalysis(_3763.InterMountableComponentConnectionStabilityAnalysis):
    """RingPinsToDiscConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RingPinsToDiscConnectionStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2281.RingPinsToDiscConnection':
        """RingPinsToDiscConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6858.RingPinsToDiscConnectionLoadCase':
        """RingPinsToDiscConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

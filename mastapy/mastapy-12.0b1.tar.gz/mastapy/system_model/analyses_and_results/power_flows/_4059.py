"""_4059.py

RollingRingConnectionPowerFlow
"""


from mastapy.system_model.connections_and_sockets import _2232
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6860
from mastapy.system_model.analyses_and_results.power_flows import _4030
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'RollingRingConnectionPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingConnectionPowerFlow',)


class RollingRingConnectionPowerFlow(_4030.InterMountableComponentConnectionPowerFlow):
    """RollingRingConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_CONNECTION_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RollingRingConnectionPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2232.RollingRingConnection':
        """RollingRingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6860.RollingRingConnectionLoadCase':
        """RollingRingConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

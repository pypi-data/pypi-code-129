"""_3985.py

ClutchConnectionPowerFlow
"""


from mastapy.system_model.connections_and_sockets.couplings import _2282
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6747
from mastapy.system_model.analyses_and_results.power_flows import _4001
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'ClutchConnectionPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchConnectionPowerFlow',)


class ClutchConnectionPowerFlow(_4001.CouplingConnectionPowerFlow):
    """ClutchConnectionPowerFlow

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchConnectionPowerFlow.TYPE'):
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

"""_3781.py

PlanetaryConnectionStabilityAnalysis
"""


from mastapy.system_model.connections_and_sockets import _2227
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6846
from mastapy.system_model.analyses_and_results.stability_analyses import _3795
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'PlanetaryConnectionStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetaryConnectionStabilityAnalysis',)


class PlanetaryConnectionStabilityAnalysis(_3795.ShaftToMountableComponentConnectionStabilityAnalysis):
    """PlanetaryConnectionStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PlanetaryConnectionStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2227.PlanetaryConnection':
        """PlanetaryConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6846.PlanetaryConnectionLoadCase':
        """PlanetaryConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

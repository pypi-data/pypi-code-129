"""_4180.py

PlanetaryConnectionCompoundPowerFlow
"""


from typing import List

from mastapy.system_model.connections_and_sockets import _2227
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4048
from mastapy.system_model.analyses_and_results.power_flows.compound import _4194
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'PlanetaryConnectionCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetaryConnectionCompoundPowerFlow',)


class PlanetaryConnectionCompoundPowerFlow(_4194.ShaftToMountableComponentConnectionCompoundPowerFlow):
    """PlanetaryConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PlanetaryConnectionCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2227.PlanetaryConnection':
        """PlanetaryConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def connection_analysis_cases_ready(self) -> 'List[_4048.PlanetaryConnectionPowerFlow]':
        """List[PlanetaryConnectionPowerFlow]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_4048.PlanetaryConnectionPowerFlow]':
        """List[PlanetaryConnectionPowerFlow]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

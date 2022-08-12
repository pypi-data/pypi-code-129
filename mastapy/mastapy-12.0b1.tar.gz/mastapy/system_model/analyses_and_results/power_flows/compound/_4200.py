"""_4200.py

SpringDamperConnectionCompoundPowerFlow
"""


from typing import List

from mastapy.system_model.connections_and_sockets.couplings import _2290
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4069
from mastapy.system_model.analyses_and_results.power_flows.compound import _4135
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'SpringDamperConnectionCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperConnectionCompoundPowerFlow',)


class SpringDamperConnectionCompoundPowerFlow(_4135.CouplingConnectionCompoundPowerFlow):
    """SpringDamperConnectionCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperConnectionCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2290.SpringDamperConnection':
        """SpringDamperConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2290.SpringDamperConnection':
        """SpringDamperConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4069.SpringDamperConnectionPowerFlow]':
        """List[SpringDamperConnectionPowerFlow]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_4069.SpringDamperConnectionPowerFlow]':
        """List[SpringDamperConnectionPowerFlow]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

"""_4221.py

WormGearMeshCompoundPowerFlow
"""


from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2269
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4091
from mastapy.system_model.analyses_and_results.power_flows.compound import _4156
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'WormGearMeshCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearMeshCompoundPowerFlow',)


class WormGearMeshCompoundPowerFlow(_4156.GearMeshCompoundPowerFlow):
    """WormGearMeshCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearMeshCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2269.WormGearMesh':
        """WormGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2269.WormGearMesh':
        """WormGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4091.WormGearMeshPowerFlow]':
        """List[WormGearMeshPowerFlow]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_4091.WormGearMeshPowerFlow]':
        """List[WormGearMeshPowerFlow]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

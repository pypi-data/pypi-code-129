"""_4161.py

HypoidGearSetCompoundPowerFlow
"""


from typing import List

from mastapy.system_model.part_model.gears import _2474
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4029
from mastapy.system_model.analyses_and_results.power_flows.compound import _4159, _4160, _4103
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'HypoidGearSetCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetCompoundPowerFlow',)


class HypoidGearSetCompoundPowerFlow(_4103.AGMAGleasonConicalGearSetCompoundPowerFlow):
    """HypoidGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSetCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2474.HypoidGearSet':
        """HypoidGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2474.HypoidGearSet':
        """HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4029.HypoidGearSetPowerFlow]':
        """List[HypoidGearSetPowerFlow]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_gears_compound_power_flow(self) -> 'List[_4159.HypoidGearCompoundPowerFlow]':
        """List[HypoidGearCompoundPowerFlow]: 'HypoidGearsCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearsCompoundPowerFlow
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_meshes_compound_power_flow(self) -> 'List[_4160.HypoidGearMeshCompoundPowerFlow]':
        """List[HypoidGearMeshCompoundPowerFlow]: 'HypoidMeshesCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidMeshesCompoundPowerFlow
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4029.HypoidGearSetPowerFlow]':
        """List[HypoidGearSetPowerFlow]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

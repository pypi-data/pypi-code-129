"""_4222.py

WormGearSetCompoundPowerFlow
"""


from typing import List

from mastapy.system_model.part_model.gears import _2491
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.worm import _366
from mastapy.system_model.analyses_and_results.power_flows import _4093
from mastapy.system_model.analyses_and_results.power_flows.compound import _4220, _4221, _4157
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'WormGearSetCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetCompoundPowerFlow',)


class WormGearSetCompoundPowerFlow(_4157.GearSetCompoundPowerFlow):
    """WormGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2491.WormGearSet':
        """WormGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2491.WormGearSet':
        """WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_duty_cycle_rating(self) -> '_366.WormGearSetDutyCycleRating':
        """WormGearSetDutyCycleRating: 'GearSetDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDutyCycleRating
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def worm_gear_set_duty_cycle_rating(self) -> '_366.WormGearSetDutyCycleRating':
        """WormGearSetDutyCycleRating: 'WormGearSetDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearSetDutyCycleRating
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4093.WormGearSetPowerFlow]':
        """List[WormGearSetPowerFlow]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_gears_compound_power_flow(self) -> 'List[_4220.WormGearCompoundPowerFlow]':
        """List[WormGearCompoundPowerFlow]: 'WormGearsCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearsCompoundPowerFlow
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_meshes_compound_power_flow(self) -> 'List[_4221.WormGearMeshCompoundPowerFlow]':
        """List[WormGearMeshCompoundPowerFlow]: 'WormMeshesCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormMeshesCompoundPowerFlow
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4093.WormGearSetPowerFlow]':
        """List[WormGearSetPowerFlow]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

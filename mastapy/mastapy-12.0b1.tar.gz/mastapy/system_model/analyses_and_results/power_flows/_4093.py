"""_4093.py

WormGearSetPowerFlow
"""


from typing import List

from mastapy.system_model.part_model.gears import _2491
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6898
from mastapy.gears.rating.worm import _367
from mastapy.system_model.analyses_and_results.power_flows import _4092, _4091, _4025
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'WormGearSetPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetPowerFlow',)


class WormGearSetPowerFlow(_4025.GearSetPowerFlow):
    """WormGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def assembly_load_case(self) -> '_6898.WormGearSetLoadCase':
        """WormGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_367.WormGearSetRating':
        """WormGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_367.WormGearSetRating':
        """WormGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gears_power_flow(self) -> 'List[_4092.WormGearPowerFlow]':
        """List[WormGearPowerFlow]: 'GearsPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearsPowerFlow
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_gears_power_flow(self) -> 'List[_4092.WormGearPowerFlow]':
        """List[WormGearPowerFlow]: 'WormGearsPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearsPowerFlow
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshes_power_flow(self) -> 'List[_4091.WormGearMeshPowerFlow]':
        """List[WormGearMeshPowerFlow]: 'MeshesPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshesPowerFlow
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_meshes_power_flow(self) -> 'List[_4091.WormGearMeshPowerFlow]':
        """List[WormGearMeshPowerFlow]: 'WormMeshesPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormMeshesPowerFlow
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

"""_3995.py

ConceptGearSetPowerFlow
"""


from typing import List

from mastapy.system_model.part_model.gears import _2461
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6757
from mastapy.gears.rating.concept import _543
from mastapy.system_model.analyses_and_results.power_flows import _3994, _3993, _4025
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'ConceptGearSetPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetPowerFlow',)


class ConceptGearSetPowerFlow(_4025.GearSetPowerFlow):
    """ConceptGearSetPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearSetPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2461.ConceptGearSet':
        """ConceptGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6757.ConceptGearSetLoadCase':
        """ConceptGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_543.ConceptGearSetRating':
        """ConceptGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_543.ConceptGearSetRating':
        """ConceptGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gears_power_flow(self) -> 'List[_3994.ConceptGearPowerFlow]':
        """List[ConceptGearPowerFlow]: 'GearsPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearsPowerFlow
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_gears_power_flow(self) -> 'List[_3994.ConceptGearPowerFlow]':
        """List[ConceptGearPowerFlow]: 'ConceptGearsPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearsPowerFlow
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshes_power_flow(self) -> 'List[_3993.ConceptGearMeshPowerFlow]':
        """List[ConceptGearMeshPowerFlow]: 'MeshesPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshesPowerFlow
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_meshes_power_flow(self) -> 'List[_3993.ConceptGearMeshPowerFlow]':
        """List[ConceptGearMeshPowerFlow]: 'ConceptMeshesPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptMeshesPowerFlow
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

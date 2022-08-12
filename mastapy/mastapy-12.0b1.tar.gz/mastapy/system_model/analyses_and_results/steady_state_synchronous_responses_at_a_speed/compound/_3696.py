"""_3696.py

ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed
"""


from typing import List

from mastapy.system_model.part_model.gears import _2493
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3566
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3694, _3695, _3586
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed',)


class ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed(_3586.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed):
    """ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2493.ZerolBevelGearSet':
        """ZerolBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2493.ZerolBevelGearSet':
        """ZerolBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3566.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed]':
        """List[ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_gears_compound_steady_state_synchronous_response_at_a_speed(self) -> 'List[_3694.ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed]':
        """List[ZerolBevelGearCompoundSteadyStateSynchronousResponseAtASpeed]: 'ZerolBevelGearsCompoundSteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearsCompoundSteadyStateSynchronousResponseAtASpeed
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_meshes_compound_steady_state_synchronous_response_at_a_speed(self) -> 'List[_3695.ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed]':
        """List[ZerolBevelGearMeshCompoundSteadyStateSynchronousResponseAtASpeed]: 'ZerolBevelMeshesCompoundSteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelMeshesCompoundSteadyStateSynchronousResponseAtASpeed
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3566.ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed]':
        """List[ZerolBevelGearSetSteadyStateSynchronousResponseAtASpeed]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

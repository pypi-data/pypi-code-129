"""_3675.py

StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed
"""


from typing import List

from mastapy.system_model.part_model.gears import _2485
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import _3545
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import _3673, _3674, _3586
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound', 'StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed',)


class StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed(_3586.BevelGearSetCompoundSteadyStateSynchronousResponseAtASpeed):
    """StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponseAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2485.StraightBevelDiffGearSet':
        """StraightBevelDiffGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2485.StraightBevelDiffGearSet':
        """StraightBevelDiffGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3545.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed]':
        """List[StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_gears_compound_steady_state_synchronous_response_at_a_speed(self) -> 'List[_3673.StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed]':
        """List[StraightBevelDiffGearCompoundSteadyStateSynchronousResponseAtASpeed]: 'StraightBevelDiffGearsCompoundSteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGearsCompoundSteadyStateSynchronousResponseAtASpeed
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_meshes_compound_steady_state_synchronous_response_at_a_speed(self) -> 'List[_3674.StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed]':
        """List[StraightBevelDiffGearMeshCompoundSteadyStateSynchronousResponseAtASpeed]: 'StraightBevelDiffMeshesCompoundSteadyStateSynchronousResponseAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffMeshesCompoundSteadyStateSynchronousResponseAtASpeed
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3545.StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed]':
        """List[StraightBevelDiffGearSetSteadyStateSynchronousResponseAtASpeed]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

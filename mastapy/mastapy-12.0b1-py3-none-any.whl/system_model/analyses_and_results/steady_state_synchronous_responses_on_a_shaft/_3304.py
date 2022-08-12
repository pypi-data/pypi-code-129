"""_3304.py

WormGearSetSteadyStateSynchronousResponseOnAShaft
"""


from typing import List

from mastapy.system_model.part_model.gears import _2491
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6898
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3305, _3303, _3238
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'WormGearSetSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetSteadyStateSynchronousResponseOnAShaft',)


class WormGearSetSteadyStateSynchronousResponseOnAShaft(_3238.GearSetSteadyStateSynchronousResponseOnAShaft):
    """WormGearSetSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetSteadyStateSynchronousResponseOnAShaft.TYPE'):
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
    def worm_gears_steady_state_synchronous_response_on_a_shaft(self) -> 'List[_3305.WormGearSteadyStateSynchronousResponseOnAShaft]':
        """List[WormGearSteadyStateSynchronousResponseOnAShaft]: 'WormGearsSteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearsSteadyStateSynchronousResponseOnAShaft
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_meshes_steady_state_synchronous_response_on_a_shaft(self) -> 'List[_3303.WormGearMeshSteadyStateSynchronousResponseOnAShaft]':
        """List[WormGearMeshSteadyStateSynchronousResponseOnAShaft]: 'WormMeshesSteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormMeshesSteadyStateSynchronousResponseOnAShaft
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

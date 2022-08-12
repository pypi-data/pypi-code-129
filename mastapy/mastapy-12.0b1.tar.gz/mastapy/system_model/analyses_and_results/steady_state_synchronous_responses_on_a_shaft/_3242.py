"""_3242.py

HypoidGearSetSteadyStateSynchronousResponseOnAShaft
"""


from typing import List

from mastapy.system_model.part_model.gears import _2474
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6821
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import _3243, _3241, _3184
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'HypoidGearSetSteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetSteadyStateSynchronousResponseOnAShaft',)


class HypoidGearSetSteadyStateSynchronousResponseOnAShaft(_3184.AGMAGleasonConicalGearSetSteadyStateSynchronousResponseOnAShaft):
    """HypoidGearSetSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSetSteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def assembly_load_case(self) -> '_6821.HypoidGearSetLoadCase':
        """HypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hypoid_gears_steady_state_synchronous_response_on_a_shaft(self) -> 'List[_3243.HypoidGearSteadyStateSynchronousResponseOnAShaft]':
        """List[HypoidGearSteadyStateSynchronousResponseOnAShaft]: 'HypoidGearsSteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearsSteadyStateSynchronousResponseOnAShaft
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_meshes_steady_state_synchronous_response_on_a_shaft(self) -> 'List[_3241.HypoidGearMeshSteadyStateSynchronousResponseOnAShaft]':
        """List[HypoidGearMeshSteadyStateSynchronousResponseOnAShaft]: 'HypoidMeshesSteadyStateSynchronousResponseOnAShaft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidMeshesSteadyStateSynchronousResponseOnAShaft
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

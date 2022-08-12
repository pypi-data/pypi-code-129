"""_3045.py

WormGearSetSteadyStateSynchronousResponse
"""


from typing import List

from mastapy.system_model.part_model.gears import _2491
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6898
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3046, _3044, _2977
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'WormGearSetSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetSteadyStateSynchronousResponse',)


class WormGearSetSteadyStateSynchronousResponse(_2977.GearSetSteadyStateSynchronousResponse):
    """WormGearSetSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetSteadyStateSynchronousResponse.TYPE'):
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
    def worm_gears_steady_state_synchronous_response(self) -> 'List[_3046.WormGearSteadyStateSynchronousResponse]':
        """List[WormGearSteadyStateSynchronousResponse]: 'WormGearsSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearsSteadyStateSynchronousResponse
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_meshes_steady_state_synchronous_response(self) -> 'List[_3044.WormGearMeshSteadyStateSynchronousResponse]':
        """List[WormGearMeshSteadyStateSynchronousResponse]: 'WormMeshesSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormMeshesSteadyStateSynchronousResponse
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

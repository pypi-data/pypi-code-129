"""_2929.py

BevelDifferentialGearSetSteadyStateSynchronousResponse
"""


from typing import List

from mastapy.system_model.part_model.gears import _2455
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6739
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2930, _2928, _2934
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'BevelDifferentialGearSetSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSetSteadyStateSynchronousResponse',)


class BevelDifferentialGearSetSteadyStateSynchronousResponse(_2934.BevelGearSetSteadyStateSynchronousResponse):
    """BevelDifferentialGearSetSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSetSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2455.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6739.BevelDifferentialGearSetLoadCase':
        """BevelDifferentialGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_differential_gears_steady_state_synchronous_response(self) -> 'List[_2930.BevelDifferentialGearSteadyStateSynchronousResponse]':
        """List[BevelDifferentialGearSteadyStateSynchronousResponse]: 'BevelDifferentialGearsSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialGearsSteadyStateSynchronousResponse
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_meshes_steady_state_synchronous_response(self) -> 'List[_2928.BevelDifferentialGearMeshSteadyStateSynchronousResponse]':
        """List[BevelDifferentialGearMeshSteadyStateSynchronousResponse]: 'BevelDifferentialMeshesSteadyStateSynchronousResponse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialMeshesSteadyStateSynchronousResponse
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

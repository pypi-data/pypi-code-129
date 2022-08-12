"""_2971.py

FaceGearMeshSteadyStateSynchronousResponse
"""


from mastapy.system_model.connections_and_sockets.gears import _2251
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6799
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2976
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'FaceGearMeshSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMeshSteadyStateSynchronousResponse',)


class FaceGearMeshSteadyStateSynchronousResponse(_2976.GearMeshSteadyStateSynchronousResponse):
    """FaceGearMeshSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearMeshSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2251.FaceGearMesh':
        """FaceGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6799.FaceGearMeshLoadCase':
        """FaceGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

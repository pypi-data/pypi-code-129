"""_6799.py

FaceGearMeshLoadCase
"""


from mastapy.system_model.connections_and_sockets.gears import _2251
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6806
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'FaceGearMeshLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMeshLoadCase',)


class FaceGearMeshLoadCase(_6806.GearMeshLoadCase):
    """FaceGearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearMeshLoadCase.TYPE'):
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

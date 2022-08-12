"""_5357.py

FaceGearMeshMultibodyDynamicsAnalysis
"""


from mastapy.system_model.connections_and_sockets.gears import _2251
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6799
from mastapy.system_model.analyses_and_results.mbd_analyses import _5362
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'FaceGearMeshMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMeshMultibodyDynamicsAnalysis',)


class FaceGearMeshMultibodyDynamicsAnalysis(_5362.GearMeshMultibodyDynamicsAnalysis):
    """FaceGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearMeshMultibodyDynamicsAnalysis.TYPE'):
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

"""_5367.py

HypoidGearMeshMultibodyDynamicsAnalysis
"""


from mastapy.system_model.connections_and_sockets.gears import _2255
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6820
from mastapy.system_model.analyses_and_results.mbd_analyses import _5305
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'HypoidGearMeshMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearMeshMultibodyDynamicsAnalysis',)


class HypoidGearMeshMultibodyDynamicsAnalysis(_5305.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis):
    """HypoidGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearMeshMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2255.HypoidGearMesh':
        """HypoidGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6820.HypoidGearMeshLoadCase':
        """HypoidGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

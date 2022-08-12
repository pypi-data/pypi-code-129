"""_2255.py

HypoidGearMesh
"""


from mastapy.gears.gear_designs.hypoid import _977
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2239
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'HypoidGearMesh')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearMesh',)


class HypoidGearMesh(_2239.AGMAGleasonConicalGearMesh):
    """HypoidGearMesh

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_mesh_design(self) -> '_977.HypoidGearMeshDesign':
        """HypoidGearMeshDesign: 'ActiveGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearMeshDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hypoid_gear_mesh_design(self) -> '_977.HypoidGearMeshDesign':
        """HypoidGearMeshDesign: 'HypoidGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearMeshDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

"""_983.py

FaceGearMeshMicroGeometry
"""


from typing import List

from mastapy.gears.gear_designs.face import _987, _982, _984
from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import _1211
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_MICRO_GEOMETRY = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Face', 'FaceGearMeshMicroGeometry')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMeshMicroGeometry',)


class FaceGearMeshMicroGeometry(_1211.GearMeshImplementationDetail):
    """FaceGearMeshMicroGeometry

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_MICRO_GEOMETRY

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearMeshMicroGeometry.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_gear_set_micro_geometry(self) -> '_987.FaceGearSetMicroGeometry':
        """FaceGearSetMicroGeometry: 'FaceGearSetMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearSetMicroGeometry
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def face_mesh(self) -> '_982.FaceGearMeshDesign':
        """FaceGearMeshDesign: 'FaceMesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceMesh
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def face_gear_micro_geometries(self) -> 'List[_984.FaceGearMicroGeometry]':
        """List[FaceGearMicroGeometry]: 'FaceGearMicroGeometries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearMicroGeometries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

"""_987.py

FaceGearSetMicroGeometry
"""


from typing import List

from mastapy.gears.gear_designs.face import _986, _984, _983
from mastapy._internal import constructor, conversion
from mastapy.gears.analysis import _1217
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_MICRO_GEOMETRY = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Face', 'FaceGearSetMicroGeometry')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetMicroGeometry',)


class FaceGearSetMicroGeometry(_1217.GearSetImplementationDetail):
    """FaceGearSetMicroGeometry

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_MICRO_GEOMETRY

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearSetMicroGeometry.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_gear_set_design(self) -> '_986.FaceGearSetDesign':
        """FaceGearSetDesign: 'FaceGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearSetDesign
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

    @property
    def face_mesh_micro_geometries(self) -> 'List[_983.FaceGearMeshMicroGeometry]':
        """List[FaceGearMeshMicroGeometry]: 'FaceMeshMicroGeometries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceMeshMicroGeometries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def duplicate(self) -> 'FaceGearSetMicroGeometry':
        """ 'Duplicate' is the original name of this method.

        Returns:
            mastapy.gears.gear_designs.face.FaceGearSetMicroGeometry
        """

        method_result = self.wrapped.Duplicate()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

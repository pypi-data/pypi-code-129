"""_2468.py

FaceGearSet
"""


from typing import List

from mastapy.gears.gear_designs.face import _986
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2467, _2471
from mastapy.system_model.connections_and_sockets.gears import _2251
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'FaceGearSet')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSet',)


class FaceGearSet(_2471.GearSet):
    """FaceGearSet

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_set_design(self) -> '_986.FaceGearSetDesign':
        """FaceGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearSetDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def face_gears(self) -> 'List[_2467.FaceGear]':
        """List[FaceGear]: 'FaceGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_meshes(self) -> 'List[_2251.FaceGearMesh]':
        """List[FaceGearMesh]: 'FaceMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceMeshes
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

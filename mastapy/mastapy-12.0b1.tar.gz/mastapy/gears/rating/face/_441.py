"""_441.py

FaceGearSetRating
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.face import _986
from mastapy.gears.rating.face import _439, _438
from mastapy.gears.rating import _354
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Face', 'FaceGearSetRating')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetRating',)


class FaceGearSetRating(_354.GearSetRating):
    """FaceGearSetRating

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearSetRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self) -> 'str':
        """str: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        return temp

    @property
    def face_gear_set(self) -> '_986.FaceGearSetDesign':
        """FaceGearSetDesign: 'FaceGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearSet
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_ratings(self) -> 'List[_439.FaceGearRating]':
        """List[FaceGearRating]: 'GearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_gear_ratings(self) -> 'List[_439.FaceGearRating]':
        """List[FaceGearRating]: 'FaceGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_mesh_ratings(self) -> 'List[_438.FaceGearMeshRating]':
        """List[FaceGearMeshRating]: 'FaceMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceMeshRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

"""_388.py

StraightBevelGearSetRating
"""


from typing import List

from mastapy.gears.gear_designs.straight_bevel import _954
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.straight_bevel import _387, _386
from mastapy.gears.rating.bevel import _546
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.StraightBevel', 'StraightBevelGearSetRating')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSetRating',)


class StraightBevelGearSetRating(_546.BevelGearSetRating):
    """StraightBevelGearSetRating

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelGearSetRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def straight_bevel_gear_set(self) -> '_954.StraightBevelGearSetDesign':
        """StraightBevelGearSetDesign: 'StraightBevelGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearSet
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def straight_bevel_gear_ratings(self) -> 'List[_387.StraightBevelGearRating]':
        """List[StraightBevelGearRating]: 'StraightBevelGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_mesh_ratings(self) -> 'List[_386.StraightBevelGearMeshRating]':
        """List[StraightBevelGearMeshRating]: 'StraightBevelMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelMeshRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

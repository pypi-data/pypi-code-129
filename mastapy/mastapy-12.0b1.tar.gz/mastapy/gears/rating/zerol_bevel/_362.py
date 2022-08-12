"""_362.py

ZerolBevelGearSetRating
"""


from typing import List

from mastapy.gears.gear_designs.zerol_bevel import _945
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.zerol_bevel import _361, _360
from mastapy.gears.rating.bevel import _546
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.ZerolBevel', 'ZerolBevelGearSetRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSetRating',)


class ZerolBevelGearSetRating(_546.BevelGearSetRating):
    """ZerolBevelGearSetRating

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSetRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def zerol_bevel_gear_set(self) -> '_945.ZerolBevelGearSetDesign':
        """ZerolBevelGearSetDesign: 'ZerolBevelGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearSet
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def zerol_bevel_gear_ratings(self) -> 'List[_361.ZerolBevelGearRating]':
        """List[ZerolBevelGearRating]: 'ZerolBevelGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_mesh_ratings(self) -> 'List[_360.ZerolBevelGearMeshRating]':
        """List[ZerolBevelGearMeshRating]: 'ZerolBevelMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelMeshRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

"""_354.py

GearSetRating
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.materials import _258
from mastapy.gears.rating import _352, _346
from mastapy._internal.python_net import python_net_import

_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating', 'GearSetRating')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetRating',)


class GearSetRating(_346.AbstractGearSetRating):
    """GearSetRating

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearSetRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property."""

        temp = self.wrapped.Name
        return temp

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value else ''

    @property
    def rating(self) -> 'str':
        """str: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        return temp

    @property
    def total_gear_set_reliability(self) -> 'float':
        """float: 'TotalGearSetReliability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalGearSetReliability
        return temp

    @property
    def lubrication_detail(self) -> '_258.LubricationDetail':
        """LubricationDetail: 'LubricationDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LubricationDetail
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_ratings(self) -> 'List[_352.GearRating]':
        """List[GearRating]: 'GearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

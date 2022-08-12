"""_431.py

HypoidGearSetRating
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.gear_designs.hypoid import _978
from mastapy.gears.rating.hypoid import _430, _429
from mastapy.gears.rating.agma_gleason_conical import _557
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Hypoid', 'HypoidGearSetRating')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetRating',)


class HypoidGearSetRating(_557.AGMAGleasonConicalGearSetRating):
    """HypoidGearSetRating

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSetRating.TYPE'):
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
    def size_factor_bending(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'SizeFactorBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SizeFactorBending
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @property
    def size_factor_contact(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'SizeFactorContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SizeFactorContact
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @property
    def hypoid_gear_set(self) -> '_978.HypoidGearSetDesign':
        """HypoidGearSetDesign: 'HypoidGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearSet
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hypoid_gear_ratings(self) -> 'List[_430.HypoidGearRating]':
        """List[HypoidGearRating]: 'HypoidGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_mesh_ratings(self) -> 'List[_429.HypoidGearMeshRating]':
        """List[HypoidGearMeshRating]: 'HypoidMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidMeshRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

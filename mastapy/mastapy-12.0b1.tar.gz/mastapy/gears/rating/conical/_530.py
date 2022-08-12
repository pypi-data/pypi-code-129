"""_530.py

ConicalGearRating
"""


from mastapy.gears.rating import _350, _352
from mastapy._internal import constructor
from mastapy.gears.rating.cylindrical import _447, _448
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Conical', 'ConicalGearRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearRating',)


class ConicalGearRating(_352.GearRating):
    """ConicalGearRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalGearRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def concave_flank_rating(self) -> '_350.GearFlankRating':
        """GearFlankRating: 'ConcaveFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConcaveFlankRating
        if _350.GearFlankRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast concave_flank_rating to GearFlankRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def convex_flank_rating(self) -> '_350.GearFlankRating':
        """GearFlankRating: 'ConvexFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConvexFlankRating
        if _350.GearFlankRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast convex_flank_rating to GearFlankRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

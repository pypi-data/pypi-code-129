"""_363.py

WormGearDutyCycleRating
"""


from typing import List

from mastapy.gears.rating import _350, _349
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.cylindrical import _447, _448
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.worm import _366, _365
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_DUTY_CYCLE_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Worm', 'WormGearDutyCycleRating')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearDutyCycleRating',)


class WormGearDutyCycleRating(_349.GearDutyCycleRating):
    """WormGearDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_DUTY_CYCLE_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearDutyCycleRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def left_flank_rating(self) -> '_350.GearFlankRating':
        """GearFlankRating: 'LeftFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlankRating
        if _350.GearFlankRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast left_flank_rating to GearFlankRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def right_flank_rating(self) -> '_350.GearFlankRating':
        """GearFlankRating: 'RightFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlankRating
        if _350.GearFlankRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast right_flank_rating to GearFlankRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_duty_cycle(self) -> '_366.WormGearSetDutyCycleRating':
        """WormGearSetDutyCycleRating: 'GearSetDesignDutyCycle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesignDutyCycle
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def worm_gear_set_design_duty_cycle(self) -> '_366.WormGearSetDutyCycleRating':
        """WormGearSetDutyCycleRating: 'WormGearSetDesignDutyCycle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearSetDesignDutyCycle
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_ratings(self) -> 'List[_365.WormGearRating]':
        """List[WormGearRating]: 'GearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_gear_ratings(self) -> 'List[_365.WormGearRating]':
        """List[WormGearRating]: 'WormGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

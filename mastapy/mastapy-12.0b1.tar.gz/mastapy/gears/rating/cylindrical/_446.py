"""_446.py

CylindricalGearDutyCycleRating
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.cylindrical import (
    _454, _447, _448, _466,
    _451
)
from mastapy.gears.rating import _350, _349
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_DUTY_CYCLE_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'CylindricalGearDutyCycleRating')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearDutyCycleRating',)


class CylindricalGearDutyCycleRating(_349.GearDutyCycleRating):
    """CylindricalGearDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_DUTY_CYCLE_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearDutyCycleRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def highest_maximum_material_exposure(self) -> 'float':
        """float: 'HighestMaximumMaterialExposure' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HighestMaximumMaterialExposure
        return temp

    @property
    def safety_factor_against_permanent_deformation(self) -> 'float':
        """float: 'SafetyFactorAgainstPermanentDeformation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorAgainstPermanentDeformation
        return temp

    @property
    def safety_factor_against_permanent_deformation_with_influence_of_rim(self) -> 'float':
        """float: 'SafetyFactorAgainstPermanentDeformationWithInfluenceOfRim' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorAgainstPermanentDeformationWithInfluenceOfRim
        return temp

    @property
    def gear_set_design_duty_cycle(self) -> '_454.CylindricalGearSetDutyCycleRating':
        """CylindricalGearSetDutyCycleRating: 'GearSetDesignDutyCycle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesignDutyCycle
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_set_design_duty_cycle(self) -> '_454.CylindricalGearSetDutyCycleRating':
        """CylindricalGearSetDutyCycleRating: 'CylindricalGearSetDesignDutyCycle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSetDesignDutyCycle
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def cylindrical_gear_mesh_ratings(self) -> 'List[_466.MeshRatingForReports]':
        """List[MeshRatingForReports]: 'CylindricalGearMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearMeshRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_ratings(self) -> 'List[_451.CylindricalGearRating]':
        """List[CylindricalGearRating]: 'GearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_gear_ratings(self) -> 'List[_451.CylindricalGearRating]':
        """List[CylindricalGearRating]: 'CylindricalGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

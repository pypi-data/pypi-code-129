"""_454.py

CylindricalGearSetDutyCycleRating
"""


from typing import List

from mastapy.gears.gear_designs.cylindrical import _1019, _1031
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.cylindrical.optimisation import _491
from mastapy.gears.rating.cylindrical import _457
from mastapy.gears.rating import _353
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_DUTY_CYCLE_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'CylindricalGearSetDutyCycleRating')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetDutyCycleRating',)


class CylindricalGearSetDutyCycleRating(_353.GearSetDutyCycleRating):
    """CylindricalGearSetDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_DUTY_CYCLE_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetDutyCycleRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cylindrical_gear_set(self) -> '_1019.CylindricalGearSetDesign':
        """CylindricalGearSetDesign: 'CylindricalGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSet
        if _1019.CylindricalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast cylindrical_gear_set to CylindricalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def optimisations(self) -> '_491.CylindricalGearSetRatingOptimisationHelper':
        """CylindricalGearSetRatingOptimisationHelper: 'Optimisations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Optimisations
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_mesh_duty_cycle_ratings(self) -> 'List[_457.CylindricalMeshDutyCycleRating]':
        """List[CylindricalMeshDutyCycleRating]: 'GearMeshDutyCycleRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshDutyCycleRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_mesh_duty_cycle_ratings(self) -> 'List[_457.CylindricalMeshDutyCycleRating]':
        """List[CylindricalMeshDutyCycleRating]: 'CylindricalMeshDutyCycleRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalMeshDutyCycleRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def set_profile_shift_to_maximum_safety_factor_fatigue_and_static(self):
        """ 'SetProfileShiftToMaximumSafetyFactorFatigueAndStatic' is the original name of this method."""

        self.wrapped.SetProfileShiftToMaximumSafetyFactorFatigueAndStatic()

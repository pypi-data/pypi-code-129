"""_455.py

CylindricalGearSetRating
"""


from typing import List

from mastapy.materials import _242
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.gears.gear_designs.cylindrical import _1019, _1031
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.cylindrical.optimisation import _491
from mastapy.gears.rating.cylindrical import _445, _451, _449
from mastapy.gears.rating.cylindrical.vdi import _479
from mastapy.gears.rating import _354
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'CylindricalGearSetRating')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetRating',)


class CylindricalGearSetRating(_354.GearSetRating):
    """CylindricalGearSetRating

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating_method(self) -> '_242.CylindricalGearRatingMethods':
        """CylindricalGearRatingMethods: 'RatingMethod' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatingMethod
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_242.CylindricalGearRatingMethods)(value) if value is not None else None

    @property
    def rating_standard_name(self) -> 'str':
        """str: 'RatingStandardName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatingStandardName
        return temp

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
    def rating_settings(self) -> '_445.CylindricalGearDesignAndRatingSettingsItem':
        """CylindricalGearDesignAndRatingSettingsItem: 'RatingSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatingSettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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

    @property
    def cylindrical_mesh_ratings(self) -> 'List[_449.CylindricalGearMeshRating]':
        """List[CylindricalGearMeshRating]: 'CylindricalMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalMeshRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def vdi_cylindrical_gear_single_flank_ratings(self) -> 'List[_479.VDI2737InternalGearSingleFlankRating]':
        """List[VDI2737InternalGearSingleFlankRating]: 'VDICylindricalGearSingleFlankRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VDICylindricalGearSingleFlankRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

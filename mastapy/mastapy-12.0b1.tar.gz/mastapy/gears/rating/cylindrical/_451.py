"""_451.py

CylindricalGearRating
"""


from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical import _1003, _1032
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating import _350, _352
from mastapy.gears.rating.cylindrical import _447, _448, _478
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'CylindricalGearRating')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearRating',)


class CylindricalGearRating(_352.GearRating):
    """CylindricalGearRating

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def damage_bending(self) -> 'float':
        """float: 'DamageBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DamageBending
        return temp

    @property
    def damage_contact(self) -> 'float':
        """float: 'DamageContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DamageContact
        return temp

    @property
    def worst_crack_initiation_safety_factor_with_influence_of_rim(self) -> 'float':
        """float: 'WorstCrackInitiationSafetyFactorWithInfluenceOfRim' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorstCrackInitiationSafetyFactorWithInfluenceOfRim
        return temp

    @property
    def worst_fatigue_fracture_safety_factor_with_influence_of_rim(self) -> 'float':
        """float: 'WorstFatigueFractureSafetyFactorWithInfluenceOfRim' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorstFatigueFractureSafetyFactorWithInfluenceOfRim
        return temp

    @property
    def worst_permanent_deformation_safety_factor_with_influence_of_rim(self) -> 'float':
        """float: 'WorstPermanentDeformationSafetyFactorWithInfluenceOfRim' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorstPermanentDeformationSafetyFactorWithInfluenceOfRim
        return temp

    @property
    def cylindrical_gear(self) -> '_1003.CylindricalGearDesign':
        """CylindricalGearDesign: 'CylindricalGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGear
        if _1003.CylindricalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast cylindrical_gear to CylindricalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

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
    def vdi2737_safety_factor(self) -> '_478.VDI2737SafetyFactorReportingObject':
        """VDI2737SafetyFactorReportingObject: 'VDI2737SafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VDI2737SafetyFactor
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

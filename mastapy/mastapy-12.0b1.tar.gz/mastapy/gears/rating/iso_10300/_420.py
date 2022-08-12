"""_420.py

ISO10300SingleFlankRating
"""


from typing import Generic, TypeVar

from mastapy._internal import constructor
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.rating.conical import _533
from mastapy.gears.rating.virtual_cylindrical_gears import _380
from mastapy._internal.python_net import python_net_import

_ISO10300_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Iso10300', 'ISO10300SingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO10300SingleFlankRating',)


T = TypeVar('T', bound='_380.VirtualCylindricalGearBasic')


class ISO10300SingleFlankRating(_533.ConicalGearSingleFlankRating, Generic[T]):
    """ISO10300SingleFlankRating

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _ISO10300_SINGLE_FLANK_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ISO10300SingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_contact_stress_number(self) -> 'float':
        """float: 'AllowableContactStressNumber' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableContactStressNumber
        return temp

    @property
    def allowable_stress_number_bending(self) -> 'float':
        """float: 'AllowableStressNumberBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableStressNumberBending
        return temp

    @property
    def constant_lubricant_film_factor_czl_method_b(self) -> 'float':
        """float: 'ConstantLubricantFilmFactorCZLMethodB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConstantLubricantFilmFactorCZLMethodB
        return temp

    @property
    def constant_roughness_factor_czr_method_b(self) -> 'float':
        """float: 'ConstantRoughnessFactorCZRMethodB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConstantRoughnessFactorCZRMethodB
        return temp

    @property
    def constant_speed_factor_czv_method_b(self) -> 'float':
        """float: 'ConstantSpeedFactorCZVMethodB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConstantSpeedFactorCZVMethodB
        return temp

    @property
    def life_factor_for_contact_stress(self) -> 'float':
        """float: 'LifeFactorForContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LifeFactorForContactStress
        return temp

    @property
    def life_factor_for_root_stress(self) -> 'float':
        """float: 'LifeFactorForRootStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LifeFactorForRootStress
        return temp

    @property
    def lubricant_factor_method_b(self) -> 'float':
        """float: 'LubricantFactorMethodB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LubricantFactorMethodB
        return temp

    @property
    def mean_pitch_diameter(self) -> 'float':
        """float: 'MeanPitchDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanPitchDiameter
        return temp

    @property
    def nominal_power(self) -> 'float':
        """float: 'NominalPower' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalPower
        return temp

    @property
    def nominal_tangential_force_of_bevel_gears(self) -> 'float':
        """float: 'NominalTangentialForceOfBevelGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalTangentialForceOfBevelGears
        return temp

    @property
    def nominal_tangential_speed_at_mean_point(self) -> 'float':
        """float: 'NominalTangentialSpeedAtMeanPoint' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalTangentialSpeedAtMeanPoint
        return temp

    @property
    def nominal_torque(self) -> 'float':
        """float: 'NominalTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalTorque
        return temp

    @property
    def product_of_lubricant_film_influence_factors(self) -> 'float':
        """float: 'ProductOfLubricantFilmInfluenceFactors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProductOfLubricantFilmInfluenceFactors
        return temp

    @property
    def relative_mass_per_unit_face_width_reference_to_line_of_action(self) -> 'float':
        """float: 'RelativeMassPerUnitFaceWidthReferenceToLineOfAction' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeMassPerUnitFaceWidthReferenceToLineOfAction
        return temp

    @property
    def relative_surface_condition_factor(self) -> 'float':
        """float: 'RelativeSurfaceConditionFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeSurfaceConditionFactor
        return temp

    @property
    def roughness_factor_for_contact_stress_method_b(self) -> 'float':
        """float: 'RoughnessFactorForContactStressMethodB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughnessFactorForContactStressMethodB
        return temp

    @property
    def single_pitch_deviation(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'SinglePitchDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SinglePitchDeviation
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @property
    def size_factor(self) -> 'float':
        """float: 'SizeFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SizeFactor
        return temp

    @property
    def size_factor_for_case_flame_induction_hardened_steels_nitrided_or_nitro_carburized_steels(self) -> 'float':
        """float: 'SizeFactorForCaseFlameInductionHardenedSteelsNitridedOrNitroCarburizedSteels' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SizeFactorForCaseFlameInductionHardenedSteelsNitridedOrNitroCarburizedSteels
        return temp

    @property
    def size_factor_for_grey_cast_iron_and_spheroidal_cast_iron(self) -> 'float':
        """float: 'SizeFactorForGreyCastIronAndSpheroidalCastIron' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SizeFactorForGreyCastIronAndSpheroidalCastIron
        return temp

    @property
    def size_factor_for_structural_and_through_hardened_steels_spheroidal_cast_iron_perlitic_malleable_cast_iron(self) -> 'float':
        """float: 'SizeFactorForStructuralAndThroughHardenedSteelsSpheroidalCastIronPerliticMalleableCastIron' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SizeFactorForStructuralAndThroughHardenedSteelsSpheroidalCastIronPerliticMalleableCastIron
        return temp

    @property
    def speed_factor_method_b(self) -> 'float':
        """float: 'SpeedFactorMethodB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpeedFactorMethodB
        return temp

    @property
    def work_hardening_factor(self) -> 'float':
        """float: 'WorkHardeningFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorkHardeningFactor
        return temp

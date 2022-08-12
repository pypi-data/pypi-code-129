"""_509.py

ISO6336AbstractMetalGearSingleFlankRating
"""


from mastapy._internal import constructor
from mastapy.gears.rating.cylindrical.iso6336 import _507
from mastapy._internal.python_net import python_net_import

_ISO6336_ABSTRACT_METAL_GEAR_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336', 'ISO6336AbstractMetalGearSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO6336AbstractMetalGearSingleFlankRating',)


class ISO6336AbstractMetalGearSingleFlankRating(_507.ISO6336AbstractGearSingleFlankRating):
    """ISO6336AbstractMetalGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _ISO6336_ABSTRACT_METAL_GEAR_SINGLE_FLANK_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ISO6336AbstractMetalGearSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def addendum_contact_ratio(self) -> 'float':
        """float: 'AddendumContactRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AddendumContactRatio
        return temp

    @property
    def base_pitch_deviation(self) -> 'float':
        """float: 'BasePitchDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasePitchDeviation
        return temp

    @property
    def life_factor_for_bending_stress(self) -> 'float':
        """float: 'LifeFactorForBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LifeFactorForBendingStress
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
    def life_factor_for_reference_bending_stress(self) -> 'float':
        """float: 'LifeFactorForReferenceBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LifeFactorForReferenceBendingStress
        return temp

    @property
    def life_factor_for_reference_contact_stress(self) -> 'float':
        """float: 'LifeFactorForReferenceContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LifeFactorForReferenceContactStress
        return temp

    @property
    def life_factor_for_static_bending_stress(self) -> 'float':
        """float: 'LifeFactorForStaticBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LifeFactorForStaticBendingStress
        return temp

    @property
    def life_factor_for_static_contact_stress(self) -> 'float':
        """float: 'LifeFactorForStaticContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LifeFactorForStaticContactStress
        return temp

    @property
    def lubricant_factor(self) -> 'float':
        """float: 'LubricantFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LubricantFactor
        return temp

    @property
    def lubricant_factor_for_reference_stress(self) -> 'float':
        """float: 'LubricantFactorForReferenceStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LubricantFactorForReferenceStress
        return temp

    @property
    def lubricant_factor_for_static_stress(self) -> 'float':
        """float: 'LubricantFactorForStaticStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LubricantFactorForStaticStress
        return temp

    @property
    def moment_of_inertia_per_unit_face_width(self) -> 'float':
        """float: 'MomentOfInertiaPerUnitFaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MomentOfInertiaPerUnitFaceWidth
        return temp

    @property
    def profile_form_deviation(self) -> 'float':
        """float: 'ProfileFormDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileFormDeviation
        return temp

    @property
    def relative_individual_gear_mass_per_unit_face_width_referenced_to_line_of_action(self) -> 'float':
        """float: 'RelativeIndividualGearMassPerUnitFaceWidthReferencedToLineOfAction' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeIndividualGearMassPerUnitFaceWidthReferencedToLineOfAction
        return temp

    @property
    def relative_notch_sensitivity_factor(self) -> 'float':
        """float: 'RelativeNotchSensitivityFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeNotchSensitivityFactor
        return temp

    @property
    def relative_notch_sensitivity_factor_for_reference_stress(self) -> 'float':
        """float: 'RelativeNotchSensitivityFactorForReferenceStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeNotchSensitivityFactorForReferenceStress
        return temp

    @property
    def relative_notch_sensitivity_factor_for_static_stress(self) -> 'float':
        """float: 'RelativeNotchSensitivityFactorForStaticStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeNotchSensitivityFactorForStaticStress
        return temp

    @property
    def relative_surface_factor(self) -> 'float':
        """float: 'RelativeSurfaceFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeSurfaceFactor
        return temp

    @property
    def relative_surface_factor_for_reference_stress(self) -> 'float':
        """float: 'RelativeSurfaceFactorForReferenceStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeSurfaceFactorForReferenceStress
        return temp

    @property
    def relative_surface_factor_for_static_stress(self) -> 'float':
        """float: 'RelativeSurfaceFactorForStaticStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeSurfaceFactorForStaticStress
        return temp

    @property
    def roughness_factor(self) -> 'float':
        """float: 'RoughnessFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughnessFactor
        return temp

    @property
    def roughness_factor_for_reference_stress(self) -> 'float':
        """float: 'RoughnessFactorForReferenceStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughnessFactorForReferenceStress
        return temp

    @property
    def roughness_factor_for_static_stress(self) -> 'float':
        """float: 'RoughnessFactorForStaticStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughnessFactorForStaticStress
        return temp

    @property
    def shot_peening_bending_stress_benefit(self) -> 'float':
        """float: 'ShotPeeningBendingStressBenefit' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShotPeeningBendingStressBenefit
        return temp

    @property
    def single_pair_tooth_contact_factor(self) -> 'float':
        """float: 'SinglePairToothContactFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SinglePairToothContactFactor
        return temp

    @property
    def size_factor(self) -> 'float':
        """float: 'SizeFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SizeFactor
        return temp

    @property
    def size_factor_tooth_root(self) -> 'float':
        """float: 'SizeFactorToothRoot' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SizeFactorToothRoot
        return temp

    @property
    def size_factor_for_reference_bending_stress(self) -> 'float':
        """float: 'SizeFactorForReferenceBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SizeFactorForReferenceBendingStress
        return temp

    @property
    def size_factor_for_reference_contact_stress(self) -> 'float':
        """float: 'SizeFactorForReferenceContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SizeFactorForReferenceContactStress
        return temp

    @property
    def size_factor_for_static_stress(self) -> 'float':
        """float: 'SizeFactorForStaticStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SizeFactorForStaticStress
        return temp

    @property
    def static_size_factor_tooth_root(self) -> 'float':
        """float: 'StaticSizeFactorToothRoot' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StaticSizeFactorToothRoot
        return temp

    @property
    def velocity_factor(self) -> 'float':
        """float: 'VelocityFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VelocityFactor
        return temp

    @property
    def velocity_factor_for_reference_stress(self) -> 'float':
        """float: 'VelocityFactorForReferenceStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VelocityFactorForReferenceStress
        return temp

    @property
    def velocity_factor_for_static_stress(self) -> 'float':
        """float: 'VelocityFactorForStaticStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VelocityFactorForStaticStress
        return temp

    @property
    def work_hardening_factor(self) -> 'float':
        """float: 'WorkHardeningFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorkHardeningFactor
        return temp

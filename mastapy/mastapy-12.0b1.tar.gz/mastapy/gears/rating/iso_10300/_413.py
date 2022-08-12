"""_413.py

ISO10300MeshSingleFlankRating
"""


from typing import Generic, TypeVar

from mastapy._internal import constructor
from mastapy.gears.rating.conical import _536
from mastapy.gears.rating.virtual_cylindrical_gears import _380
from mastapy._internal.python_net import python_net_import

_ISO10300_MESH_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Iso10300', 'ISO10300MeshSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO10300MeshSingleFlankRating',)


T = TypeVar('T', bound='_380.VirtualCylindricalGearBasic')


class ISO10300MeshSingleFlankRating(_536.ConicalMeshSingleFlankRating, Generic[T]):
    """ISO10300MeshSingleFlankRating

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _ISO10300_MESH_SINGLE_FLANK_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ISO10300MeshSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def accuracy_grade_according_to_iso17485(self) -> 'float':
        """float: 'AccuracyGradeAccordingToISO17485' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AccuracyGradeAccordingToISO17485
        return temp

    @property
    def application_factor(self) -> 'float':
        """float: 'ApplicationFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ApplicationFactor
        return temp

    @property
    def auxiliary_factor_a_for_calculating_the_dynamic_factor_kvc(self) -> 'float':
        """float: 'AuxiliaryFactorAForCalculatingTheDynamicFactorKVC' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AuxiliaryFactorAForCalculatingTheDynamicFactorKVC
        return temp

    @property
    def auxiliary_factor_x_for_calculating_the_dynamic_factor_kvc(self) -> 'float':
        """float: 'AuxiliaryFactorXForCalculatingTheDynamicFactorKVC' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AuxiliaryFactorXForCalculatingTheDynamicFactorKVC
        return temp

    @property
    def correction_factor_of_tooth_stiffness_for_non_average_conditions(self) -> 'float':
        """float: 'CorrectionFactorOfToothStiffnessForNonAverageConditions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CorrectionFactorOfToothStiffnessForNonAverageConditions
        return temp

    @property
    def cv_1_dynamic_factor_influence_factor(self) -> 'float':
        """float: 'Cv1DynamicFactorInfluenceFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Cv1DynamicFactorInfluenceFactor
        return temp

    @property
    def cv_12_dynamic_factor_influence_factor(self) -> 'float':
        """float: 'Cv12DynamicFactorInfluenceFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Cv12DynamicFactorInfluenceFactor
        return temp

    @property
    def cv_2_dynamic_factor_influence_factor(self) -> 'float':
        """float: 'Cv2DynamicFactorInfluenceFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Cv2DynamicFactorInfluenceFactor
        return temp

    @property
    def cv_3_dynamic_factor_influence_factor(self) -> 'float':
        """float: 'Cv3DynamicFactorInfluenceFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Cv3DynamicFactorInfluenceFactor
        return temp

    @property
    def cv_4_dynamic_factor_influence_factor(self) -> 'float':
        """float: 'Cv4DynamicFactorInfluenceFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Cv4DynamicFactorInfluenceFactor
        return temp

    @property
    def cv_5_dynamic_factor_influence_factor(self) -> 'float':
        """float: 'Cv5DynamicFactorInfluenceFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Cv5DynamicFactorInfluenceFactor
        return temp

    @property
    def cv_56_dynamic_factor_influence_factor(self) -> 'float':
        """float: 'Cv56DynamicFactorInfluenceFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Cv56DynamicFactorInfluenceFactor
        return temp

    @property
    def cv_6_dynamic_factor_influence_factor(self) -> 'float':
        """float: 'Cv6DynamicFactorInfluenceFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Cv6DynamicFactorInfluenceFactor
        return temp

    @property
    def cv_7_dynamic_factor_influence_factor(self) -> 'float':
        """float: 'Cv7DynamicFactorInfluenceFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Cv7DynamicFactorInfluenceFactor
        return temp

    @property
    def dimensionless_reference_speed(self) -> 'float':
        """float: 'DimensionlessReferenceSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DimensionlessReferenceSpeed
        return temp

    @property
    def dynamic_factor(self) -> 'float':
        """float: 'DynamicFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicFactor
        return temp

    @property
    def dynamic_factor_for_method_b(self) -> 'float':
        """float: 'DynamicFactorForMethodB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicFactorForMethodB
        return temp

    @property
    def dynamic_factor_for_method_b_intermediate_sector(self) -> 'float':
        """float: 'DynamicFactorForMethodBIntermediateSector' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicFactorForMethodBIntermediateSector
        return temp

    @property
    def dynamic_factor_for_method_b_main_resonance_sector(self) -> 'float':
        """float: 'DynamicFactorForMethodBMainResonanceSector' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicFactorForMethodBMainResonanceSector
        return temp

    @property
    def dynamic_factor_for_method_b_sub_critical_sector(self) -> 'float':
        """float: 'DynamicFactorForMethodBSubCriticalSector' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicFactorForMethodBSubCriticalSector
        return temp

    @property
    def dynamic_factor_for_method_b_super_critical_sector(self) -> 'float':
        """float: 'DynamicFactorForMethodBSuperCriticalSector' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicFactorForMethodBSuperCriticalSector
        return temp

    @property
    def dynamic_factor_for_method_c(self) -> 'float':
        """float: 'DynamicFactorForMethodC' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicFactorForMethodC
        return temp

    @property
    def effective_pitch_deviation(self) -> 'float':
        """float: 'EffectivePitchDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EffectivePitchDeviation
        return temp

    @property
    def elasticity_factor(self) -> 'float':
        """float: 'ElasticityFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElasticityFactor
        return temp

    @property
    def exponent_in_the_formula_for_lengthwise_curvature_factor(self) -> 'float':
        """float: 'ExponentInTheFormulaForLengthwiseCurvatureFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExponentInTheFormulaForLengthwiseCurvatureFactor
        return temp

    @property
    def face_load_factor_bending(self) -> 'float':
        """float: 'FaceLoadFactorBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceLoadFactorBending
        return temp

    @property
    def face_load_factor_contact(self) -> 'float':
        """float: 'FaceLoadFactorContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceLoadFactorContact
        return temp

    @property
    def face_load_factor_for_method_c_contact(self) -> 'float':
        """float: 'FaceLoadFactorForMethodCContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceLoadFactorForMethodCContact
        return temp

    @property
    def factor_for_calculating_the_dynamic_factor_kvb(self) -> 'float':
        """float: 'FactorForCalculatingTheDynamicFactorKVB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FactorForCalculatingTheDynamicFactorKVB
        return temp

    @property
    def lead_angle_of_face_hobbing_cutter(self) -> 'float':
        """float: 'LeadAngleOfFaceHobbingCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadAngleOfFaceHobbingCutter
        return temp

    @property
    def lengthwise_curvature_factor_for_bending_stress(self) -> 'float':
        """float: 'LengthwiseCurvatureFactorForBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LengthwiseCurvatureFactorForBendingStress
        return temp

    @property
    def lengthwise_tooth_mean_radius_of_curvature(self) -> 'float':
        """float: 'LengthwiseToothMeanRadiusOfCurvature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LengthwiseToothMeanRadiusOfCurvature
        return temp

    @property
    def max_single_pitch_deviation(self) -> 'float':
        """float: 'MaxSinglePitchDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaxSinglePitchDeviation
        return temp

    @property
    def max_wheel_tangential_speed_at_outer_end_heel_of_the_reference_cone(self) -> 'float':
        """float: 'MaxWheelTangentialSpeedAtOuterEndHeelOfTheReferenceCone' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaxWheelTangentialSpeedAtOuterEndHeelOfTheReferenceCone
        return temp

    @property
    def mean_mesh_stiffness(self) -> 'float':
        """float: 'MeanMeshStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanMeshStiffness
        return temp

    @property
    def mean_relative_roughness(self) -> 'float':
        """float: 'MeanRelativeRoughness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanRelativeRoughness
        return temp

    @property
    def modulus_of_elasticity(self) -> 'float':
        """float: 'ModulusOfElasticity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModulusOfElasticity
        return temp

    @property
    def nominal_tangential_force_of_virtual_cylindrical_gear(self) -> 'float':
        """float: 'NominalTangentialForceOfVirtualCylindricalGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalTangentialForceOfVirtualCylindricalGear
        return temp

    @property
    def pinion_running_in_allowance_for_through_hardened_steels(self) -> 'float':
        """float: 'PinionRunningInAllowanceForThroughHardenedSteels' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionRunningInAllowanceForThroughHardenedSteels
        return temp

    @property
    def preliminary_transverse_load_factor_for_contact_method_b(self) -> 'float':
        """float: 'PreliminaryTransverseLoadFactorForContactMethodB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PreliminaryTransverseLoadFactorForContactMethodB
        return temp

    @property
    def preliminary_transverse_load_factor_for_contact_method_c(self) -> 'float':
        """float: 'PreliminaryTransverseLoadFactorForContactMethodC' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PreliminaryTransverseLoadFactorForContactMethodC
        return temp

    @property
    def rating_standard_name(self) -> 'str':
        """str: 'RatingStandardName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatingStandardName
        return temp

    @property
    def relative_hypoid_offset(self) -> 'float':
        """float: 'RelativeHypoidOffset' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeHypoidOffset
        return temp

    @property
    def relative_mass_per_unit_face_width(self) -> 'float':
        """float: 'RelativeMassPerUnitFaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeMassPerUnitFaceWidth
        return temp

    @property
    def resonance_speed_of_pinion(self) -> 'float':
        """float: 'ResonanceSpeedOfPinion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResonanceSpeedOfPinion
        return temp

    @property
    def running_in_allowance(self) -> 'float':
        """float: 'RunningInAllowance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RunningInAllowance
        return temp

    @property
    def running_in_allowance_for_case_hardened_and_nitrided_gears(self) -> 'float':
        """float: 'RunningInAllowanceForCaseHardenedAndNitridedGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RunningInAllowanceForCaseHardenedAndNitridedGears
        return temp

    @property
    def running_in_allowance_for_grey_cast_iron(self) -> 'float':
        """float: 'RunningInAllowanceForGreyCastIron' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RunningInAllowanceForGreyCastIron
        return temp

    @property
    def single_stiffness(self) -> 'float':
        """float: 'SingleStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SingleStiffness
        return temp

    @property
    def tangential_force_at_mid_face_width_on_the_pitch_cone(self) -> 'float':
        """float: 'TangentialForceAtMidFaceWidthOnThePitchCone' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TangentialForceAtMidFaceWidthOnThePitchCone
        return temp

    @property
    def transverse_load_factor_for_bending_stress(self) -> 'float':
        """float: 'TransverseLoadFactorForBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseLoadFactorForBendingStress
        return temp

    @property
    def transverse_load_factor_for_bending_stress_method_b(self) -> 'float':
        """float: 'TransverseLoadFactorForBendingStressMethodB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseLoadFactorForBendingStressMethodB
        return temp

    @property
    def transverse_load_factor_for_bending_stress_method_c(self) -> 'float':
        """float: 'TransverseLoadFactorForBendingStressMethodC' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseLoadFactorForBendingStressMethodC
        return temp

    @property
    def transverse_load_factor_for_bevel_gear_with_virtual_contact_ratio_greater_than_2(self) -> 'float':
        """float: 'TransverseLoadFactorForBevelGearWithVirtualContactRatioGreaterThan2' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseLoadFactorForBevelGearWithVirtualContactRatioGreaterThan2
        return temp

    @property
    def transverse_load_factor_for_contact(self) -> 'float':
        """float: 'TransverseLoadFactorForContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseLoadFactorForContact
        return temp

    @property
    def transverse_load_factors_for_bevel_gear_with_virtual_contact_ratio_less_or_equal_to_2(self) -> 'float':
        """float: 'TransverseLoadFactorsForBevelGearWithVirtualContactRatioLessOrEqualTo2' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseLoadFactorsForBevelGearWithVirtualContactRatioLessOrEqualTo2
        return temp

    @property
    def wheel_running_in_allowance_for_through_hardened_steels(self) -> 'float':
        """float: 'WheelRunningInAllowanceForThroughHardenedSteels' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelRunningInAllowanceForThroughHardenedSteels
        return temp

    @property
    def wheel_tangential_speed_at_outer_end_heel_of_the_reference_cone(self) -> 'float':
        """float: 'WheelTangentialSpeedAtOuterEndHeelOfTheReferenceCone' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelTangentialSpeedAtOuterEndHeelOfTheReferenceCone
        return temp

    @property
    def eta_1(self) -> 'float':
        """float: 'Eta1' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Eta1
        return temp

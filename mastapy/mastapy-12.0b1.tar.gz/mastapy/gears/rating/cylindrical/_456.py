"""_456.py

CylindricalGearSingleFlankRating
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears.rating.cylindrical import _452
from mastapy.materials import _266
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.rating import _355
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'CylindricalGearSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSingleFlankRating',)


class CylindricalGearSingleFlankRating(_355.GearSingleFlankRating):
    """CylindricalGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SINGLE_FLANK_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_stress_number_bending(self) -> 'float':
        """float: 'AllowableStressNumberBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableStressNumberBending
        return temp

    @property
    def allowable_stress_number_contact(self) -> 'float':
        """float: 'AllowableStressNumberContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableStressNumberContact
        return temp

    @property
    def angular_velocity(self) -> 'float':
        """float: 'AngularVelocity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngularVelocity
        return temp

    @property
    def averaged_linear_wear(self) -> 'float':
        """float: 'AveragedLinearWear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AveragedLinearWear
        return temp

    @property
    def axial_pitch(self) -> 'float':
        """float: 'AxialPitch' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialPitch
        return temp

    @property
    def base_diameter(self) -> 'float':
        """float: 'BaseDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BaseDiameter
        return temp

    @property
    def base_helix_angle(self) -> 'float':
        """float: 'BaseHelixAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BaseHelixAngle
        return temp

    @property
    def base_transverse_pitch(self) -> 'float':
        """float: 'BaseTransversePitch' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BaseTransversePitch
        return temp

    @property
    def bending_moment_arm(self) -> 'float':
        """float: 'BendingMomentArm' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BendingMomentArm
        return temp

    @property
    def bending_safety_factor_for_fatigue(self) -> 'float':
        """float: 'BendingSafetyFactorForFatigue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BendingSafetyFactorForFatigue
        return temp

    @property
    def calculated_contact_stress(self) -> 'float':
        """float: 'CalculatedContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedContactStress
        return temp

    @property
    def combined_tip_relief(self) -> 'float':
        """float: 'CombinedTipRelief' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CombinedTipRelief
        return temp

    @property
    def contact_safety_factor_for_fatigue(self) -> 'float':
        """float: 'ContactSafetyFactorForFatigue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactSafetyFactorForFatigue
        return temp

    @property
    def contact_stress_source(self) -> 'str':
        """str: 'ContactStressSource' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactStressSource
        return temp

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
    def damage_wear(self) -> 'float':
        """float: 'DamageWear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DamageWear
        return temp

    @property
    def fillet_roughness_rz(self) -> 'float':
        """float: 'FilletRoughnessRz' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FilletRoughnessRz
        return temp

    @property
    def flank_roughness_rz(self) -> 'float':
        """float: 'FlankRoughnessRz' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlankRoughnessRz
        return temp

    @property
    def gear_rotation_speed(self) -> 'float':
        """float: 'GearRotationSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearRotationSpeed
        return temp

    @property
    def geometry_data_source_for_rating(self) -> '_452.CylindricalGearRatingGeometryDataSource':
        """CylindricalGearRatingGeometryDataSource: 'GeometryDataSourceForRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GeometryDataSourceForRating
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_452.CylindricalGearRatingGeometryDataSource)(value) if value is not None else None

    @property
    def helix_angle(self) -> 'float':
        """float: 'HelixAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixAngle
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
    def metal_plastic(self) -> '_266.MetalPlasticType':
        """MetalPlasticType: 'MetalPlastic' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MetalPlastic
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_266.MetalPlasticType)(value) if value is not None else None

    @property
    def minimum_factor_of_safety_bending_fatigue(self) -> 'float':
        """float: 'MinimumFactorOfSafetyBendingFatigue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumFactorOfSafetyBendingFatigue
        return temp

    @property
    def minimum_factor_of_safety_pitting_fatigue(self) -> 'float':
        """float: 'MinimumFactorOfSafetyPittingFatigue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumFactorOfSafetyPittingFatigue
        return temp

    @property
    def nominal_stress_number_bending(self) -> 'float':
        """float: 'NominalStressNumberBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalStressNumberBending
        return temp

    @property
    def normal_base_pitch(self) -> 'float':
        """float: 'NormalBasePitch' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalBasePitch
        return temp

    @property
    def normal_module(self) -> 'float':
        """float: 'NormalModule' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalModule
        return temp

    @property
    def normal_pitch(self) -> 'float':
        """float: 'NormalPitch' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalPitch
        return temp

    @property
    def normal_pressure_angle(self) -> 'float':
        """float: 'NormalPressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalPressureAngle
        return temp

    @property
    def permissible_contact_stress(self) -> 'float':
        """float: 'PermissibleContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermissibleContactStress
        return temp

    @property
    def permissible_contact_stress_for_reference_stress(self) -> 'float':
        """float: 'PermissibleContactStressForReferenceStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermissibleContactStressForReferenceStress
        return temp

    @property
    def permissible_contact_stress_for_static_stress(self) -> 'float':
        """float: 'PermissibleContactStressForStaticStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermissibleContactStressForStaticStress
        return temp

    @property
    def permissible_linear_wear(self) -> 'float':
        """float: 'PermissibleLinearWear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermissibleLinearWear
        return temp

    @property
    def permissible_tooth_root_bending_stress(self) -> 'float':
        """float: 'PermissibleToothRootBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermissibleToothRootBendingStress
        return temp

    @property
    def permissible_tooth_root_bending_stress_for_reference_stress(self) -> 'float':
        """float: 'PermissibleToothRootBendingStressForReferenceStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermissibleToothRootBendingStressForReferenceStress
        return temp

    @property
    def permissible_tooth_root_bending_stress_for_static_stress(self) -> 'float':
        """float: 'PermissibleToothRootBendingStressForStaticStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermissibleToothRootBendingStressForStaticStress
        return temp

    @property
    def pitch_diameter(self) -> 'float':
        """float: 'PitchDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PitchDiameter
        return temp

    @property
    def pitting_stress_limit(self) -> 'float':
        """float: 'PittingStressLimit' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PittingStressLimit
        return temp

    @property
    def pitting_stress_limit_for_reference_stress(self) -> 'float':
        """float: 'PittingStressLimitForReferenceStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PittingStressLimitForReferenceStress
        return temp

    @property
    def pitting_stress_limit_for_static_stress(self) -> 'float':
        """float: 'PittingStressLimitForStaticStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PittingStressLimitForStaticStress
        return temp

    @property
    def reliability_bending(self) -> 'float':
        """float: 'ReliabilityBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReliabilityBending
        return temp

    @property
    def reliability_contact(self) -> 'float':
        """float: 'ReliabilityContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReliabilityContact
        return temp

    @property
    def reversed_bending_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ReversedBendingFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReversedBendingFactor
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @property
    def rim_thickness(self) -> 'float':
        """float: 'RimThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RimThickness
        return temp

    @property
    def rim_thickness_factor(self) -> 'float':
        """float: 'RimThicknessFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RimThicknessFactor
        return temp

    @property
    def rim_thickness_over_normal_module(self) -> 'float':
        """float: 'RimThicknessOverNormalModule' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RimThicknessOverNormalModule
        return temp

    @property
    def root_fillet_radius(self) -> 'float':
        """float: 'RootFilletRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RootFilletRadius
        return temp

    @property
    def safety_factor_wear(self) -> 'float':
        """float: 'SafetyFactorWear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorWear
        return temp

    @property
    def size_factor_contact(self) -> 'float':
        """float: 'SizeFactorContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SizeFactorContact
        return temp

    @property
    def static_safety_factor_bending(self) -> 'float':
        """float: 'StaticSafetyFactorBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StaticSafetyFactorBending
        return temp

    @property
    def static_safety_factor_contact(self) -> 'float':
        """float: 'StaticSafetyFactorContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StaticSafetyFactorContact
        return temp

    @property
    def stress_cycle_factor_bending(self) -> 'float':
        """float: 'StressCycleFactorBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StressCycleFactorBending
        return temp

    @property
    def thermal_contact_coefficient_for_report(self) -> 'float':
        """float: 'ThermalContactCoefficientForReport' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ThermalContactCoefficientForReport
        return temp

    @property
    def tooth_passing_speed(self) -> 'float':
        """float: 'ToothPassingSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothPassingSpeed
        return temp

    @property
    def tooth_root_chord_at_critical_section(self) -> 'float':
        """float: 'ToothRootChordAtCriticalSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothRootChordAtCriticalSection
        return temp

    @property
    def tooth_root_stress(self) -> 'float':
        """float: 'ToothRootStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothRootStress
        return temp

    @property
    def tooth_root_stress_limit(self) -> 'float':
        """float: 'ToothRootStressLimit' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothRootStressLimit
        return temp

    @property
    def tooth_root_stress_limit_for_reference_stress(self) -> 'float':
        """float: 'ToothRootStressLimitForReferenceStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothRootStressLimitForReferenceStress
        return temp

    @property
    def tooth_root_stress_limit_for_static_stress(self) -> 'float':
        """float: 'ToothRootStressLimitForStaticStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothRootStressLimitForStaticStress
        return temp

    @property
    def tooth_root_stress_source(self) -> 'str':
        """str: 'ToothRootStressSource' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothRootStressSource
        return temp

    @property
    def transverse_module(self) -> 'float':
        """float: 'TransverseModule' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseModule
        return temp

    @property
    def transverse_pitch(self) -> 'float':
        """float: 'TransversePitch' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransversePitch
        return temp

    @property
    def transverse_pressure_angle(self) -> 'float':
        """float: 'TransversePressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransversePressureAngle
        return temp

    @property
    def welding_structural_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'WeldingStructuralFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WeldingStructuralFactor
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

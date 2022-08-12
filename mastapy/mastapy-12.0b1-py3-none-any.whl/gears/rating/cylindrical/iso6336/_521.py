"""_521.py

ToothFlankFractureStressStepAtAnalysisPointN1457
"""


from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.cylindrical import _1016
from mastapy._math.vector_2d import Vector2D
from mastapy.math_utility.measured_vectors import _1523
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_TOOTH_FLANK_FRACTURE_STRESS_STEP_AT_ANALYSIS_POINT_N1457 = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336', 'ToothFlankFractureStressStepAtAnalysisPointN1457')


__docformat__ = 'restructuredtext en'
__all__ = ('ToothFlankFractureStressStepAtAnalysisPointN1457',)


class ToothFlankFractureStressStepAtAnalysisPointN1457(_0.APIBase):
    """ToothFlankFractureStressStepAtAnalysisPointN1457

    This is a mastapy class.
    """

    TYPE = _TOOTH_FLANK_FRACTURE_STRESS_STEP_AT_ANALYSIS_POINT_N1457

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ToothFlankFractureStressStepAtAnalysisPointN1457.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def equivalent_stress(self) -> 'float':
        """float: 'EquivalentStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EquivalentStress
        return temp

    @property
    def fatigue_sensitivity_to_hydro_static_pressure(self) -> 'float':
        """float: 'FatigueSensitivityToHydroStaticPressure' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FatigueSensitivityToHydroStaticPressure
        return temp

    @property
    def first_hertzian_parameter(self) -> 'float':
        """float: 'FirstHertzianParameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FirstHertzianParameter
        return temp

    @property
    def global_normal_stress(self) -> 'float':
        """float: 'GlobalNormalStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GlobalNormalStress
        return temp

    @property
    def global_shear_stress(self) -> 'float':
        """float: 'GlobalShearStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GlobalShearStress
        return temp

    @property
    def global_transverse_stress(self) -> 'float':
        """float: 'GlobalTransverseStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GlobalTransverseStress
        return temp

    @property
    def hydrostatic_pressure(self) -> 'float':
        """float: 'HydrostaticPressure' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HydrostaticPressure
        return temp

    @property
    def normal_stress_due_to_friction(self) -> 'float':
        """float: 'NormalStressDueToFriction' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalStressDueToFriction
        return temp

    @property
    def normal_stress_due_to_normal_load(self) -> 'float':
        """float: 'NormalStressDueToNormalLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalStressDueToNormalLoad
        return temp

    @property
    def second_hertzian_parameter(self) -> 'float':
        """float: 'SecondHertzianParameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SecondHertzianParameter
        return temp

    @property
    def second_stress_invariant(self) -> 'float':
        """float: 'SecondStressInvariant' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SecondStressInvariant
        return temp

    @property
    def shear_stress_due_to_friction(self) -> 'float':
        """float: 'ShearStressDueToFriction' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShearStressDueToFriction
        return temp

    @property
    def shear_stress_due_to_normal_load(self) -> 'float':
        """float: 'ShearStressDueToNormalLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShearStressDueToNormalLoad
        return temp

    @property
    def third_normal_stress(self) -> 'float':
        """float: 'ThirdNormalStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ThirdNormalStress
        return temp

    @property
    def transverse_stress_due_to_friction(self) -> 'float':
        """float: 'TransverseStressDueToFriction' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseStressDueToFriction
        return temp

    @property
    def transverse_stress_due_to_normal_load(self) -> 'float':
        """float: 'TransverseStressDueToNormalLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseStressDueToNormalLoad
        return temp

    @property
    def contact_position_on_profile(self) -> '_1016.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'ContactPositionOnProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactPositionOnProfile
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def relative_coordinates(self) -> 'Vector2D':
        """Vector2D: 'RelativeCoordinates' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeCoordinates
        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def stress(self) -> '_1523.VectorWithLinearAndAngularComponents':
        """VectorWithLinearAndAngularComponents: 'Stress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Stress
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

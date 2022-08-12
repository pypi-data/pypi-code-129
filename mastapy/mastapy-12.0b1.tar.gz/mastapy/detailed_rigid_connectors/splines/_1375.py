"""_1375.py

SplineHalfDesign
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.detailed_rigid_connectors.splines import (
    _1359, _1376, _1351, _1354,
    _1358, _1361, _1362, _1369,
    _1381
)
from mastapy.detailed_rigid_connectors.splines.tolerances_and_deviations import _1382
from mastapy._internal.cast_exception import CastException
from mastapy.detailed_rigid_connectors import _1349
from mastapy._internal.python_net import python_net_import

_SPLINE_HALF_DESIGN = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Splines', 'SplineHalfDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('SplineHalfDesign',)


class SplineHalfDesign(_1349.DetailedRigidConnectorHalfDesign):
    """SplineHalfDesign

    This is a mastapy class.
    """

    TYPE = _SPLINE_HALF_DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SplineHalfDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_bending_stress(self) -> 'float':
        """float: 'AllowableBendingStress' is the original name of this property."""

        temp = self.wrapped.AllowableBendingStress
        return temp

    @allowable_bending_stress.setter
    def allowable_bending_stress(self, value: 'float'):
        self.wrapped.AllowableBendingStress = float(value) if value else 0.0

    @property
    def allowable_bursting_stress(self) -> 'float':
        """float: 'AllowableBurstingStress' is the original name of this property."""

        temp = self.wrapped.AllowableBurstingStress
        return temp

    @allowable_bursting_stress.setter
    def allowable_bursting_stress(self, value: 'float'):
        self.wrapped.AllowableBurstingStress = float(value) if value else 0.0

    @property
    def allowable_compressive_stress(self) -> 'float':
        """float: 'AllowableCompressiveStress' is the original name of this property."""

        temp = self.wrapped.AllowableCompressiveStress
        return temp

    @allowable_compressive_stress.setter
    def allowable_compressive_stress(self, value: 'float'):
        self.wrapped.AllowableCompressiveStress = float(value) if value else 0.0

    @property
    def allowable_contact_stress(self) -> 'float':
        """float: 'AllowableContactStress' is the original name of this property."""

        temp = self.wrapped.AllowableContactStress
        return temp

    @allowable_contact_stress.setter
    def allowable_contact_stress(self, value: 'float'):
        self.wrapped.AllowableContactStress = float(value) if value else 0.0

    @property
    def allowable_shear_stress(self) -> 'float':
        """float: 'AllowableShearStress' is the original name of this property."""

        temp = self.wrapped.AllowableShearStress
        return temp

    @allowable_shear_stress.setter
    def allowable_shear_stress(self, value: 'float'):
        self.wrapped.AllowableShearStress = float(value) if value else 0.0

    @property
    def ball_or_pin_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'BallOrPinDiameter' is the original name of this property."""

        temp = self.wrapped.BallOrPinDiameter
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @ball_or_pin_diameter.setter
    def ball_or_pin_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.BallOrPinDiameter = value

    @property
    def core_hardness_h_rc(self) -> 'float':
        """float: 'CoreHardnessHRc' is the original name of this property."""

        temp = self.wrapped.CoreHardnessHRc
        return temp

    @core_hardness_h_rc.setter
    def core_hardness_h_rc(self, value: 'float'):
        self.wrapped.CoreHardnessHRc = float(value) if value else 0.0

    @property
    def designation(self) -> 'str':
        """str: 'Designation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Designation
        return temp

    @property
    def form_diameter(self) -> 'float':
        """float: 'FormDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FormDiameter
        return temp

    @property
    def heat_treatment(self) -> '_1359.HeatTreatmentTypes':
        """HeatTreatmentTypes: 'HeatTreatment' is the original name of this property."""

        temp = self.wrapped.HeatTreatment
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1359.HeatTreatmentTypes)(value) if value is not None else None

    @heat_treatment.setter
    def heat_treatment(self, value: '_1359.HeatTreatmentTypes'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.HeatTreatment = value

    @property
    def major_diameter(self) -> 'float':
        """float: 'MajorDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MajorDiameter
        return temp

    @property
    def maximum_actual_space_width(self) -> 'float':
        """float: 'MaximumActualSpaceWidth' is the original name of this property."""

        temp = self.wrapped.MaximumActualSpaceWidth
        return temp

    @maximum_actual_space_width.setter
    def maximum_actual_space_width(self, value: 'float'):
        self.wrapped.MaximumActualSpaceWidth = float(value) if value else 0.0

    @property
    def maximum_actual_tooth_thickness(self) -> 'float':
        """float: 'MaximumActualToothThickness' is the original name of this property."""

        temp = self.wrapped.MaximumActualToothThickness
        return temp

    @maximum_actual_tooth_thickness.setter
    def maximum_actual_tooth_thickness(self, value: 'float'):
        self.wrapped.MaximumActualToothThickness = float(value) if value else 0.0

    @property
    def maximum_chordal_span_over_teeth(self) -> 'float':
        """float: 'MaximumChordalSpanOverTeeth' is the original name of this property."""

        temp = self.wrapped.MaximumChordalSpanOverTeeth
        return temp

    @maximum_chordal_span_over_teeth.setter
    def maximum_chordal_span_over_teeth(self, value: 'float'):
        self.wrapped.MaximumChordalSpanOverTeeth = float(value) if value else 0.0

    @property
    def maximum_dimension_over_balls(self) -> 'float':
        """float: 'MaximumDimensionOverBalls' is the original name of this property."""

        temp = self.wrapped.MaximumDimensionOverBalls
        return temp

    @maximum_dimension_over_balls.setter
    def maximum_dimension_over_balls(self, value: 'float'):
        self.wrapped.MaximumDimensionOverBalls = float(value) if value else 0.0

    @property
    def maximum_effective_tooth_thickness(self) -> 'float':
        """float: 'MaximumEffectiveToothThickness' is the original name of this property."""

        temp = self.wrapped.MaximumEffectiveToothThickness
        return temp

    @maximum_effective_tooth_thickness.setter
    def maximum_effective_tooth_thickness(self, value: 'float'):
        self.wrapped.MaximumEffectiveToothThickness = float(value) if value else 0.0

    @property
    def maximum_major_diameter(self) -> 'float':
        """float: 'MaximumMajorDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumMajorDiameter
        return temp

    @property
    def maximum_minor_diameter(self) -> 'float':
        """float: 'MaximumMinorDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumMinorDiameter
        return temp

    @property
    def mean_actual_space_width(self) -> 'float':
        """float: 'MeanActualSpaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanActualSpaceWidth
        return temp

    @property
    def mean_actual_tooth_thickness(self) -> 'float':
        """float: 'MeanActualToothThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanActualToothThickness
        return temp

    @property
    def minimum_actual_space_width(self) -> 'float':
        """float: 'MinimumActualSpaceWidth' is the original name of this property."""

        temp = self.wrapped.MinimumActualSpaceWidth
        return temp

    @minimum_actual_space_width.setter
    def minimum_actual_space_width(self, value: 'float'):
        self.wrapped.MinimumActualSpaceWidth = float(value) if value else 0.0

    @property
    def minimum_actual_tooth_thickness(self) -> 'float':
        """float: 'MinimumActualToothThickness' is the original name of this property."""

        temp = self.wrapped.MinimumActualToothThickness
        return temp

    @minimum_actual_tooth_thickness.setter
    def minimum_actual_tooth_thickness(self, value: 'float'):
        self.wrapped.MinimumActualToothThickness = float(value) if value else 0.0

    @property
    def minimum_chordal_span_over_teeth(self) -> 'float':
        """float: 'MinimumChordalSpanOverTeeth' is the original name of this property."""

        temp = self.wrapped.MinimumChordalSpanOverTeeth
        return temp

    @minimum_chordal_span_over_teeth.setter
    def minimum_chordal_span_over_teeth(self, value: 'float'):
        self.wrapped.MinimumChordalSpanOverTeeth = float(value) if value else 0.0

    @property
    def minimum_dimension_over_balls(self) -> 'float':
        """float: 'MinimumDimensionOverBalls' is the original name of this property."""

        temp = self.wrapped.MinimumDimensionOverBalls
        return temp

    @minimum_dimension_over_balls.setter
    def minimum_dimension_over_balls(self, value: 'float'):
        self.wrapped.MinimumDimensionOverBalls = float(value) if value else 0.0

    @property
    def minimum_effective_space_width(self) -> 'float':
        """float: 'MinimumEffectiveSpaceWidth' is the original name of this property."""

        temp = self.wrapped.MinimumEffectiveSpaceWidth
        return temp

    @minimum_effective_space_width.setter
    def minimum_effective_space_width(self, value: 'float'):
        self.wrapped.MinimumEffectiveSpaceWidth = float(value) if value else 0.0

    @property
    def minimum_major_diameter(self) -> 'float':
        """float: 'MinimumMajorDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumMajorDiameter
        return temp

    @property
    def minimum_minor_diameter(self) -> 'float':
        """float: 'MinimumMinorDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumMinorDiameter
        return temp

    @property
    def minor_diameter(self) -> 'float':
        """float: 'MinorDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinorDiameter
        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name
        return temp

    @property
    def nominal_chordal_span_over_teeth(self) -> 'float':
        """float: 'NominalChordalSpanOverTeeth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalChordalSpanOverTeeth
        return temp

    @property
    def nominal_dimension_over_balls(self) -> 'float':
        """float: 'NominalDimensionOverBalls' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalDimensionOverBalls
        return temp

    @property
    def number_of_teeth_for_chordal_span_test(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'NumberOfTeethForChordalSpanTest' is the original name of this property."""

        temp = self.wrapped.NumberOfTeethForChordalSpanTest
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @number_of_teeth_for_chordal_span_test.setter
    def number_of_teeth_for_chordal_span_test(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.NumberOfTeethForChordalSpanTest = value

    @property
    def pointed_flank_diameter(self) -> 'float':
        """float: 'PointedFlankDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PointedFlankDiameter
        return temp

    @property
    def root_fillet_radius_factor(self) -> 'float':
        """float: 'RootFilletRadiusFactor' is the original name of this property."""

        temp = self.wrapped.RootFilletRadiusFactor
        return temp

    @root_fillet_radius_factor.setter
    def root_fillet_radius_factor(self, value: 'float'):
        self.wrapped.RootFilletRadiusFactor = float(value) if value else 0.0

    @property
    def root_radius(self) -> 'float':
        """float: 'RootRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RootRadius
        return temp

    @property
    def surface_hardness_h_rc(self) -> 'float':
        """float: 'SurfaceHardnessHRc' is the original name of this property."""

        temp = self.wrapped.SurfaceHardnessHRc
        return temp

    @surface_hardness_h_rc.setter
    def surface_hardness_h_rc(self, value: 'float'):
        self.wrapped.SurfaceHardnessHRc = float(value) if value else 0.0

    @property
    def theoretical_dimension_over_balls(self) -> 'float':
        """float: 'TheoreticalDimensionOverBalls' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TheoreticalDimensionOverBalls
        return temp

    @property
    def tooth_height(self) -> 'float':
        """float: 'ToothHeight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothHeight
        return temp

    @property
    def fit_and_tolerance(self) -> '_1382.FitAndTolerance':
        """FitAndTolerance: 'FitAndTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FitAndTolerance
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def spline_joint_design(self) -> '_1376.SplineJointDesign':
        """SplineJointDesign: 'SplineJointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SplineJointDesign
        if _1376.SplineJointDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast spline_joint_design to SplineJointDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def spline_joint_design_of_type_custom_spline_joint_design(self) -> '_1351.CustomSplineJointDesign':
        """CustomSplineJointDesign: 'SplineJointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SplineJointDesign
        if _1351.CustomSplineJointDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast spline_joint_design to CustomSplineJointDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def spline_joint_design_of_type_din5480_spline_joint_design(self) -> '_1354.DIN5480SplineJointDesign':
        """DIN5480SplineJointDesign: 'SplineJointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SplineJointDesign
        if _1354.DIN5480SplineJointDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast spline_joint_design to DIN5480SplineJointDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def spline_joint_design_of_type_gbt3478_spline_joint_design(self) -> '_1358.GBT3478SplineJointDesign':
        """GBT3478SplineJointDesign: 'SplineJointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SplineJointDesign
        if _1358.GBT3478SplineJointDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast spline_joint_design to GBT3478SplineJointDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def spline_joint_design_of_type_iso4156_spline_joint_design(self) -> '_1361.ISO4156SplineJointDesign':
        """ISO4156SplineJointDesign: 'SplineJointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SplineJointDesign
        if _1361.ISO4156SplineJointDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast spline_joint_design to ISO4156SplineJointDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def spline_joint_design_of_type_jisb1603_spline_joint_design(self) -> '_1362.JISB1603SplineJointDesign':
        """JISB1603SplineJointDesign: 'SplineJointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SplineJointDesign
        if _1362.JISB1603SplineJointDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast spline_joint_design to JISB1603SplineJointDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def spline_joint_design_of_type_sae_spline_joint_design(self) -> '_1369.SAESplineJointDesign':
        """SAESplineJointDesign: 'SplineJointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SplineJointDesign
        if _1369.SAESplineJointDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast spline_joint_design to SAESplineJointDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def spline_joint_design_of_type_standard_spline_joint_design(self) -> '_1381.StandardSplineJointDesign':
        """StandardSplineJointDesign: 'SplineJointDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SplineJointDesign
        if _1381.StandardSplineJointDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast spline_joint_design to StandardSplineJointDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

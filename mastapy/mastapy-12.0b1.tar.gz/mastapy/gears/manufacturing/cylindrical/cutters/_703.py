"""_703.py

CylindricalGearRealCutterDesign
"""


from PIL.Image import Image

from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.gears.manufacturing.cylindrical.cutters import _694, _696
from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import (
    _713, _714, _715, _716,
    _717, _718, _720
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_REAL_CUTTER_DESIGN = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters', 'CylindricalGearRealCutterDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearRealCutterDesign',)


class CylindricalGearRealCutterDesign(_696.CylindricalGearAbstractCutterDesign):
    """CylindricalGearRealCutterDesign

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_REAL_CUTTER_DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearRealCutterDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cutter_and_gear_normal_base_pitch_comparison_tolerance(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CutterAndGearNormalBasePitchComparisonTolerance' is the original name of this property."""

        temp = self.wrapped.CutterAndGearNormalBasePitchComparisonTolerance
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @cutter_and_gear_normal_base_pitch_comparison_tolerance.setter
    def cutter_and_gear_normal_base_pitch_comparison_tolerance(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CutterAndGearNormalBasePitchComparisonTolerance = value

    @property
    def has_tolerances(self) -> 'bool':
        """bool: 'HasTolerances' is the original name of this property."""

        temp = self.wrapped.HasTolerances
        return temp

    @has_tolerances.setter
    def has_tolerances(self, value: 'bool'):
        self.wrapped.HasTolerances = bool(value) if value else False

    @property
    def nominal_cutter_drawing(self) -> 'Image':
        """Image: 'NominalCutterDrawing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalCutterDrawing
        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def normal_base_pitch(self) -> 'float':
        """float: 'NormalBasePitch' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalBasePitch
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
    def normal_pressure_angle_constant_base_pitch(self) -> 'float':
        """float: 'NormalPressureAngleConstantBasePitch' is the original name of this property."""

        temp = self.wrapped.NormalPressureAngleConstantBasePitch
        return temp

    @normal_pressure_angle_constant_base_pitch.setter
    def normal_pressure_angle_constant_base_pitch(self, value: 'float'):
        self.wrapped.NormalPressureAngleConstantBasePitch = float(value) if value else 0.0

    @property
    def number_of_points_for_reporting_fillet_shape(self) -> 'overridable.Overridable_int':
        """overridable.Overridable_int: 'NumberOfPointsForReportingFilletShape' is the original name of this property."""

        temp = self.wrapped.NumberOfPointsForReportingFilletShape
        return constructor.new_from_mastapy_type(overridable.Overridable_int)(temp) if temp is not None else None

    @number_of_points_for_reporting_fillet_shape.setter
    def number_of_points_for_reporting_fillet_shape(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0, is_overridden)
        self.wrapped.NumberOfPointsForReportingFilletShape = value

    @property
    def number_of_points_for_reporting_main_blade_shape(self) -> 'overridable.Overridable_int':
        """overridable.Overridable_int: 'NumberOfPointsForReportingMainBladeShape' is the original name of this property."""

        temp = self.wrapped.NumberOfPointsForReportingMainBladeShape
        return constructor.new_from_mastapy_type(overridable.Overridable_int)(temp) if temp is not None else None

    @number_of_points_for_reporting_main_blade_shape.setter
    def number_of_points_for_reporting_main_blade_shape(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0, is_overridden)
        self.wrapped.NumberOfPointsForReportingMainBladeShape = value

    @property
    def specify_custom_blade_shape(self) -> 'bool':
        """bool: 'SpecifyCustomBladeShape' is the original name of this property."""

        temp = self.wrapped.SpecifyCustomBladeShape
        return temp

    @specify_custom_blade_shape.setter
    def specify_custom_blade_shape(self, value: 'bool'):
        self.wrapped.SpecifyCustomBladeShape = bool(value) if value else False

    @property
    def customised_cutting_edge_profile(self) -> '_694.CustomisableEdgeProfile':
        """CustomisableEdgeProfile: 'CustomisedCuttingEdgeProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CustomisedCuttingEdgeProfile
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def nominal_cutter_shape(self) -> '_713.CutterShapeDefinition':
        """CutterShapeDefinition: 'NominalCutterShape' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalCutterShape
        if _713.CutterShapeDefinition.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast nominal_cutter_shape to CutterShapeDefinition. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def nominal_cutter_shape_of_type_cylindrical_gear_formed_wheel_grinder_tangible(self) -> '_714.CylindricalGearFormedWheelGrinderTangible':
        """CylindricalGearFormedWheelGrinderTangible: 'NominalCutterShape' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalCutterShape
        if _714.CylindricalGearFormedWheelGrinderTangible.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast nominal_cutter_shape to CylindricalGearFormedWheelGrinderTangible. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def nominal_cutter_shape_of_type_cylindrical_gear_hob_shape(self) -> '_715.CylindricalGearHobShape':
        """CylindricalGearHobShape: 'NominalCutterShape' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalCutterShape
        if _715.CylindricalGearHobShape.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast nominal_cutter_shape to CylindricalGearHobShape. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def nominal_cutter_shape_of_type_cylindrical_gear_shaper_tangible(self) -> '_716.CylindricalGearShaperTangible':
        """CylindricalGearShaperTangible: 'NominalCutterShape' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalCutterShape
        if _716.CylindricalGearShaperTangible.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast nominal_cutter_shape to CylindricalGearShaperTangible. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def nominal_cutter_shape_of_type_cylindrical_gear_shaver_tangible(self) -> '_717.CylindricalGearShaverTangible':
        """CylindricalGearShaverTangible: 'NominalCutterShape' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalCutterShape
        if _717.CylindricalGearShaverTangible.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast nominal_cutter_shape to CylindricalGearShaverTangible. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def nominal_cutter_shape_of_type_cylindrical_gear_worm_grinder_shape(self) -> '_718.CylindricalGearWormGrinderShape':
        """CylindricalGearWormGrinderShape: 'NominalCutterShape' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalCutterShape
        if _718.CylindricalGearWormGrinderShape.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast nominal_cutter_shape to CylindricalGearWormGrinderShape. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def nominal_cutter_shape_of_type_rack_shape(self) -> '_720.RackShape':
        """RackShape: 'NominalCutterShape' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalCutterShape
        if _720.RackShape.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast nominal_cutter_shape to RackShape. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

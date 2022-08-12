"""_988.py

FaceGearWheelDesign
"""


from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears.gear_designs.face import _981, _980
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_WHEEL_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Face', 'FaceGearWheelDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearWheelDesign',)


class FaceGearWheelDesign(_980.FaceGearDesign):
    """FaceGearWheelDesign

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_WHEEL_DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearWheelDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def addendum(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Addendum' is the original name of this property."""

        temp = self.wrapped.Addendum
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @addendum.setter
    def addendum(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Addendum = value

    @property
    def addendum_from_pitch_line_at_inner_end(self) -> 'float':
        """float: 'AddendumFromPitchLineAtInnerEnd' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AddendumFromPitchLineAtInnerEnd
        return temp

    @property
    def addendum_from_pitch_line_at_mid_face(self) -> 'float':
        """float: 'AddendumFromPitchLineAtMidFace' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AddendumFromPitchLineAtMidFace
        return temp

    @property
    def addendum_from_pitch_line_at_outer_end(self) -> 'float':
        """float: 'AddendumFromPitchLineAtOuterEnd' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AddendumFromPitchLineAtOuterEnd
        return temp

    @property
    def dedendum(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Dedendum' is the original name of this property."""

        temp = self.wrapped.Dedendum
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @dedendum.setter
    def dedendum(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Dedendum = value

    @property
    def dedendum_from_pitch_line_at_inner_end(self) -> 'float':
        """float: 'DedendumFromPitchLineAtInnerEnd' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DedendumFromPitchLineAtInnerEnd
        return temp

    @property
    def dedendum_from_pitch_line_at_mid_face(self) -> 'float':
        """float: 'DedendumFromPitchLineAtMidFace' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DedendumFromPitchLineAtMidFace
        return temp

    @property
    def dedendum_from_pitch_line_at_outer_end(self) -> 'float':
        """float: 'DedendumFromPitchLineAtOuterEnd' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DedendumFromPitchLineAtOuterEnd
        return temp

    @property
    def face_width_offset(self) -> 'float':
        """float: 'FaceWidthOffset' is the original name of this property."""

        temp = self.wrapped.FaceWidthOffset
        return temp

    @face_width_offset.setter
    def face_width_offset(self, value: 'float'):
        self.wrapped.FaceWidthOffset = float(value) if value else 0.0

    @property
    def face_width_and_diameters_specification_method(self) -> '_981.FaceGearDiameterFaceWidthSpecificationMethod':
        """FaceGearDiameterFaceWidthSpecificationMethod: 'FaceWidthAndDiametersSpecificationMethod' is the original name of this property."""

        temp = self.wrapped.FaceWidthAndDiametersSpecificationMethod
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_981.FaceGearDiameterFaceWidthSpecificationMethod)(value) if value is not None else None

    @face_width_and_diameters_specification_method.setter
    def face_width_and_diameters_specification_method(self, value: '_981.FaceGearDiameterFaceWidthSpecificationMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.FaceWidthAndDiametersSpecificationMethod = value

    @property
    def fillet_radius_at_reference_section(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'FilletRadiusAtReferenceSection' is the original name of this property."""

        temp = self.wrapped.FilletRadiusAtReferenceSection
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @fillet_radius_at_reference_section.setter
    def fillet_radius_at_reference_section(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.FilletRadiusAtReferenceSection = value

    @property
    def inner_diameter(self) -> 'float':
        """float: 'InnerDiameter' is the original name of this property."""

        temp = self.wrapped.InnerDiameter
        return temp

    @inner_diameter.setter
    def inner_diameter(self, value: 'float'):
        self.wrapped.InnerDiameter = float(value) if value else 0.0

    @property
    def mean_diameter(self) -> 'float':
        """float: 'MeanDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanDiameter
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
    def mean_pitch_radius(self) -> 'float':
        """float: 'MeanPitchRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanPitchRadius
        return temp

    @property
    def normal_pressure_angle_at_inner_end(self) -> 'float':
        """float: 'NormalPressureAngleAtInnerEnd' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalPressureAngleAtInnerEnd
        return temp

    @property
    def normal_pressure_angle_at_mid_face(self) -> 'float':
        """float: 'NormalPressureAngleAtMidFace' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalPressureAngleAtMidFace
        return temp

    @property
    def normal_pressure_angle_at_outer_end(self) -> 'float':
        """float: 'NormalPressureAngleAtOuterEnd' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalPressureAngleAtOuterEnd
        return temp

    @property
    def normal_thickness_at_reference_section(self) -> 'float':
        """float: 'NormalThicknessAtReferenceSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalThicknessAtReferenceSection
        return temp

    @property
    def outer_diameter(self) -> 'float':
        """float: 'OuterDiameter' is the original name of this property."""

        temp = self.wrapped.OuterDiameter
        return temp

    @outer_diameter.setter
    def outer_diameter(self, value: 'float'):
        self.wrapped.OuterDiameter = float(value) if value else 0.0

    @property
    def profile_shift_coefficient(self) -> 'float':
        """float: 'ProfileShiftCoefficient' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileShiftCoefficient
        return temp

    @property
    def radius_at_inner_end(self) -> 'float':
        """float: 'RadiusAtInnerEnd' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadiusAtInnerEnd
        return temp

    @property
    def radius_at_mid_face(self) -> 'float':
        """float: 'RadiusAtMidFace' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadiusAtMidFace
        return temp

    @property
    def radius_at_outer_end(self) -> 'float':
        """float: 'RadiusAtOuterEnd' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadiusAtOuterEnd
        return temp

    @property
    def reference_pitch_radius(self) -> 'float':
        """float: 'ReferencePitchRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReferencePitchRadius
        return temp

    @property
    def rim_thickness(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RimThickness' is the original name of this property."""

        temp = self.wrapped.RimThickness
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @rim_thickness.setter
    def rim_thickness(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RimThickness = value

    @property
    def whole_depth(self) -> 'float':
        """float: 'WholeDepth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WholeDepth
        return temp

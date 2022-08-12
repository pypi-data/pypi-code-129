"""_1003.py

CylindricalGearDesign
"""


from typing import List

from PIL.Image import Image

from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears import _324, _305
from mastapy.geometry.two_d import _303
from mastapy._internal.python_net import python_net_import
from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import (
    _1124, _1126, _1122, _1123,
    _1125, _1127, _1130, _1131,
    _1132, _1128, _1133, _1129
)
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.agma_gleason_conical import _1180
from mastapy.gears.gear_designs.cylindrical import (
    _992, _1001, _1013, _1019,
    _1031, _1036, _1045, _1044,
    _1046, _1047, _1008, _1011,
    _1075, _1056, _1068, _1070,
    _1009
)
from mastapy.gears.manufacturing.cylindrical import _602
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1091, _1090, _1094
from mastapy.gears.gear_designs.cylindrical.thickness_stock_and_backlash import _1079
from mastapy.gears.materials import (
    _584, _573, _575, _577,
    _581, _587, _591, _593
)
from mastapy.gears.rating.cylindrical import _445
from mastapy.gears.gear_designs import _938

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_CYLINDRICAL_GEAR_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalGearDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearDesign',)


class CylindricalGearDesign(_938.GearDesign):
    """CylindricalGearDesign

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def absolute_rim_diameter(self) -> 'float':
        """float: 'AbsoluteRimDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AbsoluteRimDiameter
        return temp

    @property
    def addendum(self) -> 'float':
        """float: 'Addendum' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Addendum
        return temp

    @property
    def dedendum(self) -> 'float':
        """float: 'Dedendum' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Dedendum
        return temp

    @property
    def effective_web_thickness(self) -> 'float':
        """float: 'EffectiveWebThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EffectiveWebThickness
        return temp

    @property
    def face_width(self) -> 'float':
        """float: 'FaceWidth' is the original name of this property."""

        temp = self.wrapped.FaceWidth
        return temp

    @face_width.setter
    def face_width(self, value: 'float'):
        self.wrapped.FaceWidth = float(value) if value else 0.0

    @property
    def factor_for_the_increase_of_the_yield_point_under_compression(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'FactorForTheIncreaseOfTheYieldPointUnderCompression' is the original name of this property."""

        temp = self.wrapped.FactorForTheIncreaseOfTheYieldPointUnderCompression
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @factor_for_the_increase_of_the_yield_point_under_compression.setter
    def factor_for_the_increase_of_the_yield_point_under_compression(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.FactorForTheIncreaseOfTheYieldPointUnderCompression = value

    @property
    def flank_heat_transfer_coefficient(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'FlankHeatTransferCoefficient' is the original name of this property."""

        temp = self.wrapped.FlankHeatTransferCoefficient
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @flank_heat_transfer_coefficient.setter
    def flank_heat_transfer_coefficient(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.FlankHeatTransferCoefficient = value

    @property
    def gear_drawing(self) -> 'Image':
        """Image: 'GearDrawing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDrawing
        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def gear_hand(self) -> 'str':
        """str: 'GearHand' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearHand
        return temp

    @property
    def gear_tooth_drawing(self) -> 'Image':
        """Image: 'GearToothDrawing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearToothDrawing
        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def hand(self) -> '_324.Hand':
        """Hand: 'Hand' is the original name of this property."""

        temp = self.wrapped.Hand
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_324.Hand)(value) if value is not None else None

    @hand.setter
    def hand(self, value: '_324.Hand'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.Hand = value

    @property
    def helix_angle(self) -> 'float':
        """float: 'HelixAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixAngle
        return temp

    @property
    def helix_angle_at_tip_form_diameter(self) -> 'float':
        """float: 'HelixAngleAtTipFormDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixAngleAtTipFormDiameter
        return temp

    @property
    def initial_clocking_angle(self) -> 'float':
        """float: 'InitialClockingAngle' is the original name of this property."""

        temp = self.wrapped.InitialClockingAngle
        return temp

    @initial_clocking_angle.setter
    def initial_clocking_angle(self, value: 'float'):
        self.wrapped.InitialClockingAngle = float(value) if value else 0.0

    @property
    def internal_external(self) -> '_303.InternalExternalType':
        """InternalExternalType: 'InternalExternal' is the original name of this property."""

        temp = self.wrapped.InternalExternal
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_303.InternalExternalType)(value) if value is not None else None

    @internal_external.setter
    def internal_external(self, value: '_303.InternalExternalType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.InternalExternal = value

    @property
    def is_asymmetric(self) -> 'bool':
        """bool: 'IsAsymmetric' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsAsymmetric
        return temp

    @property
    def lead(self) -> 'float':
        """float: 'Lead' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Lead
        return temp

    @property
    def mass(self) -> 'float':
        """float: 'Mass' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mass
        return temp

    @property
    def material_agma(self) -> 'str':
        """str: 'MaterialAGMA' is the original name of this property."""

        temp = self.wrapped.MaterialAGMA.SelectedItemName
        return temp

    @material_agma.setter
    def material_agma(self, value: 'str'):
        self.wrapped.MaterialAGMA.SetSelectedItem(str(value) if value else '')

    @property
    def material_iso(self) -> 'str':
        """str: 'MaterialISO' is the original name of this property."""

        temp = self.wrapped.MaterialISO.SelectedItemName
        return temp

    @material_iso.setter
    def material_iso(self, value: 'str'):
        self.wrapped.MaterialISO.SetSelectedItem(str(value) if value else '')

    @property
    def material_name(self) -> 'str':
        """str: 'MaterialName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaterialName
        return temp

    @property
    def maximum_tip_diameter(self) -> 'float':
        """float: 'MaximumTipDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumTipDiameter
        return temp

    @property
    def mean_generating_circle_diameter(self) -> 'float':
        """float: 'MeanGeneratingCircleDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanGeneratingCircleDiameter
        return temp

    @property
    def mean_normal_thickness_at_half_depth(self) -> 'float':
        """float: 'MeanNormalThicknessAtHalfDepth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanNormalThicknessAtHalfDepth
        return temp

    @property
    def minimum_required_rim_thickness_by_standard_iso8140042005(self) -> 'float':
        """float: 'MinimumRequiredRimThicknessByStandardISO8140042005' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumRequiredRimThicknessByStandardISO8140042005
        return temp

    @property
    def minimum_root_diameter(self) -> 'float':
        """float: 'MinimumRootDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumRootDiameter
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
    def normal_space_width_at_root_form_diameter(self) -> 'float':
        """float: 'NormalSpaceWidthAtRootFormDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalSpaceWidthAtRootFormDiameter
        return temp

    @property
    def normal_thickness_at_tip_form_diameter_at_lower_backlash_allowance(self) -> 'float':
        """float: 'NormalThicknessAtTipFormDiameterAtLowerBacklashAllowance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalThicknessAtTipFormDiameterAtLowerBacklashAllowance
        return temp

    @property
    def normal_thickness_at_tip_form_diameter_at_lower_backlash_allowance_over_normal_module(self) -> 'float':
        """float: 'NormalThicknessAtTipFormDiameterAtLowerBacklashAllowanceOverNormalModule' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalThicknessAtTipFormDiameterAtLowerBacklashAllowanceOverNormalModule
        return temp

    @property
    def normal_thickness_at_tip_form_diameter_at_upper_backlash_allowance(self) -> 'float':
        """float: 'NormalThicknessAtTipFormDiameterAtUpperBacklashAllowance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalThicknessAtTipFormDiameterAtUpperBacklashAllowance
        return temp

    @property
    def normal_tooth_thickness_at_the_base_circle(self) -> 'float':
        """float: 'NormalToothThicknessAtTheBaseCircle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalToothThicknessAtTheBaseCircle
        return temp

    @property
    def number_of_teeth_unsigned(self) -> 'float':
        """float: 'NumberOfTeethUnsigned' is the original name of this property."""

        temp = self.wrapped.NumberOfTeethUnsigned
        return temp

    @number_of_teeth_unsigned.setter
    def number_of_teeth_unsigned(self, value: 'float'):
        self.wrapped.NumberOfTeethUnsigned = float(value) if value else 0.0

    @property
    def number_of_teeth_with_centre_distance_adjustment(self) -> 'int':
        """int: 'NumberOfTeethWithCentreDistanceAdjustment' is the original name of this property."""

        temp = self.wrapped.NumberOfTeethWithCentreDistanceAdjustment
        return temp

    @number_of_teeth_with_centre_distance_adjustment.setter
    def number_of_teeth_with_centre_distance_adjustment(self, value: 'int'):
        self.wrapped.NumberOfTeethWithCentreDistanceAdjustment = int(value) if value else 0

    @property
    def number_of_teeth_maintaining_ratio_calculating_normal_module(self) -> 'int':
        """int: 'NumberOfTeethMaintainingRatioCalculatingNormalModule' is the original name of this property."""

        temp = self.wrapped.NumberOfTeethMaintainingRatioCalculatingNormalModule
        return temp

    @number_of_teeth_maintaining_ratio_calculating_normal_module.setter
    def number_of_teeth_maintaining_ratio_calculating_normal_module(self, value: 'int'):
        self.wrapped.NumberOfTeethMaintainingRatioCalculatingNormalModule = int(value) if value else 0

    @property
    def number_of_teeth_with_normal_module_adjustment(self) -> 'int':
        """int: 'NumberOfTeethWithNormalModuleAdjustment' is the original name of this property."""

        temp = self.wrapped.NumberOfTeethWithNormalModuleAdjustment
        return temp

    @number_of_teeth_with_normal_module_adjustment.setter
    def number_of_teeth_with_normal_module_adjustment(self, value: 'int'):
        self.wrapped.NumberOfTeethWithNormalModuleAdjustment = int(value) if value else 0

    @property
    def permissible_linear_wear(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'PermissibleLinearWear' is the original name of this property."""

        temp = self.wrapped.PermissibleLinearWear
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @permissible_linear_wear.setter
    def permissible_linear_wear(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.PermissibleLinearWear = value

    @property
    def radii_of_curvature_at_tip(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RadiiOfCurvatureAtTip' is the original name of this property."""

        temp = self.wrapped.RadiiOfCurvatureAtTip
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @radii_of_curvature_at_tip.setter
    def radii_of_curvature_at_tip(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RadiiOfCurvatureAtTip = value

    @property
    def radii_of_curvature_at_tip_right_flank(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RadiiOfCurvatureAtTipRightFlank' is the original name of this property."""

        temp = self.wrapped.RadiiOfCurvatureAtTipRightFlank
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @radii_of_curvature_at_tip_right_flank.setter
    def radii_of_curvature_at_tip_right_flank(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RadiiOfCurvatureAtTipRightFlank = value

    @property
    def reference_diameter(self) -> 'float':
        """float: 'ReferenceDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReferenceDiameter
        return temp

    @property
    def rim_diameter(self) -> 'float':
        """float: 'RimDiameter' is the original name of this property."""

        temp = self.wrapped.RimDiameter
        return temp

    @rim_diameter.setter
    def rim_diameter(self, value: 'float'):
        self.wrapped.RimDiameter = float(value) if value else 0.0

    @property
    def rim_thickness(self) -> 'float':
        """float: 'RimThickness' is the original name of this property."""

        temp = self.wrapped.RimThickness
        return temp

    @rim_thickness.setter
    def rim_thickness(self, value: 'float'):
        self.wrapped.RimThickness = float(value) if value else 0.0

    @property
    def rim_thickness_normal_module_ratio(self) -> 'float':
        """float: 'RimThicknessNormalModuleRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RimThicknessNormalModuleRatio
        return temp

    @property
    def root_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RootDiameter' is the original name of this property."""

        temp = self.wrapped.RootDiameter
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @root_diameter.setter
    def root_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RootDiameter = value

    @property
    def root_heat_transfer_coefficient(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RootHeatTransferCoefficient' is the original name of this property."""

        temp = self.wrapped.RootHeatTransferCoefficient
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @root_heat_transfer_coefficient.setter
    def root_heat_transfer_coefficient(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RootHeatTransferCoefficient = value

    @property
    def rotation_angle(self) -> 'float':
        """float: 'RotationAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RotationAngle
        return temp

    @property
    def signed_root_diameter(self) -> 'float':
        """float: 'SignedRootDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SignedRootDiameter
        return temp

    @property
    def signed_tip_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'SignedTipDiameter' is the original name of this property."""

        temp = self.wrapped.SignedTipDiameter
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @signed_tip_diameter.setter
    def signed_tip_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.SignedTipDiameter = value

    @property
    def specified_web_thickness(self) -> 'float':
        """float: 'SpecifiedWebThickness' is the original name of this property."""

        temp = self.wrapped.SpecifiedWebThickness
        return temp

    @specified_web_thickness.setter
    def specified_web_thickness(self, value: 'float'):
        self.wrapped.SpecifiedWebThickness = float(value) if value else 0.0

    @property
    def thermal_contact_coefficient(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ThermalContactCoefficient' is the original name of this property."""

        temp = self.wrapped.ThermalContactCoefficient
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @thermal_contact_coefficient.setter
    def thermal_contact_coefficient(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.ThermalContactCoefficient = value

    @property
    def tip_alteration_coefficient(self) -> 'float':
        """float: 'TipAlterationCoefficient' is the original name of this property."""

        temp = self.wrapped.TipAlterationCoefficient
        return temp

    @tip_alteration_coefficient.setter
    def tip_alteration_coefficient(self, value: 'float'):
        self.wrapped.TipAlterationCoefficient = float(value) if value else 0.0

    @property
    def tip_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'TipDiameter' is the original name of this property."""

        temp = self.wrapped.TipDiameter
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @tip_diameter.setter
    def tip_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.TipDiameter = value

    @property
    def tip_thickness(self) -> 'float':
        """float: 'TipThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TipThickness
        return temp

    @property
    def tip_thickness_at_lower_backlash_allowance(self) -> 'float':
        """float: 'TipThicknessAtLowerBacklashAllowance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TipThicknessAtLowerBacklashAllowance
        return temp

    @property
    def tip_thickness_at_lower_backlash_allowance_over_normal_module(self) -> 'float':
        """float: 'TipThicknessAtLowerBacklashAllowanceOverNormalModule' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TipThicknessAtLowerBacklashAllowanceOverNormalModule
        return temp

    @property
    def tip_thickness_at_upper_backlash_allowance(self) -> 'float':
        """float: 'TipThicknessAtUpperBacklashAllowance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TipThicknessAtUpperBacklashAllowance
        return temp

    @property
    def tooth_depth(self) -> 'float':
        """float: 'ToothDepth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothDepth
        return temp

    @property
    def transverse_tooth_thickness_at_the_base_circle(self) -> 'float':
        """float: 'TransverseToothThicknessAtTheBaseCircle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseToothThicknessAtTheBaseCircle
        return temp

    @property
    def use_default_design_material(self) -> 'bool':
        """bool: 'UseDefaultDesignMaterial' is the original name of this property."""

        temp = self.wrapped.UseDefaultDesignMaterial
        return temp

    @use_default_design_material.setter
    def use_default_design_material(self, value: 'bool'):
        self.wrapped.UseDefaultDesignMaterial = bool(value) if value else False

    @property
    def web_centre_offset(self) -> 'float':
        """float: 'WebCentreOffset' is the original name of this property."""

        temp = self.wrapped.WebCentreOffset
        return temp

    @web_centre_offset.setter
    def web_centre_offset(self, value: 'float'):
        self.wrapped.WebCentreOffset = float(value) if value else 0.0

    @property
    def web_status(self) -> 'str':
        """str: 'WebStatus' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WebStatus
        return temp

    @property
    def agma_accuracy_grade(self) -> '_1124.AGMA20151AccuracyGrades':
        """AGMA20151AccuracyGrades: 'AGMAAccuracyGrade' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AGMAAccuracyGrade
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def accuracy_grade_allowances_and_tolerances(self) -> '_1126.CylindricalAccuracyGrader':
        """CylindricalAccuracyGrader: 'AccuracyGradeAllowancesAndTolerances' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AccuracyGradeAllowancesAndTolerances
        if _1126.CylindricalAccuracyGrader.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grade_allowances_and_tolerances to CylindricalAccuracyGrader. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def accuracy_grade_allowances_and_tolerances_of_type_agma2000_accuracy_grader(self) -> '_1122.AGMA2000AccuracyGrader':
        """AGMA2000AccuracyGrader: 'AccuracyGradeAllowancesAndTolerances' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AccuracyGradeAllowancesAndTolerances
        if _1122.AGMA2000AccuracyGrader.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grade_allowances_and_tolerances to AGMA2000AccuracyGrader. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def accuracy_grade_allowances_and_tolerances_of_type_agma20151_accuracy_grader(self) -> '_1123.AGMA20151AccuracyGrader':
        """AGMA20151AccuracyGrader: 'AccuracyGradeAllowancesAndTolerances' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AccuracyGradeAllowancesAndTolerances
        if _1123.AGMA20151AccuracyGrader.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grade_allowances_and_tolerances to AGMA20151AccuracyGrader. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def accuracy_grade_allowances_and_tolerances_of_type_agmaiso13282013_accuracy_grader(self) -> '_1125.AGMAISO13282013AccuracyGrader':
        """AGMAISO13282013AccuracyGrader: 'AccuracyGradeAllowancesAndTolerances' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AccuracyGradeAllowancesAndTolerances
        if _1125.AGMAISO13282013AccuracyGrader.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grade_allowances_and_tolerances to AGMAISO13282013AccuracyGrader. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def accuracy_grade_allowances_and_tolerances_of_type_cylindrical_accuracy_grader_with_profile_form_and_slope(self) -> '_1127.CylindricalAccuracyGraderWithProfileFormAndSlope':
        """CylindricalAccuracyGraderWithProfileFormAndSlope: 'AccuracyGradeAllowancesAndTolerances' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AccuracyGradeAllowancesAndTolerances
        if _1127.CylindricalAccuracyGraderWithProfileFormAndSlope.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grade_allowances_and_tolerances to CylindricalAccuracyGraderWithProfileFormAndSlope. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def accuracy_grade_allowances_and_tolerances_of_type_iso13282013_accuracy_grader(self) -> '_1130.ISO13282013AccuracyGrader':
        """ISO13282013AccuracyGrader: 'AccuracyGradeAllowancesAndTolerances' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AccuracyGradeAllowancesAndTolerances
        if _1130.ISO13282013AccuracyGrader.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grade_allowances_and_tolerances to ISO13282013AccuracyGrader. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def accuracy_grade_allowances_and_tolerances_of_type_iso1328_accuracy_grader(self) -> '_1131.ISO1328AccuracyGrader':
        """ISO1328AccuracyGrader: 'AccuracyGradeAllowancesAndTolerances' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AccuracyGradeAllowancesAndTolerances
        if _1131.ISO1328AccuracyGrader.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grade_allowances_and_tolerances to ISO1328AccuracyGrader. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def accuracy_grade_allowances_and_tolerances_of_type_iso1328_accuracy_grader_common(self) -> '_1132.ISO1328AccuracyGraderCommon':
        """ISO1328AccuracyGraderCommon: 'AccuracyGradeAllowancesAndTolerances' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AccuracyGradeAllowancesAndTolerances
        if _1132.ISO1328AccuracyGraderCommon.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grade_allowances_and_tolerances to ISO1328AccuracyGraderCommon. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def accuracy_grades_specified_accuracy(self) -> '_305.AccuracyGrades':
        """AccuracyGrades: 'AccuracyGradesSpecifiedAccuracy' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AccuracyGradesSpecifiedAccuracy
        if _305.AccuracyGrades.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grades_specified_accuracy to AccuracyGrades. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def accuracy_grades_specified_accuracy_of_type_agma20151_accuracy_grades(self) -> '_1124.AGMA20151AccuracyGrades':
        """AGMA20151AccuracyGrades: 'AccuracyGradesSpecifiedAccuracy' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AccuracyGradesSpecifiedAccuracy
        if _1124.AGMA20151AccuracyGrades.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grades_specified_accuracy to AGMA20151AccuracyGrades. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def accuracy_grades_specified_accuracy_of_type_cylindrical_accuracy_grades(self) -> '_1128.CylindricalAccuracyGrades':
        """CylindricalAccuracyGrades: 'AccuracyGradesSpecifiedAccuracy' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AccuracyGradesSpecifiedAccuracy
        if _1128.CylindricalAccuracyGrades.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grades_specified_accuracy to CylindricalAccuracyGrades. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def accuracy_grades_specified_accuracy_of_type_iso1328_accuracy_grades(self) -> '_1133.ISO1328AccuracyGrades':
        """ISO1328AccuracyGrades: 'AccuracyGradesSpecifiedAccuracy' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AccuracyGradesSpecifiedAccuracy
        if _1133.ISO1328AccuracyGrades.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grades_specified_accuracy to ISO1328AccuracyGrades. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def accuracy_grades_specified_accuracy_of_type_agma_gleason_conical_accuracy_grades(self) -> '_1180.AGMAGleasonConicalAccuracyGrades':
        """AGMAGleasonConicalAccuracyGrades: 'AccuracyGradesSpecifiedAccuracy' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AccuracyGradesSpecifiedAccuracy
        if _1180.AGMAGleasonConicalAccuracyGrades.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast accuracy_grades_specified_accuracy to AGMAGleasonConicalAccuracyGrades. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def case_hardening_properties(self) -> '_992.CaseHardeningProperties':
        """CaseHardeningProperties: 'CaseHardeningProperties' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CaseHardeningProperties
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_cutting_options(self) -> '_1001.CylindricalGearCuttingOptions':
        """CylindricalGearCuttingOptions: 'CylindricalGearCuttingOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearCuttingOptions
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_manufacturing_configuration(self) -> '_602.CylindricalGearManufacturingConfig':
        """CylindricalGearManufacturingConfig: 'CylindricalGearManufacturingConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearManufacturingConfiguration
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_micro_geometry(self) -> '_1091.CylindricalGearMicroGeometryBase':
        """CylindricalGearMicroGeometryBase: 'CylindricalGearMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearMicroGeometry
        if _1091.CylindricalGearMicroGeometryBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast cylindrical_gear_micro_geometry to CylindricalGearMicroGeometryBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_micro_geometry_of_type_cylindrical_gear_micro_geometry(self) -> '_1090.CylindricalGearMicroGeometry':
        """CylindricalGearMicroGeometry: 'CylindricalGearMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearMicroGeometry
        if _1090.CylindricalGearMicroGeometry.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast cylindrical_gear_micro_geometry to CylindricalGearMicroGeometry. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_micro_geometry_of_type_cylindrical_gear_micro_geometry_per_tooth(self) -> '_1094.CylindricalGearMicroGeometryPerTooth':
        """CylindricalGearMicroGeometryPerTooth: 'CylindricalGearMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearMicroGeometry
        if _1094.CylindricalGearMicroGeometryPerTooth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast cylindrical_gear_micro_geometry to CylindricalGearMicroGeometryPerTooth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_micro_geometry_settings(self) -> '_1013.CylindricalGearMicroGeometrySettingsItem':
        """CylindricalGearMicroGeometrySettingsItem: 'CylindricalGearMicroGeometrySettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearMicroGeometrySettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def finish_stock_specification(self) -> '_1079.FinishStockSpecification':
        """FinishStockSpecification: 'FinishStockSpecification' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishStockSpecification
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def finished_tooth_thickness_specification(self) -> '_1036.FinishToothThicknessDesignSpecification':
        """FinishToothThicknessDesignSpecification: 'FinishedToothThicknessSpecification' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FinishedToothThicknessSpecification
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def iso6336_geometry(self) -> '_1045.ISO6336GeometryBase':
        """ISO6336GeometryBase: 'ISO6336Geometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO6336Geometry
        if _1045.ISO6336GeometryBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast iso6336_geometry to ISO6336GeometryBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def iso6336_geometry_of_type_iso6336_geometry(self) -> '_1044.ISO6336Geometry':
        """ISO6336Geometry: 'ISO6336Geometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO6336Geometry
        if _1044.ISO6336Geometry.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast iso6336_geometry to ISO6336Geometry. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def iso6336_geometry_of_type_iso6336_geometry_for_shaped_gears(self) -> '_1046.ISO6336GeometryForShapedGears':
        """ISO6336GeometryForShapedGears: 'ISO6336Geometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO6336Geometry
        if _1046.ISO6336GeometryForShapedGears.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast iso6336_geometry to ISO6336GeometryForShapedGears. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def iso6336_geometry_of_type_iso6336_geometry_manufactured(self) -> '_1047.ISO6336GeometryManufactured':
        """ISO6336GeometryManufactured: 'ISO6336Geometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO6336Geometry
        if _1047.ISO6336GeometryManufactured.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast iso6336_geometry to ISO6336GeometryManufactured. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def iso_accuracy_grade(self) -> '_1133.ISO1328AccuracyGrades':
        """ISO1328AccuracyGrades: 'ISOAccuracyGrade' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISOAccuracyGrade
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def left_flank(self) -> '_1008.CylindricalGearFlankDesign':
        """CylindricalGearFlankDesign: 'LeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlank
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def material(self) -> '_584.GearMaterial':
        """GearMaterial: 'Material' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Material
        if _584.GearMaterial.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast material to GearMaterial. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def material_of_type_agma_cylindrical_gear_material(self) -> '_573.AGMACylindricalGearMaterial':
        """AGMACylindricalGearMaterial: 'Material' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Material
        if _573.AGMACylindricalGearMaterial.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast material to AGMACylindricalGearMaterial. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def material_of_type_bevel_gear_iso_material(self) -> '_575.BevelGearISOMaterial':
        """BevelGearISOMaterial: 'Material' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Material
        if _575.BevelGearISOMaterial.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast material to BevelGearISOMaterial. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def material_of_type_bevel_gear_material(self) -> '_577.BevelGearMaterial':
        """BevelGearMaterial: 'Material' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Material
        if _577.BevelGearMaterial.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast material to BevelGearMaterial. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def material_of_type_cylindrical_gear_material(self) -> '_581.CylindricalGearMaterial':
        """CylindricalGearMaterial: 'Material' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Material
        if _581.CylindricalGearMaterial.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast material to CylindricalGearMaterial. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def material_of_type_iso_cylindrical_gear_material(self) -> '_587.ISOCylindricalGearMaterial':
        """ISOCylindricalGearMaterial: 'Material' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Material
        if _587.ISOCylindricalGearMaterial.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast material to ISOCylindricalGearMaterial. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def material_of_type_klingelnberg_cyclo_palloid_conical_gear_material(self) -> '_591.KlingelnbergCycloPalloidConicalGearMaterial':
        """KlingelnbergCycloPalloidConicalGearMaterial: 'Material' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Material
        if _591.KlingelnbergCycloPalloidConicalGearMaterial.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast material to KlingelnbergCycloPalloidConicalGearMaterial. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def material_of_type_plastic_cylindrical_gear_material(self) -> '_593.PlasticCylindricalGearMaterial':
        """PlasticCylindricalGearMaterial: 'Material' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Material
        if _593.PlasticCylindricalGearMaterial.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast material to PlasticCylindricalGearMaterial. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def micro_geometry_settings(self) -> '_1011.CylindricalGearMicroGeometrySettings':
        """CylindricalGearMicroGeometrySettings: 'MicroGeometrySettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicroGeometrySettings
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
    def right_flank(self) -> '_1008.CylindricalGearFlankDesign':
        """CylindricalGearFlankDesign: 'RightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlank
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rough_tooth_thickness_specification(self) -> '_1075.ToothThicknessSpecification':
        """ToothThicknessSpecification: 'RoughToothThicknessSpecification' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RoughToothThicknessSpecification
        if _1075.ToothThicknessSpecification.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rough_tooth_thickness_specification to ToothThicknessSpecification. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def surface_roughness(self) -> '_1068.SurfaceRoughness':
        """SurfaceRoughness: 'SurfaceRoughness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SurfaceRoughness
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_of_gear_fits(self) -> '_1129.DIN3967SystemOfGearFits':
        """DIN3967SystemOfGearFits: 'SystemOfGearFits' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemOfGearFits
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def tiff_analysis_settings(self) -> '_1070.TiffAnalysisSettings':
        """TiffAnalysisSettings: 'TIFFAnalysisSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TIFFAnalysisSettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_meshes(self) -> 'List[_1009.CylindricalGearMeshDesign]':
        """List[CylindricalGearMeshDesign]: 'CylindricalMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalMeshes
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def flanks(self) -> 'List[_1008.CylindricalGearFlankDesign]':
        """List[CylindricalGearFlankDesign]: 'Flanks' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Flanks
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def both_flanks(self) -> '_1008.CylindricalGearFlankDesign':
        """CylindricalGearFlankDesign: 'BothFlanks' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BothFlanks
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def manufacturing_configurations(self) -> 'List[_602.CylindricalGearManufacturingConfig]':
        """List[CylindricalGearManufacturingConfig]: 'ManufacturingConfigurations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ManufacturingConfigurations
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def micro_geometries(self) -> 'List[_1091.CylindricalGearMicroGeometryBase]':
        """List[CylindricalGearMicroGeometryBase]: 'MicroGeometries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicroGeometries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

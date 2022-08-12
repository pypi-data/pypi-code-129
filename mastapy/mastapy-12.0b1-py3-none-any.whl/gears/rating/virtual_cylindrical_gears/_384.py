"""_384.py

VirtualCylindricalGearSetISO10300MethodB1
"""


from mastapy._internal import constructor
from mastapy.gears.rating.virtual_cylindrical_gears import _383, _381
from mastapy._internal.python_net import python_net_import

_VIRTUAL_CYLINDRICAL_GEAR_SET_ISO10300_METHOD_B1 = python_net_import('SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears', 'VirtualCylindricalGearSetISO10300MethodB1')


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualCylindricalGearSetISO10300MethodB1',)


class VirtualCylindricalGearSetISO10300MethodB1(_383.VirtualCylindricalGearSet['_381.VirtualCylindricalGearISO10300MethodB1']):
    """VirtualCylindricalGearSetISO10300MethodB1

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_CYLINDRICAL_GEAR_SET_ISO10300_METHOD_B1

    __hash__ = None

    def __init__(self, instance_to_wrap: 'VirtualCylindricalGearSetISO10300MethodB1.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def auxiliary_angle_for_virtual_face_width_method_b1(self) -> 'float':
        """float: 'AuxiliaryAngleForVirtualFaceWidthMethodB1' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AuxiliaryAngleForVirtualFaceWidthMethodB1
        return temp

    @property
    def correction_factor_for_theoretical_length_of_middle_contact_line_for_surface_durability(self) -> 'float':
        """float: 'CorrectionFactorForTheoreticalLengthOfMiddleContactLineForSurfaceDurability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CorrectionFactorForTheoreticalLengthOfMiddleContactLineForSurfaceDurability
        return temp

    @property
    def distance_of_the_middle_contact_line_in_the_zone_of_action_for_surface_durability(self) -> 'float':
        """float: 'DistanceOfTheMiddleContactLineInTheZoneOfActionForSurfaceDurability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DistanceOfTheMiddleContactLineInTheZoneOfActionForSurfaceDurability
        return temp

    @property
    def distance_of_the_middle_contact_line_in_the_zone_of_action_for_tooth_root_strength(self) -> 'float':
        """float: 'DistanceOfTheMiddleContactLineInTheZoneOfActionForToothRootStrength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DistanceOfTheMiddleContactLineInTheZoneOfActionForToothRootStrength
        return temp

    @property
    def distance_of_the_root_contact_line_in_the_zone_of_action_for_surface_durability(self) -> 'float':
        """float: 'DistanceOfTheRootContactLineInTheZoneOfActionForSurfaceDurability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DistanceOfTheRootContactLineInTheZoneOfActionForSurfaceDurability
        return temp

    @property
    def distance_of_the_root_contact_line_in_the_zone_of_action_for_tooth_root_strength(self) -> 'float':
        """float: 'DistanceOfTheRootContactLineInTheZoneOfActionForToothRootStrength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DistanceOfTheRootContactLineInTheZoneOfActionForToothRootStrength
        return temp

    @property
    def distance_of_the_tip_contact_line_in_the_zone_of_action_for_surface_durability(self) -> 'float':
        """float: 'DistanceOfTheTipContactLineInTheZoneOfActionForSurfaceDurability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DistanceOfTheTipContactLineInTheZoneOfActionForSurfaceDurability
        return temp

    @property
    def distance_of_the_tip_contact_line_in_the_zone_of_action_for_tooth_root_strength(self) -> 'float':
        """float: 'DistanceOfTheTipContactLineInTheZoneOfActionForToothRootStrength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DistanceOfTheTipContactLineInTheZoneOfActionForToothRootStrength
        return temp

    @property
    def inclination_angle_of_contact_line(self) -> 'float':
        """float: 'InclinationAngleOfContactLine' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InclinationAngleOfContactLine
        return temp

    @property
    def length_of_middle_contact_line_for_surface_durability(self) -> 'float':
        """float: 'LengthOfMiddleContactLineForSurfaceDurability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LengthOfMiddleContactLineForSurfaceDurability
        return temp

    @property
    def length_of_middle_contact_line_for_tooth_root_strength(self) -> 'float':
        """float: 'LengthOfMiddleContactLineForToothRootStrength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LengthOfMiddleContactLineForToothRootStrength
        return temp

    @property
    def length_of_path_of_contact_of_virtual_cylindrical_gear_in_transverse_section(self) -> 'float':
        """float: 'LengthOfPathOfContactOfVirtualCylindricalGearInTransverseSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LengthOfPathOfContactOfVirtualCylindricalGearInTransverseSection
        return temp

    @property
    def length_of_root_contact_line_for_surface_durability(self) -> 'float':
        """float: 'LengthOfRootContactLineForSurfaceDurability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LengthOfRootContactLineForSurfaceDurability
        return temp

    @property
    def length_of_root_contact_line_for_tooth_root_strength(self) -> 'float':
        """float: 'LengthOfRootContactLineForToothRootStrength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LengthOfRootContactLineForToothRootStrength
        return temp

    @property
    def length_of_tip_contact_line_for_surface_durability(self) -> 'float':
        """float: 'LengthOfTipContactLineForSurfaceDurability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LengthOfTipContactLineForSurfaceDurability
        return temp

    @property
    def length_of_tip_contact_line_for_tooth_root_strength(self) -> 'float':
        """float: 'LengthOfTipContactLineForToothRootStrength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LengthOfTipContactLineForToothRootStrength
        return temp

    @property
    def maximum_distance_from_middle_contact_line(self) -> 'float':
        """float: 'MaximumDistanceFromMiddleContactLine' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumDistanceFromMiddleContactLine
        return temp

    @property
    def maximum_distance_from_middle_contact_line_at_left_side_of_contact_pattern(self) -> 'float':
        """float: 'MaximumDistanceFromMiddleContactLineAtLeftSideOfContactPattern' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumDistanceFromMiddleContactLineAtLeftSideOfContactPattern
        return temp

    @property
    def maximum_distance_from_middle_contact_line_at_right_side_of_contact_pattern(self) -> 'float':
        """float: 'MaximumDistanceFromMiddleContactLineAtRightSideOfContactPattern' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumDistanceFromMiddleContactLineAtRightSideOfContactPattern
        return temp

    @property
    def projected_auxiliary_angle_for_length_of_contact_line(self) -> 'float':
        """float: 'ProjectedAuxiliaryAngleForLengthOfContactLine' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProjectedAuxiliaryAngleForLengthOfContactLine
        return temp

    @property
    def radius_of_relative_curvature_in_normal_section_at_the_mean_point(self) -> 'float':
        """float: 'RadiusOfRelativeCurvatureInNormalSectionAtTheMeanPoint' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadiusOfRelativeCurvatureInNormalSectionAtTheMeanPoint
        return temp

    @property
    def radius_of_relative_curvature_vertical_to_the_contact_line(self) -> 'float':
        """float: 'RadiusOfRelativeCurvatureVerticalToTheContactLine' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadiusOfRelativeCurvatureVerticalToTheContactLine
        return temp

    @property
    def tan_auxiliary_angle_for_length_of_contact_line_calculation(self) -> 'float':
        """float: 'TanAuxiliaryAngleForLengthOfContactLineCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TanAuxiliaryAngleForLengthOfContactLineCalculation
        return temp

    @property
    def wheel_effective_face_width_factor(self) -> 'float':
        """float: 'WheelEffectiveFaceWidthFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelEffectiveFaceWidthFactor
        return temp

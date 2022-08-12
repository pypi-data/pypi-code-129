"""_55.py

CylindricalMisalignmentCalculator
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy._math.vector_3d import Vector3D
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MISALIGNMENT_CALCULATOR = python_net_import('SMT.MastaAPI.NodalAnalysis', 'CylindricalMisalignmentCalculator')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalMisalignmentCalculator',)


class CylindricalMisalignmentCalculator(_0.APIBase):
    """CylindricalMisalignmentCalculator

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MISALIGNMENT_CALCULATOR

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalMisalignmentCalculator.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_a_equivalent_misalignment_for_rating(self) -> 'float':
        """float: 'GearAEquivalentMisalignmentForRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearAEquivalentMisalignmentForRating
        return temp

    @property
    def gear_a_line_fit_misalignment(self) -> 'float':
        """float: 'GearALineFitMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearALineFitMisalignment
        return temp

    @property
    def gear_a_line_fit_misalignment_angle(self) -> 'float':
        """float: 'GearALineFitMisalignmentAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearALineFitMisalignmentAngle
        return temp

    @property
    def gear_a_radial_angular_component_of_rigid_body_misalignment(self) -> 'float':
        """float: 'GearARadialAngularComponentOfRigidBodyMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearARadialAngularComponentOfRigidBodyMisalignment
        return temp

    @property
    def gear_a_rigid_body_misalignment(self) -> 'float':
        """float: 'GearARigidBodyMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearARigidBodyMisalignment
        return temp

    @property
    def gear_a_rigid_body_misalignment_angle(self) -> 'float':
        """float: 'GearARigidBodyMisalignmentAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearARigidBodyMisalignmentAngle
        return temp

    @property
    def gear_a_single_node_misalignment_angle_due_to_tilt(self) -> 'float':
        """float: 'GearASingleNodeMisalignmentAngleDueToTilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearASingleNodeMisalignmentAngleDueToTilt
        return temp

    @property
    def gear_a_single_node_misalignment_due_to_tilt(self) -> 'float':
        """float: 'GearASingleNodeMisalignmentDueToTilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearASingleNodeMisalignmentDueToTilt
        return temp

    @property
    def gear_a_single_node_misalignment_due_to_twist(self) -> 'float':
        """float: 'GearASingleNodeMisalignmentDueToTwist' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearASingleNodeMisalignmentDueToTwist
        return temp

    @property
    def gear_a_tangential_angular_component_of_rigid_body_misalignment(self) -> 'float':
        """float: 'GearATangentialAngularComponentOfRigidBodyMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearATangentialAngularComponentOfRigidBodyMisalignment
        return temp

    @property
    def gear_a_transverse_separations(self) -> 'List[float]':
        """List[float]: 'GearATransverseSeparations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearATransverseSeparations
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def gear_b_equivalent_misalignment_for_rating(self) -> 'float':
        """float: 'GearBEquivalentMisalignmentForRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBEquivalentMisalignmentForRating
        return temp

    @property
    def gear_b_line_fit_misalignment(self) -> 'float':
        """float: 'GearBLineFitMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBLineFitMisalignment
        return temp

    @property
    def gear_b_line_fit_misalignment_angle(self) -> 'float':
        """float: 'GearBLineFitMisalignmentAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBLineFitMisalignmentAngle
        return temp

    @property
    def gear_b_radial_angular_component_of_rigid_body_misalignment(self) -> 'float':
        """float: 'GearBRadialAngularComponentOfRigidBodyMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBRadialAngularComponentOfRigidBodyMisalignment
        return temp

    @property
    def gear_b_rigid_body_misalignment(self) -> 'float':
        """float: 'GearBRigidBodyMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBRigidBodyMisalignment
        return temp

    @property
    def gear_b_rigid_body_misalignment_angle(self) -> 'float':
        """float: 'GearBRigidBodyMisalignmentAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBRigidBodyMisalignmentAngle
        return temp

    @property
    def gear_b_single_node_misalignment_angle_due_to_tilt(self) -> 'float':
        """float: 'GearBSingleNodeMisalignmentAngleDueToTilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBSingleNodeMisalignmentAngleDueToTilt
        return temp

    @property
    def gear_b_single_node_misalignment_due_to_tilt(self) -> 'float':
        """float: 'GearBSingleNodeMisalignmentDueToTilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBSingleNodeMisalignmentDueToTilt
        return temp

    @property
    def gear_b_single_node_misalignment_due_to_twist(self) -> 'float':
        """float: 'GearBSingleNodeMisalignmentDueToTwist' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBSingleNodeMisalignmentDueToTwist
        return temp

    @property
    def gear_b_tangential_angular_component_of_rigid_body_misalignment(self) -> 'float':
        """float: 'GearBTangentialAngularComponentOfRigidBodyMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBTangentialAngularComponentOfRigidBodyMisalignment
        return temp

    @property
    def gear_b_transverse_separations(self) -> 'List[float]':
        """List[float]: 'GearBTransverseSeparations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBTransverseSeparations
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def total_equivalent_misalignment_for_rating(self) -> 'float':
        """float: 'TotalEquivalentMisalignmentForRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalEquivalentMisalignmentForRating
        return temp

    @property
    def total_line_fit_misalignment(self) -> 'float':
        """float: 'TotalLineFitMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalLineFitMisalignment
        return temp

    @property
    def total_line_fit_misalignment_angle(self) -> 'float':
        """float: 'TotalLineFitMisalignmentAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalLineFitMisalignmentAngle
        return temp

    @property
    def total_radial_angular_component_of_rigid_body_misalignment(self) -> 'float':
        """float: 'TotalRadialAngularComponentOfRigidBodyMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalRadialAngularComponentOfRigidBodyMisalignment
        return temp

    @property
    def total_rigid_body_misalignment(self) -> 'float':
        """float: 'TotalRigidBodyMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalRigidBodyMisalignment
        return temp

    @property
    def total_rigid_body_misalignment_angle(self) -> 'float':
        """float: 'TotalRigidBodyMisalignmentAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalRigidBodyMisalignmentAngle
        return temp

    @property
    def total_single_node_misalignment(self) -> 'float':
        """float: 'TotalSingleNodeMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalSingleNodeMisalignment
        return temp

    @property
    def total_single_node_misalignment_angle_due_to_tilt(self) -> 'float':
        """float: 'TotalSingleNodeMisalignmentAngleDueToTilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalSingleNodeMisalignmentAngleDueToTilt
        return temp

    @property
    def total_single_node_misalignment_due_to_tilt(self) -> 'float':
        """float: 'TotalSingleNodeMisalignmentDueToTilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalSingleNodeMisalignmentDueToTilt
        return temp

    @property
    def total_single_node_misalignment_due_to_twist(self) -> 'float':
        """float: 'TotalSingleNodeMisalignmentDueToTwist' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalSingleNodeMisalignmentDueToTwist
        return temp

    @property
    def total_tangential_angular_component_of_rigid_body_misalignment(self) -> 'float':
        """float: 'TotalTangentialAngularComponentOfRigidBodyMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalTangentialAngularComponentOfRigidBodyMisalignment
        return temp

    @property
    def rigid_body_coordinate_system_x_axis(self) -> 'Vector3D':
        """Vector3D: 'RigidBodyCoordinateSystemXAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RigidBodyCoordinateSystemXAxis
        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def rigid_body_coordinate_system_y_axis(self) -> 'Vector3D':
        """Vector3D: 'RigidBodyCoordinateSystemYAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RigidBodyCoordinateSystemYAxis
        value = conversion.pn_to_mp_vector3d(temp)
        return value

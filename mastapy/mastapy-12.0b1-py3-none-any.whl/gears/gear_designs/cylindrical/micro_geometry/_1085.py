"""_1085.py

CylindricalGearFlankMicroGeometry
"""


from typing import List

from mastapy.math_utility.measured_data import _1525
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.cylindrical.micro_geometry import (
    _1083, _1086, _1087, _1093,
    _1095, _1096, _1100, _1104,
    _1106, _1115, _1117, _1120,
    _1121
)
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.cylindrical import _1016, _1003, _1032
from mastapy.gears.micro_geometry import _560
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_FLANK_MICRO_GEOMETRY = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'CylindricalGearFlankMicroGeometry')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearFlankMicroGeometry',)


class CylindricalGearFlankMicroGeometry(_560.FlankMicroGeometry):
    """CylindricalGearFlankMicroGeometry

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_FLANK_MICRO_GEOMETRY

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearFlankMicroGeometry.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def micro_geometry_matrix(self) -> '_1525.GriddedSurfaceAccessor':
        """GriddedSurfaceAccessor: 'MicroGeometryMatrix' is the original name of this property."""

        temp = self.wrapped.MicroGeometryMatrix
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @micro_geometry_matrix.setter
    def micro_geometry_matrix(self, value: '_1525.GriddedSurfaceAccessor'):
        value = value.wrapped if value else None
        self.wrapped.MicroGeometryMatrix = value

    @property
    def modified_normal_pressure_angle_due_to_helix_angle_modification_assuming_unmodified_normal_module_and_pressure_angle_modification(self) -> 'float':
        """float: 'ModifiedNormalPressureAngleDueToHelixAngleModificationAssumingUnmodifiedNormalModuleAndPressureAngleModification' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModifiedNormalPressureAngleDueToHelixAngleModificationAssumingUnmodifiedNormalModuleAndPressureAngleModification
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
    def use_measured_map_data(self) -> 'bool':
        """bool: 'UseMeasuredMapData' is the original name of this property."""

        temp = self.wrapped.UseMeasuredMapData
        return temp

    @use_measured_map_data.setter
    def use_measured_map_data(self, value: 'bool'):
        self.wrapped.UseMeasuredMapData = bool(value) if value else False

    @property
    def bias(self) -> '_1083.CylindricalGearBiasModification':
        """CylindricalGearBiasModification: 'Bias' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bias
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def lead_relief(self) -> '_1086.CylindricalGearLeadModification':
        """CylindricalGearLeadModification: 'LeadRelief' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadRelief
        if _1086.CylindricalGearLeadModification.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast lead_relief to CylindricalGearLeadModification. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def micro_geometry_map(self) -> '_1093.CylindricalGearMicroGeometryMap':
        """CylindricalGearMicroGeometryMap: 'MicroGeometryMap' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicroGeometryMap
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_control_point(self) -> '_1016.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'ProfileControlPoint' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileControlPoint
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_relief(self) -> '_1095.CylindricalGearProfileModification':
        """CylindricalGearProfileModification: 'ProfileRelief' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileRelief
        if _1095.CylindricalGearProfileModification.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast profile_relief to CylindricalGearProfileModification. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def triangular_end_relief(self) -> '_1100.CylindricalGearTriangularEndModification':
        """CylindricalGearTriangularEndModification: 'TriangularEndRelief' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TriangularEndRelief
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def lead_form_deviation_points(self) -> 'List[_1104.LeadFormReliefWithDeviation]':
        """List[LeadFormReliefWithDeviation]: 'LeadFormDeviationPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadFormDeviationPoints
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def lead_slope_deviation_points(self) -> 'List[_1106.LeadSlopeReliefWithDeviation]':
        """List[LeadSlopeReliefWithDeviation]: 'LeadSlopeDeviationPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadSlopeDeviationPoints
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def profile_form_deviation_points(self) -> 'List[_1115.ProfileFormReliefWithDeviation]':
        """List[ProfileFormReliefWithDeviation]: 'ProfileFormDeviationPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileFormDeviationPoints
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def profile_slope_deviation_at_10_percent_face_width(self) -> 'List[_1117.ProfileSlopeReliefWithDeviation]':
        """List[ProfileSlopeReliefWithDeviation]: 'ProfileSlopeDeviationAt10PercentFaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileSlopeDeviationAt10PercentFaceWidth
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def profile_slope_deviation_at_50_percent_face_width(self) -> 'List[_1117.ProfileSlopeReliefWithDeviation]':
        """List[ProfileSlopeReliefWithDeviation]: 'ProfileSlopeDeviationAt50PercentFaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileSlopeDeviationAt50PercentFaceWidth
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def profile_slope_deviation_at_90_percent_face_width(self) -> 'List[_1117.ProfileSlopeReliefWithDeviation]':
        """List[ProfileSlopeReliefWithDeviation]: 'ProfileSlopeDeviationAt90PercentFaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileSlopeDeviationAt90PercentFaceWidth
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def total_lead_relief_points(self) -> 'List[_1120.TotalLeadReliefWithDeviation]':
        """List[TotalLeadReliefWithDeviation]: 'TotalLeadReliefPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalLeadReliefPoints
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def total_profile_relief_points(self) -> 'List[_1121.TotalProfileReliefWithDeviation]':
        """List[TotalProfileReliefWithDeviation]: 'TotalProfileReliefPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalProfileReliefPoints
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_design(self) -> '_1003.CylindricalGearDesign':
        """CylindricalGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDesign
        if _1003.CylindricalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_design to CylindricalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def total_relief(self, face_width: 'float', roll_distance: 'float') -> 'float':
        """ 'TotalRelief' is the original name of this method.

        Args:
            face_width (float)
            roll_distance (float)

        Returns:
            float
        """

        face_width = float(face_width)
        roll_distance = float(roll_distance)
        method_result = self.wrapped.TotalRelief(face_width if face_width else 0.0, roll_distance if roll_distance else 0.0)
        return method_result

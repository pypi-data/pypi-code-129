"""_1091.py

CylindricalGearMicroGeometryBase
"""


from typing import List

from mastapy.utility.report import _1744
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1084, _1099
from mastapy.gears.gear_designs.cylindrical import _1003, _1032, _1016
from mastapy._internal.cast_exception import CastException
from mastapy.gears.analysis import _1207
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MICRO_GEOMETRY_BASE = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'CylindricalGearMicroGeometryBase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMicroGeometryBase',)


class CylindricalGearMicroGeometryBase(_1207.GearImplementationDetail):
    """CylindricalGearMicroGeometryBase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MICRO_GEOMETRY_BASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearMicroGeometryBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def lead_form_chart(self) -> '_1744.LegacyChartDefinition':
        """LegacyChartDefinition: 'LeadFormChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadFormChart
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def lead_slope_chart(self) -> '_1744.LegacyChartDefinition':
        """LegacyChartDefinition: 'LeadSlopeChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadSlopeChart
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def lead_total_nominal_chart(self) -> '_1744.LegacyChartDefinition':
        """LegacyChartDefinition: 'LeadTotalNominalChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadTotalNominalChart
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def lead_total_chart(self) -> '_1744.LegacyChartDefinition':
        """LegacyChartDefinition: 'LeadTotalChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadTotalChart
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_control_point_is_user_specified(self) -> 'bool':
        """bool: 'ProfileControlPointIsUserSpecified' is the original name of this property."""

        temp = self.wrapped.ProfileControlPointIsUserSpecified
        return temp

    @profile_control_point_is_user_specified.setter
    def profile_control_point_is_user_specified(self, value: 'bool'):
        self.wrapped.ProfileControlPointIsUserSpecified = bool(value) if value else False

    @property
    def profile_form_10_percent_chart(self) -> '_1744.LegacyChartDefinition':
        """LegacyChartDefinition: 'ProfileForm10PercentChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileForm10PercentChart
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_form_50_percent_chart(self) -> '_1744.LegacyChartDefinition':
        """LegacyChartDefinition: 'ProfileForm50PercentChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileForm50PercentChart
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_form_90_percent_chart(self) -> '_1744.LegacyChartDefinition':
        """LegacyChartDefinition: 'ProfileForm90PercentChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileForm90PercentChart
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_form_chart(self) -> '_1744.LegacyChartDefinition':
        """LegacyChartDefinition: 'ProfileFormChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileFormChart
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_total_nominal_chart(self) -> '_1744.LegacyChartDefinition':
        """LegacyChartDefinition: 'ProfileTotalNominalChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileTotalNominalChart
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_total_chart(self) -> '_1744.LegacyChartDefinition':
        """LegacyChartDefinition: 'ProfileTotalChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileTotalChart
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def use_same_micro_geometry_on_both_flanks(self) -> 'bool':
        """bool: 'UseSameMicroGeometryOnBothFlanks' is the original name of this property."""

        temp = self.wrapped.UseSameMicroGeometryOnBothFlanks
        return temp

    @use_same_micro_geometry_on_both_flanks.setter
    def use_same_micro_geometry_on_both_flanks(self, value: 'bool'):
        self.wrapped.UseSameMicroGeometryOnBothFlanks = bool(value) if value else False

    @property
    def common_micro_geometry_of_left_flank(self) -> '_1084.CylindricalGearCommonFlankMicroGeometry':
        """CylindricalGearCommonFlankMicroGeometry: 'CommonMicroGeometryOfLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CommonMicroGeometryOfLeftFlank
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def common_micro_geometry_of_right_flank(self) -> '_1084.CylindricalGearCommonFlankMicroGeometry':
        """CylindricalGearCommonFlankMicroGeometry: 'CommonMicroGeometryOfRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CommonMicroGeometryOfRightFlank
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear(self) -> '_1003.CylindricalGearDesign':
        """CylindricalGearDesign: 'CylindricalGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGear
        if _1003.CylindricalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast cylindrical_gear to CylindricalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

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
    def common_micro_geometries_of_flanks(self) -> 'List[_1084.CylindricalGearCommonFlankMicroGeometry]':
        """List[CylindricalGearCommonFlankMicroGeometry]: 'CommonMicroGeometriesOfFlanks' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CommonMicroGeometriesOfFlanks
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def tooth_micro_geometries(self) -> 'List[_1099.CylindricalGearToothMicroGeometry]':
        """List[CylindricalGearToothMicroGeometry]: 'ToothMicroGeometries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothMicroGeometries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

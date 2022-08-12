"""_1529.py

DataScalingOptions
"""


from typing import List

from mastapy._internal.implicit import enum_with_selected_value
from mastapy.math_utility import _1464, _1449
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy.math_utility.measured_data_scaling import _1530
from mastapy.utility.units_and_measurements.measurements import (
    _1572, _1577, _1581, _1595,
    _1601, _1653, _1652, _1658,
    _1575, _1691, _1684, _1629
)
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_DATA_SCALING_OPTIONS = python_net_import('SMT.MastaAPI.MathUtility.MeasuredDataScaling', 'DataScalingOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('DataScalingOptions',)


class DataScalingOptions(_0.APIBase):
    """DataScalingOptions

    This is a mastapy class.
    """

    TYPE = _DATA_SCALING_OPTIONS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DataScalingOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def dynamic_scaling(self) -> 'enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseScaling':
        """enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseScaling: 'DynamicScaling' is the original name of this property."""

        temp = self.wrapped.DynamicScaling
        value = enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseScaling.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @dynamic_scaling.setter
    def dynamic_scaling(self, value: 'enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseScaling.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_DynamicsResponseScaling.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.DynamicScaling = value

    @property
    def weighting(self) -> '_1449.AcousticWeighting':
        """AcousticWeighting: 'Weighting' is the original name of this property."""

        temp = self.wrapped.Weighting
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1449.AcousticWeighting)(value) if value is not None else None

    @weighting.setter
    def weighting(self, value: '_1449.AcousticWeighting'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.Weighting = value

    @property
    def acceleration_reference_values(self) -> '_1530.DataScalingReferenceValues[_1572.Acceleration]':
        """DataScalingReferenceValues[Acceleration]: 'AccelerationReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AccelerationReferenceValues
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1572.Acceleration](temp) if temp is not None else None

    @property
    def angular_acceleration_reference_values(self) -> '_1530.DataScalingReferenceValues[_1577.AngularAcceleration]':
        """DataScalingReferenceValues[AngularAcceleration]: 'AngularAccelerationReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngularAccelerationReferenceValues
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1577.AngularAcceleration](temp) if temp is not None else None

    @property
    def angular_velocity_reference_values(self) -> '_1530.DataScalingReferenceValues[_1581.AngularVelocity]':
        """DataScalingReferenceValues[AngularVelocity]: 'AngularVelocityReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngularVelocityReferenceValues
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1581.AngularVelocity](temp) if temp is not None else None

    @property
    def energy_reference_values(self) -> '_1530.DataScalingReferenceValues[_1595.Energy]':
        """DataScalingReferenceValues[Energy]: 'EnergyReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EnergyReferenceValues
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1595.Energy](temp) if temp is not None else None

    @property
    def force_reference_values(self) -> '_1530.DataScalingReferenceValues[_1601.Force]':
        """DataScalingReferenceValues[Force]: 'ForceReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceReferenceValues
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1601.Force](temp) if temp is not None else None

    @property
    def power_small_per_unit_area_reference_values(self) -> '_1530.DataScalingReferenceValues[_1653.PowerSmallPerArea]':
        """DataScalingReferenceValues[PowerSmallPerArea]: 'PowerSmallPerUnitAreaReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerSmallPerUnitAreaReferenceValues
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1653.PowerSmallPerArea](temp) if temp is not None else None

    @property
    def power_small_reference_values(self) -> '_1530.DataScalingReferenceValues[_1652.PowerSmall]':
        """DataScalingReferenceValues[PowerSmall]: 'PowerSmallReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerSmallReferenceValues
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1652.PowerSmall](temp) if temp is not None else None

    @property
    def pressure_reference_values(self) -> '_1530.DataScalingReferenceValues[_1658.Pressure]':
        """DataScalingReferenceValues[Pressure]: 'PressureReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PressureReferenceValues
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1658.Pressure](temp) if temp is not None else None

    @property
    def small_angle_reference_values(self) -> '_1530.DataScalingReferenceValues[_1575.AngleSmall]':
        """DataScalingReferenceValues[AngleSmall]: 'SmallAngleReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmallAngleReferenceValues
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1575.AngleSmall](temp) if temp is not None else None

    @property
    def small_velocity_reference_values(self) -> '_1530.DataScalingReferenceValues[_1691.VelocitySmall]':
        """DataScalingReferenceValues[VelocitySmall]: 'SmallVelocityReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmallVelocityReferenceValues
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1691.VelocitySmall](temp) if temp is not None else None

    @property
    def torque_reference_values(self) -> '_1530.DataScalingReferenceValues[_1684.Torque]':
        """DataScalingReferenceValues[Torque]: 'TorqueReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueReferenceValues
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1684.Torque](temp) if temp is not None else None

    @property
    def very_short_length_reference_values(self) -> '_1530.DataScalingReferenceValues[_1629.LengthVeryShort]':
        """DataScalingReferenceValues[LengthVeryShort]: 'VeryShortLengthReferenceValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VeryShortLengthReferenceValues
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1629.LengthVeryShort](temp) if temp is not None else None

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames
        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result

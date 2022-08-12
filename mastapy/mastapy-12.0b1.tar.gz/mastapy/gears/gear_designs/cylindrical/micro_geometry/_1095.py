"""_1095.py

CylindricalGearProfileModification
"""


from mastapy._internal import constructor
from mastapy.utility_gui.charts import (
    _1815, _1805, _1810, _1812
)
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.cylindrical import _1016
from mastapy.gears.micro_geometry import _572
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_PROFILE_MODIFICATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'CylindricalGearProfileModification')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearProfileModification',)


class CylindricalGearProfileModification(_572.ProfileModification):
    """CylindricalGearProfileModification

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_PROFILE_MODIFICATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearProfileModification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def barrelling_peak_point_diameter(self) -> 'float':
        """float: 'BarrellingPeakPointDiameter' is the original name of this property."""

        temp = self.wrapped.BarrellingPeakPointDiameter
        return temp

    @barrelling_peak_point_diameter.setter
    def barrelling_peak_point_diameter(self, value: 'float'):
        self.wrapped.BarrellingPeakPointDiameter = float(value) if value else 0.0

    @property
    def barrelling_peak_point_radius(self) -> 'float':
        """float: 'BarrellingPeakPointRadius' is the original name of this property."""

        temp = self.wrapped.BarrellingPeakPointRadius
        return temp

    @barrelling_peak_point_radius.setter
    def barrelling_peak_point_radius(self, value: 'float'):
        self.wrapped.BarrellingPeakPointRadius = float(value) if value else 0.0

    @property
    def barrelling_peak_point_roll_angle(self) -> 'float':
        """float: 'BarrellingPeakPointRollAngle' is the original name of this property."""

        temp = self.wrapped.BarrellingPeakPointRollAngle
        return temp

    @barrelling_peak_point_roll_angle.setter
    def barrelling_peak_point_roll_angle(self, value: 'float'):
        self.wrapped.BarrellingPeakPointRollAngle = float(value) if value else 0.0

    @property
    def barrelling_peak_point_roll_distance(self) -> 'float':
        """float: 'BarrellingPeakPointRollDistance' is the original name of this property."""

        temp = self.wrapped.BarrellingPeakPointRollDistance
        return temp

    @barrelling_peak_point_roll_distance.setter
    def barrelling_peak_point_roll_distance(self, value: 'float'):
        self.wrapped.BarrellingPeakPointRollDistance = float(value) if value else 0.0

    @property
    def evaluation_lower_limit_diameter(self) -> 'float':
        """float: 'EvaluationLowerLimitDiameter' is the original name of this property."""

        temp = self.wrapped.EvaluationLowerLimitDiameter
        return temp

    @evaluation_lower_limit_diameter.setter
    def evaluation_lower_limit_diameter(self, value: 'float'):
        self.wrapped.EvaluationLowerLimitDiameter = float(value) if value else 0.0

    @property
    def evaluation_lower_limit_diameter_for_zero_root_relief(self) -> 'float':
        """float: 'EvaluationLowerLimitDiameterForZeroRootRelief' is the original name of this property."""

        temp = self.wrapped.EvaluationLowerLimitDiameterForZeroRootRelief
        return temp

    @evaluation_lower_limit_diameter_for_zero_root_relief.setter
    def evaluation_lower_limit_diameter_for_zero_root_relief(self, value: 'float'):
        self.wrapped.EvaluationLowerLimitDiameterForZeroRootRelief = float(value) if value else 0.0

    @property
    def evaluation_lower_limit_radius(self) -> 'float':
        """float: 'EvaluationLowerLimitRadius' is the original name of this property."""

        temp = self.wrapped.EvaluationLowerLimitRadius
        return temp

    @evaluation_lower_limit_radius.setter
    def evaluation_lower_limit_radius(self, value: 'float'):
        self.wrapped.EvaluationLowerLimitRadius = float(value) if value else 0.0

    @property
    def evaluation_lower_limit_radius_for_zero_root_relief(self) -> 'float':
        """float: 'EvaluationLowerLimitRadiusForZeroRootRelief' is the original name of this property."""

        temp = self.wrapped.EvaluationLowerLimitRadiusForZeroRootRelief
        return temp

    @evaluation_lower_limit_radius_for_zero_root_relief.setter
    def evaluation_lower_limit_radius_for_zero_root_relief(self, value: 'float'):
        self.wrapped.EvaluationLowerLimitRadiusForZeroRootRelief = float(value) if value else 0.0

    @property
    def evaluation_lower_limit_roll_angle(self) -> 'float':
        """float: 'EvaluationLowerLimitRollAngle' is the original name of this property."""

        temp = self.wrapped.EvaluationLowerLimitRollAngle
        return temp

    @evaluation_lower_limit_roll_angle.setter
    def evaluation_lower_limit_roll_angle(self, value: 'float'):
        self.wrapped.EvaluationLowerLimitRollAngle = float(value) if value else 0.0

    @property
    def evaluation_lower_limit_roll_angle_for_zero_root_relief(self) -> 'float':
        """float: 'EvaluationLowerLimitRollAngleForZeroRootRelief' is the original name of this property."""

        temp = self.wrapped.EvaluationLowerLimitRollAngleForZeroRootRelief
        return temp

    @evaluation_lower_limit_roll_angle_for_zero_root_relief.setter
    def evaluation_lower_limit_roll_angle_for_zero_root_relief(self, value: 'float'):
        self.wrapped.EvaluationLowerLimitRollAngleForZeroRootRelief = float(value) if value else 0.0

    @property
    def evaluation_lower_limit_roll_distance(self) -> 'float':
        """float: 'EvaluationLowerLimitRollDistance' is the original name of this property."""

        temp = self.wrapped.EvaluationLowerLimitRollDistance
        return temp

    @evaluation_lower_limit_roll_distance.setter
    def evaluation_lower_limit_roll_distance(self, value: 'float'):
        self.wrapped.EvaluationLowerLimitRollDistance = float(value) if value else 0.0

    @property
    def evaluation_lower_limit_roll_distance_for_zero_root_relief(self) -> 'float':
        """float: 'EvaluationLowerLimitRollDistanceForZeroRootRelief' is the original name of this property."""

        temp = self.wrapped.EvaluationLowerLimitRollDistanceForZeroRootRelief
        return temp

    @evaluation_lower_limit_roll_distance_for_zero_root_relief.setter
    def evaluation_lower_limit_roll_distance_for_zero_root_relief(self, value: 'float'):
        self.wrapped.EvaluationLowerLimitRollDistanceForZeroRootRelief = float(value) if value else 0.0

    @property
    def evaluation_of_linear_root_relief_diameter(self) -> 'float':
        """float: 'EvaluationOfLinearRootReliefDiameter' is the original name of this property."""

        temp = self.wrapped.EvaluationOfLinearRootReliefDiameter
        return temp

    @evaluation_of_linear_root_relief_diameter.setter
    def evaluation_of_linear_root_relief_diameter(self, value: 'float'):
        self.wrapped.EvaluationOfLinearRootReliefDiameter = float(value) if value else 0.0

    @property
    def evaluation_of_linear_root_relief_radius(self) -> 'float':
        """float: 'EvaluationOfLinearRootReliefRadius' is the original name of this property."""

        temp = self.wrapped.EvaluationOfLinearRootReliefRadius
        return temp

    @evaluation_of_linear_root_relief_radius.setter
    def evaluation_of_linear_root_relief_radius(self, value: 'float'):
        self.wrapped.EvaluationOfLinearRootReliefRadius = float(value) if value else 0.0

    @property
    def evaluation_of_linear_root_relief_roll_angle(self) -> 'float':
        """float: 'EvaluationOfLinearRootReliefRollAngle' is the original name of this property."""

        temp = self.wrapped.EvaluationOfLinearRootReliefRollAngle
        return temp

    @evaluation_of_linear_root_relief_roll_angle.setter
    def evaluation_of_linear_root_relief_roll_angle(self, value: 'float'):
        self.wrapped.EvaluationOfLinearRootReliefRollAngle = float(value) if value else 0.0

    @property
    def evaluation_of_linear_root_relief_roll_distance(self) -> 'float':
        """float: 'EvaluationOfLinearRootReliefRollDistance' is the original name of this property."""

        temp = self.wrapped.EvaluationOfLinearRootReliefRollDistance
        return temp

    @evaluation_of_linear_root_relief_roll_distance.setter
    def evaluation_of_linear_root_relief_roll_distance(self, value: 'float'):
        self.wrapped.EvaluationOfLinearRootReliefRollDistance = float(value) if value else 0.0

    @property
    def evaluation_of_linear_tip_relief_diameter(self) -> 'float':
        """float: 'EvaluationOfLinearTipReliefDiameter' is the original name of this property."""

        temp = self.wrapped.EvaluationOfLinearTipReliefDiameter
        return temp

    @evaluation_of_linear_tip_relief_diameter.setter
    def evaluation_of_linear_tip_relief_diameter(self, value: 'float'):
        self.wrapped.EvaluationOfLinearTipReliefDiameter = float(value) if value else 0.0

    @property
    def evaluation_of_linear_tip_relief_radius(self) -> 'float':
        """float: 'EvaluationOfLinearTipReliefRadius' is the original name of this property."""

        temp = self.wrapped.EvaluationOfLinearTipReliefRadius
        return temp

    @evaluation_of_linear_tip_relief_radius.setter
    def evaluation_of_linear_tip_relief_radius(self, value: 'float'):
        self.wrapped.EvaluationOfLinearTipReliefRadius = float(value) if value else 0.0

    @property
    def evaluation_of_linear_tip_relief_roll_angle(self) -> 'float':
        """float: 'EvaluationOfLinearTipReliefRollAngle' is the original name of this property."""

        temp = self.wrapped.EvaluationOfLinearTipReliefRollAngle
        return temp

    @evaluation_of_linear_tip_relief_roll_angle.setter
    def evaluation_of_linear_tip_relief_roll_angle(self, value: 'float'):
        self.wrapped.EvaluationOfLinearTipReliefRollAngle = float(value) if value else 0.0

    @property
    def evaluation_of_linear_tip_relief_roll_distance(self) -> 'float':
        """float: 'EvaluationOfLinearTipReliefRollDistance' is the original name of this property."""

        temp = self.wrapped.EvaluationOfLinearTipReliefRollDistance
        return temp

    @evaluation_of_linear_tip_relief_roll_distance.setter
    def evaluation_of_linear_tip_relief_roll_distance(self, value: 'float'):
        self.wrapped.EvaluationOfLinearTipReliefRollDistance = float(value) if value else 0.0

    @property
    def evaluation_of_parabolic_root_relief_diameter(self) -> 'float':
        """float: 'EvaluationOfParabolicRootReliefDiameter' is the original name of this property."""

        temp = self.wrapped.EvaluationOfParabolicRootReliefDiameter
        return temp

    @evaluation_of_parabolic_root_relief_diameter.setter
    def evaluation_of_parabolic_root_relief_diameter(self, value: 'float'):
        self.wrapped.EvaluationOfParabolicRootReliefDiameter = float(value) if value else 0.0

    @property
    def evaluation_of_parabolic_root_relief_radius(self) -> 'float':
        """float: 'EvaluationOfParabolicRootReliefRadius' is the original name of this property."""

        temp = self.wrapped.EvaluationOfParabolicRootReliefRadius
        return temp

    @evaluation_of_parabolic_root_relief_radius.setter
    def evaluation_of_parabolic_root_relief_radius(self, value: 'float'):
        self.wrapped.EvaluationOfParabolicRootReliefRadius = float(value) if value else 0.0

    @property
    def evaluation_of_parabolic_root_relief_roll_angle(self) -> 'float':
        """float: 'EvaluationOfParabolicRootReliefRollAngle' is the original name of this property."""

        temp = self.wrapped.EvaluationOfParabolicRootReliefRollAngle
        return temp

    @evaluation_of_parabolic_root_relief_roll_angle.setter
    def evaluation_of_parabolic_root_relief_roll_angle(self, value: 'float'):
        self.wrapped.EvaluationOfParabolicRootReliefRollAngle = float(value) if value else 0.0

    @property
    def evaluation_of_parabolic_root_relief_roll_distance(self) -> 'float':
        """float: 'EvaluationOfParabolicRootReliefRollDistance' is the original name of this property."""

        temp = self.wrapped.EvaluationOfParabolicRootReliefRollDistance
        return temp

    @evaluation_of_parabolic_root_relief_roll_distance.setter
    def evaluation_of_parabolic_root_relief_roll_distance(self, value: 'float'):
        self.wrapped.EvaluationOfParabolicRootReliefRollDistance = float(value) if value else 0.0

    @property
    def evaluation_of_parabolic_tip_relief_diameter(self) -> 'float':
        """float: 'EvaluationOfParabolicTipReliefDiameter' is the original name of this property."""

        temp = self.wrapped.EvaluationOfParabolicTipReliefDiameter
        return temp

    @evaluation_of_parabolic_tip_relief_diameter.setter
    def evaluation_of_parabolic_tip_relief_diameter(self, value: 'float'):
        self.wrapped.EvaluationOfParabolicTipReliefDiameter = float(value) if value else 0.0

    @property
    def evaluation_of_parabolic_tip_relief_radius(self) -> 'float':
        """float: 'EvaluationOfParabolicTipReliefRadius' is the original name of this property."""

        temp = self.wrapped.EvaluationOfParabolicTipReliefRadius
        return temp

    @evaluation_of_parabolic_tip_relief_radius.setter
    def evaluation_of_parabolic_tip_relief_radius(self, value: 'float'):
        self.wrapped.EvaluationOfParabolicTipReliefRadius = float(value) if value else 0.0

    @property
    def evaluation_of_parabolic_tip_relief_roll_angle(self) -> 'float':
        """float: 'EvaluationOfParabolicTipReliefRollAngle' is the original name of this property."""

        temp = self.wrapped.EvaluationOfParabolicTipReliefRollAngle
        return temp

    @evaluation_of_parabolic_tip_relief_roll_angle.setter
    def evaluation_of_parabolic_tip_relief_roll_angle(self, value: 'float'):
        self.wrapped.EvaluationOfParabolicTipReliefRollAngle = float(value) if value else 0.0

    @property
    def evaluation_of_parabolic_tip_relief_roll_distance(self) -> 'float':
        """float: 'EvaluationOfParabolicTipReliefRollDistance' is the original name of this property."""

        temp = self.wrapped.EvaluationOfParabolicTipReliefRollDistance
        return temp

    @evaluation_of_parabolic_tip_relief_roll_distance.setter
    def evaluation_of_parabolic_tip_relief_roll_distance(self, value: 'float'):
        self.wrapped.EvaluationOfParabolicTipReliefRollDistance = float(value) if value else 0.0

    @property
    def evaluation_upper_limit_diameter(self) -> 'float':
        """float: 'EvaluationUpperLimitDiameter' is the original name of this property."""

        temp = self.wrapped.EvaluationUpperLimitDiameter
        return temp

    @evaluation_upper_limit_diameter.setter
    def evaluation_upper_limit_diameter(self, value: 'float'):
        self.wrapped.EvaluationUpperLimitDiameter = float(value) if value else 0.0

    @property
    def evaluation_upper_limit_diameter_for_zero_tip_relief(self) -> 'float':
        """float: 'EvaluationUpperLimitDiameterForZeroTipRelief' is the original name of this property."""

        temp = self.wrapped.EvaluationUpperLimitDiameterForZeroTipRelief
        return temp

    @evaluation_upper_limit_diameter_for_zero_tip_relief.setter
    def evaluation_upper_limit_diameter_for_zero_tip_relief(self, value: 'float'):
        self.wrapped.EvaluationUpperLimitDiameterForZeroTipRelief = float(value) if value else 0.0

    @property
    def evaluation_upper_limit_radius(self) -> 'float':
        """float: 'EvaluationUpperLimitRadius' is the original name of this property."""

        temp = self.wrapped.EvaluationUpperLimitRadius
        return temp

    @evaluation_upper_limit_radius.setter
    def evaluation_upper_limit_radius(self, value: 'float'):
        self.wrapped.EvaluationUpperLimitRadius = float(value) if value else 0.0

    @property
    def evaluation_upper_limit_radius_for_zero_tip_relief(self) -> 'float':
        """float: 'EvaluationUpperLimitRadiusForZeroTipRelief' is the original name of this property."""

        temp = self.wrapped.EvaluationUpperLimitRadiusForZeroTipRelief
        return temp

    @evaluation_upper_limit_radius_for_zero_tip_relief.setter
    def evaluation_upper_limit_radius_for_zero_tip_relief(self, value: 'float'):
        self.wrapped.EvaluationUpperLimitRadiusForZeroTipRelief = float(value) if value else 0.0

    @property
    def evaluation_upper_limit_roll_angle(self) -> 'float':
        """float: 'EvaluationUpperLimitRollAngle' is the original name of this property."""

        temp = self.wrapped.EvaluationUpperLimitRollAngle
        return temp

    @evaluation_upper_limit_roll_angle.setter
    def evaluation_upper_limit_roll_angle(self, value: 'float'):
        self.wrapped.EvaluationUpperLimitRollAngle = float(value) if value else 0.0

    @property
    def evaluation_upper_limit_roll_angle_for_zero_tip_relief(self) -> 'float':
        """float: 'EvaluationUpperLimitRollAngleForZeroTipRelief' is the original name of this property."""

        temp = self.wrapped.EvaluationUpperLimitRollAngleForZeroTipRelief
        return temp

    @evaluation_upper_limit_roll_angle_for_zero_tip_relief.setter
    def evaluation_upper_limit_roll_angle_for_zero_tip_relief(self, value: 'float'):
        self.wrapped.EvaluationUpperLimitRollAngleForZeroTipRelief = float(value) if value else 0.0

    @property
    def evaluation_upper_limit_roll_distance(self) -> 'float':
        """float: 'EvaluationUpperLimitRollDistance' is the original name of this property."""

        temp = self.wrapped.EvaluationUpperLimitRollDistance
        return temp

    @evaluation_upper_limit_roll_distance.setter
    def evaluation_upper_limit_roll_distance(self, value: 'float'):
        self.wrapped.EvaluationUpperLimitRollDistance = float(value) if value else 0.0

    @property
    def evaluation_upper_limit_roll_distance_for_zero_tip_relief(self) -> 'float':
        """float: 'EvaluationUpperLimitRollDistanceForZeroTipRelief' is the original name of this property."""

        temp = self.wrapped.EvaluationUpperLimitRollDistanceForZeroTipRelief
        return temp

    @evaluation_upper_limit_roll_distance_for_zero_tip_relief.setter
    def evaluation_upper_limit_roll_distance_for_zero_tip_relief(self, value: 'float'):
        self.wrapped.EvaluationUpperLimitRollDistanceForZeroTipRelief = float(value) if value else 0.0

    @property
    def linear_relief_isoagmadin(self) -> 'float':
        """float: 'LinearReliefISOAGMADIN' is the original name of this property."""

        temp = self.wrapped.LinearReliefISOAGMADIN
        return temp

    @linear_relief_isoagmadin.setter
    def linear_relief_isoagmadin(self, value: 'float'):
        self.wrapped.LinearReliefISOAGMADIN = float(value) if value else 0.0

    @property
    def linear_relief_ldp(self) -> 'float':
        """float: 'LinearReliefLDP' is the original name of this property."""

        temp = self.wrapped.LinearReliefLDP
        return temp

    @linear_relief_ldp.setter
    def linear_relief_ldp(self, value: 'float'):
        self.wrapped.LinearReliefLDP = float(value) if value else 0.0

    @property
    def linear_relief_vdi(self) -> 'float':
        """float: 'LinearReliefVDI' is the original name of this property."""

        temp = self.wrapped.LinearReliefVDI
        return temp

    @linear_relief_vdi.setter
    def linear_relief_vdi(self, value: 'float'):
        self.wrapped.LinearReliefVDI = float(value) if value else 0.0

    @property
    def pressure_angle_modification(self) -> 'float':
        """float: 'PressureAngleModification' is the original name of this property."""

        temp = self.wrapped.PressureAngleModification
        return temp

    @pressure_angle_modification.setter
    def pressure_angle_modification(self, value: 'float'):
        self.wrapped.PressureAngleModification = float(value) if value else 0.0

    @property
    def profile_modification_chart(self) -> '_1815.TwoDChartDefinition':
        """TwoDChartDefinition: 'ProfileModificationChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileModificationChart
        if _1815.TwoDChartDefinition.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast profile_modification_chart to TwoDChartDefinition. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def start_of_linear_root_relief_diameter(self) -> 'float':
        """float: 'StartOfLinearRootReliefDiameter' is the original name of this property."""

        temp = self.wrapped.StartOfLinearRootReliefDiameter
        return temp

    @start_of_linear_root_relief_diameter.setter
    def start_of_linear_root_relief_diameter(self, value: 'float'):
        self.wrapped.StartOfLinearRootReliefDiameter = float(value) if value else 0.0

    @property
    def start_of_linear_root_relief_radius(self) -> 'float':
        """float: 'StartOfLinearRootReliefRadius' is the original name of this property."""

        temp = self.wrapped.StartOfLinearRootReliefRadius
        return temp

    @start_of_linear_root_relief_radius.setter
    def start_of_linear_root_relief_radius(self, value: 'float'):
        self.wrapped.StartOfLinearRootReliefRadius = float(value) if value else 0.0

    @property
    def start_of_linear_root_relief_roll_angle(self) -> 'float':
        """float: 'StartOfLinearRootReliefRollAngle' is the original name of this property."""

        temp = self.wrapped.StartOfLinearRootReliefRollAngle
        return temp

    @start_of_linear_root_relief_roll_angle.setter
    def start_of_linear_root_relief_roll_angle(self, value: 'float'):
        self.wrapped.StartOfLinearRootReliefRollAngle = float(value) if value else 0.0

    @property
    def start_of_linear_root_relief_roll_distance(self) -> 'float':
        """float: 'StartOfLinearRootReliefRollDistance' is the original name of this property."""

        temp = self.wrapped.StartOfLinearRootReliefRollDistance
        return temp

    @start_of_linear_root_relief_roll_distance.setter
    def start_of_linear_root_relief_roll_distance(self, value: 'float'):
        self.wrapped.StartOfLinearRootReliefRollDistance = float(value) if value else 0.0

    @property
    def start_of_linear_tip_relief_diameter(self) -> 'float':
        """float: 'StartOfLinearTipReliefDiameter' is the original name of this property."""

        temp = self.wrapped.StartOfLinearTipReliefDiameter
        return temp

    @start_of_linear_tip_relief_diameter.setter
    def start_of_linear_tip_relief_diameter(self, value: 'float'):
        self.wrapped.StartOfLinearTipReliefDiameter = float(value) if value else 0.0

    @property
    def start_of_linear_tip_relief_radius(self) -> 'float':
        """float: 'StartOfLinearTipReliefRadius' is the original name of this property."""

        temp = self.wrapped.StartOfLinearTipReliefRadius
        return temp

    @start_of_linear_tip_relief_radius.setter
    def start_of_linear_tip_relief_radius(self, value: 'float'):
        self.wrapped.StartOfLinearTipReliefRadius = float(value) if value else 0.0

    @property
    def start_of_linear_tip_relief_roll_angle(self) -> 'float':
        """float: 'StartOfLinearTipReliefRollAngle' is the original name of this property."""

        temp = self.wrapped.StartOfLinearTipReliefRollAngle
        return temp

    @start_of_linear_tip_relief_roll_angle.setter
    def start_of_linear_tip_relief_roll_angle(self, value: 'float'):
        self.wrapped.StartOfLinearTipReliefRollAngle = float(value) if value else 0.0

    @property
    def start_of_linear_tip_relief_roll_distance(self) -> 'float':
        """float: 'StartOfLinearTipReliefRollDistance' is the original name of this property."""

        temp = self.wrapped.StartOfLinearTipReliefRollDistance
        return temp

    @start_of_linear_tip_relief_roll_distance.setter
    def start_of_linear_tip_relief_roll_distance(self, value: 'float'):
        self.wrapped.StartOfLinearTipReliefRollDistance = float(value) if value else 0.0

    @property
    def start_of_parabolic_root_relief_diameter(self) -> 'float':
        """float: 'StartOfParabolicRootReliefDiameter' is the original name of this property."""

        temp = self.wrapped.StartOfParabolicRootReliefDiameter
        return temp

    @start_of_parabolic_root_relief_diameter.setter
    def start_of_parabolic_root_relief_diameter(self, value: 'float'):
        self.wrapped.StartOfParabolicRootReliefDiameter = float(value) if value else 0.0

    @property
    def start_of_parabolic_root_relief_radius(self) -> 'float':
        """float: 'StartOfParabolicRootReliefRadius' is the original name of this property."""

        temp = self.wrapped.StartOfParabolicRootReliefRadius
        return temp

    @start_of_parabolic_root_relief_radius.setter
    def start_of_parabolic_root_relief_radius(self, value: 'float'):
        self.wrapped.StartOfParabolicRootReliefRadius = float(value) if value else 0.0

    @property
    def start_of_parabolic_root_relief_roll_angle(self) -> 'float':
        """float: 'StartOfParabolicRootReliefRollAngle' is the original name of this property."""

        temp = self.wrapped.StartOfParabolicRootReliefRollAngle
        return temp

    @start_of_parabolic_root_relief_roll_angle.setter
    def start_of_parabolic_root_relief_roll_angle(self, value: 'float'):
        self.wrapped.StartOfParabolicRootReliefRollAngle = float(value) if value else 0.0

    @property
    def start_of_parabolic_root_relief_roll_distance(self) -> 'float':
        """float: 'StartOfParabolicRootReliefRollDistance' is the original name of this property."""

        temp = self.wrapped.StartOfParabolicRootReliefRollDistance
        return temp

    @start_of_parabolic_root_relief_roll_distance.setter
    def start_of_parabolic_root_relief_roll_distance(self, value: 'float'):
        self.wrapped.StartOfParabolicRootReliefRollDistance = float(value) if value else 0.0

    @property
    def start_of_parabolic_tip_relief_diameter(self) -> 'float':
        """float: 'StartOfParabolicTipReliefDiameter' is the original name of this property."""

        temp = self.wrapped.StartOfParabolicTipReliefDiameter
        return temp

    @start_of_parabolic_tip_relief_diameter.setter
    def start_of_parabolic_tip_relief_diameter(self, value: 'float'):
        self.wrapped.StartOfParabolicTipReliefDiameter = float(value) if value else 0.0

    @property
    def start_of_parabolic_tip_relief_radius(self) -> 'float':
        """float: 'StartOfParabolicTipReliefRadius' is the original name of this property."""

        temp = self.wrapped.StartOfParabolicTipReliefRadius
        return temp

    @start_of_parabolic_tip_relief_radius.setter
    def start_of_parabolic_tip_relief_radius(self, value: 'float'):
        self.wrapped.StartOfParabolicTipReliefRadius = float(value) if value else 0.0

    @property
    def start_of_parabolic_tip_relief_roll_angle(self) -> 'float':
        """float: 'StartOfParabolicTipReliefRollAngle' is the original name of this property."""

        temp = self.wrapped.StartOfParabolicTipReliefRollAngle
        return temp

    @start_of_parabolic_tip_relief_roll_angle.setter
    def start_of_parabolic_tip_relief_roll_angle(self, value: 'float'):
        self.wrapped.StartOfParabolicTipReliefRollAngle = float(value) if value else 0.0

    @property
    def start_of_parabolic_tip_relief_roll_distance(self) -> 'float':
        """float: 'StartOfParabolicTipReliefRollDistance' is the original name of this property."""

        temp = self.wrapped.StartOfParabolicTipReliefRollDistance
        return temp

    @start_of_parabolic_tip_relief_roll_distance.setter
    def start_of_parabolic_tip_relief_roll_distance(self, value: 'float'):
        self.wrapped.StartOfParabolicTipReliefRollDistance = float(value) if value else 0.0

    @property
    def use_measured_data(self) -> 'bool':
        """bool: 'UseMeasuredData' is the original name of this property."""

        temp = self.wrapped.UseMeasuredData
        return temp

    @use_measured_data.setter
    def use_measured_data(self, value: 'bool'):
        self.wrapped.UseMeasuredData = bool(value) if value else False

    @property
    def barrelling_peak_point(self) -> '_1016.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'BarrellingPeakPoint' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BarrellingPeakPoint
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def evaluation_lower_limit(self) -> '_1016.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'EvaluationLowerLimit' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EvaluationLowerLimit
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def evaluation_lower_limit_for_zero_root_relief(self) -> '_1016.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'EvaluationLowerLimitForZeroRootRelief' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EvaluationLowerLimitForZeroRootRelief
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def evaluation_upper_limit(self) -> '_1016.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'EvaluationUpperLimit' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EvaluationUpperLimit
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def evaluation_upper_limit_for_zero_tip_relief(self) -> '_1016.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'EvaluationUpperLimitForZeroTipRelief' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EvaluationUpperLimitForZeroTipRelief
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def linear_root_relief_evaluation(self) -> '_1016.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'LinearRootReliefEvaluation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LinearRootReliefEvaluation
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def linear_root_relief_start(self) -> '_1016.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'LinearRootReliefStart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LinearRootReliefStart
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def linear_tip_relief_evaluation(self) -> '_1016.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'LinearTipReliefEvaluation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LinearTipReliefEvaluation
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def linear_tip_relief_start(self) -> '_1016.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'LinearTipReliefStart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LinearTipReliefStart
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def parabolic_root_relief_evaluation(self) -> '_1016.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'ParabolicRootReliefEvaluation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParabolicRootReliefEvaluation
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def parabolic_root_relief_start(self) -> '_1016.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'ParabolicRootReliefStart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParabolicRootReliefStart
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def parabolic_tip_relief_evaluation(self) -> '_1016.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'ParabolicTipReliefEvaluation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParabolicTipReliefEvaluation
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def parabolic_tip_relief_start(self) -> '_1016.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'ParabolicTipReliefStart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParabolicTipReliefStart
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def relief_of(self, roll_distance: 'float') -> 'float':
        """ 'ReliefOf' is the original name of this method.

        Args:
            roll_distance (float)

        Returns:
            float
        """

        roll_distance = float(roll_distance)
        method_result = self.wrapped.ReliefOf(roll_distance if roll_distance else 0.0)
        return method_result

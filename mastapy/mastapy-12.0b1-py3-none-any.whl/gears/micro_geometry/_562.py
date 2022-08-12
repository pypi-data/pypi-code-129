"""_562.py

LeadModification
"""


from mastapy._internal import constructor
from mastapy.math_utility import _1493
from mastapy.gears.micro_geometry import _569
from mastapy._internal.python_net import python_net_import

_LEAD_MODIFICATION = python_net_import('SMT.MastaAPI.Gears.MicroGeometry', 'LeadModification')


__docformat__ = 'restructuredtext en'
__all__ = ('LeadModification',)


class LeadModification(_569.Modification):
    """LeadModification

    This is a mastapy class.
    """

    TYPE = _LEAD_MODIFICATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'LeadModification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def crowning_relief(self) -> 'float':
        """float: 'CrowningRelief' is the original name of this property."""

        temp = self.wrapped.CrowningRelief
        return temp

    @crowning_relief.setter
    def crowning_relief(self, value: 'float'):
        self.wrapped.CrowningRelief = float(value) if value else 0.0

    @property
    def evaluation_left_limit_factor(self) -> 'float':
        """float: 'EvaluationLeftLimitFactor' is the original name of this property."""

        temp = self.wrapped.EvaluationLeftLimitFactor
        return temp

    @evaluation_left_limit_factor.setter
    def evaluation_left_limit_factor(self, value: 'float'):
        self.wrapped.EvaluationLeftLimitFactor = float(value) if value else 0.0

    @property
    def evaluation_right_limit_factor(self) -> 'float':
        """float: 'EvaluationRightLimitFactor' is the original name of this property."""

        temp = self.wrapped.EvaluationRightLimitFactor
        return temp

    @evaluation_right_limit_factor.setter
    def evaluation_right_limit_factor(self, value: 'float'):
        self.wrapped.EvaluationRightLimitFactor = float(value) if value else 0.0

    @property
    def linear_left_relief(self) -> 'float':
        """float: 'LinearLeftRelief' is the original name of this property."""

        temp = self.wrapped.LinearLeftRelief
        return temp

    @linear_left_relief.setter
    def linear_left_relief(self, value: 'float'):
        self.wrapped.LinearLeftRelief = float(value) if value else 0.0

    @property
    def linear_relief(self) -> 'float':
        """float: 'LinearRelief' is the original name of this property."""

        temp = self.wrapped.LinearRelief
        return temp

    @linear_relief.setter
    def linear_relief(self, value: 'float'):
        self.wrapped.LinearRelief = float(value) if value else 0.0

    @property
    def linear_right_relief(self) -> 'float':
        """float: 'LinearRightRelief' is the original name of this property."""

        temp = self.wrapped.LinearRightRelief
        return temp

    @linear_right_relief.setter
    def linear_right_relief(self, value: 'float'):
        self.wrapped.LinearRightRelief = float(value) if value else 0.0

    @property
    def measured_data(self) -> '_1493.Vector2DListAccessor':
        """Vector2DListAccessor: 'MeasuredData' is the original name of this property."""

        temp = self.wrapped.MeasuredData
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measured_data.setter
    def measured_data(self, value: '_1493.Vector2DListAccessor'):
        value = value.wrapped if value else None
        self.wrapped.MeasuredData = value

    @property
    def parabolic_left_relief(self) -> 'float':
        """float: 'ParabolicLeftRelief' is the original name of this property."""

        temp = self.wrapped.ParabolicLeftRelief
        return temp

    @parabolic_left_relief.setter
    def parabolic_left_relief(self, value: 'float'):
        self.wrapped.ParabolicLeftRelief = float(value) if value else 0.0

    @property
    def parabolic_right_relief(self) -> 'float':
        """float: 'ParabolicRightRelief' is the original name of this property."""

        temp = self.wrapped.ParabolicRightRelief
        return temp

    @parabolic_right_relief.setter
    def parabolic_right_relief(self, value: 'float'):
        self.wrapped.ParabolicRightRelief = float(value) if value else 0.0

    @property
    def start_of_linear_left_relief_factor(self) -> 'float':
        """float: 'StartOfLinearLeftReliefFactor' is the original name of this property."""

        temp = self.wrapped.StartOfLinearLeftReliefFactor
        return temp

    @start_of_linear_left_relief_factor.setter
    def start_of_linear_left_relief_factor(self, value: 'float'):
        self.wrapped.StartOfLinearLeftReliefFactor = float(value) if value else 0.0

    @property
    def start_of_linear_right_relief_factor(self) -> 'float':
        """float: 'StartOfLinearRightReliefFactor' is the original name of this property."""

        temp = self.wrapped.StartOfLinearRightReliefFactor
        return temp

    @start_of_linear_right_relief_factor.setter
    def start_of_linear_right_relief_factor(self, value: 'float'):
        self.wrapped.StartOfLinearRightReliefFactor = float(value) if value else 0.0

    @property
    def start_of_parabolic_left_relief_factor(self) -> 'float':
        """float: 'StartOfParabolicLeftReliefFactor' is the original name of this property."""

        temp = self.wrapped.StartOfParabolicLeftReliefFactor
        return temp

    @start_of_parabolic_left_relief_factor.setter
    def start_of_parabolic_left_relief_factor(self, value: 'float'):
        self.wrapped.StartOfParabolicLeftReliefFactor = float(value) if value else 0.0

    @property
    def start_of_parabolic_right_relief_factor(self) -> 'float':
        """float: 'StartOfParabolicRightReliefFactor' is the original name of this property."""

        temp = self.wrapped.StartOfParabolicRightReliefFactor
        return temp

    @start_of_parabolic_right_relief_factor.setter
    def start_of_parabolic_right_relief_factor(self, value: 'float'):
        self.wrapped.StartOfParabolicRightReliefFactor = float(value) if value else 0.0

    @property
    def use_measured_data(self) -> 'bool':
        """bool: 'UseMeasuredData' is the original name of this property."""

        temp = self.wrapped.UseMeasuredData
        return temp

    @use_measured_data.setter
    def use_measured_data(self, value: 'bool'):
        self.wrapped.UseMeasuredData = bool(value) if value else False

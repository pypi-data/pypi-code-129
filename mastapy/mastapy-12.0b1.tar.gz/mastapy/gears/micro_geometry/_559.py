"""_559.py

BiasModification
"""


from mastapy._internal import constructor
from mastapy.gears.micro_geometry import _569
from mastapy._internal.python_net import python_net_import

_BIAS_MODIFICATION = python_net_import('SMT.MastaAPI.Gears.MicroGeometry', 'BiasModification')


__docformat__ = 'restructuredtext en'
__all__ = ('BiasModification',)


class BiasModification(_569.Modification):
    """BiasModification

    This is a mastapy class.
    """

    TYPE = _BIAS_MODIFICATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BiasModification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def lead_evaluation_left_limit_factor(self) -> 'float':
        """float: 'LeadEvaluationLeftLimitFactor' is the original name of this property."""

        temp = self.wrapped.LeadEvaluationLeftLimitFactor
        return temp

    @lead_evaluation_left_limit_factor.setter
    def lead_evaluation_left_limit_factor(self, value: 'float'):
        self.wrapped.LeadEvaluationLeftLimitFactor = float(value) if value else 0.0

    @property
    def lead_evaluation_right_limit_factor(self) -> 'float':
        """float: 'LeadEvaluationRightLimitFactor' is the original name of this property."""

        temp = self.wrapped.LeadEvaluationRightLimitFactor
        return temp

    @lead_evaluation_right_limit_factor.setter
    def lead_evaluation_right_limit_factor(self, value: 'float'):
        self.wrapped.LeadEvaluationRightLimitFactor = float(value) if value else 0.0

    @property
    def profile_evaluation_lower_limit_factor(self) -> 'float':
        """float: 'ProfileEvaluationLowerLimitFactor' is the original name of this property."""

        temp = self.wrapped.ProfileEvaluationLowerLimitFactor
        return temp

    @profile_evaluation_lower_limit_factor.setter
    def profile_evaluation_lower_limit_factor(self, value: 'float'):
        self.wrapped.ProfileEvaluationLowerLimitFactor = float(value) if value else 0.0

    @property
    def profile_evaluation_upper_limit_factor(self) -> 'float':
        """float: 'ProfileEvaluationUpperLimitFactor' is the original name of this property."""

        temp = self.wrapped.ProfileEvaluationUpperLimitFactor
        return temp

    @profile_evaluation_upper_limit_factor.setter
    def profile_evaluation_upper_limit_factor(self, value: 'float'):
        self.wrapped.ProfileEvaluationUpperLimitFactor = float(value) if value else 0.0

    @property
    def profile_factor_for_0_bias_relief(self) -> 'float':
        """float: 'ProfileFactorFor0BiasRelief' is the original name of this property."""

        temp = self.wrapped.ProfileFactorFor0BiasRelief
        return temp

    @profile_factor_for_0_bias_relief.setter
    def profile_factor_for_0_bias_relief(self, value: 'float'):
        self.wrapped.ProfileFactorFor0BiasRelief = float(value) if value else 0.0

    @property
    def relief_at_left_limit(self) -> 'float':
        """float: 'ReliefAtLeftLimit' is the original name of this property."""

        temp = self.wrapped.ReliefAtLeftLimit
        return temp

    @relief_at_left_limit.setter
    def relief_at_left_limit(self, value: 'float'):
        self.wrapped.ReliefAtLeftLimit = float(value) if value else 0.0

    @property
    def relief_at_right_limit(self) -> 'float':
        """float: 'ReliefAtRightLimit' is the original name of this property."""

        temp = self.wrapped.ReliefAtRightLimit
        return temp

    @relief_at_right_limit.setter
    def relief_at_right_limit(self, value: 'float'):
        self.wrapped.ReliefAtRightLimit = float(value) if value else 0.0

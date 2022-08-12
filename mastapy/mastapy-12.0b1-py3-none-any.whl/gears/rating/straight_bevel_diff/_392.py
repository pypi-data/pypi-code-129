"""_392.py

StraightBevelDiffMeshedGearRating
"""


from mastapy._internal import constructor
from mastapy.gears.rating.conical import _535
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_MESHED_GEAR_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.StraightBevelDiff', 'StraightBevelDiffMeshedGearRating')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffMeshedGearRating',)


class StraightBevelDiffMeshedGearRating(_535.ConicalMeshedGearRating):
    """StraightBevelDiffMeshedGearRating

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_MESHED_GEAR_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffMeshedGearRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_bending_stress_for_peak_torque(self) -> 'float':
        """float: 'AllowableBendingStressForPeakTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableBendingStressForPeakTorque
        return temp

    @property
    def allowable_bending_stress_for_performance_torque(self) -> 'float':
        """float: 'AllowableBendingStressForPerformanceTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableBendingStressForPerformanceTorque
        return temp

    @property
    def calculated_bending_stress_for_peak_torque(self) -> 'float':
        """float: 'CalculatedBendingStressForPeakTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedBendingStressForPeakTorque
        return temp

    @property
    def calculated_bending_stress_for_performance_torque(self) -> 'float':
        """float: 'CalculatedBendingStressForPerformanceTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedBendingStressForPerformanceTorque
        return temp

    @property
    def peak_torque(self) -> 'float':
        """float: 'PeakTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakTorque
        return temp

    @property
    def performance_torque(self) -> 'float':
        """float: 'PerformanceTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PerformanceTorque
        return temp

    @property
    def rating_result(self) -> 'str':
        """str: 'RatingResult' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatingResult
        return temp

    @property
    def safety_factor_for_peak_torque(self) -> 'float':
        """float: 'SafetyFactorForPeakTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorForPeakTorque
        return temp

    @property
    def safety_factor_for_performance_torque(self) -> 'float':
        """float: 'SafetyFactorForPerformanceTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorForPerformanceTorque
        return temp

    @property
    def strength_factor(self) -> 'float':
        """float: 'StrengthFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StrengthFactor
        return temp

    @property
    def total_torque_transmitted(self) -> 'float':
        """float: 'TotalTorqueTransmitted' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalTorqueTransmitted
        return temp

    @property
    def total_transmitted_peak_torque(self) -> 'float':
        """float: 'TotalTransmittedPeakTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalTransmittedPeakTorque
        return temp

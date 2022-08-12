"""_1943.py

LoadedBallBearingDutyCycle
"""


from mastapy._internal import constructor
from mastapy.utility.property import _1795
from mastapy.bearings.bearing_results.rolling import _1946
from mastapy.bearings.bearing_results import _1907
from mastapy._internal.python_net import python_net_import

_LOADED_BALL_BEARING_DUTY_CYCLE = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedBallBearingDutyCycle')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedBallBearingDutyCycle',)


class LoadedBallBearingDutyCycle(_1907.LoadedRollingBearingDutyCycle):
    """LoadedBallBearingDutyCycle

    This is a mastapy class.
    """

    TYPE = _LOADED_BALL_BEARING_DUTY_CYCLE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'LoadedBallBearingDutyCycle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def track_truncation_safety_factor(self) -> 'float':
        """float: 'TrackTruncationSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TrackTruncationSafetyFactor
        return temp

    @property
    def track_truncation_inner_summary(self) -> '_1795.DutyCyclePropertySummaryPercentage[_1946.LoadedBallBearingResults]':
        """DutyCyclePropertySummaryPercentage[LoadedBallBearingResults]: 'TrackTruncationInnerSummary' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TrackTruncationInnerSummary
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1946.LoadedBallBearingResults](temp) if temp is not None else None

    @property
    def track_truncation_outer_summary(self) -> '_1795.DutyCyclePropertySummaryPercentage[_1946.LoadedBallBearingResults]':
        """DutyCyclePropertySummaryPercentage[LoadedBallBearingResults]: 'TrackTruncationOuterSummary' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TrackTruncationOuterSummary
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1946.LoadedBallBearingResults](temp) if temp is not None else None

"""_1796.py

DutyCyclePropertySummarySmallAngle
"""


from typing import Generic, TypeVar

from mastapy._internal import constructor
from mastapy.utility.property import _1793
from mastapy.utility.units_and_measurements.measurements import _1575
from mastapy._internal.python_net import python_net_import

_DUTY_CYCLE_PROPERTY_SUMMARY_SMALL_ANGLE = python_net_import('SMT.MastaAPI.Utility.Property', 'DutyCyclePropertySummarySmallAngle')


__docformat__ = 'restructuredtext en'
__all__ = ('DutyCyclePropertySummarySmallAngle',)


T = TypeVar('T')


class DutyCyclePropertySummarySmallAngle(_1793.DutyCyclePropertySummary['_1575.AngleSmall', 'T'], Generic[T]):
    """DutyCyclePropertySummarySmallAngle

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _DUTY_CYCLE_PROPERTY_SUMMARY_SMALL_ANGLE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DutyCyclePropertySummarySmallAngle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_value(self) -> 'float':
        """float: 'AverageValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageValue
        return temp

    @property
    def maximum_value(self) -> 'float':
        """float: 'MaximumValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumValue
        return temp

    @property
    def minimum_value(self) -> 'float':
        """float: 'MinimumValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumValue
        return temp

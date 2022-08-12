"""_1694.py

VoltagePerAngularVelocity
"""


from mastapy.utility.units_and_measurements import _1565
from mastapy._internal.python_net import python_net_import

_VOLTAGE_PER_ANGULAR_VELOCITY = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'VoltagePerAngularVelocity')


__docformat__ = 'restructuredtext en'
__all__ = ('VoltagePerAngularVelocity',)


class VoltagePerAngularVelocity(_1565.MeasurementBase):
    """VoltagePerAngularVelocity

    This is a mastapy class.
    """

    TYPE = _VOLTAGE_PER_ANGULAR_VELOCITY

    __hash__ = None

    def __init__(self, instance_to_wrap: 'VoltagePerAngularVelocity.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

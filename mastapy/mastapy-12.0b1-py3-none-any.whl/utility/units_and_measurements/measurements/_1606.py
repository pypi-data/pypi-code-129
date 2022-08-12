"""_1606.py

FractionPerTemperature
"""


from mastapy.utility.units_and_measurements import _1565
from mastapy._internal.python_net import python_net_import

_FRACTION_PER_TEMPERATURE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'FractionPerTemperature')


__docformat__ = 'restructuredtext en'
__all__ = ('FractionPerTemperature',)


class FractionPerTemperature(_1565.MeasurementBase):
    """FractionPerTemperature

    This is a mastapy class.
    """

    TYPE = _FRACTION_PER_TEMPERATURE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FractionPerTemperature.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

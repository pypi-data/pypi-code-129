"""_1584.py

CurrentDensity
"""


from mastapy.utility.units_and_measurements import _1565
from mastapy._internal.python_net import python_net_import

_CURRENT_DENSITY = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'CurrentDensity')


__docformat__ = 'restructuredtext en'
__all__ = ('CurrentDensity',)


class CurrentDensity(_1565.MeasurementBase):
    """CurrentDensity

    This is a mastapy class.
    """

    TYPE = _CURRENT_DENSITY

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CurrentDensity.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

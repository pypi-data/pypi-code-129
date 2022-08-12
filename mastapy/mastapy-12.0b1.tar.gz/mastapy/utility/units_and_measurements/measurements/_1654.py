"""_1654.py

PowerSmallPerMass
"""


from mastapy.utility.units_and_measurements import _1565
from mastapy._internal.python_net import python_net_import

_POWER_SMALL_PER_MASS = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'PowerSmallPerMass')


__docformat__ = 'restructuredtext en'
__all__ = ('PowerSmallPerMass',)


class PowerSmallPerMass(_1565.MeasurementBase):
    """PowerSmallPerMass

    This is a mastapy class.
    """

    TYPE = _POWER_SMALL_PER_MASS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PowerSmallPerMass.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

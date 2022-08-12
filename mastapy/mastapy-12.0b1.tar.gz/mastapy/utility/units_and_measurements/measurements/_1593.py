"""_1593.py

ElectricalResistivity
"""


from mastapy.utility.units_and_measurements import _1565
from mastapy._internal.python_net import python_net_import

_ELECTRICAL_RESISTIVITY = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'ElectricalResistivity')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricalResistivity',)


class ElectricalResistivity(_1565.MeasurementBase):
    """ElectricalResistivity

    This is a mastapy class.
    """

    TYPE = _ELECTRICAL_RESISTIVITY

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ElectricalResistivity.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

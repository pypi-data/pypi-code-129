"""_1640.py

MagnetomotiveForce
"""


from mastapy.utility.units_and_measurements import _1565
from mastapy._internal.python_net import python_net_import

_MAGNETOMOTIVE_FORCE = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements.Measurements', 'MagnetomotiveForce')


__docformat__ = 'restructuredtext en'
__all__ = ('MagnetomotiveForce',)


class MagnetomotiveForce(_1565.MeasurementBase):
    """MagnetomotiveForce

    This is a mastapy class.
    """

    TYPE = _MAGNETOMOTIVE_FORCE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MagnetomotiveForce.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

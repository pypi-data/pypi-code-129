"""_1267.py

PermanentMagnetRotor
"""


from mastapy.electric_machines import _1270
from mastapy._internal.python_net import python_net_import

_PERMANENT_MAGNET_ROTOR = python_net_import('SMT.MastaAPI.ElectricMachines', 'PermanentMagnetRotor')


__docformat__ = 'restructuredtext en'
__all__ = ('PermanentMagnetRotor',)


class PermanentMagnetRotor(_1270.Rotor):
    """PermanentMagnetRotor

    This is a mastapy class.
    """

    TYPE = _PERMANENT_MAGNET_ROTOR

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PermanentMagnetRotor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

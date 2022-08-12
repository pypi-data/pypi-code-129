"""_2234.py

ShaftSocket
"""


from mastapy.system_model.connections_and_sockets import _2216
from mastapy._internal.python_net import python_net_import

_SHAFT_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'ShaftSocket')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftSocket',)


class ShaftSocket(_2216.CylindricalSocket):
    """ShaftSocket

    This is a mastapy class.
    """

    TYPE = _SHAFT_SOCKET

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShaftSocket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

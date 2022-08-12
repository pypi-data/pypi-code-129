"""_2385.py

ComponentsConnectedResult
"""


from mastapy._internal import constructor
from mastapy.system_model.part_model import _2386
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_COMPONENTS_CONNECTED_RESULT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'ComponentsConnectedResult')


__docformat__ = 'restructuredtext en'
__all__ = ('ComponentsConnectedResult',)


class ComponentsConnectedResult(_0.APIBase):
    """ComponentsConnectedResult

    This is a mastapy class.
    """

    TYPE = _COMPONENTS_CONNECTED_RESULT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ComponentsConnectedResult.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_failed(self) -> 'bool':
        """bool: 'ConnectionFailed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionFailed
        return temp

    @property
    def failure_message(self) -> 'str':
        """str: 'FailureMessage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FailureMessage
        return temp

    @property
    def was_connection_created(self) -> 'bool':
        """bool: 'WasConnectionCreated' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WasConnectionCreated
        return temp

    @property
    def created_socket_connection(self) -> '_2386.ConnectedSockets':
        """ConnectedSockets: 'CreatedSocketConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CreatedSocketConnection
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

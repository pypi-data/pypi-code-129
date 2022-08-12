"""_7464.py

ConsoleProgress
"""


from mastapy._internal import constructor
from mastapy import _7471
from mastapy._internal.python_net import python_net_import

_CONSOLE_PROGRESS = python_net_import('SMT.MastaAPIUtility', 'ConsoleProgress')


__docformat__ = 'restructuredtext en'
__all__ = ('ConsoleProgress',)


class ConsoleProgress(_7471.TaskProgress):
    """ConsoleProgress

    This is a mastapy class.
    """

    TYPE = _CONSOLE_PROGRESS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConsoleProgress.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def id(self) -> 'int':
        """int: 'Id' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Id
        return temp

    def add_error(self, error: 'str'):
        """ 'AddError' is the original name of this method.

        Args:
            error (str)
        """

        error = str(error)
        self.wrapped.AddError(error if error else '')

    def complete(self):
        """ 'Complete' is the original name of this method."""

        self.wrapped.Complete()

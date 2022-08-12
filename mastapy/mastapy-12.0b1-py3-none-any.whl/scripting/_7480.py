"""_7480.py

ScriptingCommand
"""


from mastapy._internal import constructor
from mastapy import _7465
from mastapy._internal.python_net import python_net_import

_SCRIPTING_COMMAND = python_net_import('SMT.MastaAPIUtility.Scripting', 'ScriptingCommand')


__docformat__ = 'restructuredtext en'
__all__ = ('ScriptingCommand',)


class ScriptingCommand(_7465.MarshalByRefObjectPermanent):
    """ScriptingCommand

    This is a mastapy class.
    """

    TYPE = _SCRIPTING_COMMAND

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ScriptingCommand.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    def execute(self):
        """ 'Execute' is the original name of this method."""

        self.wrapped.Execute()

"""_1709.py

CustomDrawing
"""


from mastapy.utility.report import _1710
from mastapy._internal.python_net import python_net_import

_CUSTOM_DRAWING = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomDrawing')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomDrawing',)


class CustomDrawing(_1710.CustomGraphic):
    """CustomDrawing

    This is a mastapy class.
    """

    TYPE = _CUSTOM_DRAWING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CustomDrawing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

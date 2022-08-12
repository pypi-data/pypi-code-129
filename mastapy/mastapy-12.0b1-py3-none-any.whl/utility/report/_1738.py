"""_1738.py

CustomTable
"""


from mastapy._internal import constructor
from mastapy.utility.report import _1727, _1736
from mastapy._internal.python_net import python_net_import

_CUSTOM_TABLE = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomTable')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomTable',)


class CustomTable(_1727.CustomReportMultiPropertyItem['_1736.CustomRow']):
    """CustomTable

    This is a mastapy class.
    """

    TYPE = _CUSTOM_TABLE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CustomTable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_main_report_item(self) -> 'bool':
        """bool: 'IsMainReportItem' is the original name of this property."""

        temp = self.wrapped.IsMainReportItem
        return temp

    @is_main_report_item.setter
    def is_main_report_item(self, value: 'bool'):
        self.wrapped.IsMainReportItem = bool(value) if value else False

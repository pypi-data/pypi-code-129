"""_1731.py

CustomReportPropertyItem
"""


from mastapy.utility.report import _1741, _1742
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.utility.reporting_property_framework import _1746
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_PROPERTY_ITEM = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportPropertyItem')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportPropertyItem',)


class CustomReportPropertyItem(_0.APIBase):
    """CustomReportPropertyItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_PROPERTY_ITEM

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CustomReportPropertyItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def font_style(self) -> '_1741.FontStyle':
        """FontStyle: 'FontStyle' is the original name of this property."""

        temp = self.wrapped.FontStyle
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1741.FontStyle)(value) if value is not None else None

    @font_style.setter
    def font_style(self, value: '_1741.FontStyle'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.FontStyle = value

    @property
    def font_weight(self) -> '_1742.FontWeight':
        """FontWeight: 'FontWeight' is the original name of this property."""

        temp = self.wrapped.FontWeight
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1742.FontWeight)(value) if value is not None else None

    @font_weight.setter
    def font_weight(self, value: '_1742.FontWeight'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.FontWeight = value

    @property
    def horizontal_position(self) -> '_1746.CellValuePosition':
        """CellValuePosition: 'HorizontalPosition' is the original name of this property."""

        temp = self.wrapped.HorizontalPosition
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1746.CellValuePosition)(value) if value is not None else None

    @horizontal_position.setter
    def horizontal_position(self, value: '_1746.CellValuePosition'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.HorizontalPosition = value

    @property
    def show_property_name(self) -> 'bool':
        """bool: 'ShowPropertyName' is the original name of this property."""

        temp = self.wrapped.ShowPropertyName
        return temp

    @show_property_name.setter
    def show_property_name(self, value: 'bool'):
        self.wrapped.ShowPropertyName = bool(value) if value else False

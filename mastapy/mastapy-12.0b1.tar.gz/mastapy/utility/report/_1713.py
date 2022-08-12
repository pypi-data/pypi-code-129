"""_1713.py

CustomReportCadDrawing
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.utility.cad_export import _1789
from mastapy.utility.report import _1729
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_CAD_DRAWING = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportCadDrawing')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportCadDrawing',)


class CustomReportCadDrawing(_1729.CustomReportNameableItem):
    """CustomReportCadDrawing

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_CAD_DRAWING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CustomReportCadDrawing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def scale(self) -> 'float':
        """float: 'Scale' is the original name of this property."""

        temp = self.wrapped.Scale
        return temp

    @scale.setter
    def scale(self, value: 'float'):
        self.wrapped.Scale = float(value) if value else 0.0

    @property
    def stock_drawing(self) -> '_1789.StockDrawings':
        """StockDrawings: 'StockDrawing' is the original name of this property."""

        temp = self.wrapped.StockDrawing
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1789.StockDrawings)(value) if value is not None else None

    @stock_drawing.setter
    def stock_drawing(self, value: '_1789.StockDrawings'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.StockDrawing = value

    @property
    def use_stock_drawing(self) -> 'bool':
        """bool: 'UseStockDrawing' is the original name of this property."""

        temp = self.wrapped.UseStockDrawing
        return temp

    @use_stock_drawing.setter
    def use_stock_drawing(self, value: 'bool'):
        self.wrapped.UseStockDrawing = bool(value) if value else False

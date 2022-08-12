"""_1715.py

CustomReportChartItem
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.utility.report import _1707, _1731
from mastapy._internal.python_net import python_net_import

_CUSTOM_REPORT_CHART_ITEM = python_net_import('SMT.MastaAPI.Utility.Report', 'CustomReportChartItem')


__docformat__ = 'restructuredtext en'
__all__ = ('CustomReportChartItem',)


class CustomReportChartItem(_1731.CustomReportPropertyItem):
    """CustomReportChartItem

    This is a mastapy class.
    """

    TYPE = _CUSTOM_REPORT_CHART_ITEM

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CustomReportChartItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def has_marker(self) -> 'bool':
        """bool: 'HasMarker' is the original name of this property."""

        temp = self.wrapped.HasMarker
        return temp

    @has_marker.setter
    def has_marker(self, value: 'bool'):
        self.wrapped.HasMarker = bool(value) if value else False

    @property
    def marker_size(self) -> 'float':
        """float: 'MarkerSize' is the original name of this property."""

        temp = self.wrapped.MarkerSize
        return temp

    @marker_size.setter
    def marker_size(self, value: 'float'):
        self.wrapped.MarkerSize = float(value) if value else 0.0

    @property
    def point_shape(self) -> '_1707.SMTChartPointShape':
        """SMTChartPointShape: 'PointShape' is the original name of this property."""

        temp = self.wrapped.PointShape
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1707.SMTChartPointShape)(value) if value is not None else None

    @point_shape.setter
    def point_shape(self, value: '_1707.SMTChartPointShape'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.PointShape = value

    @property
    def smooth_lines(self) -> 'bool':
        """bool: 'SmoothLines' is the original name of this property."""

        temp = self.wrapped.SmoothLines
        return temp

    @smooth_lines.setter
    def smooth_lines(self, value: 'bool'):
        self.wrapped.SmoothLines = bool(value) if value else False

"""_1740.py

DynamicCustomReportItem
"""


from mastapy._internal import constructor
from mastapy.utility.report import (
    _1721, _1701, _1708, _1709,
    _1710, _1711, _1712, _1713,
    _1714, _1716, _1717, _1718,
    _1719, _1720, _1722, _1724,
    _1725, _1728, _1729, _1730,
    _1732, _1733, _1734, _1735,
    _1737, _1738
)
from mastapy.shafts import _20
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.cylindrical import _1025
from mastapy.utility_gui.charts import _1806, _1807
from mastapy.bearings.bearing_results import (
    _1894, _1895, _1898, _1906
)
from mastapy.system_model.analyses_and_results.system_deflections.reporting import _2783
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4316
from mastapy.system_model.analyses_and_results.modal_analyses.reporting import _4644, _4648
from mastapy._internal.python_net import python_net_import

_DYNAMIC_CUSTOM_REPORT_ITEM = python_net_import('SMT.MastaAPI.Utility.Report', 'DynamicCustomReportItem')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicCustomReportItem',)


class DynamicCustomReportItem(_1729.CustomReportNameableItem):
    """DynamicCustomReportItem

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_CUSTOM_REPORT_ITEM

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DynamicCustomReportItem.TYPE'):
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

    @property
    def inner_item(self) -> '_1721.CustomReportItem':
        """CustomReportItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1721.CustomReportItem.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportItem. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_shaft_damage_results_table_and_chart(self) -> '_20.ShaftDamageResultsTableAndChart':
        """ShaftDamageResultsTableAndChart: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _20.ShaftDamageResultsTableAndChart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to ShaftDamageResultsTableAndChart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_cylindrical_gear_table_with_mg_charts(self) -> '_1025.CylindricalGearTableWithMGCharts':
        """CylindricalGearTableWithMGCharts: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1025.CylindricalGearTableWithMGCharts.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CylindricalGearTableWithMGCharts. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_ad_hoc_custom_table(self) -> '_1701.AdHocCustomTable':
        """AdHocCustomTable: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1701.AdHocCustomTable.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to AdHocCustomTable. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_custom_chart(self) -> '_1708.CustomChart':
        """CustomChart: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1708.CustomChart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomChart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_custom_drawing(self) -> '_1709.CustomDrawing':
        """CustomDrawing: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1709.CustomDrawing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomDrawing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_custom_graphic(self) -> '_1710.CustomGraphic':
        """CustomGraphic: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1710.CustomGraphic.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomGraphic. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_custom_image(self) -> '_1711.CustomImage':
        """CustomImage: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1711.CustomImage.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomImage. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_custom_report(self) -> '_1712.CustomReport':
        """CustomReport: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1712.CustomReport.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReport. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_custom_report_cad_drawing(self) -> '_1713.CustomReportCadDrawing':
        """CustomReportCadDrawing: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1713.CustomReportCadDrawing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportCadDrawing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_custom_report_chart(self) -> '_1714.CustomReportChart':
        """CustomReportChart: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1714.CustomReportChart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportChart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_custom_report_column(self) -> '_1716.CustomReportColumn':
        """CustomReportColumn: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1716.CustomReportColumn.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportColumn. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_custom_report_columns(self) -> '_1717.CustomReportColumns':
        """CustomReportColumns: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1717.CustomReportColumns.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportColumns. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_custom_report_definition_item(self) -> '_1718.CustomReportDefinitionItem':
        """CustomReportDefinitionItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1718.CustomReportDefinitionItem.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportDefinitionItem. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_custom_report_horizontal_line(self) -> '_1719.CustomReportHorizontalLine':
        """CustomReportHorizontalLine: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1719.CustomReportHorizontalLine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportHorizontalLine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_custom_report_html_item(self) -> '_1720.CustomReportHtmlItem':
        """CustomReportHtmlItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1720.CustomReportHtmlItem.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportHtmlItem. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_custom_report_item_container(self) -> '_1722.CustomReportItemContainer':
        """CustomReportItemContainer: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1722.CustomReportItemContainer.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportItemContainer. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_custom_report_item_container_collection_base(self) -> '_1724.CustomReportItemContainerCollectionBase':
        """CustomReportItemContainerCollectionBase: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1724.CustomReportItemContainerCollectionBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportItemContainerCollectionBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_custom_report_item_container_collection_item(self) -> '_1725.CustomReportItemContainerCollectionItem':
        """CustomReportItemContainerCollectionItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1725.CustomReportItemContainerCollectionItem.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportItemContainerCollectionItem. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_custom_report_multi_property_item_base(self) -> '_1728.CustomReportMultiPropertyItemBase':
        """CustomReportMultiPropertyItemBase: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1728.CustomReportMultiPropertyItemBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportMultiPropertyItemBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_custom_report_nameable_item(self) -> '_1729.CustomReportNameableItem':
        """CustomReportNameableItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1729.CustomReportNameableItem.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportNameableItem. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_custom_report_named_item(self) -> '_1730.CustomReportNamedItem':
        """CustomReportNamedItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1730.CustomReportNamedItem.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportNamedItem. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_custom_report_status_item(self) -> '_1732.CustomReportStatusItem':
        """CustomReportStatusItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1732.CustomReportStatusItem.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportStatusItem. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_custom_report_tab(self) -> '_1733.CustomReportTab':
        """CustomReportTab: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1733.CustomReportTab.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportTab. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_custom_report_tabs(self) -> '_1734.CustomReportTabs':
        """CustomReportTabs: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1734.CustomReportTabs.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportTabs. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_custom_report_text(self) -> '_1735.CustomReportText':
        """CustomReportText: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1735.CustomReportText.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomReportText. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_custom_sub_report(self) -> '_1737.CustomSubReport':
        """CustomSubReport: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1737.CustomSubReport.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomSubReport. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_custom_table(self) -> '_1738.CustomTable':
        """CustomTable: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1738.CustomTable.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomTable. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_dynamic_custom_report_item(self) -> 'DynamicCustomReportItem':
        """DynamicCustomReportItem: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if DynamicCustomReportItem.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to DynamicCustomReportItem. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_custom_line_chart(self) -> '_1806.CustomLineChart':
        """CustomLineChart: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1806.CustomLineChart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomLineChart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_custom_table_and_chart(self) -> '_1807.CustomTableAndChart':
        """CustomTableAndChart: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1807.CustomTableAndChart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CustomTableAndChart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_loaded_ball_element_chart_reporter(self) -> '_1894.LoadedBallElementChartReporter':
        """LoadedBallElementChartReporter: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1894.LoadedBallElementChartReporter.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to LoadedBallElementChartReporter. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_loaded_bearing_chart_reporter(self) -> '_1895.LoadedBearingChartReporter':
        """LoadedBearingChartReporter: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1895.LoadedBearingChartReporter.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to LoadedBearingChartReporter. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_loaded_bearing_temperature_chart(self) -> '_1898.LoadedBearingTemperatureChart':
        """LoadedBearingTemperatureChart: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1898.LoadedBearingTemperatureChart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to LoadedBearingTemperatureChart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_loaded_roller_element_chart_reporter(self) -> '_1906.LoadedRollerElementChartReporter':
        """LoadedRollerElementChartReporter: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _1906.LoadedRollerElementChartReporter.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to LoadedRollerElementChartReporter. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_shaft_system_deflection_sections_report(self) -> '_2783.ShaftSystemDeflectionSectionsReport':
        """ShaftSystemDeflectionSectionsReport: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _2783.ShaftSystemDeflectionSectionsReport.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to ShaftSystemDeflectionSectionsReport. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_parametric_study_histogram(self) -> '_4316.ParametricStudyHistogram':
        """ParametricStudyHistogram: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _4316.ParametricStudyHistogram.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to ParametricStudyHistogram. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_campbell_diagram_report(self) -> '_4644.CampbellDiagramReport':
        """CampbellDiagramReport: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _4644.CampbellDiagramReport.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to CampbellDiagramReport. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_item_of_type_per_mode_results_report(self) -> '_4648.PerModeResultsReport':
        """PerModeResultsReport: 'InnerItem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerItem
        if _4648.PerModeResultsReport.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_item to PerModeResultsReport. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

"""_1303.py

ElectricMachineResultsViewable
"""


from typing import List

from mastapy.utility_gui.charts.colour import _1816
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.electric_machines.results import _1304, _1294
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.electric_machines import _1272, _1269
from mastapy.utility.property import _1798
from mastapy.nodal_analysis.elmer import _168
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_RESULTS_VIEWABLE = python_net_import('SMT.MastaAPI.ElectricMachines.Results', 'ElectricMachineResultsViewable')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineResultsViewable',)


class ElectricMachineResultsViewable(_168.ElmerResultsViewable):
    """ElectricMachineResultsViewable

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_RESULTS_VIEWABLE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ElectricMachineResultsViewable.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def field_lines_colour_map(self) -> '_1816.ColourMapOption':
        """ColourMapOption: 'FieldLinesColourMap' is the original name of this property."""

        temp = self.wrapped.FieldLinesColourMap
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1816.ColourMapOption)(value) if value is not None else None

    @field_lines_colour_map.setter
    def field_lines_colour_map(self, value: '_1816.ColourMapOption'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.FieldLinesColourMap = value

    @property
    def force_view_options(self) -> '_1304.ElectricMachineForceViewOptions':
        """ElectricMachineForceViewOptions: 'ForceViewOptions' is the original name of this property."""

        temp = self.wrapped.ForceViewOptions
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1304.ElectricMachineForceViewOptions)(value) if value is not None else None

    @force_view_options.setter
    def force_view_options(self, value: '_1304.ElectricMachineForceViewOptions'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ForceViewOptions = value

    @property
    def number_of_lines(self) -> 'int':
        """int: 'NumberOfLines' is the original name of this property."""

        temp = self.wrapped.NumberOfLines
        return temp

    @number_of_lines.setter
    def number_of_lines(self, value: 'int'):
        self.wrapped.NumberOfLines = int(value) if value else 0

    @property
    def results(self) -> 'list_with_selected_item.ListWithSelectedItem_ElectricMachineResults':
        """list_with_selected_item.ListWithSelectedItem_ElectricMachineResults: 'Results' is the original name of this property."""

        temp = self.wrapped.Results
        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_ElectricMachineResults)(temp) if temp is not None else None

    @results.setter
    def results(self, value: 'list_with_selected_item.ListWithSelectedItem_ElectricMachineResults.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_ElectricMachineResults.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_ElectricMachineResults.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.Results = value

    @property
    def show_field_lines(self) -> 'bool':
        """bool: 'ShowFieldLines' is the original name of this property."""

        temp = self.wrapped.ShowFieldLines
        return temp

    @show_field_lines.setter
    def show_field_lines(self, value: 'bool'):
        self.wrapped.ShowFieldLines = bool(value) if value else False

    @property
    def slice(self) -> 'list_with_selected_item.ListWithSelectedItem_RotorSkewSlice':
        """list_with_selected_item.ListWithSelectedItem_RotorSkewSlice: 'Slice' is the original name of this property."""

        temp = self.wrapped.Slice
        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_RotorSkewSlice)(temp) if temp is not None else None

    @slice.setter
    def slice(self, value: 'list_with_selected_item.ListWithSelectedItem_RotorSkewSlice.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_RotorSkewSlice.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_RotorSkewSlice.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.Slice = value

    @property
    def parts_to_view(self) -> 'List[_1798.EnumWithBool[_1269.RegionID]]':
        """List[EnumWithBool[RegionID]]: 'PartsToView' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PartsToView
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def deselect_all(self):
        """ 'DeselectAll' is the original name of this method."""

        self.wrapped.DeselectAll()

    def select_all(self):
        """ 'SelectAll' is the original name of this method."""

        self.wrapped.SelectAll()

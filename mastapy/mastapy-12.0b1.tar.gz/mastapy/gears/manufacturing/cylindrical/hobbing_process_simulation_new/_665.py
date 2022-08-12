"""_665.py

HobbingProcessTotalModificationCalculation
"""


from mastapy._internal import constructor
from mastapy.utility_gui.charts import _1813
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _656
from mastapy._internal.python_net import python_net_import

_HOBBING_PROCESS_TOTAL_MODIFICATION_CALCULATION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'HobbingProcessTotalModificationCalculation')


__docformat__ = 'restructuredtext en'
__all__ = ('HobbingProcessTotalModificationCalculation',)


class HobbingProcessTotalModificationCalculation(_656.HobbingProcessCalculation):
    """HobbingProcessTotalModificationCalculation

    This is a mastapy class.
    """

    TYPE = _HOBBING_PROCESS_TOTAL_MODIFICATION_CALCULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HobbingProcessTotalModificationCalculation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def lead_range_max(self) -> 'float':
        """float: 'LeadRangeMax' is the original name of this property."""

        temp = self.wrapped.LeadRangeMax
        return temp

    @lead_range_max.setter
    def lead_range_max(self, value: 'float'):
        self.wrapped.LeadRangeMax = float(value) if value else 0.0

    @property
    def lead_range_min(self) -> 'float':
        """float: 'LeadRangeMin' is the original name of this property."""

        temp = self.wrapped.LeadRangeMin
        return temp

    @lead_range_min.setter
    def lead_range_min(self, value: 'float'):
        self.wrapped.LeadRangeMin = float(value) if value else 0.0

    @property
    def number_of_lead_bands(self) -> 'int':
        """int: 'NumberOfLeadBands' is the original name of this property."""

        temp = self.wrapped.NumberOfLeadBands
        return temp

    @number_of_lead_bands.setter
    def number_of_lead_bands(self, value: 'int'):
        self.wrapped.NumberOfLeadBands = int(value) if value else 0

    @property
    def number_of_profile_bands(self) -> 'int':
        """int: 'NumberOfProfileBands' is the original name of this property."""

        temp = self.wrapped.NumberOfProfileBands
        return temp

    @number_of_profile_bands.setter
    def number_of_profile_bands(self, value: 'int'):
        self.wrapped.NumberOfProfileBands = int(value) if value else 0

    @property
    def total_errors_chart_left_flank(self) -> '_1813.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'TotalErrorsChartLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalErrorsChartLeftFlank
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def total_errors_chart_right_flank(self) -> '_1813.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'TotalErrorsChartRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalErrorsChartRightFlank
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

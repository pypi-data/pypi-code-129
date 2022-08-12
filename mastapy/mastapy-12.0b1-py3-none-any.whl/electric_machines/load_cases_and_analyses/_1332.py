"""_1332.py

SingleOperatingPointAnalysis
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.electric_machines.results import _1296
from mastapy.electric_machines.load_cases_and_analyses import (
    _1321, _1338, _1333, _1316
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SINGLE_OPERATING_POINT_ANALYSIS = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'SingleOperatingPointAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SingleOperatingPointAnalysis',)


class SingleOperatingPointAnalysis(_1316.ElectricMachineAnalysis):
    """SingleOperatingPointAnalysis

    This is a mastapy class.
    """

    TYPE = _SINGLE_OPERATING_POINT_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SingleOperatingPointAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def current_angle(self) -> 'float':
        """float: 'CurrentAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentAngle
        return temp

    @property
    def d_axis_current(self) -> 'float':
        """float: 'DAxisCurrent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DAxisCurrent
        return temp

    @property
    def electrical_frequency(self) -> 'float':
        """float: 'ElectricalFrequency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricalFrequency
        return temp

    @property
    def electrical_period(self) -> 'float':
        """float: 'ElectricalPeriod' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricalPeriod
        return temp

    @property
    def mechanical_period(self) -> 'float':
        """float: 'MechanicalPeriod' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MechanicalPeriod
        return temp

    @property
    def peak_line_current(self) -> 'float':
        """float: 'PeakLineCurrent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakLineCurrent
        return temp

    @property
    def peak_phase_current(self) -> 'float':
        """float: 'PeakPhaseCurrent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakPhaseCurrent
        return temp

    @property
    def phase_current_drms(self) -> 'float':
        """float: 'PhaseCurrentDRMS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseCurrentDRMS
        return temp

    @property
    def phase_current_qrms(self) -> 'float':
        """float: 'PhaseCurrentQRMS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseCurrentQRMS
        return temp

    @property
    def q_axis_current(self) -> 'float':
        """float: 'QAxisCurrent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.QAxisCurrent
        return temp

    @property
    def rms_phase_current(self) -> 'float':
        """float: 'RMSPhaseCurrent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RMSPhaseCurrent
        return temp

    @property
    def slot_passing_period(self) -> 'float':
        """float: 'SlotPassingPeriod' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlotPassingPeriod
        return temp

    @property
    def time_step_increment(self) -> 'float':
        """float: 'TimeStepIncrement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TimeStepIncrement
        return temp

    @property
    def electric_machine_results(self) -> '_1296.ElectricMachineResultsForOpenCircuitAndOnLoad':
        """ElectricMachineResultsForOpenCircuitAndOnLoad: 'ElectricMachineResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def load_case(self) -> '_1321.ElectricMachineLoadCase':
        """ElectricMachineLoadCase: 'LoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadCase
        if _1321.ElectricMachineLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast load_case to ElectricMachineLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def slot_section_details_for_analysis(self) -> 'List[_1333.SlotDetailForAnalysis]':
        """List[SlotDetailForAnalysis]: 'SlotSectionDetailsForAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlotSectionDetailsForAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

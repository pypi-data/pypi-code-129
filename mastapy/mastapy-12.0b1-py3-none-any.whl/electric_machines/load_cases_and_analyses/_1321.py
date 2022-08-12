"""_1321.py

ElectricMachineLoadCase
"""


from mastapy._internal.implicit import enum_with_selected_value
from mastapy.nodal_analysis.elmer import _166
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy.electric_machines.load_cases_and_analyses import (
    _1324, _1328, _1320, _1322
)
from mastapy.electric_machines import _1248
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_LOAD_CASE = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'ElectricMachineLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineLoadCase',)


class ElectricMachineLoadCase(_1322.ElectricMachineLoadCaseBase):
    """ElectricMachineLoadCase

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ElectricMachineLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis_period(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ElectricMachineAnalysisPeriod':
        """enum_with_selected_value.EnumWithSelectedValue_ElectricMachineAnalysisPeriod: 'AnalysisPeriod' is the original name of this property."""

        temp = self.wrapped.AnalysisPeriod
        value = enum_with_selected_value.EnumWithSelectedValue_ElectricMachineAnalysisPeriod.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @analysis_period.setter
    def analysis_period(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ElectricMachineAnalysisPeriod.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ElectricMachineAnalysisPeriod.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.AnalysisPeriod = value

    @property
    def core_loss_minor_loop_hysteresis_loss_factor(self) -> 'float':
        """float: 'CoreLossMinorLoopHysteresisLossFactor' is the original name of this property."""

        temp = self.wrapped.CoreLossMinorLoopHysteresisLossFactor
        return temp

    @core_loss_minor_loop_hysteresis_loss_factor.setter
    def core_loss_minor_loop_hysteresis_loss_factor(self, value: 'float'):
        self.wrapped.CoreLossMinorLoopHysteresisLossFactor = float(value) if value else 0.0

    @property
    def current_angle(self) -> 'float':
        """float: 'CurrentAngle' is the original name of this property."""

        temp = self.wrapped.CurrentAngle
        return temp

    @current_angle.setter
    def current_angle(self, value: 'float'):
        self.wrapped.CurrentAngle = float(value) if value else 0.0

    @property
    def end_winding_inductance_method(self) -> '_1324.EndWindingInductanceMethod':
        """EndWindingInductanceMethod: 'EndWindingInductanceMethod' is the original name of this property."""

        temp = self.wrapped.EndWindingInductanceMethod
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1324.EndWindingInductanceMethod)(value) if value is not None else None

    @end_winding_inductance_method.setter
    def end_winding_inductance_method(self, value: '_1324.EndWindingInductanceMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.EndWindingInductanceMethod = value

    @property
    def include_iron_and_eddy_current_losses(self) -> 'bool':
        """bool: 'IncludeIronAndEddyCurrentLosses' is the original name of this property."""

        temp = self.wrapped.IncludeIronAndEddyCurrentLosses
        return temp

    @include_iron_and_eddy_current_losses.setter
    def include_iron_and_eddy_current_losses(self, value: 'bool'):
        self.wrapped.IncludeIronAndEddyCurrentLosses = bool(value) if value else False

    @property
    def include_open_circuit_calculation(self) -> 'bool':
        """bool: 'IncludeOpenCircuitCalculation' is the original name of this property."""

        temp = self.wrapped.IncludeOpenCircuitCalculation
        return temp

    @include_open_circuit_calculation.setter
    def include_open_circuit_calculation(self, value: 'bool'):
        self.wrapped.IncludeOpenCircuitCalculation = bool(value) if value else False

    @property
    def minimum_number_of_steps_for_voltages_and_losses_calculation(self) -> 'int':
        """int: 'MinimumNumberOfStepsForVoltagesAndLossesCalculation' is the original name of this property."""

        temp = self.wrapped.MinimumNumberOfStepsForVoltagesAndLossesCalculation
        return temp

    @minimum_number_of_steps_for_voltages_and_losses_calculation.setter
    def minimum_number_of_steps_for_voltages_and_losses_calculation(self, value: 'int'):
        self.wrapped.MinimumNumberOfStepsForVoltagesAndLossesCalculation = int(value) if value else 0

    @property
    def motoring_or_generating(self) -> '_1328.MotoringOrGenerating':
        """MotoringOrGenerating: 'MotoringOrGenerating' is the original name of this property."""

        temp = self.wrapped.MotoringOrGenerating
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1328.MotoringOrGenerating)(value) if value is not None else None

    @motoring_or_generating.setter
    def motoring_or_generating(self, value: '_1328.MotoringOrGenerating'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.MotoringOrGenerating = value

    @property
    def number_of_cycles(self) -> 'int':
        """int: 'NumberOfCycles' is the original name of this property."""

        temp = self.wrapped.NumberOfCycles
        return temp

    @number_of_cycles.setter
    def number_of_cycles(self, value: 'int'):
        self.wrapped.NumberOfCycles = int(value) if value else 0

    @property
    def number_of_steps_per_cycle(self) -> 'int':
        """int: 'NumberOfStepsPerCycle' is the original name of this property."""

        temp = self.wrapped.NumberOfStepsPerCycle
        return temp

    @number_of_steps_per_cycle.setter
    def number_of_steps_per_cycle(self, value: 'int'):
        self.wrapped.NumberOfStepsPerCycle = int(value) if value else 0

    @property
    def override_design_end_winding_inductance_method(self) -> 'bool':
        """bool: 'OverrideDesignEndWindingInductanceMethod' is the original name of this property."""

        temp = self.wrapped.OverrideDesignEndWindingInductanceMethod
        return temp

    @override_design_end_winding_inductance_method.setter
    def override_design_end_winding_inductance_method(self, value: 'bool'):
        self.wrapped.OverrideDesignEndWindingInductanceMethod = bool(value) if value else False

    @property
    def peak_line_current(self) -> 'float':
        """float: 'PeakLineCurrent' is the original name of this property."""

        temp = self.wrapped.PeakLineCurrent
        return temp

    @peak_line_current.setter
    def peak_line_current(self, value: 'float'):
        self.wrapped.PeakLineCurrent = float(value) if value else 0.0

    @property
    def rms_line_current(self) -> 'float':
        """float: 'RMSLineCurrent' is the original name of this property."""

        temp = self.wrapped.RMSLineCurrent
        return temp

    @rms_line_current.setter
    def rms_line_current(self, value: 'float'):
        self.wrapped.RMSLineCurrent = float(value) if value else 0.0

    @property
    def speed(self) -> 'float':
        """float: 'Speed' is the original name of this property."""

        temp = self.wrapped.Speed
        return temp

    @speed.setter
    def speed(self, value: 'float'):
        self.wrapped.Speed = float(value) if value else 0.0

    @property
    def total_number_of_time_steps(self) -> 'int':
        """int: 'TotalNumberOfTimeSteps' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalNumberOfTimeSteps
        return temp

    @property
    def user_specified_end_winding_inductance(self) -> 'float':
        """float: 'UserSpecifiedEndWindingInductance' is the original name of this property."""

        temp = self.wrapped.UserSpecifiedEndWindingInductance
        return temp

    @user_specified_end_winding_inductance.setter
    def user_specified_end_winding_inductance(self, value: 'float'):
        self.wrapped.UserSpecifiedEndWindingInductance = float(value) if value else 0.0

    def analysis_for(self, setup: '_1248.ElectricMachineSetup') -> '_1320.ElectricMachineFEAnalysis':
        """ 'AnalysisFor' is the original name of this method.

        Args:
            setup (mastapy.electric_machines.ElectricMachineSetup)

        Returns:
            mastapy.electric_machines.load_cases_and_analyses.ElectricMachineFEAnalysis
        """

        method_result = self.wrapped.AnalysisFor(setup.wrapped if setup else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

"""_1310.py

OnLoadElectricMachineResults
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.electric_machines.load_cases_and_analyses import _1325
from mastapy.electric_machines import _1289
from mastapy.electric_machines.results import _1294
from mastapy._internal.python_net import python_net_import

_ON_LOAD_ELECTRIC_MACHINE_RESULTS = python_net_import('SMT.MastaAPI.ElectricMachines.Results', 'OnLoadElectricMachineResults')


__docformat__ = 'restructuredtext en'
__all__ = ('OnLoadElectricMachineResults',)


class OnLoadElectricMachineResults(_1294.ElectricMachineResults):
    """OnLoadElectricMachineResults

    This is a mastapy class.
    """

    TYPE = _ON_LOAD_ELECTRIC_MACHINE_RESULTS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'OnLoadElectricMachineResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_power_factor(self) -> 'float':
        """float: 'AveragePowerFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AveragePowerFactor
        return temp

    @property
    def average_power_factor_angle(self) -> 'float':
        """float: 'AveragePowerFactorAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AveragePowerFactorAngle
        return temp

    @property
    def average_power_factor_with_harmonic_distortion_adjustment(self) -> 'float':
        """float: 'AveragePowerFactorWithHarmonicDistortionAdjustment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AveragePowerFactorWithHarmonicDistortionAdjustment
        return temp

    @property
    def average_torque_dq(self) -> 'float':
        """float: 'AverageTorqueDQ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageTorqueDQ
        return temp

    @property
    def dc_winding_losses(self) -> 'float':
        """float: 'DCWindingLosses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DCWindingLosses
        return temp

    @property
    def efficiency(self) -> 'float':
        """float: 'Efficiency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Efficiency
        return temp

    @property
    def electrical_loading(self) -> 'float':
        """float: 'ElectricalLoading' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricalLoading
        return temp

    @property
    def input_power(self) -> 'float':
        """float: 'InputPower' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InputPower
        return temp

    @property
    def line_resistance(self) -> 'float':
        """float: 'LineResistance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LineResistance
        return temp

    @property
    def line_to_line_terminal_voltage_peak(self) -> 'float':
        """float: 'LineToLineTerminalVoltagePeak' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LineToLineTerminalVoltagePeak
        return temp

    @property
    def line_to_line_terminal_voltage_rms(self) -> 'float':
        """float: 'LineToLineTerminalVoltageRMS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LineToLineTerminalVoltageRMS
        return temp

    @property
    def line_to_line_terminal_voltage_total_harmonic_distortion(self) -> 'float':
        """float: 'LineToLineTerminalVoltageTotalHarmonicDistortion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LineToLineTerminalVoltageTotalHarmonicDistortion
        return temp

    @property
    def motor_constant(self) -> 'float':
        """float: 'MotorConstant' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MotorConstant
        return temp

    @property
    def output_power(self) -> 'float':
        """float: 'OutputPower' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OutputPower
        return temp

    @property
    def phase_resistance(self) -> 'float':
        """float: 'PhaseResistance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseResistance
        return temp

    @property
    def phase_resistive_voltage_peak(self) -> 'float':
        """float: 'PhaseResistiveVoltagePeak' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseResistiveVoltagePeak
        return temp

    @property
    def phase_resistive_voltage_rms(self) -> 'float':
        """float: 'PhaseResistiveVoltageRMS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseResistiveVoltageRMS
        return temp

    @property
    def phase_resistive_voltage_drms(self) -> 'float':
        """float: 'PhaseResistiveVoltageDRMS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseResistiveVoltageDRMS
        return temp

    @property
    def phase_resistive_voltage_qrms(self) -> 'float':
        """float: 'PhaseResistiveVoltageQRMS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseResistiveVoltageQRMS
        return temp

    @property
    def phase_terminal_voltage_peak(self) -> 'float':
        """float: 'PhaseTerminalVoltagePeak' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseTerminalVoltagePeak
        return temp

    @property
    def phase_terminal_voltage_rms(self) -> 'float':
        """float: 'PhaseTerminalVoltageRMS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseTerminalVoltageRMS
        return temp

    @property
    def phase_terminal_voltage_total_harmonic_distortion(self) -> 'float':
        """float: 'PhaseTerminalVoltageTotalHarmonicDistortion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseTerminalVoltageTotalHarmonicDistortion
        return temp

    @property
    def power_factor_direction(self) -> '_1325.LeadingOrLagging':
        """LeadingOrLagging: 'PowerFactorDirection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFactorDirection
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1325.LeadingOrLagging)(value) if value is not None else None

    @property
    def stall_current(self) -> 'float':
        """float: 'StallCurrent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StallCurrent
        return temp

    @property
    def stall_torque(self) -> 'float':
        """float: 'StallTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StallTorque
        return temp

    @property
    def torque_constant(self) -> 'float':
        """float: 'TorqueConstant' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueConstant
        return temp

    @property
    def torque_ripple_percentage_mst(self) -> 'float':
        """float: 'TorqueRipplePercentageMST' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueRipplePercentageMST
        return temp

    @property
    def total_power_loss(self) -> 'float':
        """float: 'TotalPowerLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalPowerLoss
        return temp

    @property
    def winding_material_resistivity(self) -> 'float':
        """float: 'WindingMaterialResistivity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WindingMaterialResistivity
        return temp

    @property
    def windings(self) -> '_1289.Windings':
        """Windings: 'Windings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Windings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

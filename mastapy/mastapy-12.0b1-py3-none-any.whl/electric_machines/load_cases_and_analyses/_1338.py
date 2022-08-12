"""_1338.py

SpeedTorqueLoadCase
"""


from mastapy.electric_machines.load_cases_and_analyses import (
    _1318, _1334, _1317, _1321
)
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.python_net import python_net_import

_SPEED_TORQUE_LOAD_CASE = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'SpeedTorqueLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('SpeedTorqueLoadCase',)


class SpeedTorqueLoadCase(_1321.ElectricMachineLoadCase):
    """SpeedTorqueLoadCase

    This is a mastapy class.
    """

    TYPE = _SPEED_TORQUE_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpeedTorqueLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def control_strategy(self) -> '_1318.ElectricMachineControlStrategy':
        """ElectricMachineControlStrategy: 'ControlStrategy' is the original name of this property."""

        temp = self.wrapped.ControlStrategy
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1318.ElectricMachineControlStrategy)(value) if value is not None else None

    @control_strategy.setter
    def control_strategy(self, value: '_1318.ElectricMachineControlStrategy'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ControlStrategy = value

    @property
    def include_resistive_voltages(self) -> 'bool':
        """bool: 'IncludeResistiveVoltages' is the original name of this property."""

        temp = self.wrapped.IncludeResistiveVoltages
        return temp

    @include_resistive_voltages.setter
    def include_resistive_voltages(self, value: 'bool'):
        self.wrapped.IncludeResistiveVoltages = bool(value) if value else False

    @property
    def load_specification(self) -> '_1334.SpecifyTorqueOrCurrent':
        """SpecifyTorqueOrCurrent: 'LoadSpecification' is the original name of this property."""

        temp = self.wrapped.LoadSpecification
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1334.SpecifyTorqueOrCurrent)(value) if value is not None else None

    @load_specification.setter
    def load_specification(self, value: '_1334.SpecifyTorqueOrCurrent'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.LoadSpecification = value

    @property
    def target_torque(self) -> 'float':
        """float: 'TargetTorque' is the original name of this property."""

        temp = self.wrapped.TargetTorque
        return temp

    @target_torque.setter
    def target_torque(self, value: 'float'):
        self.wrapped.TargetTorque = float(value) if value else 0.0

    @property
    def basic_mechanical_loss_settings(self) -> '_1317.ElectricMachineBasicMechanicalLossSettings':
        """ElectricMachineBasicMechanicalLossSettings: 'BasicMechanicalLossSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicMechanicalLossSettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

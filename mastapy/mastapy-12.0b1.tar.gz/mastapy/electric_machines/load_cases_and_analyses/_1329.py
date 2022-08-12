"""_1329.py

NonLinearDQModelMultipleOperatingPointsLoadCase
"""


from mastapy.electric_machines.load_cases_and_analyses import _1318, _1317, _1322
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.python_net import python_net_import

_NON_LINEAR_DQ_MODEL_MULTIPLE_OPERATING_POINTS_LOAD_CASE = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'NonLinearDQModelMultipleOperatingPointsLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('NonLinearDQModelMultipleOperatingPointsLoadCase',)


class NonLinearDQModelMultipleOperatingPointsLoadCase(_1322.ElectricMachineLoadCaseBase):
    """NonLinearDQModelMultipleOperatingPointsLoadCase

    This is a mastapy class.
    """

    TYPE = _NON_LINEAR_DQ_MODEL_MULTIPLE_OPERATING_POINTS_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'NonLinearDQModelMultipleOperatingPointsLoadCase.TYPE'):
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
    def basic_mechanical_loss_settings(self) -> '_1317.ElectricMachineBasicMechanicalLossSettings':
        """ElectricMachineBasicMechanicalLossSettings: 'BasicMechanicalLossSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicMechanicalLossSettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

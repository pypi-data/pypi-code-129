"""_1308.py

NonLinearDQModel
"""


from mastapy.utility_gui.charts import (
    _1813, _1815, _1805, _1810,
    _1812
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.electric_machines.results import _1309, _1293
from mastapy._internal.python_net import python_net_import

_NON_LINEAR_DQ_MODEL = python_net_import('SMT.MastaAPI.ElectricMachines.Results', 'NonLinearDQModel')


__docformat__ = 'restructuredtext en'
__all__ = ('NonLinearDQModel',)


class NonLinearDQModel(_1293.ElectricMachineDQModel):
    """NonLinearDQModel

    This is a mastapy class.
    """

    TYPE = _NON_LINEAR_DQ_MODEL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'NonLinearDQModel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def alignment_torque_map_at_reference_temperatures(self) -> '_1813.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'AlignmentTorqueMapAtReferenceTemperatures' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AlignmentTorqueMapAtReferenceTemperatures
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def d_axis_armature_flux_linkage_map(self) -> '_1813.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'DAxisArmatureFluxLinkageMap' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DAxisArmatureFluxLinkageMap
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name
        return temp

    @property
    def number_of_current_angle_values(self) -> 'int':
        """int: 'NumberOfCurrentAngleValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfCurrentAngleValues
        return temp

    @property
    def number_of_current_values(self) -> 'int':
        """int: 'NumberOfCurrentValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfCurrentValues
        return temp

    @property
    def q_axis_armature_flux_linkage_map(self) -> '_1813.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'QAxisArmatureFluxLinkageMap' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.QAxisArmatureFluxLinkageMap
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def reluctance_torque_map_at_reference_temperatures(self) -> '_1813.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'ReluctanceTorqueMapAtReferenceTemperatures' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReluctanceTorqueMapAtReferenceTemperatures
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rotor_eddy_current_loss_per_frequency_exponent_map(self) -> '_1813.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'RotorEddyCurrentLossPerFrequencyExponentMap' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RotorEddyCurrentLossPerFrequencyExponentMap
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rotor_excess_loss_per_frequency_exponent_map(self) -> '_1813.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'RotorExcessLossPerFrequencyExponentMap' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RotorExcessLossPerFrequencyExponentMap
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rotor_hysteresis_loss_per_frequency_exponent_map(self) -> '_1813.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'RotorHysteresisLossPerFrequencyExponentMap' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RotorHysteresisLossPerFrequencyExponentMap
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stator_eddy_current_loss_per_frequency_exponent_map(self) -> '_1813.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'StatorEddyCurrentLossPerFrequencyExponentMap' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StatorEddyCurrentLossPerFrequencyExponentMap
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stator_excess_loss_per_frequency_exponent_map(self) -> '_1813.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'StatorExcessLossPerFrequencyExponentMap' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StatorExcessLossPerFrequencyExponentMap
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stator_hysteresis_loss_per_frequency_exponent_map(self) -> '_1813.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'StatorHysteresisLossPerFrequencyExponentMap' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StatorHysteresisLossPerFrequencyExponentMap
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def torque_map_at_reference_temperatures(self) -> '_1813.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'TorqueMapAtReferenceTemperatures' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueMapAtReferenceTemperatures
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def torque_at_max_current_and_reference_temperatures(self) -> '_1815.TwoDChartDefinition':
        """TwoDChartDefinition: 'TorqueAtMaxCurrentAndReferenceTemperatures' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueAtMaxCurrentAndReferenceTemperatures
        if _1815.TwoDChartDefinition.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast torque_at_max_current_and_reference_temperatures to TwoDChartDefinition. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def non_linear_dq_model_generator_settings(self) -> '_1309.NonLinearDQModelSettings':
        """NonLinearDQModelSettings: 'NonLinearDQModelGeneratorSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NonLinearDQModelGeneratorSettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

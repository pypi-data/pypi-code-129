"""_6853.py

PowerLoadLoadCase
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.math_utility import _1493
from mastapy._internal.implicit import overridable, list_with_selected_item, enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model import _2159, _2161, _2160
from mastapy.math_utility.measured_data import _1525
from mastapy.system_model.fe import _2313
from mastapy.system_model.analyses_and_results.static_loads import _6891, _6785, _6895
from mastapy.system_model.analyses_and_results.mbd_analyses import _5440
from mastapy.nodal_analysis.varying_input_components import _96
from mastapy.system_model.part_model import _2412
from mastapy.math_utility.control import _1536
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'PowerLoadLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('PowerLoadLoadCase',)


class PowerLoadLoadCase(_6895.VirtualComponentLoadCase):
    """PowerLoadLoadCase

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PowerLoadLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def constant_resistance_coefficient(self) -> 'float':
        """float: 'ConstantResistanceCoefficient' is the original name of this property."""

        temp = self.wrapped.ConstantResistanceCoefficient
        return temp

    @constant_resistance_coefficient.setter
    def constant_resistance_coefficient(self, value: 'float'):
        self.wrapped.ConstantResistanceCoefficient = float(value) if value else 0.0

    @property
    def constant_resistance_coefficient_time_profile(self) -> '_1493.Vector2DListAccessor':
        """Vector2DListAccessor: 'ConstantResistanceCoefficientTimeProfile' is the original name of this property."""

        temp = self.wrapped.ConstantResistanceCoefficientTimeProfile
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @constant_resistance_coefficient_time_profile.setter
    def constant_resistance_coefficient_time_profile(self, value: '_1493.Vector2DListAccessor'):
        value = value.wrapped if value else None
        self.wrapped.ConstantResistanceCoefficientTimeProfile = value

    @property
    def constant_torque(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ConstantTorque' is the original name of this property."""

        temp = self.wrapped.ConstantTorque
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @constant_torque.setter
    def constant_torque(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.ConstantTorque = value

    @property
    def drag_torque_specification_method(self) -> '_2159.PowerLoadDragTorqueSpecificationMethod':
        """PowerLoadDragTorqueSpecificationMethod: 'DragTorqueSpecificationMethod' is the original name of this property."""

        temp = self.wrapped.DragTorqueSpecificationMethod
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_2159.PowerLoadDragTorqueSpecificationMethod)(value) if value is not None else None

    @drag_torque_specification_method.setter
    def drag_torque_specification_method(self, value: '_2159.PowerLoadDragTorqueSpecificationMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.DragTorqueSpecificationMethod = value

    @property
    def drag_torque_vs_speed_and_time(self) -> '_1525.GriddedSurfaceAccessor':
        """GriddedSurfaceAccessor: 'DragTorqueVsSpeedAndTime' is the original name of this property."""

        temp = self.wrapped.DragTorqueVsSpeedAndTime
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @drag_torque_vs_speed_and_time.setter
    def drag_torque_vs_speed_and_time(self, value: '_1525.GriddedSurfaceAccessor'):
        value = value.wrapped if value else None
        self.wrapped.DragTorqueVsSpeedAndTime = value

    @property
    def dynamic_torsional_stiffness(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'DynamicTorsionalStiffness' is the original name of this property."""

        temp = self.wrapped.DynamicTorsionalStiffness
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @dynamic_torsional_stiffness.setter
    def dynamic_torsional_stiffness(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.DynamicTorsionalStiffness = value

    @property
    def electric_machine_data_set_selector(self) -> 'list_with_selected_item.ListWithSelectedItem_ElectricMachineDataSet':
        """list_with_selected_item.ListWithSelectedItem_ElectricMachineDataSet: 'ElectricMachineDataSetSelector' is the original name of this property."""

        temp = self.wrapped.ElectricMachineDataSetSelector
        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_ElectricMachineDataSet)(temp) if temp is not None else None

    @electric_machine_data_set_selector.setter
    def electric_machine_data_set_selector(self, value: 'list_with_selected_item.ListWithSelectedItem_ElectricMachineDataSet.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_ElectricMachineDataSet.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_ElectricMachineDataSet.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.ElectricMachineDataSetSelector = value

    @property
    def engine_throttle_position(self) -> 'float':
        """float: 'EngineThrottlePosition' is the original name of this property."""

        temp = self.wrapped.EngineThrottlePosition
        return temp

    @engine_throttle_position.setter
    def engine_throttle_position(self, value: 'float'):
        self.wrapped.EngineThrottlePosition = float(value) if value else 0.0

    @property
    def engine_throttle_time_profile(self) -> '_1493.Vector2DListAccessor':
        """Vector2DListAccessor: 'EngineThrottleTimeProfile' is the original name of this property."""

        temp = self.wrapped.EngineThrottleTimeProfile
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @engine_throttle_time_profile.setter
    def engine_throttle_time_profile(self, value: '_1493.Vector2DListAccessor'):
        value = value.wrapped if value else None
        self.wrapped.EngineThrottleTimeProfile = value

    @property
    def first_order_lag_cutoff_frequency(self) -> 'float':
        """float: 'FirstOrderLagCutoffFrequency' is the original name of this property."""

        temp = self.wrapped.FirstOrderLagCutoffFrequency
        return temp

    @first_order_lag_cutoff_frequency.setter
    def first_order_lag_cutoff_frequency(self, value: 'float'):
        self.wrapped.FirstOrderLagCutoffFrequency = float(value) if value else 0.0

    @property
    def first_order_lag_time_constant(self) -> 'float':
        """float: 'FirstOrderLagTimeConstant' is the original name of this property."""

        temp = self.wrapped.FirstOrderLagTimeConstant
        return temp

    @first_order_lag_time_constant.setter
    def first_order_lag_time_constant(self, value: 'float'):
        self.wrapped.FirstOrderLagTimeConstant = float(value) if value else 0.0

    @property
    def include_in_torsional_stiffness_calculation(self) -> 'overridable.Overridable_bool':
        """overridable.Overridable_bool: 'IncludeInTorsionalStiffnessCalculation' is the original name of this property."""

        temp = self.wrapped.IncludeInTorsionalStiffnessCalculation
        return constructor.new_from_mastapy_type(overridable.Overridable_bool)(temp) if temp is not None else None

    @include_in_torsional_stiffness_calculation.setter
    def include_in_torsional_stiffness_calculation(self, value: 'overridable.Overridable_bool.implicit_type()'):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else False, is_overridden)
        self.wrapped.IncludeInTorsionalStiffnessCalculation = value

    @property
    def initial_angular_acceleration(self) -> 'float':
        """float: 'InitialAngularAcceleration' is the original name of this property."""

        temp = self.wrapped.InitialAngularAcceleration
        return temp

    @initial_angular_acceleration.setter
    def initial_angular_acceleration(self, value: 'float'):
        self.wrapped.InitialAngularAcceleration = float(value) if value else 0.0

    @property
    def initial_angular_displacement(self) -> 'float':
        """float: 'InitialAngularDisplacement' is the original name of this property."""

        temp = self.wrapped.InitialAngularDisplacement
        return temp

    @initial_angular_displacement.setter
    def initial_angular_displacement(self, value: 'float'):
        self.wrapped.InitialAngularDisplacement = float(value) if value else 0.0

    @property
    def initial_angular_velocity(self) -> 'float':
        """float: 'InitialAngularVelocity' is the original name of this property."""

        temp = self.wrapped.InitialAngularVelocity
        return temp

    @initial_angular_velocity.setter
    def initial_angular_velocity(self, value: 'float'):
        self.wrapped.InitialAngularVelocity = float(value) if value else 0.0

    @property
    def is_wheel_using_static_friction_initially(self) -> 'bool':
        """bool: 'IsWheelUsingStaticFrictionInitially' is the original name of this property."""

        temp = self.wrapped.IsWheelUsingStaticFrictionInitially
        return temp

    @is_wheel_using_static_friction_initially.setter
    def is_wheel_using_static_friction_initially(self, value: 'bool'):
        self.wrapped.IsWheelUsingStaticFrictionInitially = bool(value) if value else False

    @property
    def linear_resistance_coefficient(self) -> 'float':
        """float: 'LinearResistanceCoefficient' is the original name of this property."""

        temp = self.wrapped.LinearResistanceCoefficient
        return temp

    @linear_resistance_coefficient.setter
    def linear_resistance_coefficient(self, value: 'float'):
        self.wrapped.LinearResistanceCoefficient = float(value) if value else 0.0

    @property
    def linear_resistance_coefficient_time_profile(self) -> '_1493.Vector2DListAccessor':
        """Vector2DListAccessor: 'LinearResistanceCoefficientTimeProfile' is the original name of this property."""

        temp = self.wrapped.LinearResistanceCoefficientTimeProfile
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @linear_resistance_coefficient_time_profile.setter
    def linear_resistance_coefficient_time_profile(self, value: '_1493.Vector2DListAccessor'):
        value = value.wrapped if value else None
        self.wrapped.LinearResistanceCoefficientTimeProfile = value

    @property
    def maximum_throttle_in_drive_cycle(self) -> 'float':
        """float: 'MaximumThrottleInDriveCycle' is the original name of this property."""

        temp = self.wrapped.MaximumThrottleInDriveCycle
        return temp

    @maximum_throttle_in_drive_cycle.setter
    def maximum_throttle_in_drive_cycle(self, value: 'float'):
        self.wrapped.MaximumThrottleInDriveCycle = float(value) if value else 0.0

    @property
    def power(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Power' is the original name of this property."""

        temp = self.wrapped.Power
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @power.setter
    def power(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Power = value

    @property
    def power_load_for_pid_control(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'PowerLoadForPIDControl' is the original name of this property."""

        temp = self.wrapped.PowerLoadForPIDControl
        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_str)(temp) if temp is not None else None

    @power_load_for_pid_control.setter
    def power_load_for_pid_control(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.PowerLoadForPIDControl = value

    @property
    def proportion_of_vehicle_weight_carried(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ProportionOfVehicleWeightCarried' is the original name of this property."""

        temp = self.wrapped.ProportionOfVehicleWeightCarried
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @proportion_of_vehicle_weight_carried.setter
    def proportion_of_vehicle_weight_carried(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.ProportionOfVehicleWeightCarried = value

    @property
    def quadratic_resistance_coefficient(self) -> 'float':
        """float: 'QuadraticResistanceCoefficient' is the original name of this property."""

        temp = self.wrapped.QuadraticResistanceCoefficient
        return temp

    @quadratic_resistance_coefficient.setter
    def quadratic_resistance_coefficient(self, value: 'float'):
        self.wrapped.QuadraticResistanceCoefficient = float(value) if value else 0.0

    @property
    def quadratic_resistance_coefficient_time_profile(self) -> '_1493.Vector2DListAccessor':
        """Vector2DListAccessor: 'QuadraticResistanceCoefficientTimeProfile' is the original name of this property."""

        temp = self.wrapped.QuadraticResistanceCoefficientTimeProfile
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @quadratic_resistance_coefficient_time_profile.setter
    def quadratic_resistance_coefficient_time_profile(self, value: '_1493.Vector2DListAccessor'):
        value = value.wrapped if value else None
        self.wrapped.QuadraticResistanceCoefficientTimeProfile = value

    @property
    def specified_angle_for_input_torque(self) -> 'float':
        """float: 'SpecifiedAngleForInputTorque' is the original name of this property."""

        temp = self.wrapped.SpecifiedAngleForInputTorque
        return temp

    @specified_angle_for_input_torque.setter
    def specified_angle_for_input_torque(self, value: 'float'):
        self.wrapped.SpecifiedAngleForInputTorque = float(value) if value else 0.0

    @property
    def specified_time_for_input_torque(self) -> 'float':
        """float: 'SpecifiedTimeForInputTorque' is the original name of this property."""

        temp = self.wrapped.SpecifiedTimeForInputTorque
        return temp

    @specified_time_for_input_torque.setter
    def specified_time_for_input_torque(self, value: 'float'):
        self.wrapped.SpecifiedTimeForInputTorque = float(value) if value else 0.0

    @property
    def specify_initial_acceleration(self) -> 'bool':
        """bool: 'SpecifyInitialAcceleration' is the original name of this property."""

        temp = self.wrapped.SpecifyInitialAcceleration
        return temp

    @specify_initial_acceleration.setter
    def specify_initial_acceleration(self, value: 'bool'):
        self.wrapped.SpecifyInitialAcceleration = bool(value) if value else False

    @property
    def specify_initial_displacement(self) -> 'bool':
        """bool: 'SpecifyInitialDisplacement' is the original name of this property."""

        temp = self.wrapped.SpecifyInitialDisplacement
        return temp

    @specify_initial_displacement.setter
    def specify_initial_displacement(self, value: 'bool'):
        self.wrapped.SpecifyInitialDisplacement = bool(value) if value else False

    @property
    def specify_initial_velocity(self) -> 'bool':
        """bool: 'SpecifyInitialVelocity' is the original name of this property."""

        temp = self.wrapped.SpecifyInitialVelocity
        return temp

    @specify_initial_velocity.setter
    def specify_initial_velocity(self, value: 'bool'):
        self.wrapped.SpecifyInitialVelocity = bool(value) if value else False

    @property
    def speed(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Speed' is the original name of this property."""

        temp = self.wrapped.Speed
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @speed.setter
    def speed(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Speed = value

    @property
    def speed_vs_time(self) -> '_1493.Vector2DListAccessor':
        """Vector2DListAccessor: 'SpeedVsTime' is the original name of this property."""

        temp = self.wrapped.SpeedVsTime
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @speed_vs_time.setter
    def speed_vs_time(self, value: '_1493.Vector2DListAccessor'):
        value = value.wrapped if value else None
        self.wrapped.SpeedVsTime = value

    @property
    def system_deflection_torque_also_applies_to_advanced_system_deflection(self) -> 'bool':
        """bool: 'SystemDeflectionTorqueAlsoAppliesToAdvancedSystemDeflection' is the original name of this property."""

        temp = self.wrapped.SystemDeflectionTorqueAlsoAppliesToAdvancedSystemDeflection
        return temp

    @system_deflection_torque_also_applies_to_advanced_system_deflection.setter
    def system_deflection_torque_also_applies_to_advanced_system_deflection(self, value: 'bool'):
        self.wrapped.SystemDeflectionTorqueAlsoAppliesToAdvancedSystemDeflection = bool(value) if value else False

    @property
    def system_deflection_torque_method(self) -> 'enum_with_selected_value.EnumWithSelectedValue_TorqueSpecificationForSystemDeflection':
        """enum_with_selected_value.EnumWithSelectedValue_TorqueSpecificationForSystemDeflection: 'SystemDeflectionTorqueMethod' is the original name of this property."""

        temp = self.wrapped.SystemDeflectionTorqueMethod
        value = enum_with_selected_value.EnumWithSelectedValue_TorqueSpecificationForSystemDeflection.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @system_deflection_torque_method.setter
    def system_deflection_torque_method(self, value: 'enum_with_selected_value.EnumWithSelectedValue_TorqueSpecificationForSystemDeflection.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_TorqueSpecificationForSystemDeflection.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.SystemDeflectionTorqueMethod = value

    @property
    def target_engine_idle_speed(self) -> 'float':
        """float: 'TargetEngineIdleSpeed' is the original name of this property."""

        temp = self.wrapped.TargetEngineIdleSpeed
        return temp

    @target_engine_idle_speed.setter
    def target_engine_idle_speed(self, value: 'float'):
        self.wrapped.TargetEngineIdleSpeed = float(value) if value else 0.0

    @property
    def target_speed(self) -> 'float':
        """float: 'TargetSpeed' is the original name of this property."""

        temp = self.wrapped.TargetSpeed
        return temp

    @target_speed.setter
    def target_speed(self, value: 'float'):
        self.wrapped.TargetSpeed = float(value) if value else 0.0

    @property
    def target_speed_input_type(self) -> '_2161.PowerLoadPIDControlSpeedInputType':
        """PowerLoadPIDControlSpeedInputType: 'TargetSpeedInputType' is the original name of this property."""

        temp = self.wrapped.TargetSpeedInputType
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_2161.PowerLoadPIDControlSpeedInputType)(value) if value is not None else None

    @target_speed_input_type.setter
    def target_speed_input_type(self, value: '_2161.PowerLoadPIDControlSpeedInputType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.TargetSpeedInputType = value

    @property
    def target_speed_vs_time(self) -> '_1493.Vector2DListAccessor':
        """Vector2DListAccessor: 'TargetSpeedVsTime' is the original name of this property."""

        temp = self.wrapped.TargetSpeedVsTime
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @target_speed_vs_time.setter
    def target_speed_vs_time(self, value: '_1493.Vector2DListAccessor'):
        value = value.wrapped if value else None
        self.wrapped.TargetSpeedVsTime = value

    @property
    def torque(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Torque' is the original name of this property."""

        temp = self.wrapped.Torque
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @torque.setter
    def torque(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Torque = value

    @property
    def torque_input_method(self) -> 'enum_with_selected_value.EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod':
        """enum_with_selected_value.EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod: 'TorqueInputMethod' is the original name of this property."""

        temp = self.wrapped.TorqueInputMethod
        value = enum_with_selected_value.EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @torque_input_method.setter
    def torque_input_method(self, value: 'enum_with_selected_value.EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.TorqueInputMethod = value

    @property
    def torque_time_profile_repeats(self) -> 'bool':
        """bool: 'TorqueTimeProfileRepeats' is the original name of this property."""

        temp = self.wrapped.TorqueTimeProfileRepeats
        return temp

    @torque_time_profile_repeats.setter
    def torque_time_profile_repeats(self, value: 'bool'):
        self.wrapped.TorqueTimeProfileRepeats = bool(value) if value else False

    @property
    def torque_vs_angle(self) -> '_1493.Vector2DListAccessor':
        """Vector2DListAccessor: 'TorqueVsAngle' is the original name of this property."""

        temp = self.wrapped.TorqueVsAngle
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @torque_vs_angle.setter
    def torque_vs_angle(self, value: '_1493.Vector2DListAccessor'):
        value = value.wrapped if value else None
        self.wrapped.TorqueVsAngle = value

    @property
    def torque_vs_angle_and_speed(self) -> '_1525.GriddedSurfaceAccessor':
        """GriddedSurfaceAccessor: 'TorqueVsAngleAndSpeed' is the original name of this property."""

        temp = self.wrapped.TorqueVsAngleAndSpeed
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @torque_vs_angle_and_speed.setter
    def torque_vs_angle_and_speed(self, value: '_1525.GriddedSurfaceAccessor'):
        value = value.wrapped if value else None
        self.wrapped.TorqueVsAngleAndSpeed = value

    @property
    def torque_vs_time(self) -> '_1493.Vector2DListAccessor':
        """Vector2DListAccessor: 'TorqueVsTime' is the original name of this property."""

        temp = self.wrapped.TorqueVsTime
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @torque_vs_time.setter
    def torque_vs_time(self, value: '_1493.Vector2DListAccessor'):
        value = value.wrapped if value else None
        self.wrapped.TorqueVsTime = value

    @property
    def total_mean_rotor_x_force_over_all_nodes(self) -> 'float':
        """float: 'TotalMeanRotorXForceOverAllNodes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalMeanRotorXForceOverAllNodes
        return temp

    @property
    def total_mean_rotor_y_force_over_all_nodes(self) -> 'float':
        """float: 'TotalMeanRotorYForceOverAllNodes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalMeanRotorYForceOverAllNodes
        return temp

    @property
    def unbalanced_magnetic_pull_stiffness(self) -> 'float':
        """float: 'UnbalancedMagneticPullStiffness' is the original name of this property."""

        temp = self.wrapped.UnbalancedMagneticPullStiffness
        return temp

    @unbalanced_magnetic_pull_stiffness.setter
    def unbalanced_magnetic_pull_stiffness(self, value: 'float'):
        self.wrapped.UnbalancedMagneticPullStiffness = float(value) if value else 0.0

    @property
    def use_engine_idle_speed_control(self) -> 'bool':
        """bool: 'UseEngineIdleSpeedControl' is the original name of this property."""

        temp = self.wrapped.UseEngineIdleSpeedControl
        return temp

    @use_engine_idle_speed_control.setter
    def use_engine_idle_speed_control(self, value: 'bool'):
        self.wrapped.UseEngineIdleSpeedControl = bool(value) if value else False

    @property
    def use_time_dependent_constant_resistance_coefficient(self) -> 'bool':
        """bool: 'UseTimeDependentConstantResistanceCoefficient' is the original name of this property."""

        temp = self.wrapped.UseTimeDependentConstantResistanceCoefficient
        return temp

    @use_time_dependent_constant_resistance_coefficient.setter
    def use_time_dependent_constant_resistance_coefficient(self, value: 'bool'):
        self.wrapped.UseTimeDependentConstantResistanceCoefficient = bool(value) if value else False

    @property
    def use_time_dependent_linear_resistance_coefficient(self) -> 'bool':
        """bool: 'UseTimeDependentLinearResistanceCoefficient' is the original name of this property."""

        temp = self.wrapped.UseTimeDependentLinearResistanceCoefficient
        return temp

    @use_time_dependent_linear_resistance_coefficient.setter
    def use_time_dependent_linear_resistance_coefficient(self, value: 'bool'):
        self.wrapped.UseTimeDependentLinearResistanceCoefficient = bool(value) if value else False

    @property
    def use_time_dependent_quadratic_resistance_coefficient(self) -> 'bool':
        """bool: 'UseTimeDependentQuadraticResistanceCoefficient' is the original name of this property."""

        temp = self.wrapped.UseTimeDependentQuadraticResistanceCoefficient
        return temp

    @use_time_dependent_quadratic_resistance_coefficient.setter
    def use_time_dependent_quadratic_resistance_coefficient(self, value: 'bool'):
        self.wrapped.UseTimeDependentQuadraticResistanceCoefficient = bool(value) if value else False

    @property
    def use_time_dependent_throttle(self) -> 'bool':
        """bool: 'UseTimeDependentThrottle' is the original name of this property."""

        temp = self.wrapped.UseTimeDependentThrottle
        return temp

    @use_time_dependent_throttle.setter
    def use_time_dependent_throttle(self, value: 'bool'):
        self.wrapped.UseTimeDependentThrottle = bool(value) if value else False

    @property
    def vehicle_speed_to_start_idle_control(self) -> 'float':
        """float: 'VehicleSpeedToStartIdleControl' is the original name of this property."""

        temp = self.wrapped.VehicleSpeedToStartIdleControl
        return temp

    @vehicle_speed_to_start_idle_control.setter
    def vehicle_speed_to_start_idle_control(self, value: 'float'):
        self.wrapped.VehicleSpeedToStartIdleControl = float(value) if value else 0.0

    @property
    def vehicle_speed_to_stop_idle_control(self) -> 'float':
        """float: 'VehicleSpeedToStopIdleControl' is the original name of this property."""

        temp = self.wrapped.VehicleSpeedToStopIdleControl
        return temp

    @vehicle_speed_to_stop_idle_control.setter
    def vehicle_speed_to_stop_idle_control(self, value: 'float'):
        self.wrapped.VehicleSpeedToStopIdleControl = float(value) if value else 0.0

    @property
    def wheel_slip_model(self) -> '_5440.WheelSlipType':
        """WheelSlipType: 'WheelSlipModel' is the original name of this property."""

        temp = self.wrapped.WheelSlipModel
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_5440.WheelSlipType)(value) if value is not None else None

    @wheel_slip_model.setter
    def wheel_slip_model(self, value: '_5440.WheelSlipType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.WheelSlipModel = value

    @property
    def wheel_static_to_dynamic_friction_ratio(self) -> 'float':
        """float: 'WheelStaticToDynamicFrictionRatio' is the original name of this property."""

        temp = self.wrapped.WheelStaticToDynamicFrictionRatio
        return temp

    @wheel_static_to_dynamic_friction_ratio.setter
    def wheel_static_to_dynamic_friction_ratio(self, value: 'float'):
        self.wrapped.WheelStaticToDynamicFrictionRatio = float(value) if value else 0.0

    @property
    def wheel_to_vehicle_stiffness(self) -> 'float':
        """float: 'WheelToVehicleStiffness' is the original name of this property."""

        temp = self.wrapped.WheelToVehicleStiffness
        return temp

    @wheel_to_vehicle_stiffness.setter
    def wheel_to_vehicle_stiffness(self, value: 'float'):
        self.wrapped.WheelToVehicleStiffness = float(value) if value else 0.0

    @property
    def coefficient_of_friction_with_ground(self) -> '_96.NonDimensionalInputComponent':
        """NonDimensionalInputComponent: 'CoefficientOfFrictionWithGround' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoefficientOfFrictionWithGround
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design(self) -> '_2412.PowerLoad':
        """PowerLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def engine_idle_speed_control_pid_settings(self) -> '_1536.PIDControlSettings':
        """PIDControlSettings: 'EngineIdleSpeedControlPIDSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EngineIdleSpeedControlPIDSettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pid_control_settings(self) -> '_1536.PIDControlSettings':
        """PIDControlSettings: 'PIDControlSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PIDControlSettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def get_harmonic_load_data_for_import(self) -> '_6785.ElectricMachineHarmonicLoadData':
        """ 'GetHarmonicLoadDataForImport' is the original name of this method.

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.ElectricMachineHarmonicLoadData
        """

        method_result = self.wrapped.GetHarmonicLoadDataForImport()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

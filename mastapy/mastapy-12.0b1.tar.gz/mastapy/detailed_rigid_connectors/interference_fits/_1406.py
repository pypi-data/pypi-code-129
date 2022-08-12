"""_1406.py

InterferenceFitDesign
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.detailed_rigid_connectors.interference_fits import _1404, _1405, _1409
from mastapy._internal.implicit import overridable, enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.detailed_rigid_connectors import _1348
from mastapy._internal.python_net import python_net_import

_INTERFERENCE_FIT_DESIGN = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.InterferenceFits', 'InterferenceFitDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('InterferenceFitDesign',)


class InterferenceFitDesign(_1348.DetailedRigidConnectorDesign):
    """InterferenceFitDesign

    This is a mastapy class.
    """

    TYPE = _INTERFERENCE_FIT_DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'InterferenceFitDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_interference(self) -> 'float':
        """float: 'AssemblyInterference' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyInterference
        return temp

    @property
    def assembly_method(self) -> '_1404.AssemblyMethods':
        """AssemblyMethods: 'AssemblyMethod' is the original name of this property."""

        temp = self.wrapped.AssemblyMethod
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1404.AssemblyMethods)(value) if value is not None else None

    @assembly_method.setter
    def assembly_method(self, value: '_1404.AssemblyMethods'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.AssemblyMethod = value

    @property
    def auxiliary_elasticity_parameter(self) -> 'float':
        """float: 'AuxiliaryElasticityParameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AuxiliaryElasticityParameter
        return temp

    @property
    def average_allowable_axial_force(self) -> 'float':
        """float: 'AverageAllowableAxialForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageAllowableAxialForce
        return temp

    @property
    def average_allowable_torque(self) -> 'float':
        """float: 'AverageAllowableTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageAllowableTorque
        return temp

    @property
    def average_effective_interference(self) -> 'float':
        """float: 'AverageEffectiveInterference' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageEffectiveInterference
        return temp

    @property
    def average_interference(self) -> 'float':
        """float: 'AverageInterference' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageInterference
        return temp

    @property
    def average_joint_pressure(self) -> 'float':
        """float: 'AverageJointPressure' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageJointPressure
        return temp

    @property
    def average_permissible_axial_force(self) -> 'float':
        """float: 'AveragePermissibleAxialForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AveragePermissibleAxialForce
        return temp

    @property
    def average_permissible_torque(self) -> 'float':
        """float: 'AveragePermissibleTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AveragePermissibleTorque
        return temp

    @property
    def average_relative_interference(self) -> 'float':
        """float: 'AverageRelativeInterference' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageRelativeInterference
        return temp

    @property
    def calculation_method(self) -> '_1405.CalculationMethods':
        """CalculationMethods: 'CalculationMethod' is the original name of this property."""

        temp = self.wrapped.CalculationMethod
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1405.CalculationMethods)(value) if value is not None else None

    @calculation_method.setter
    def calculation_method(self, value: '_1405.CalculationMethods'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.CalculationMethod = value

    @property
    def coefficient_of_friction_assembly(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CoefficientOfFrictionAssembly' is the original name of this property."""

        temp = self.wrapped.CoefficientOfFrictionAssembly
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @coefficient_of_friction_assembly.setter
    def coefficient_of_friction_assembly(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CoefficientOfFrictionAssembly = value

    @property
    def coefficient_of_friction_circumferential(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CoefficientOfFrictionCircumferential' is the original name of this property."""

        temp = self.wrapped.CoefficientOfFrictionCircumferential
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @coefficient_of_friction_circumferential.setter
    def coefficient_of_friction_circumferential(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CoefficientOfFrictionCircumferential = value

    @property
    def coefficient_of_friction_longitudinal(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CoefficientOfFrictionLongitudinal' is the original name of this property."""

        temp = self.wrapped.CoefficientOfFrictionLongitudinal
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @coefficient_of_friction_longitudinal.setter
    def coefficient_of_friction_longitudinal(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CoefficientOfFrictionLongitudinal = value

    @property
    def diameter_of_joint(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'DiameterOfJoint' is the original name of this property."""

        temp = self.wrapped.DiameterOfJoint
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @diameter_of_joint.setter
    def diameter_of_joint(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.DiameterOfJoint = value

    @property
    def dimensionless_plasticity_diameter(self) -> 'float':
        """float: 'DimensionlessPlasticityDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DimensionlessPlasticityDiameter
        return temp

    @property
    def insertion_force(self) -> 'float':
        """float: 'InsertionForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InsertionForce
        return temp

    @property
    def joining_play(self) -> 'float':
        """float: 'JoiningPlay' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.JoiningPlay
        return temp

    @property
    def joint_interface_type(self) -> 'enum_with_selected_value.EnumWithSelectedValue_Table4JointInterfaceTypes':
        """enum_with_selected_value.EnumWithSelectedValue_Table4JointInterfaceTypes: 'JointInterfaceType' is the original name of this property."""

        temp = self.wrapped.JointInterfaceType
        value = enum_with_selected_value.EnumWithSelectedValue_Table4JointInterfaceTypes.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @joint_interface_type.setter
    def joint_interface_type(self, value: 'enum_with_selected_value.EnumWithSelectedValue_Table4JointInterfaceTypes.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_Table4JointInterfaceTypes.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.JointInterfaceType = value

    @property
    def maximum_allowable_axial_force(self) -> 'float':
        """float: 'MaximumAllowableAxialForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumAllowableAxialForce
        return temp

    @property
    def maximum_allowable_torque(self) -> 'float':
        """float: 'MaximumAllowableTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumAllowableTorque
        return temp

    @property
    def maximum_assembly_interference(self) -> 'float':
        """float: 'MaximumAssemblyInterference' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumAssemblyInterference
        return temp

    @property
    def maximum_effective_interference(self) -> 'float':
        """float: 'MaximumEffectiveInterference' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumEffectiveInterference
        return temp

    @property
    def maximum_interference(self) -> 'float':
        """float: 'MaximumInterference' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumInterference
        return temp

    @property
    def maximum_joint_pressure(self) -> 'float':
        """float: 'MaximumJointPressure' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumJointPressure
        return temp

    @property
    def maximum_permissible_axial_force(self) -> 'float':
        """float: 'MaximumPermissibleAxialForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumPermissibleAxialForce
        return temp

    @property
    def maximum_permissible_torque(self) -> 'float':
        """float: 'MaximumPermissibleTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumPermissibleTorque
        return temp

    @property
    def maximum_relative_interference(self) -> 'float':
        """float: 'MaximumRelativeInterference' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumRelativeInterference
        return temp

    @property
    def minimum_allowable_axial_force(self) -> 'float':
        """float: 'MinimumAllowableAxialForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumAllowableAxialForce
        return temp

    @property
    def minimum_allowable_torque(self) -> 'float':
        """float: 'MinimumAllowableTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumAllowableTorque
        return temp

    @property
    def minimum_effective_interference(self) -> 'float':
        """float: 'MinimumEffectiveInterference' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumEffectiveInterference
        return temp

    @property
    def minimum_interference(self) -> 'float':
        """float: 'MinimumInterference' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumInterference
        return temp

    @property
    def minimum_joint_pressure(self) -> 'float':
        """float: 'MinimumJointPressure' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumJointPressure
        return temp

    @property
    def minimum_permissible_axial_force(self) -> 'float':
        """float: 'MinimumPermissibleAxialForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumPermissibleAxialForce
        return temp

    @property
    def minimum_permissible_torque(self) -> 'float':
        """float: 'MinimumPermissibleTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumPermissibleTorque
        return temp

    @property
    def minimum_relative_interference(self) -> 'float':
        """float: 'MinimumRelativeInterference' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumRelativeInterference
        return temp

    @property
    def permissible_dimensionless_plasticity_diameter(self) -> 'float':
        """float: 'PermissibleDimensionlessPlasticityDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermissibleDimensionlessPlasticityDiameter
        return temp

    @property
    def proportion_of_outer_plastically_stressed(self) -> 'float':
        """float: 'ProportionOfOuterPlasticallyStressed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProportionOfOuterPlasticallyStressed
        return temp

    @property
    def ratio_of_joint_length_to_joint_diameter(self) -> 'float':
        """float: 'RatioOfJointLengthToJointDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatioOfJointLengthToJointDiameter
        return temp

    @property
    def required_assembly_temperature_of_the_outer_part(self) -> 'float':
        """float: 'RequiredAssemblyTemperatureOfTheOuterPart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RequiredAssemblyTemperatureOfTheOuterPart
        return temp

    @property
    def room_temperature_during_assembly(self) -> 'float':
        """float: 'RoomTemperatureDuringAssembly' is the original name of this property."""

        temp = self.wrapped.RoomTemperatureDuringAssembly
        return temp

    @room_temperature_during_assembly.setter
    def room_temperature_during_assembly(self, value: 'float'):
        self.wrapped.RoomTemperatureDuringAssembly = float(value) if value else 0.0

    @property
    def specified_joint_pressure(self) -> 'float':
        """float: 'SpecifiedJointPressure' is the original name of this property."""

        temp = self.wrapped.SpecifiedJointPressure
        return temp

    @specified_joint_pressure.setter
    def specified_joint_pressure(self, value: 'float'):
        self.wrapped.SpecifiedJointPressure = float(value) if value else 0.0

    @property
    def temperature_of_inner_part_during_assembly(self) -> 'float':
        """float: 'TemperatureOfInnerPartDuringAssembly' is the original name of this property."""

        temp = self.wrapped.TemperatureOfInnerPartDuringAssembly
        return temp

    @temperature_of_inner_part_during_assembly.setter
    def temperature_of_inner_part_during_assembly(self, value: 'float'):
        self.wrapped.TemperatureOfInnerPartDuringAssembly = float(value) if value else 0.0

"""_1143.py

ConicalGearMeshDesign
"""


from mastapy.gears.gear_designs.bevel import _1175, _1172, _1176
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.gear_designs import _940
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Conical', 'ConicalGearMeshDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearMeshDesign',)


class ConicalGearMeshDesign(_940.GearMeshDesign):
    """ConicalGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalGearMeshDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def driven_machine_characteristic(self) -> '_1175.MachineCharacteristicAGMAKlingelnberg':
        """MachineCharacteristicAGMAKlingelnberg: 'DrivenMachineCharacteristic' is the original name of this property."""

        temp = self.wrapped.DrivenMachineCharacteristic
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1175.MachineCharacteristicAGMAKlingelnberg)(value) if value is not None else None

    @driven_machine_characteristic.setter
    def driven_machine_characteristic(self, value: '_1175.MachineCharacteristicAGMAKlingelnberg'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.DrivenMachineCharacteristic = value

    @property
    def driven_machine_characteristic_gleason(self) -> '_1172.DrivenMachineCharacteristicGleason':
        """DrivenMachineCharacteristicGleason: 'DrivenMachineCharacteristicGleason' is the original name of this property."""

        temp = self.wrapped.DrivenMachineCharacteristicGleason
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1172.DrivenMachineCharacteristicGleason)(value) if value is not None else None

    @driven_machine_characteristic_gleason.setter
    def driven_machine_characteristic_gleason(self, value: '_1172.DrivenMachineCharacteristicGleason'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.DrivenMachineCharacteristicGleason = value

    @property
    def maximum_normal_backlash(self) -> 'float':
        """float: 'MaximumNormalBacklash' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalBacklash
        return temp

    @property
    def minimum_normal_backlash(self) -> 'float':
        """float: 'MinimumNormalBacklash' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumNormalBacklash
        return temp

    @property
    def overload_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'OverloadFactor' is the original name of this property."""

        temp = self.wrapped.OverloadFactor
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @overload_factor.setter
    def overload_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.OverloadFactor = value

    @property
    def pinion_full_circle_edge_radius(self) -> 'float':
        """float: 'PinionFullCircleEdgeRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionFullCircleEdgeRadius
        return temp

    @property
    def prime_mover_characteristic(self) -> '_1175.MachineCharacteristicAGMAKlingelnberg':
        """MachineCharacteristicAGMAKlingelnberg: 'PrimeMoverCharacteristic' is the original name of this property."""

        temp = self.wrapped.PrimeMoverCharacteristic
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1175.MachineCharacteristicAGMAKlingelnberg)(value) if value is not None else None

    @prime_mover_characteristic.setter
    def prime_mover_characteristic(self, value: '_1175.MachineCharacteristicAGMAKlingelnberg'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.PrimeMoverCharacteristic = value

    @property
    def prime_mover_characteristic_gleason(self) -> '_1176.PrimeMoverCharacteristicGleason':
        """PrimeMoverCharacteristicGleason: 'PrimeMoverCharacteristicGleason' is the original name of this property."""

        temp = self.wrapped.PrimeMoverCharacteristicGleason
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1176.PrimeMoverCharacteristicGleason)(value) if value is not None else None

    @prime_mover_characteristic_gleason.setter
    def prime_mover_characteristic_gleason(self, value: '_1176.PrimeMoverCharacteristicGleason'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.PrimeMoverCharacteristicGleason = value

    @property
    def shaft_angle(self) -> 'float':
        """float: 'ShaftAngle' is the original name of this property."""

        temp = self.wrapped.ShaftAngle
        return temp

    @shaft_angle.setter
    def shaft_angle(self, value: 'float'):
        self.wrapped.ShaftAngle = float(value) if value else 0.0

    @property
    def specified_backlash_range_max(self) -> 'float':
        """float: 'SpecifiedBacklashRangeMax' is the original name of this property."""

        temp = self.wrapped.SpecifiedBacklashRangeMax
        return temp

    @specified_backlash_range_max.setter
    def specified_backlash_range_max(self, value: 'float'):
        self.wrapped.SpecifiedBacklashRangeMax = float(value) if value else 0.0

    @property
    def specified_backlash_range_min(self) -> 'float':
        """float: 'SpecifiedBacklashRangeMin' is the original name of this property."""

        temp = self.wrapped.SpecifiedBacklashRangeMin
        return temp

    @specified_backlash_range_min.setter
    def specified_backlash_range_min(self, value: 'float'):
        self.wrapped.SpecifiedBacklashRangeMin = float(value) if value else 0.0

    @property
    def specify_backlash(self) -> 'bool':
        """bool: 'SpecifyBacklash' is the original name of this property."""

        temp = self.wrapped.SpecifyBacklash
        return temp

    @specify_backlash.setter
    def specify_backlash(self, value: 'bool'):
        self.wrapped.SpecifyBacklash = bool(value) if value else False

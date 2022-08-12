"""_1254.py

InteriorPermanentMagnetAndSynchronousReluctanceRotor
"""


from typing import List

from mastapy.electric_machines import (
    _1252, _1273, _1238, _1265,
    _1284, _1285, _1267
)
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.python_net import python_net_import

_INTERIOR_PERMANENT_MAGNET_AND_SYNCHRONOUS_RELUCTANCE_ROTOR = python_net_import('SMT.MastaAPI.ElectricMachines', 'InteriorPermanentMagnetAndSynchronousReluctanceRotor')


__docformat__ = 'restructuredtext en'
__all__ = ('InteriorPermanentMagnetAndSynchronousReluctanceRotor',)


class InteriorPermanentMagnetAndSynchronousReluctanceRotor(_1267.PermanentMagnetRotor):
    """InteriorPermanentMagnetAndSynchronousReluctanceRotor

    This is a mastapy class.
    """

    TYPE = _INTERIOR_PERMANENT_MAGNET_AND_SYNCHRONOUS_RELUCTANCE_ROTOR

    __hash__ = None

    def __init__(self, instance_to_wrap: 'InteriorPermanentMagnetAndSynchronousReluctanceRotor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def flux_barrier_style(self) -> '_1252.FluxBarrierStyle':
        """FluxBarrierStyle: 'FluxBarrierStyle' is the original name of this property."""

        temp = self.wrapped.FluxBarrierStyle
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1252.FluxBarrierStyle)(value) if value is not None else None

    @flux_barrier_style.setter
    def flux_barrier_style(self, value: '_1252.FluxBarrierStyle'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.FluxBarrierStyle = value

    @property
    def number_of_cooling_duct_layers(self) -> 'int':
        """int: 'NumberOfCoolingDuctLayers' is the original name of this property."""

        temp = self.wrapped.NumberOfCoolingDuctLayers
        return temp

    @number_of_cooling_duct_layers.setter
    def number_of_cooling_duct_layers(self, value: 'int'):
        self.wrapped.NumberOfCoolingDuctLayers = int(value) if value else 0

    @property
    def number_of_magnet_flux_barrier_layers(self) -> 'int':
        """int: 'NumberOfMagnetFluxBarrierLayers' is the original name of this property."""

        temp = self.wrapped.NumberOfMagnetFluxBarrierLayers
        return temp

    @number_of_magnet_flux_barrier_layers.setter
    def number_of_magnet_flux_barrier_layers(self, value: 'int'):
        self.wrapped.NumberOfMagnetFluxBarrierLayers = int(value) if value else 0

    @property
    def number_of_notch_specifications(self) -> 'int':
        """int: 'NumberOfNotchSpecifications' is the original name of this property."""

        temp = self.wrapped.NumberOfNotchSpecifications
        return temp

    @number_of_notch_specifications.setter
    def number_of_notch_specifications(self, value: 'int'):
        self.wrapped.NumberOfNotchSpecifications = int(value) if value else 0

    @property
    def rotor_type(self) -> '_1273.RotorType':
        """RotorType: 'RotorType' is the original name of this property."""

        temp = self.wrapped.RotorType
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1273.RotorType)(value) if value is not None else None

    @rotor_type.setter
    def rotor_type(self, value: '_1273.RotorType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.RotorType = value

    @property
    def cooling_duct_layers(self) -> 'List[_1238.CoolingDuctLayerSpecification]':
        """List[CoolingDuctLayerSpecification]: 'CoolingDuctLayers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoolingDuctLayers
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def notch_specifications(self) -> 'List[_1265.NotchSpecification]':
        """List[NotchSpecification]: 'NotchSpecifications' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NotchSpecifications
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def u_shape_layers(self) -> 'List[_1284.UShapedLayerSpecification]':
        """List[UShapedLayerSpecification]: 'UShapeLayers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UShapeLayers
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def v_shape_magnet_layers(self) -> 'List[_1285.VShapedMagnetLayerSpecification]':
        """List[VShapedMagnetLayerSpecification]: 'VShapeMagnetLayers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VShapeMagnetLayers
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

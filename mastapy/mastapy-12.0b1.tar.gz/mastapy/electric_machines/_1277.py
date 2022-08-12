"""_1277.py

StatorRotorMaterial
"""


from typing import List

from mastapy.electric_machines import _1256, _1241
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.materials import _239, _260
from mastapy.math_utility import (
    _1483, _1467, _1482, _1484,
    _1489, _1494
)
from mastapy._internal.cast_exception import CastException
from mastapy._math.matrix_4x4 import Matrix4x4
from mastapy._internal.python_net import python_net_import
from mastapy.utility import _1551

_ARRAY = python_net_import('System', 'Array')
_STATOR_ROTOR_MATERIAL = python_net_import('SMT.MastaAPI.ElectricMachines', 'StatorRotorMaterial')


__docformat__ = 'restructuredtext en'
__all__ = ('StatorRotorMaterial',)


class StatorRotorMaterial(_260.Material):
    """StatorRotorMaterial

    This is a mastapy class.
    """

    TYPE = _STATOR_ROTOR_MATERIAL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StatorRotorMaterial.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def coefficient_specification_method(self) -> '_1256.IronLossCoefficientSpecificationMethod':
        """IronLossCoefficientSpecificationMethod: 'CoefficientSpecificationMethod' is the original name of this property."""

        temp = self.wrapped.CoefficientSpecificationMethod
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1256.IronLossCoefficientSpecificationMethod)(value) if value is not None else None

    @coefficient_specification_method.setter
    def coefficient_specification_method(self, value: '_1256.IronLossCoefficientSpecificationMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.CoefficientSpecificationMethod = value

    @property
    def electrical_resistivity(self) -> 'float':
        """float: 'ElectricalResistivity' is the original name of this property."""

        temp = self.wrapped.ElectricalResistivity
        return temp

    @electrical_resistivity.setter
    def electrical_resistivity(self, value: 'float'):
        self.wrapped.ElectricalResistivity = float(value) if value else 0.0

    @property
    def lamination_thickness(self) -> 'float':
        """float: 'LaminationThickness' is the original name of this property."""

        temp = self.wrapped.LaminationThickness
        return temp

    @lamination_thickness.setter
    def lamination_thickness(self, value: 'float'):
        self.wrapped.LaminationThickness = float(value) if value else 0.0

    @property
    def stacking_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'StackingFactor' is the original name of this property."""

        temp = self.wrapped.StackingFactor
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @stacking_factor.setter
    def stacking_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.StackingFactor = value

    @property
    def bh_curve_specification(self) -> '_239.BHCurveSpecification':
        """BHCurveSpecification: 'BHCurveSpecification' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BHCurveSpecification
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def core_loss_coefficients(self) -> '_1241.CoreLossCoefficients':
        """CoreLossCoefficients: 'CoreLossCoefficients' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoreLossCoefficients
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def loss_curve_data(self) -> '_1483.RealMatrix':
        """RealMatrix: 'LossCurveData' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LossCurveData
        if _1483.RealMatrix.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast loss_curve_data to RealMatrix. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def set_loss_curve_data(self, frequencies: 'List[float]', flux_densities: 'List[float]', loss: 'List[float]'):
        """ 'SetLossCurveData' is the original name of this method.

        Args:
            frequencies (List[float])
            flux_densities (List[float])
            loss (List[float])
        """

        frequencies = conversion.mp_to_pn_array_float(frequencies)
        flux_densities = conversion.mp_to_pn_array_float(flux_densities)
        loss = conversion.mp_to_pn_array_float(loss)
        self.wrapped.SetLossCurveData(frequencies, flux_densities, loss)

    def try_update_coefficients_from_loss_curve_data(self) -> '_1551.MethodOutcome':
        """ 'TryUpdateCoefficientsFromLossCurveData' is the original name of this method.

        Returns:
            mastapy.utility.MethodOutcome
        """

        method_result = self.wrapped.TryUpdateCoefficientsFromLossCurveData()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

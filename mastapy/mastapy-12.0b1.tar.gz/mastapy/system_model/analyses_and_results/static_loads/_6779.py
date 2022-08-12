"""_6779.py

CylindricalGearSetLoadCase
"""


from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears import _310
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.materials.efficiency import _285
from mastapy.system_model.analyses_and_results.static_loads import (
    _6855, _6775, _6777, _6778,
    _6809
)
from mastapy.system_model.part_model.gears import _2465, _2481
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.cylindrical import _1049
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1097
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CylindricalGearSetLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetLoadCase',)


class CylindricalGearSetLoadCase(_6809.GearSetLoadCase):
    """CylindricalGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def boost_pressure(self) -> 'float':
        """float: 'BoostPressure' is the original name of this property."""

        temp = self.wrapped.BoostPressure
        return temp

    @boost_pressure.setter
    def boost_pressure(self, value: 'float'):
        self.wrapped.BoostPressure = float(value) if value else 0.0

    @property
    def coefficient_of_friction_calculation_method(self) -> '_310.CoefficientOfFrictionCalculationMethod':
        """CoefficientOfFrictionCalculationMethod: 'CoefficientOfFrictionCalculationMethod' is the original name of this property."""

        temp = self.wrapped.CoefficientOfFrictionCalculationMethod
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_310.CoefficientOfFrictionCalculationMethod)(value) if value is not None else None

    @coefficient_of_friction_calculation_method.setter
    def coefficient_of_friction_calculation_method(self, value: '_310.CoefficientOfFrictionCalculationMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.CoefficientOfFrictionCalculationMethod = value

    @property
    def dynamic_load_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'DynamicLoadFactor' is the original name of this property."""

        temp = self.wrapped.DynamicLoadFactor
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @dynamic_load_factor.setter
    def dynamic_load_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.DynamicLoadFactor = value

    @property
    def efficiency_rating_method(self) -> 'overridable.Overridable_EfficiencyRatingMethod':
        """overridable.Overridable_EfficiencyRatingMethod: 'EfficiencyRatingMethod' is the original name of this property."""

        temp = self.wrapped.EfficiencyRatingMethod
        value = overridable.Overridable_EfficiencyRatingMethod.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @efficiency_rating_method.setter
    def efficiency_rating_method(self, value: 'overridable.Overridable_EfficiencyRatingMethod.implicit_type()'):
        wrapper_type = overridable.Overridable_EfficiencyRatingMethod.wrapper_type()
        enclosed_type = overridable.Overridable_EfficiencyRatingMethod.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value is not None else None, is_overridden)
        self.wrapped.EfficiencyRatingMethod = value

    @property
    def override_micro_geometry(self) -> 'bool':
        """bool: 'OverrideMicroGeometry' is the original name of this property."""

        temp = self.wrapped.OverrideMicroGeometry
        return temp

    @override_micro_geometry.setter
    def override_micro_geometry(self, value: 'bool'):
        self.wrapped.OverrideMicroGeometry = bool(value) if value else False

    @property
    def reset_micro_geometry(self) -> '_6855.ResetMicroGeometryOptions':
        """ResetMicroGeometryOptions: 'ResetMicroGeometry' is the original name of this property."""

        temp = self.wrapped.ResetMicroGeometry
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_6855.ResetMicroGeometryOptions)(value) if value is not None else None

    @reset_micro_geometry.setter
    def reset_micro_geometry(self, value: '_6855.ResetMicroGeometryOptions'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ResetMicroGeometry = value

    @property
    def use_design_coefficient_of_friction_calculation_method(self) -> 'bool':
        """bool: 'UseDesignCoefficientOfFrictionCalculationMethod' is the original name of this property."""

        temp = self.wrapped.UseDesignCoefficientOfFrictionCalculationMethod
        return temp

    @use_design_coefficient_of_friction_calculation_method.setter
    def use_design_coefficient_of_friction_calculation_method(self, value: 'bool'):
        self.wrapped.UseDesignCoefficientOfFrictionCalculationMethod = bool(value) if value else False

    @property
    def use_design_default_ltca_settings(self) -> 'bool':
        """bool: 'UseDesignDefaultLTCASettings' is the original name of this property."""

        temp = self.wrapped.UseDesignDefaultLTCASettings
        return temp

    @use_design_default_ltca_settings.setter
    def use_design_default_ltca_settings(self, value: 'bool'):
        self.wrapped.UseDesignDefaultLTCASettings = bool(value) if value else False

    @property
    def assembly_design(self) -> '_2465.CylindricalGearSet':
        """CylindricalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        if _2465.CylindricalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to CylindricalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ltca(self) -> '_1049.LTCALoadCaseModifiableSettings':
        """LTCALoadCaseModifiableSettings: 'LTCA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LTCA
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def overridden_micro_geometry(self) -> '_1097.CylindricalGearSetMicroGeometry':
        """CylindricalGearSetMicroGeometry: 'OverriddenMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OverriddenMicroGeometry
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gears(self) -> 'List[_6775.CylindricalGearLoadCase]':
        """List[CylindricalGearLoadCase]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_gears_load_case(self) -> 'List[_6775.CylindricalGearLoadCase]':
        """List[CylindricalGearLoadCase]: 'CylindricalGearsLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearsLoadCase
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_meshes_load_case(self) -> 'List[_6777.CylindricalGearMeshLoadCase]':
        """List[CylindricalGearMeshLoadCase]: 'CylindricalMeshesLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalMeshesLoadCase
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def get_harmonic_load_data_for_import(self) -> '_6778.CylindricalGearSetHarmonicLoadData':
        """ 'GetHarmonicLoadDataForImport' is the original name of this method.

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetHarmonicLoadData
        """

        method_result = self.wrapped.GetHarmonicLoadDataForImport()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

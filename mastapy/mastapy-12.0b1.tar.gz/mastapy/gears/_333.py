"""_333.py

PocketingPowerLossCoefficients
"""


from typing import List

from mastapy._internal.implicit import enum_with_selected_value
from mastapy.math_utility import _1468
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import enum_with_selected_value_runtime, conversion, constructor
from mastapy.math_utility.measured_data import _1525
from mastapy.gears import _337
from mastapy.utility.databases import _1785
from mastapy._internal.python_net import python_net_import

_POCKETING_POWER_LOSS_COEFFICIENTS = python_net_import('SMT.MastaAPI.Gears', 'PocketingPowerLossCoefficients')


__docformat__ = 'restructuredtext en'
__all__ = ('PocketingPowerLossCoefficients',)


class PocketingPowerLossCoefficients(_1785.NamedDatabaseItem):
    """PocketingPowerLossCoefficients

    This is a mastapy class.
    """

    TYPE = _POCKETING_POWER_LOSS_COEFFICIENTS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PocketingPowerLossCoefficients.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def extrapolation_options(self) -> 'enum_with_selected_value.EnumWithSelectedValue_ExtrapolationOptions':
        """enum_with_selected_value.EnumWithSelectedValue_ExtrapolationOptions: 'ExtrapolationOptions' is the original name of this property."""

        temp = self.wrapped.ExtrapolationOptions
        value = enum_with_selected_value.EnumWithSelectedValue_ExtrapolationOptions.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @extrapolation_options.setter
    def extrapolation_options(self, value: 'enum_with_selected_value.EnumWithSelectedValue_ExtrapolationOptions.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_ExtrapolationOptions.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.ExtrapolationOptions = value

    @property
    def intercept_of_linear_equation_defining_the_effect_of_gear_face_width(self) -> 'float':
        """float: 'InterceptOfLinearEquationDefiningTheEffectOfGearFaceWidth' is the original name of this property."""

        temp = self.wrapped.InterceptOfLinearEquationDefiningTheEffectOfGearFaceWidth
        return temp

    @intercept_of_linear_equation_defining_the_effect_of_gear_face_width.setter
    def intercept_of_linear_equation_defining_the_effect_of_gear_face_width(self, value: 'float'):
        self.wrapped.InterceptOfLinearEquationDefiningTheEffectOfGearFaceWidth = float(value) if value else 0.0

    @property
    def intercept_of_linear_equation_defining_the_effect_of_helix_angle(self) -> 'float':
        """float: 'InterceptOfLinearEquationDefiningTheEffectOfHelixAngle' is the original name of this property."""

        temp = self.wrapped.InterceptOfLinearEquationDefiningTheEffectOfHelixAngle
        return temp

    @intercept_of_linear_equation_defining_the_effect_of_helix_angle.setter
    def intercept_of_linear_equation_defining_the_effect_of_helix_angle(self, value: 'float'):
        self.wrapped.InterceptOfLinearEquationDefiningTheEffectOfHelixAngle = float(value) if value else 0.0

    @property
    def lower_bound_for_oil_kinematic_viscosity(self) -> 'float':
        """float: 'LowerBoundForOilKinematicViscosity' is the original name of this property."""

        temp = self.wrapped.LowerBoundForOilKinematicViscosity
        return temp

    @lower_bound_for_oil_kinematic_viscosity.setter
    def lower_bound_for_oil_kinematic_viscosity(self, value: 'float'):
        self.wrapped.LowerBoundForOilKinematicViscosity = float(value) if value else 0.0

    @property
    def raw_pocketing_power_loss_lookup_table(self) -> '_1525.GriddedSurfaceAccessor':
        """GriddedSurfaceAccessor: 'RawPocketingPowerLossLookupTable' is the original name of this property."""

        temp = self.wrapped.RawPocketingPowerLossLookupTable
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @raw_pocketing_power_loss_lookup_table.setter
    def raw_pocketing_power_loss_lookup_table(self, value: '_1525.GriddedSurfaceAccessor'):
        value = value.wrapped if value else None
        self.wrapped.RawPocketingPowerLossLookupTable = value

    @property
    def reference_gear_outer_diameter(self) -> 'float':
        """float: 'ReferenceGearOuterDiameter' is the original name of this property."""

        temp = self.wrapped.ReferenceGearOuterDiameter
        return temp

    @reference_gear_outer_diameter.setter
    def reference_gear_outer_diameter(self, value: 'float'):
        self.wrapped.ReferenceGearOuterDiameter = float(value) if value else 0.0

    @property
    def reference_gear_pocket_dimension(self) -> 'float':
        """float: 'ReferenceGearPocketDimension' is the original name of this property."""

        temp = self.wrapped.ReferenceGearPocketDimension
        return temp

    @reference_gear_pocket_dimension.setter
    def reference_gear_pocket_dimension(self, value: 'float'):
        self.wrapped.ReferenceGearPocketDimension = float(value) if value else 0.0

    @property
    def slope_of_linear_equation_defining_the_effect_of_gear_face_width(self) -> 'float':
        """float: 'SlopeOfLinearEquationDefiningTheEffectOfGearFaceWidth' is the original name of this property."""

        temp = self.wrapped.SlopeOfLinearEquationDefiningTheEffectOfGearFaceWidth
        return temp

    @slope_of_linear_equation_defining_the_effect_of_gear_face_width.setter
    def slope_of_linear_equation_defining_the_effect_of_gear_face_width(self, value: 'float'):
        self.wrapped.SlopeOfLinearEquationDefiningTheEffectOfGearFaceWidth = float(value) if value else 0.0

    @property
    def slope_of_linear_equation_defining_the_effect_of_helix_angle(self) -> 'float':
        """float: 'SlopeOfLinearEquationDefiningTheEffectOfHelixAngle' is the original name of this property."""

        temp = self.wrapped.SlopeOfLinearEquationDefiningTheEffectOfHelixAngle
        return temp

    @slope_of_linear_equation_defining_the_effect_of_helix_angle.setter
    def slope_of_linear_equation_defining_the_effect_of_helix_angle(self, value: 'float'):
        self.wrapped.SlopeOfLinearEquationDefiningTheEffectOfHelixAngle = float(value) if value else 0.0

    @property
    def upper_bound_for_oil_kinematic_viscosity(self) -> 'float':
        """float: 'UpperBoundForOilKinematicViscosity' is the original name of this property."""

        temp = self.wrapped.UpperBoundForOilKinematicViscosity
        return temp

    @upper_bound_for_oil_kinematic_viscosity.setter
    def upper_bound_for_oil_kinematic_viscosity(self, value: 'float'):
        self.wrapped.UpperBoundForOilKinematicViscosity = float(value) if value else 0.0

    @property
    def specifications_for_the_effect_of_oil_kinematic_viscosity(self) -> 'List[_337.SpecificationForTheEffectOfOilKinematicViscosity]':
        """List[SpecificationForTheEffectOfOilKinematicViscosity]: 'SpecificationsForTheEffectOfOilKinematicViscosity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpecificationsForTheEffectOfOilKinematicViscosity
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

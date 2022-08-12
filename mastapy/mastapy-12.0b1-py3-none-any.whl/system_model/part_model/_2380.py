"""_2380.py

Bearing
"""


from typing import List, Optional

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import overridable, enum_with_selected_value
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.bearings.tolerances import (
    _1852, _1853, _1862, _1856,
    _1869, _1855, _1866, _1861,
    _1871, _1873
)
from mastapy.bearings import (
    _1822, _1835, _1826, _1818
)
from mastapy.materials.efficiency import _283
from mastapy.utility.report import _1744
from mastapy._internal.python_net import python_net_import
from mastapy.bearings.bearing_results import _1908, _1891, _1909
from mastapy.system_model.part_model import (
    _2379, _2413, _2381, _2385,
    _2387
)
from mastapy.bearings.bearing_designs import (
    _2073, _2074, _2075, _2076,
    _2077
)
from mastapy._internal.cast_exception import CastException
from mastapy.bearings.bearing_designs.rolling import (
    _2078, _2079, _2080, _2081,
    _2082, _2083, _2085, _2091,
    _2092, _2093, _2097, _2102,
    _2103, _2104, _2105, _2108,
    _2109, _2112, _2113, _2114,
    _2115, _2116, _2117
)
from mastapy.bearings.bearing_designs.fluid_film import (
    _2130, _2132, _2134, _2136,
    _2137, _2138
)
from mastapy.bearings.bearing_designs.concept import _2140, _2141, _2142
from mastapy.math_utility.measured_vectors import _1523
from mastapy.bearings.bearing_results.rolling import _2014
from mastapy.materials import _258
from mastapy.system_model.part_model.shaft_model import _2422

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_ARRAY = python_net_import('System', 'Array')
_BEARING = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Bearing')


__docformat__ = 'restructuredtext en'
__all__ = ('Bearing',)


class Bearing(_2387.Connector):
    """Bearing

    This is a mastapy class.
    """

    TYPE = _BEARING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'Bearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_displacement_preload(self) -> 'float':
        """float: 'AxialDisplacementPreload' is the original name of this property."""

        temp = self.wrapped.AxialDisplacementPreload
        return temp

    @axial_displacement_preload.setter
    def axial_displacement_preload(self, value: 'float'):
        self.wrapped.AxialDisplacementPreload = float(value) if value else 0.0

    @property
    def axial_force_preload(self) -> 'float':
        """float: 'AxialForcePreload' is the original name of this property."""

        temp = self.wrapped.AxialForcePreload
        return temp

    @axial_force_preload.setter
    def axial_force_preload(self, value: 'float'):
        self.wrapped.AxialForcePreload = float(value) if value else 0.0

    @property
    def axial_internal_clearance(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'AxialInternalClearance' is the original name of this property."""

        temp = self.wrapped.AxialInternalClearance
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @axial_internal_clearance.setter
    def axial_internal_clearance(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.AxialInternalClearance = value

    @property
    def axial_stiffness_at_mounting_points(self) -> 'float':
        """float: 'AxialStiffnessAtMountingPoints' is the original name of this property."""

        temp = self.wrapped.AxialStiffnessAtMountingPoints
        return temp

    @axial_stiffness_at_mounting_points.setter
    def axial_stiffness_at_mounting_points(self, value: 'float'):
        self.wrapped.AxialStiffnessAtMountingPoints = float(value) if value else 0.0

    @property
    def bearing_life_adjustment_factor_for_operating_conditions(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'BearingLifeAdjustmentFactorForOperatingConditions' is the original name of this property."""

        temp = self.wrapped.BearingLifeAdjustmentFactorForOperatingConditions
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @bearing_life_adjustment_factor_for_operating_conditions.setter
    def bearing_life_adjustment_factor_for_operating_conditions(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.BearingLifeAdjustmentFactorForOperatingConditions = value

    @property
    def bearing_life_adjustment_factor_for_special_bearing_properties(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'BearingLifeAdjustmentFactorForSpecialBearingProperties' is the original name of this property."""

        temp = self.wrapped.BearingLifeAdjustmentFactorForSpecialBearingProperties
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @bearing_life_adjustment_factor_for_special_bearing_properties.setter
    def bearing_life_adjustment_factor_for_special_bearing_properties(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.BearingLifeAdjustmentFactorForSpecialBearingProperties = value

    @property
    def bearing_life_modification_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'BearingLifeModificationFactor' is the original name of this property."""

        temp = self.wrapped.BearingLifeModificationFactor
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @bearing_life_modification_factor.setter
    def bearing_life_modification_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.BearingLifeModificationFactor = value

    @property
    def bearing_tolerance_class(self) -> 'enum_with_selected_value.EnumWithSelectedValue_BearingToleranceClass':
        """enum_with_selected_value.EnumWithSelectedValue_BearingToleranceClass: 'BearingToleranceClass' is the original name of this property."""

        temp = self.wrapped.BearingToleranceClass
        value = enum_with_selected_value.EnumWithSelectedValue_BearingToleranceClass.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @bearing_tolerance_class.setter
    def bearing_tolerance_class(self, value: 'enum_with_selected_value.EnumWithSelectedValue_BearingToleranceClass.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_BearingToleranceClass.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.BearingToleranceClass = value

    @property
    def bearing_tolerance_definition(self) -> '_1853.BearingToleranceDefinitionOptions':
        """BearingToleranceDefinitionOptions: 'BearingToleranceDefinition' is the original name of this property."""

        temp = self.wrapped.BearingToleranceDefinition
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1853.BearingToleranceDefinitionOptions)(value) if value is not None else None

    @bearing_tolerance_definition.setter
    def bearing_tolerance_definition(self, value: '_1853.BearingToleranceDefinitionOptions'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.BearingToleranceDefinition = value

    @property
    def coefficient_of_friction(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'CoefficientOfFriction' is the original name of this property."""

        temp = self.wrapped.CoefficientOfFriction
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @coefficient_of_friction.setter
    def coefficient_of_friction(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.CoefficientOfFriction = value

    @property
    def damping_options(self) -> '_1822.BearingDampingMatrixOption':
        """BearingDampingMatrixOption: 'DampingOptions' is the original name of this property."""

        temp = self.wrapped.DampingOptions
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1822.BearingDampingMatrixOption)(value) if value is not None else None

    @damping_options.setter
    def damping_options(self, value: '_1822.BearingDampingMatrixOption'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.DampingOptions = value

    @property
    def diameter_of_contact_on_inner_race_at_nominal_contact_angle(self) -> 'float':
        """float: 'DiameterOfContactOnInnerRaceAtNominalContactAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DiameterOfContactOnInnerRaceAtNominalContactAngle
        return temp

    @property
    def diameter_of_contact_on_left_race(self) -> 'float':
        """float: 'DiameterOfContactOnLeftRace' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DiameterOfContactOnLeftRace
        return temp

    @property
    def diameter_of_contact_on_outer_race_at_nominal_contact_angle(self) -> 'float':
        """float: 'DiameterOfContactOnOuterRaceAtNominalContactAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DiameterOfContactOnOuterRaceAtNominalContactAngle
        return temp

    @property
    def diameter_of_contact_on_right_race(self) -> 'float':
        """float: 'DiameterOfContactOnRightRace' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DiameterOfContactOnRightRace
        return temp

    @property
    def difference_between_inner_diameter_and_diameter_of_connected_component_at_inner_connection(self) -> 'float':
        """float: 'DifferenceBetweenInnerDiameterAndDiameterOfConnectedComponentAtInnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DifferenceBetweenInnerDiameterAndDiameterOfConnectedComponentAtInnerConnection
        return temp

    @property
    def difference_between_outer_diameter_and_diameter_of_connected_component_at_outer_connection(self) -> 'float':
        """float: 'DifferenceBetweenOuterDiameterAndDiameterOfConnectedComponentAtOuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DifferenceBetweenOuterDiameterAndDiameterOfConnectedComponentAtOuterConnection
        return temp

    @property
    def efficiency_rating_method(self) -> 'overridable.Overridable_BearingEfficiencyRatingMethod':
        """overridable.Overridable_BearingEfficiencyRatingMethod: 'EfficiencyRatingMethod' is the original name of this property."""

        temp = self.wrapped.EfficiencyRatingMethod
        value = overridable.Overridable_BearingEfficiencyRatingMethod.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @efficiency_rating_method.setter
    def efficiency_rating_method(self, value: 'overridable.Overridable_BearingEfficiencyRatingMethod.implicit_type()'):
        wrapper_type = overridable.Overridable_BearingEfficiencyRatingMethod.wrapper_type()
        enclosed_type = overridable.Overridable_BearingEfficiencyRatingMethod.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value is not None else None, is_overridden)
        self.wrapped.EfficiencyRatingMethod = value

    @property
    def first_element_angle(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'FirstElementAngle' is the original name of this property."""

        temp = self.wrapped.FirstElementAngle
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @first_element_angle.setter
    def first_element_angle(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.FirstElementAngle = value

    @property
    def has_radial_mounting_clearance(self) -> 'bool':
        """bool: 'HasRadialMountingClearance' is the original name of this property."""

        temp = self.wrapped.HasRadialMountingClearance
        return temp

    @has_radial_mounting_clearance.setter
    def has_radial_mounting_clearance(self, value: 'bool'):
        self.wrapped.HasRadialMountingClearance = bool(value) if value else False

    @property
    def inner_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'InnerDiameter' is the original name of this property."""

        temp = self.wrapped.InnerDiameter
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @inner_diameter.setter
    def inner_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.InnerDiameter = value

    @property
    def inner_fitting_chart(self) -> '_1744.LegacyChartDefinition':
        """LegacyChartDefinition: 'InnerFittingChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerFittingChart
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_node_position_from_centre(self) -> 'float':
        """float: 'InnerNodePositionFromCentre' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerNodePositionFromCentre
        return temp

    @property
    def is_internal_clearance_adjusted_after_fitting(self) -> 'overridable.Overridable_bool':
        """overridable.Overridable_bool: 'IsInternalClearanceAdjustedAfterFitting' is the original name of this property."""

        temp = self.wrapped.IsInternalClearanceAdjustedAfterFitting
        return constructor.new_from_mastapy_type(overridable.Overridable_bool)(temp) if temp is not None else None

    @is_internal_clearance_adjusted_after_fitting.setter
    def is_internal_clearance_adjusted_after_fitting(self, value: 'overridable.Overridable_bool.implicit_type()'):
        wrapper_type = overridable.Overridable_bool.wrapper_type()
        enclosed_type = overridable.Overridable_bool.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else False, is_overridden)
        self.wrapped.IsInternalClearanceAdjustedAfterFitting = value

    @property
    def journal_bearing_type(self) -> '_1835.JournalBearingType':
        """JournalBearingType: 'JournalBearingType' is the original name of this property."""

        temp = self.wrapped.JournalBearingType
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1835.JournalBearingType)(value) if value is not None else None

    @journal_bearing_type.setter
    def journal_bearing_type(self, value: '_1835.JournalBearingType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.JournalBearingType = value

    @property
    def left_node_position_from_centre(self) -> 'float':
        """float: 'LeftNodePositionFromCentre' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftNodePositionFromCentre
        return temp

    @property
    def length(self) -> 'float':
        """float: 'Length' is the original name of this property."""

        temp = self.wrapped.Length
        return temp

    @length.setter
    def length(self, value: 'float'):
        self.wrapped.Length = float(value) if value else 0.0

    @property
    def lubrication_detail(self) -> 'str':
        """str: 'LubricationDetail' is the original name of this property."""

        temp = self.wrapped.LubricationDetail.SelectedItemName
        return temp

    @lubrication_detail.setter
    def lubrication_detail(self, value: 'str'):
        self.wrapped.LubricationDetail.SetSelectedItem(str(value) if value else '')

    @property
    def maximum_bearing_life_modification_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MaximumBearingLifeModificationFactor' is the original name of this property."""

        temp = self.wrapped.MaximumBearingLifeModificationFactor
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @maximum_bearing_life_modification_factor.setter
    def maximum_bearing_life_modification_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MaximumBearingLifeModificationFactor = value

    @property
    def model(self) -> 'enum_with_selected_value.EnumWithSelectedValue_BearingModel':
        """enum_with_selected_value.EnumWithSelectedValue_BearingModel: 'Model' is the original name of this property."""

        temp = self.wrapped.Model
        value = enum_with_selected_value.EnumWithSelectedValue_BearingModel.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @model.setter
    def model(self, value: 'enum_with_selected_value.EnumWithSelectedValue_BearingModel.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_BearingModel.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.Model = value

    @property
    def offset_of_contact_on_inner_race_at_nominal_contact_angle(self) -> 'float':
        """float: 'OffsetOfContactOnInnerRaceAtNominalContactAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OffsetOfContactOnInnerRaceAtNominalContactAngle
        return temp

    @property
    def offset_of_contact_on_left_race(self) -> 'float':
        """float: 'OffsetOfContactOnLeftRace' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OffsetOfContactOnLeftRace
        return temp

    @property
    def offset_of_contact_on_outer_race_at_nominal_contact_angle(self) -> 'float':
        """float: 'OffsetOfContactOnOuterRaceAtNominalContactAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OffsetOfContactOnOuterRaceAtNominalContactAngle
        return temp

    @property
    def offset_of_contact_on_right_race(self) -> 'float':
        """float: 'OffsetOfContactOnRightRace' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OffsetOfContactOnRightRace
        return temp

    @property
    def orientation(self) -> '_1908.Orientations':
        """Orientations: 'Orientation' is the original name of this property."""

        temp = self.wrapped.Orientation
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1908.Orientations)(value) if value is not None else None

    @orientation.setter
    def orientation(self, value: '_1908.Orientations'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.Orientation = value

    @property
    def outer_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'OuterDiameter' is the original name of this property."""

        temp = self.wrapped.OuterDiameter
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @outer_diameter.setter
    def outer_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.OuterDiameter = value

    @property
    def outer_fitting_chart(self) -> '_1744.LegacyChartDefinition':
        """LegacyChartDefinition: 'OuterFittingChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterFittingChart
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_node_position_from_centre(self) -> 'float':
        """float: 'OuterNodePositionFromCentre' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterNodePositionFromCentre
        return temp

    @property
    def override_design_lubrication_detail(self) -> 'bool':
        """bool: 'OverrideDesignLubricationDetail' is the original name of this property."""

        temp = self.wrapped.OverrideDesignLubricationDetail
        return temp

    @override_design_lubrication_detail.setter
    def override_design_lubrication_detail(self, value: 'bool'):
        self.wrapped.OverrideDesignLubricationDetail = bool(value) if value else False

    @property
    def percentage_difference_between_inner_diameter_and_diameter_of_connected_component_at_inner_connection(self) -> 'float':
        """float: 'PercentageDifferenceBetweenInnerDiameterAndDiameterOfConnectedComponentAtInnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PercentageDifferenceBetweenInnerDiameterAndDiameterOfConnectedComponentAtInnerConnection
        return temp

    @property
    def percentage_difference_between_outer_diameter_and_diameter_of_connected_component_at_outer_connection(self) -> 'float':
        """float: 'PercentageDifferenceBetweenOuterDiameterAndDiameterOfConnectedComponentAtOuterConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PercentageDifferenceBetweenOuterDiameterAndDiameterOfConnectedComponentAtOuterConnection
        return temp

    @property
    def permissible_axial_load_calculation_method(self) -> 'overridable.Overridable_CylindricalRollerMaxAxialLoadMethod':
        """overridable.Overridable_CylindricalRollerMaxAxialLoadMethod: 'PermissibleAxialLoadCalculationMethod' is the original name of this property."""

        temp = self.wrapped.PermissibleAxialLoadCalculationMethod
        value = overridable.Overridable_CylindricalRollerMaxAxialLoadMethod.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @permissible_axial_load_calculation_method.setter
    def permissible_axial_load_calculation_method(self, value: 'overridable.Overridable_CylindricalRollerMaxAxialLoadMethod.implicit_type()'):
        wrapper_type = overridable.Overridable_CylindricalRollerMaxAxialLoadMethod.wrapper_type()
        enclosed_type = overridable.Overridable_CylindricalRollerMaxAxialLoadMethod.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value if value is not None else None, is_overridden)
        self.wrapped.PermissibleAxialLoadCalculationMethod = value

    @property
    def permissible_track_truncation(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'PermissibleTrackTruncation' is the original name of this property."""

        temp = self.wrapped.PermissibleTrackTruncation
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @permissible_track_truncation.setter
    def permissible_track_truncation(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.PermissibleTrackTruncation = value

    @property
    def preload(self) -> 'enum_with_selected_value.EnumWithSelectedValue_PreloadType':
        """enum_with_selected_value.EnumWithSelectedValue_PreloadType: 'Preload' is the original name of this property."""

        temp = self.wrapped.Preload
        value = enum_with_selected_value.EnumWithSelectedValue_PreloadType.wrapped_type()
        return enum_with_selected_value_runtime.create(temp, value) if temp is not None else None

    @preload.setter
    def preload(self, value: 'enum_with_selected_value.EnumWithSelectedValue_PreloadType.implicit_type()'):
        wrapper_type = enum_with_selected_value_runtime.ENUM_WITH_SELECTED_VALUE
        enclosed_type = enum_with_selected_value.EnumWithSelectedValue_PreloadType.implicit_type()
        value = conversion.mp_to_pn_enum(value)
        value = wrapper_type[enclosed_type](value)
        self.wrapped.Preload = value

    @property
    def preload_spring_initial_compression(self) -> 'float':
        """float: 'PreloadSpringInitialCompression' is the original name of this property."""

        temp = self.wrapped.PreloadSpringInitialCompression
        return temp

    @preload_spring_initial_compression.setter
    def preload_spring_initial_compression(self, value: 'float'):
        self.wrapped.PreloadSpringInitialCompression = float(value) if value else 0.0

    @property
    def preload_spring_max_travel(self) -> 'float':
        """float: 'PreloadSpringMaxTravel' is the original name of this property."""

        temp = self.wrapped.PreloadSpringMaxTravel
        return temp

    @preload_spring_max_travel.setter
    def preload_spring_max_travel(self, value: 'float'):
        self.wrapped.PreloadSpringMaxTravel = float(value) if value else 0.0

    @property
    def preload_spring_stiffness(self) -> 'float':
        """float: 'PreloadSpringStiffness' is the original name of this property."""

        temp = self.wrapped.PreloadSpringStiffness
        return temp

    @preload_spring_stiffness.setter
    def preload_spring_stiffness(self, value: 'float'):
        self.wrapped.PreloadSpringStiffness = float(value) if value else 0.0

    @property
    def preload_spring_on_outer(self) -> 'bool':
        """bool: 'PreloadSpringOnOuter' is the original name of this property."""

        temp = self.wrapped.PreloadSpringOnOuter
        return temp

    @preload_spring_on_outer.setter
    def preload_spring_on_outer(self, value: 'bool'):
        self.wrapped.PreloadSpringOnOuter = bool(value) if value else False

    @property
    def preload_is_from_left(self) -> 'bool':
        """bool: 'PreloadIsFromLeft' is the original name of this property."""

        temp = self.wrapped.PreloadIsFromLeft
        return temp

    @preload_is_from_left.setter
    def preload_is_from_left(self, value: 'bool'):
        self.wrapped.PreloadIsFromLeft = bool(value) if value else False

    @property
    def radial_internal_clearance(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RadialInternalClearance' is the original name of this property."""

        temp = self.wrapped.RadialInternalClearance
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @radial_internal_clearance.setter
    def radial_internal_clearance(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RadialInternalClearance = value

    @property
    def right_node_position_from_centre(self) -> 'float':
        """float: 'RightNodePositionFromCentre' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightNodePositionFromCentre
        return temp

    @property
    def use_design_iso14179_settings(self) -> 'bool':
        """bool: 'UseDesignISO14179Settings' is the original name of this property."""

        temp = self.wrapped.UseDesignISO14179Settings
        return temp

    @use_design_iso14179_settings.setter
    def use_design_iso14179_settings(self, value: 'bool'):
        self.wrapped.UseDesignISO14179Settings = bool(value) if value else False

    @property
    def axial_internal_clearance_tolerance(self) -> '_2379.AxialInternalClearanceTolerance':
        """AxialInternalClearanceTolerance: 'AxialInternalClearanceTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialInternalClearanceTolerance
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail(self) -> '_2073.BearingDesign':
        """BearingDesign: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2073.BearingDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to BearingDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_detailed_bearing(self) -> '_2074.DetailedBearing':
        """DetailedBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2074.DetailedBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to DetailedBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_dummy_rolling_bearing(self) -> '_2075.DummyRollingBearing':
        """DummyRollingBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2075.DummyRollingBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to DummyRollingBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_linear_bearing(self) -> '_2076.LinearBearing':
        """LinearBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2076.LinearBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to LinearBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_non_linear_bearing(self) -> '_2077.NonLinearBearing':
        """NonLinearBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2077.NonLinearBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to NonLinearBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_angular_contact_ball_bearing(self) -> '_2078.AngularContactBallBearing':
        """AngularContactBallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2078.AngularContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to AngularContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_angular_contact_thrust_ball_bearing(self) -> '_2079.AngularContactThrustBallBearing':
        """AngularContactThrustBallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2079.AngularContactThrustBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to AngularContactThrustBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_asymmetric_spherical_roller_bearing(self) -> '_2080.AsymmetricSphericalRollerBearing':
        """AsymmetricSphericalRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2080.AsymmetricSphericalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to AsymmetricSphericalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_axial_thrust_cylindrical_roller_bearing(self) -> '_2081.AxialThrustCylindricalRollerBearing':
        """AxialThrustCylindricalRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2081.AxialThrustCylindricalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to AxialThrustCylindricalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_axial_thrust_needle_roller_bearing(self) -> '_2082.AxialThrustNeedleRollerBearing':
        """AxialThrustNeedleRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2082.AxialThrustNeedleRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to AxialThrustNeedleRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_ball_bearing(self) -> '_2083.BallBearing':
        """BallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2083.BallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to BallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_barrel_roller_bearing(self) -> '_2085.BarrelRollerBearing':
        """BarrelRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2085.BarrelRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to BarrelRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_crossed_roller_bearing(self) -> '_2091.CrossedRollerBearing':
        """CrossedRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2091.CrossedRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to CrossedRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_cylindrical_roller_bearing(self) -> '_2092.CylindricalRollerBearing':
        """CylindricalRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2092.CylindricalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to CylindricalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_deep_groove_ball_bearing(self) -> '_2093.DeepGrooveBallBearing':
        """DeepGrooveBallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2093.DeepGrooveBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to DeepGrooveBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_four_point_contact_ball_bearing(self) -> '_2097.FourPointContactBallBearing':
        """FourPointContactBallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2097.FourPointContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to FourPointContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_multi_point_contact_ball_bearing(self) -> '_2102.MultiPointContactBallBearing':
        """MultiPointContactBallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2102.MultiPointContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to MultiPointContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_needle_roller_bearing(self) -> '_2103.NeedleRollerBearing':
        """NeedleRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2103.NeedleRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to NeedleRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_non_barrel_roller_bearing(self) -> '_2104.NonBarrelRollerBearing':
        """NonBarrelRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2104.NonBarrelRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to NonBarrelRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_roller_bearing(self) -> '_2105.RollerBearing':
        """RollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2105.RollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to RollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_rolling_bearing(self) -> '_2108.RollingBearing':
        """RollingBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2108.RollingBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to RollingBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_self_aligning_ball_bearing(self) -> '_2109.SelfAligningBallBearing':
        """SelfAligningBallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2109.SelfAligningBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to SelfAligningBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_spherical_roller_bearing(self) -> '_2112.SphericalRollerBearing':
        """SphericalRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2112.SphericalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to SphericalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_spherical_roller_thrust_bearing(self) -> '_2113.SphericalRollerThrustBearing':
        """SphericalRollerThrustBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2113.SphericalRollerThrustBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to SphericalRollerThrustBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_taper_roller_bearing(self) -> '_2114.TaperRollerBearing':
        """TaperRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2114.TaperRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to TaperRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_three_point_contact_ball_bearing(self) -> '_2115.ThreePointContactBallBearing':
        """ThreePointContactBallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2115.ThreePointContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to ThreePointContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_thrust_ball_bearing(self) -> '_2116.ThrustBallBearing':
        """ThrustBallBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2116.ThrustBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to ThrustBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_toroidal_roller_bearing(self) -> '_2117.ToroidalRollerBearing':
        """ToroidalRollerBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2117.ToroidalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to ToroidalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_pad_fluid_film_bearing(self) -> '_2130.PadFluidFilmBearing':
        """PadFluidFilmBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2130.PadFluidFilmBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to PadFluidFilmBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_plain_grease_filled_journal_bearing(self) -> '_2132.PlainGreaseFilledJournalBearing':
        """PlainGreaseFilledJournalBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2132.PlainGreaseFilledJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to PlainGreaseFilledJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_plain_journal_bearing(self) -> '_2134.PlainJournalBearing':
        """PlainJournalBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2134.PlainJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to PlainJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_plain_oil_fed_journal_bearing(self) -> '_2136.PlainOilFedJournalBearing':
        """PlainOilFedJournalBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2136.PlainOilFedJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to PlainOilFedJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_tilting_pad_journal_bearing(self) -> '_2137.TiltingPadJournalBearing':
        """TiltingPadJournalBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2137.TiltingPadJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to TiltingPadJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_tilting_pad_thrust_bearing(self) -> '_2138.TiltingPadThrustBearing':
        """TiltingPadThrustBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2138.TiltingPadThrustBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to TiltingPadThrustBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_concept_axial_clearance_bearing(self) -> '_2140.ConceptAxialClearanceBearing':
        """ConceptAxialClearanceBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2140.ConceptAxialClearanceBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to ConceptAxialClearanceBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_concept_clearance_bearing(self) -> '_2141.ConceptClearanceBearing':
        """ConceptClearanceBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2141.ConceptClearanceBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to ConceptClearanceBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def detail_of_type_concept_radial_clearance_bearing(self) -> '_2142.ConceptRadialClearanceBearing':
        """ConceptRadialClearanceBearing: 'Detail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Detail
        if _2142.ConceptRadialClearanceBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast detail to ConceptRadialClearanceBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def force_at_zero_displacement(self) -> '_1523.VectorWithLinearAndAngularComponents':
        """VectorWithLinearAndAngularComponents: 'ForceAtZeroDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceAtZeroDisplacement
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def friction_coefficients(self) -> '_2014.RollingBearingFrictionCoefficients':
        """RollingBearingFrictionCoefficients: 'FrictionCoefficients' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FrictionCoefficients
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_mounting_sleeve_bore_tolerance(self) -> '_1862.OuterSupportTolerance':
        """OuterSupportTolerance: 'InnerMountingSleeveBoreTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerMountingSleeveBoreTolerance
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_mounting_sleeve_outer_diameter_tolerance(self) -> '_1856.InnerSupportTolerance':
        """InnerSupportTolerance: 'InnerMountingSleeveOuterDiameterTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerMountingSleeveOuterDiameterTolerance
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_support_detail(self) -> '_1869.SupportDetail':
        """SupportDetail: 'InnerSupportDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSupportDetail
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def left_support_detail(self) -> '_1869.SupportDetail':
        """SupportDetail: 'LeftSupportDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftSupportDetail
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_mounting_sleeve_bore_tolerance(self) -> '_1862.OuterSupportTolerance':
        """OuterSupportTolerance: 'OuterMountingSleeveBoreTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterMountingSleeveBoreTolerance
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_mounting_sleeve_outer_diameter_tolerance(self) -> '_1856.InnerSupportTolerance':
        """InnerSupportTolerance: 'OuterMountingSleeveOuterDiameterTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterMountingSleeveOuterDiameterTolerance
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_support_detail(self) -> '_1869.SupportDetail':
        """SupportDetail: 'OuterSupportDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterSupportDetail
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def overridden_lubrication_detail(self) -> '_258.LubricationDetail':
        """LubricationDetail: 'OverriddenLubricationDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OverriddenLubricationDetail
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def radial_internal_clearance_tolerance(self) -> '_2413.RadialInternalClearanceTolerance':
        """RadialInternalClearanceTolerance: 'RadialInternalClearanceTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadialInternalClearanceTolerance
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def right_support_detail(self) -> '_1869.SupportDetail':
        """SupportDetail: 'RightSupportDetail' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightSupportDetail
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ring_tolerance_inner(self) -> '_1855.InnerRingTolerance':
        """InnerRingTolerance: 'RingToleranceInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingToleranceInner
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ring_tolerance_left(self) -> '_1866.RingTolerance':
        """RingTolerance: 'RingToleranceLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingToleranceLeft
        if _1866.RingTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast ring_tolerance_left to RingTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ring_tolerance_left_of_type_inner_ring_tolerance(self) -> '_1855.InnerRingTolerance':
        """InnerRingTolerance: 'RingToleranceLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingToleranceLeft
        if _1855.InnerRingTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast ring_tolerance_left to InnerRingTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ring_tolerance_left_of_type_outer_ring_tolerance(self) -> '_1861.OuterRingTolerance':
        """OuterRingTolerance: 'RingToleranceLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingToleranceLeft
        if _1861.OuterRingTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast ring_tolerance_left to OuterRingTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ring_tolerance_outer(self) -> '_1861.OuterRingTolerance':
        """OuterRingTolerance: 'RingToleranceOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingToleranceOuter
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ring_tolerance_right(self) -> '_1866.RingTolerance':
        """RingTolerance: 'RingToleranceRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingToleranceRight
        if _1866.RingTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast ring_tolerance_right to RingTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ring_tolerance_right_of_type_inner_ring_tolerance(self) -> '_1855.InnerRingTolerance':
        """InnerRingTolerance: 'RingToleranceRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingToleranceRight
        if _1855.InnerRingTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast ring_tolerance_right to InnerRingTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ring_tolerance_right_of_type_outer_ring_tolerance(self) -> '_1861.OuterRingTolerance':
        """OuterRingTolerance: 'RingToleranceRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingToleranceRight
        if _1861.OuterRingTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast ring_tolerance_right to OuterRingTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property(self) -> '_2073.BearingDesign':
        """BearingDesign: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2073.BearingDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to BearingDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_detailed_bearing(self) -> '_2074.DetailedBearing':
        """DetailedBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2074.DetailedBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to DetailedBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_dummy_rolling_bearing(self) -> '_2075.DummyRollingBearing':
        """DummyRollingBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2075.DummyRollingBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to DummyRollingBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_linear_bearing(self) -> '_2076.LinearBearing':
        """LinearBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2076.LinearBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to LinearBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_non_linear_bearing(self) -> '_2077.NonLinearBearing':
        """NonLinearBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2077.NonLinearBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to NonLinearBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_angular_contact_ball_bearing(self) -> '_2078.AngularContactBallBearing':
        """AngularContactBallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2078.AngularContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to AngularContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_angular_contact_thrust_ball_bearing(self) -> '_2079.AngularContactThrustBallBearing':
        """AngularContactThrustBallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2079.AngularContactThrustBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to AngularContactThrustBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_asymmetric_spherical_roller_bearing(self) -> '_2080.AsymmetricSphericalRollerBearing':
        """AsymmetricSphericalRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2080.AsymmetricSphericalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to AsymmetricSphericalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_axial_thrust_cylindrical_roller_bearing(self) -> '_2081.AxialThrustCylindricalRollerBearing':
        """AxialThrustCylindricalRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2081.AxialThrustCylindricalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to AxialThrustCylindricalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_axial_thrust_needle_roller_bearing(self) -> '_2082.AxialThrustNeedleRollerBearing':
        """AxialThrustNeedleRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2082.AxialThrustNeedleRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to AxialThrustNeedleRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_ball_bearing(self) -> '_2083.BallBearing':
        """BallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2083.BallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to BallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_barrel_roller_bearing(self) -> '_2085.BarrelRollerBearing':
        """BarrelRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2085.BarrelRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to BarrelRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_crossed_roller_bearing(self) -> '_2091.CrossedRollerBearing':
        """CrossedRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2091.CrossedRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to CrossedRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_cylindrical_roller_bearing(self) -> '_2092.CylindricalRollerBearing':
        """CylindricalRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2092.CylindricalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to CylindricalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_deep_groove_ball_bearing(self) -> '_2093.DeepGrooveBallBearing':
        """DeepGrooveBallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2093.DeepGrooveBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to DeepGrooveBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_four_point_contact_ball_bearing(self) -> '_2097.FourPointContactBallBearing':
        """FourPointContactBallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2097.FourPointContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to FourPointContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_multi_point_contact_ball_bearing(self) -> '_2102.MultiPointContactBallBearing':
        """MultiPointContactBallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2102.MultiPointContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to MultiPointContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_needle_roller_bearing(self) -> '_2103.NeedleRollerBearing':
        """NeedleRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2103.NeedleRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to NeedleRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_non_barrel_roller_bearing(self) -> '_2104.NonBarrelRollerBearing':
        """NonBarrelRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2104.NonBarrelRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to NonBarrelRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_roller_bearing(self) -> '_2105.RollerBearing':
        """RollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2105.RollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to RollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_rolling_bearing(self) -> '_2108.RollingBearing':
        """RollingBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2108.RollingBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to RollingBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_self_aligning_ball_bearing(self) -> '_2109.SelfAligningBallBearing':
        """SelfAligningBallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2109.SelfAligningBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to SelfAligningBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_spherical_roller_bearing(self) -> '_2112.SphericalRollerBearing':
        """SphericalRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2112.SphericalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to SphericalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_spherical_roller_thrust_bearing(self) -> '_2113.SphericalRollerThrustBearing':
        """SphericalRollerThrustBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2113.SphericalRollerThrustBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to SphericalRollerThrustBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_taper_roller_bearing(self) -> '_2114.TaperRollerBearing':
        """TaperRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2114.TaperRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to TaperRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_three_point_contact_ball_bearing(self) -> '_2115.ThreePointContactBallBearing':
        """ThreePointContactBallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2115.ThreePointContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to ThreePointContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_thrust_ball_bearing(self) -> '_2116.ThrustBallBearing':
        """ThrustBallBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2116.ThrustBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to ThrustBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_toroidal_roller_bearing(self) -> '_2117.ToroidalRollerBearing':
        """ToroidalRollerBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2117.ToroidalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to ToroidalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_pad_fluid_film_bearing(self) -> '_2130.PadFluidFilmBearing':
        """PadFluidFilmBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2130.PadFluidFilmBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to PadFluidFilmBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_plain_grease_filled_journal_bearing(self) -> '_2132.PlainGreaseFilledJournalBearing':
        """PlainGreaseFilledJournalBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2132.PlainGreaseFilledJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to PlainGreaseFilledJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_plain_journal_bearing(self) -> '_2134.PlainJournalBearing':
        """PlainJournalBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2134.PlainJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to PlainJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_plain_oil_fed_journal_bearing(self) -> '_2136.PlainOilFedJournalBearing':
        """PlainOilFedJournalBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2136.PlainOilFedJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to PlainOilFedJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_tilting_pad_journal_bearing(self) -> '_2137.TiltingPadJournalBearing':
        """TiltingPadJournalBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2137.TiltingPadJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to TiltingPadJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_tilting_pad_thrust_bearing(self) -> '_2138.TiltingPadThrustBearing':
        """TiltingPadThrustBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2138.TiltingPadThrustBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to TiltingPadThrustBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_concept_axial_clearance_bearing(self) -> '_2140.ConceptAxialClearanceBearing':
        """ConceptAxialClearanceBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2140.ConceptAxialClearanceBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to ConceptAxialClearanceBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_concept_clearance_bearing(self) -> '_2141.ConceptClearanceBearing':
        """ConceptClearanceBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2141.ConceptClearanceBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to ConceptClearanceBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def simple_bearing_detail_property_of_type_concept_radial_clearance_bearing(self) -> '_2142.ConceptRadialClearanceBearing':
        """ConceptRadialClearanceBearing: 'SimpleBearingDetailProperty' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleBearingDetailProperty
        if _2142.ConceptRadialClearanceBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast simple_bearing_detail_property to ConceptRadialClearanceBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def support_tolerance_inner(self) -> '_1856.InnerSupportTolerance':
        """InnerSupportTolerance: 'SupportToleranceInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SupportToleranceInner
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def support_tolerance_left(self) -> '_1871.SupportTolerance':
        """SupportTolerance: 'SupportToleranceLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SupportToleranceLeft
        if _1871.SupportTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast support_tolerance_left to SupportTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def support_tolerance_left_of_type_inner_support_tolerance(self) -> '_1856.InnerSupportTolerance':
        """InnerSupportTolerance: 'SupportToleranceLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SupportToleranceLeft
        if _1856.InnerSupportTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast support_tolerance_left to InnerSupportTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def support_tolerance_left_of_type_outer_support_tolerance(self) -> '_1862.OuterSupportTolerance':
        """OuterSupportTolerance: 'SupportToleranceLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SupportToleranceLeft
        if _1862.OuterSupportTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast support_tolerance_left to OuterSupportTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def support_tolerance_outer(self) -> '_1862.OuterSupportTolerance':
        """OuterSupportTolerance: 'SupportToleranceOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SupportToleranceOuter
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def support_tolerance_right(self) -> '_1871.SupportTolerance':
        """SupportTolerance: 'SupportToleranceRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SupportToleranceRight
        if _1871.SupportTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast support_tolerance_right to SupportTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def support_tolerance_right_of_type_inner_support_tolerance(self) -> '_1856.InnerSupportTolerance':
        """InnerSupportTolerance: 'SupportToleranceRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SupportToleranceRight
        if _1856.InnerSupportTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast support_tolerance_right to InnerSupportTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def support_tolerance_right_of_type_outer_support_tolerance(self) -> '_1862.OuterSupportTolerance':
        """OuterSupportTolerance: 'SupportToleranceRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SupportToleranceRight
        if _1862.OuterSupportTolerance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast support_tolerance_right to OuterSupportTolerance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mounting(self) -> 'List[_2381.BearingRaceMountingOptions]':
        """List[BearingRaceMountingOptions]: 'Mounting' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mounting
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def tolerance_combinations(self) -> 'List[_1873.ToleranceCombination]':
        """List[ToleranceCombination]: 'ToleranceCombinations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToleranceCombinations
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def is_radial_bearing(self) -> 'bool':
        """bool: 'IsRadialBearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsRadialBearing
        return temp

    @property
    def specified_stiffness_for_linear_bearing_in_local_coordinate_system(self) -> 'List[List[float]]':
        """List[List[float]]: 'SpecifiedStiffnessForLinearBearingInLocalCoordinateSystem' is the original name of this property."""

        temp = self.wrapped.SpecifiedStiffnessForLinearBearingInLocalCoordinateSystem
        value = conversion.pn_to_mp_list_float_2d(temp)
        return value

    @specified_stiffness_for_linear_bearing_in_local_coordinate_system.setter
    def specified_stiffness_for_linear_bearing_in_local_coordinate_system(self, value: 'List[List[float]]'):
        value = value if value else None
        value = conversion.mp_to_pn_list_float_2d(value)
        self.wrapped.SpecifiedStiffnessForLinearBearingInLocalCoordinateSystem = value

    def set_detail_from_catalogue(self, catalogue: '_1818.BearingCatalog', designation: 'str'):
        """ 'SetDetailFromCatalogue' is the original name of this method.

        Args:
            catalogue (mastapy.bearings.BearingCatalog)
            designation (str)
        """

        catalogue = conversion.mp_to_pn_enum(catalogue)
        designation = str(designation)
        self.wrapped.SetDetailFromCatalogue(catalogue, designation if designation else '')

    def try_attach_left_side_to(self, shaft: '_2422.Shaft', offset: Optional['float'] = float('nan')) -> '_2385.ComponentsConnectedResult':
        """ 'TryAttachLeftSideTo' is the original name of this method.

        Args:
            shaft (mastapy.system_model.part_model.shaft_model.Shaft)
            offset (float, optional)

        Returns:
            mastapy.system_model.part_model.ComponentsConnectedResult
        """

        offset = float(offset)
        method_result = self.wrapped.TryAttachLeftSideTo(shaft.wrapped if shaft else None, offset if offset else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def try_attach_right_side_to(self, shaft: '_2422.Shaft', offset: Optional['float'] = float('nan')) -> '_2385.ComponentsConnectedResult':
        """ 'TryAttachRightSideTo' is the original name of this method.

        Args:
            shaft (mastapy.system_model.part_model.shaft_model.Shaft)
            offset (float, optional)

        Returns:
            mastapy.system_model.part_model.ComponentsConnectedResult
        """

        offset = float(offset)
        method_result = self.wrapped.TryAttachRightSideTo(shaft.wrapped if shaft else None, offset if offset else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

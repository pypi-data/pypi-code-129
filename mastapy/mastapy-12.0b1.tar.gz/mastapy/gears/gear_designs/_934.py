"""_934.py

BevelHypoidGearRatingSettingsItem
"""


from mastapy.gears.materials import _595
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.gears.rating.iso_10300 import _411, _426, _419
from mastapy.gears.rating.hypoid import _432
from mastapy.utility.databases import _1785
from mastapy._internal.python_net import python_net_import

_BEVEL_HYPOID_GEAR_RATING_SETTINGS_ITEM = python_net_import('SMT.MastaAPI.Gears.GearDesigns', 'BevelHypoidGearRatingSettingsItem')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelHypoidGearRatingSettingsItem',)


class BevelHypoidGearRatingSettingsItem(_1785.NamedDatabaseItem):
    """BevelHypoidGearRatingSettingsItem

    This is a mastapy class.
    """

    TYPE = _BEVEL_HYPOID_GEAR_RATING_SETTINGS_ITEM

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelHypoidGearRatingSettingsItem.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bevel_gear_rating_method(self) -> '_595.RatingMethods':
        """RatingMethods: 'BevelGearRatingMethod' is the original name of this property."""

        temp = self.wrapped.BevelGearRatingMethod
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_595.RatingMethods)(value) if value is not None else None

    @bevel_gear_rating_method.setter
    def bevel_gear_rating_method(self, value: '_595.RatingMethods'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.BevelGearRatingMethod = value

    @property
    def bevel_general_load_factors_k_method(self) -> '_411.GeneralLoadFactorCalculationMethod':
        """GeneralLoadFactorCalculationMethod: 'BevelGeneralLoadFactorsKMethod' is the original name of this property."""

        temp = self.wrapped.BevelGeneralLoadFactorsKMethod
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_411.GeneralLoadFactorCalculationMethod)(value) if value is not None else None

    @bevel_general_load_factors_k_method.setter
    def bevel_general_load_factors_k_method(self, value: '_411.GeneralLoadFactorCalculationMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.BevelGeneralLoadFactorsKMethod = value

    @property
    def bevel_pitting_factor_calculation_method(self) -> '_426.PittingFactorCalculationMethod':
        """PittingFactorCalculationMethod: 'BevelPittingFactorCalculationMethod' is the original name of this property."""

        temp = self.wrapped.BevelPittingFactorCalculationMethod
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_426.PittingFactorCalculationMethod)(value) if value is not None else None

    @bevel_pitting_factor_calculation_method.setter
    def bevel_pitting_factor_calculation_method(self, value: '_426.PittingFactorCalculationMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.BevelPittingFactorCalculationMethod = value

    @property
    def hypoid_gear_rating_method(self) -> '_432.HypoidRatingMethod':
        """HypoidRatingMethod: 'HypoidGearRatingMethod' is the original name of this property."""

        temp = self.wrapped.HypoidGearRatingMethod
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_432.HypoidRatingMethod)(value) if value is not None else None

    @hypoid_gear_rating_method.setter
    def hypoid_gear_rating_method(self, value: '_432.HypoidRatingMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.HypoidGearRatingMethod = value

    @property
    def hypoid_general_load_factors_k_method(self) -> '_411.GeneralLoadFactorCalculationMethod':
        """GeneralLoadFactorCalculationMethod: 'HypoidGeneralLoadFactorsKMethod' is the original name of this property."""

        temp = self.wrapped.HypoidGeneralLoadFactorsKMethod
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_411.GeneralLoadFactorCalculationMethod)(value) if value is not None else None

    @hypoid_general_load_factors_k_method.setter
    def hypoid_general_load_factors_k_method(self, value: '_411.GeneralLoadFactorCalculationMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.HypoidGeneralLoadFactorsKMethod = value

    @property
    def hypoid_pitting_factor_calculation_method(self) -> '_426.PittingFactorCalculationMethod':
        """PittingFactorCalculationMethod: 'HypoidPittingFactorCalculationMethod' is the original name of this property."""

        temp = self.wrapped.HypoidPittingFactorCalculationMethod
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_426.PittingFactorCalculationMethod)(value) if value is not None else None

    @hypoid_pitting_factor_calculation_method.setter
    def hypoid_pitting_factor_calculation_method(self, value: '_426.PittingFactorCalculationMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.HypoidPittingFactorCalculationMethod = value

    @property
    def iso_rating_method_for_bevel_gears(self) -> '_419.ISO10300RatingMethod':
        """ISO10300RatingMethod: 'ISORatingMethodForBevelGears' is the original name of this property."""

        temp = self.wrapped.ISORatingMethodForBevelGears
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_419.ISO10300RatingMethod)(value) if value is not None else None

    @iso_rating_method_for_bevel_gears.setter
    def iso_rating_method_for_bevel_gears(self, value: '_419.ISO10300RatingMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ISORatingMethodForBevelGears = value

    @property
    def iso_rating_method_for_hypoid_gears(self) -> '_419.ISO10300RatingMethod':
        """ISO10300RatingMethod: 'ISORatingMethodForHypoidGears' is the original name of this property."""

        temp = self.wrapped.ISORatingMethodForHypoidGears
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_419.ISO10300RatingMethod)(value) if value is not None else None

    @iso_rating_method_for_hypoid_gears.setter
    def iso_rating_method_for_hypoid_gears(self, value: '_419.ISO10300RatingMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ISORatingMethodForHypoidGears = value

    @property
    def include_mesh_node_misalignments_in_default_report(self) -> 'bool':
        """bool: 'IncludeMeshNodeMisalignmentsInDefaultReport' is the original name of this property."""

        temp = self.wrapped.IncludeMeshNodeMisalignmentsInDefaultReport
        return temp

    @include_mesh_node_misalignments_in_default_report.setter
    def include_mesh_node_misalignments_in_default_report(self, value: 'bool'):
        self.wrapped.IncludeMeshNodeMisalignmentsInDefaultReport = bool(value) if value else False

"""_481.py

PlasticGearVDI2736AbstractGearSingleFlankRating
"""


from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.rating import _348
from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _485
from mastapy.materials import _276, _277
from mastapy.gears.rating.cylindrical.iso6336 import _507
from mastapy._internal.python_net import python_net_import

_PLASTIC_GEAR_VDI2736_ABSTRACT_GEAR_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.PlasticVDI2736', 'PlasticGearVDI2736AbstractGearSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('PlasticGearVDI2736AbstractGearSingleFlankRating',)


class PlasticGearVDI2736AbstractGearSingleFlankRating(_507.ISO6336AbstractGearSingleFlankRating):
    """PlasticGearVDI2736AbstractGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _PLASTIC_GEAR_VDI2736_ABSTRACT_GEAR_SINGLE_FLANK_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PlasticGearVDI2736AbstractGearSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_stress_number_bending(self) -> 'float':
        """float: 'AllowableStressNumberBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableStressNumberBending
        return temp

    @property
    def allowable_stress_number_contact(self) -> 'float':
        """float: 'AllowableStressNumberContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableStressNumberContact
        return temp

    @property
    def averaged_linear_wear(self) -> 'float':
        """float: 'AveragedLinearWear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AveragedLinearWear
        return temp

    @property
    def flank_heat_transfer_coefficient(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'FlankHeatTransferCoefficient' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlankHeatTransferCoefficient
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @property
    def flank_temperature(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'FlankTemperature' is the original name of this property."""

        temp = self.wrapped.FlankTemperature
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @flank_temperature.setter
    def flank_temperature(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.FlankTemperature = value

    @property
    def important_note_on_contact_durability_of_pom(self) -> 'str':
        """str: 'ImportantNoteOnContactDurabilityOfPOM' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ImportantNoteOnContactDurabilityOfPOM
        return temp

    @property
    def is_gear_driving_or_driven(self) -> '_348.FlankLoadingState':
        """FlankLoadingState: 'IsGearDrivingOrDriven' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsGearDrivingOrDriven
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_348.FlankLoadingState)(value) if value is not None else None

    @property
    def minimum_factor_of_safety_bending_fatigue(self) -> 'float':
        """float: 'MinimumFactorOfSafetyBendingFatigue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumFactorOfSafetyBendingFatigue
        return temp

    @property
    def minimum_factor_of_safety_pitting_fatigue(self) -> 'float':
        """float: 'MinimumFactorOfSafetyPittingFatigue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumFactorOfSafetyPittingFatigue
        return temp

    @property
    def minimum_factor_of_safety_wear(self) -> 'float':
        """float: 'MinimumFactorOfSafetyWear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumFactorOfSafetyWear
        return temp

    @property
    def nominal_tooth_root_stress(self) -> 'float':
        """float: 'NominalToothRootStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalToothRootStress
        return temp

    @property
    def permissible_contact_stress(self) -> 'float':
        """float: 'PermissibleContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermissibleContactStress
        return temp

    @property
    def permissible_tooth_root_bending_stress(self) -> 'float':
        """float: 'PermissibleToothRootBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermissibleToothRootBendingStress
        return temp

    @property
    def pitting_stress_limit(self) -> 'float':
        """float: 'PittingStressLimit' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PittingStressLimit
        return temp

    @property
    def profile_line_length_of_the_active_tooth_flank(self) -> 'float':
        """float: 'ProfileLineLengthOfTheActiveToothFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileLineLengthOfTheActiveToothFlank
        return temp

    @property
    def root_heat_transfer_coefficient(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RootHeatTransferCoefficient' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RootHeatTransferCoefficient
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @property
    def root_temperature(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RootTemperature' is the original name of this property."""

        temp = self.wrapped.RootTemperature
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @root_temperature.setter
    def root_temperature(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RootTemperature = value

    @property
    def tooth_root_stress_limit(self) -> 'float':
        """float: 'ToothRootStressLimit' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothRootStressLimit
        return temp

    @property
    def standard_plastic_sn_curve_for_the_specified_operating_conditions(self) -> '_485.PlasticSNCurveForTheSpecifiedOperatingConditions':
        """PlasticSNCurveForTheSpecifiedOperatingConditions: 'StandardPlasticSNCurveForTheSpecifiedOperatingConditions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StandardPlasticSNCurveForTheSpecifiedOperatingConditions
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bending_stress_cycle_data_for_damage_tables(self) -> 'List[_276.StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial]':
        """List[StressCyclesDataForTheBendingSNCurveOfAPlasticMaterial]: 'BendingStressCycleDataForDamageTables' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BendingStressCycleDataForDamageTables
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def contact_stress_cycle_data_for_damage_tables(self) -> 'List[_277.StressCyclesDataForTheContactSNCurveOfAPlasticMaterial]':
        """List[StressCyclesDataForTheContactSNCurveOfAPlasticMaterial]: 'ContactStressCycleDataForDamageTables' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactStressCycleDataForDamageTables
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

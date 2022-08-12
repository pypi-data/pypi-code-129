"""_1977.py

LoadedRollingBearingResults
"""


from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.bearings import _1833
from mastapy.bearings.bearing_results.rolling.abma import _2060, _2058, _2059
from mastapy._internal.cast_exception import CastException
from mastapy.bearings.bearing_results.rolling import (
    _1917, _1921, _2018, _2004,
    _1978
)
from mastapy.bearings.bearing_results.rolling.iso_rating_results import (
    _2047, _2045, _2051, _2048,
    _2050, _2046, _2052
)
from mastapy.bearings.bearing_results.rolling.fitting import _2054, _2056, _2057
from mastapy.bearings.bearing_results.rolling.skf_module import _2042
from mastapy.bearings.bearing_results import _1902
from mastapy._internal.python_net import python_net_import

_LOADED_ROLLING_BEARING_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedRollingBearingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedRollingBearingResults',)


class LoadedRollingBearingResults(_1902.LoadedDetailedBearingResults):
    """LoadedRollingBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_ROLLING_BEARING_RESULTS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'LoadedRollingBearingResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_to_radial_load_ratio(self) -> 'float':
        """float: 'AxialToRadialLoadRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialToRadialLoadRatio
        return temp

    @property
    def bearing_dip_factor(self) -> 'float':
        """float: 'BearingDipFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDipFactor
        return temp

    @property
    def bearing_dip_factor_max(self) -> 'float':
        """float: 'BearingDipFactorMax' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDipFactorMax
        return temp

    @property
    def bearing_dip_factor_min(self) -> 'float':
        """float: 'BearingDipFactorMin' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDipFactorMin
        return temp

    @property
    def cage_angular_velocity(self) -> 'float':
        """float: 'CageAngularVelocity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CageAngularVelocity
        return temp

    @property
    def change_in_element_diameter_due_to_thermal_expansion(self) -> 'float':
        """float: 'ChangeInElementDiameterDueToThermalExpansion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ChangeInElementDiameterDueToThermalExpansion
        return temp

    @property
    def change_in_operating_radial_internal_clearance_due_to_element_thermal_expansion(self) -> 'float':
        """float: 'ChangeInOperatingRadialInternalClearanceDueToElementThermalExpansion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ChangeInOperatingRadialInternalClearanceDueToElementThermalExpansion
        return temp

    @property
    def coefficient_for_no_load_power_loss(self) -> 'float':
        """float: 'CoefficientForNoLoadPowerLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoefficientForNoLoadPowerLoss
        return temp

    @property
    def drag_loss_factor(self) -> 'float':
        """float: 'DragLossFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DragLossFactor
        return temp

    @property
    def dynamic_axial_load_factor_for_isotr141792001(self) -> 'float':
        """float: 'DynamicAxialLoadFactorForISOTR141792001' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicAxialLoadFactorForISOTR141792001
        return temp

    @property
    def dynamic_equivalent_load_isotr141792001(self) -> 'float':
        """float: 'DynamicEquivalentLoadISOTR141792001' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicEquivalentLoadISOTR141792001
        return temp

    @property
    def dynamic_radial_load_factor_for_isotr141792001(self) -> 'float':
        """float: 'DynamicRadialLoadFactorForISOTR141792001' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicRadialLoadFactorForISOTR141792001
        return temp

    @property
    def dynamic_viscosity(self) -> 'float':
        """float: 'DynamicViscosity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicViscosity
        return temp

    @property
    def element_temperature(self) -> 'float':
        """float: 'ElementTemperature' is the original name of this property."""

        temp = self.wrapped.ElementTemperature
        return temp

    @element_temperature.setter
    def element_temperature(self, value: 'float'):
        self.wrapped.ElementTemperature = float(value) if value else 0.0

    @property
    def fluid_film_density(self) -> 'float':
        """float: 'FluidFilmDensity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FluidFilmDensity
        return temp

    @property
    def fluid_film_temperature_source(self) -> '_1833.FluidFilmTemperatureOptions':
        """FluidFilmTemperatureOptions: 'FluidFilmTemperatureSource' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FluidFilmTemperatureSource
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1833.FluidFilmTemperatureOptions)(value) if value is not None else None

    @property
    def frequency_of_over_rolling_on_inner_ring(self) -> 'float':
        """float: 'FrequencyOfOverRollingOnInnerRing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FrequencyOfOverRollingOnInnerRing
        return temp

    @property
    def frequency_of_over_rolling_on_outer_ring(self) -> 'float':
        """float: 'FrequencyOfOverRollingOnOuterRing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FrequencyOfOverRollingOnOuterRing
        return temp

    @property
    def frequency_of_over_rolling_on_rolling_element(self) -> 'float':
        """float: 'FrequencyOfOverRollingOnRollingElement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FrequencyOfOverRollingOnRollingElement
        return temp

    @property
    def frictional_moment_of_drag_losses(self) -> 'float':
        """float: 'FrictionalMomentOfDragLosses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FrictionalMomentOfDragLosses
        return temp

    @property
    def frictional_moment_of_seals(self) -> 'float':
        """float: 'FrictionalMomentOfSeals' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FrictionalMomentOfSeals
        return temp

    @property
    def frictional_moment_of_the_bearing_seal(self) -> 'float':
        """float: 'FrictionalMomentOfTheBearingSeal' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FrictionalMomentOfTheBearingSeal
        return temp

    @property
    def heat_emitting_reference_surface_area(self) -> 'float':
        """float: 'HeatEmittingReferenceSurfaceArea' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HeatEmittingReferenceSurfaceArea
        return temp

    @property
    def include_centrifugal_effects(self) -> 'bool':
        """bool: 'IncludeCentrifugalEffects' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IncludeCentrifugalEffects
        return temp

    @property
    def include_centrifugal_ring_expansion(self) -> 'bool':
        """bool: 'IncludeCentrifugalRingExpansion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IncludeCentrifugalRingExpansion
        return temp

    @property
    def include_fitting_effects(self) -> 'bool':
        """bool: 'IncludeFittingEffects' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IncludeFittingEffects
        return temp

    @property
    def include_gear_blank_elastic_distortion(self) -> 'bool':
        """bool: 'IncludeGearBlankElasticDistortion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IncludeGearBlankElasticDistortion
        return temp

    @property
    def include_inner_race_deflections(self) -> 'bool':
        """bool: 'IncludeInnerRaceDeflections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IncludeInnerRaceDeflections
        return temp

    @property
    def include_thermal_expansion_effects(self) -> 'bool':
        """bool: 'IncludeThermalExpansionEffects' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IncludeThermalExpansionEffects
        return temp

    @property
    def is_inner_ring_rotating_relative_to_load(self) -> 'bool':
        """bool: 'IsInnerRingRotatingRelativeToLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsInnerRingRotatingRelativeToLoad
        return temp

    @property
    def is_outer_ring_rotating_relative_to_load(self) -> 'bool':
        """bool: 'IsOuterRingRotatingRelativeToLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsOuterRingRotatingRelativeToLoad
        return temp

    @property
    def kinematic_viscosity(self) -> 'float':
        """float: 'KinematicViscosity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KinematicViscosity
        return temp

    @property
    def kinematic_viscosity_of_oil_for_efficiency_calculations(self) -> 'float':
        """float: 'KinematicViscosityOfOilForEfficiencyCalculations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KinematicViscosityOfOilForEfficiencyCalculations
        return temp

    @property
    def lambda_ratio_inner(self) -> 'float':
        """float: 'LambdaRatioInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LambdaRatioInner
        return temp

    @property
    def lambda_ratio_outer(self) -> 'float':
        """float: 'LambdaRatioOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LambdaRatioOuter
        return temp

    @property
    def load_dependent_torque(self) -> 'float':
        """float: 'LoadDependentTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadDependentTorque
        return temp

    @property
    def lubricant_film_temperature(self) -> 'float':
        """float: 'LubricantFilmTemperature' is the original name of this property."""

        temp = self.wrapped.LubricantFilmTemperature
        return temp

    @lubricant_film_temperature.setter
    def lubricant_film_temperature(self, value: 'float'):
        self.wrapped.LubricantFilmTemperature = float(value) if value else 0.0

    @property
    def lubricant_windage_and_churning_temperature(self) -> 'float':
        """float: 'LubricantWindageAndChurningTemperature' is the original name of this property."""

        temp = self.wrapped.LubricantWindageAndChurningTemperature
        return temp

    @lubricant_windage_and_churning_temperature.setter
    def lubricant_windage_and_churning_temperature(self, value: 'float'):
        self.wrapped.LubricantWindageAndChurningTemperature = float(value) if value else 0.0

    @property
    def maximum_normal_load_inner(self) -> 'float':
        """float: 'MaximumNormalLoadInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalLoadInner
        return temp

    @property
    def maximum_normal_load_outer(self) -> 'float':
        """float: 'MaximumNormalLoadOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalLoadOuter
        return temp

    @property
    def maximum_normal_stress(self) -> 'float':
        """float: 'MaximumNormalStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalStress
        return temp

    @property
    def maximum_normal_stress_inner(self) -> 'float':
        """float: 'MaximumNormalStressInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalStressInner
        return temp

    @property
    def maximum_normal_stress_outer(self) -> 'float':
        """float: 'MaximumNormalStressOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalStressOuter
        return temp

    @property
    def minimum_lubricating_film_thickness_inner(self) -> 'float':
        """float: 'MinimumLubricatingFilmThicknessInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumLubricatingFilmThicknessInner
        return temp

    @property
    def minimum_lubricating_film_thickness_outer(self) -> 'float':
        """float: 'MinimumLubricatingFilmThicknessOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumLubricatingFilmThicknessOuter
        return temp

    @property
    def no_load_bearing_resistive_torque(self) -> 'float':
        """float: 'NoLoadBearingResistiveTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NoLoadBearingResistiveTorque
        return temp

    @property
    def number_of_elements_in_contact(self) -> 'int':
        """int: 'NumberOfElementsInContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfElementsInContact
        return temp

    @property
    def oil_dip_coefficient(self) -> 'float':
        """float: 'OilDipCoefficient' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OilDipCoefficient
        return temp

    @property
    def oil_dip_coefficient_thermal_speeds(self) -> 'float':
        """float: 'OilDipCoefficientThermalSpeeds' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OilDipCoefficientThermalSpeeds
        return temp

    @property
    def power_rating_f0(self) -> 'float':
        """float: 'PowerRatingF0' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerRatingF0
        return temp

    @property
    def power_rating_f1(self) -> 'float':
        """float: 'PowerRatingF1' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerRatingF1
        return temp

    @property
    def ratio_of_operating_element_diameter_to_element_pcd(self) -> 'float':
        """float: 'RatioOfOperatingElementDiameterToElementPCD' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatioOfOperatingElementDiameterToElementPCD
        return temp

    @property
    def relative_misalignment(self) -> 'float':
        """float: 'RelativeMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeMisalignment
        return temp

    @property
    def rolling_frictional_moment(self) -> 'float':
        """float: 'RollingFrictionalMoment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollingFrictionalMoment
        return temp

    @property
    def sliding_friction_coefficient(self) -> 'float':
        """float: 'SlidingFrictionCoefficient' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingFrictionCoefficient
        return temp

    @property
    def sliding_frictional_moment(self) -> 'float':
        """float: 'SlidingFrictionalMoment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingFrictionalMoment
        return temp

    @property
    def speed_factor_dmn(self) -> 'float':
        """float: 'SpeedFactorDmn' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpeedFactorDmn
        return temp

    @property
    def speed_factor_dn(self) -> 'float':
        """float: 'SpeedFactorDn' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpeedFactorDn
        return temp

    @property
    def static_axial_load_factor_for_isotr141792001(self) -> 'float':
        """float: 'StaticAxialLoadFactorForISOTR141792001' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StaticAxialLoadFactorForISOTR141792001
        return temp

    @property
    def static_equivalent_load_capacity_ratio_limit(self) -> 'float':
        """float: 'StaticEquivalentLoadCapacityRatioLimit' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StaticEquivalentLoadCapacityRatioLimit
        return temp

    @property
    def static_equivalent_load_for_isotr141792001(self) -> 'float':
        """float: 'StaticEquivalentLoadForISOTR141792001' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StaticEquivalentLoadForISOTR141792001
        return temp

    @property
    def static_radial_load_factor_for_isotr141792001(self) -> 'float':
        """float: 'StaticRadialLoadFactorForISOTR141792001' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StaticRadialLoadFactorForISOTR141792001
        return temp

    @property
    def surrounding_lubricant_density(self) -> 'float':
        """float: 'SurroundingLubricantDensity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SurroundingLubricantDensity
        return temp

    @property
    def total_frictional_moment_from_skf_loss_method(self) -> 'float':
        """float: 'TotalFrictionalMomentFromSKFLossMethod' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalFrictionalMomentFromSKFLossMethod
        return temp

    @property
    def ansiabma(self) -> '_2060.ANSIABMAResults':
        """ANSIABMAResults: 'ANSIABMA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ANSIABMA
        if _2060.ANSIABMAResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast ansiabma to ANSIABMAResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ansiabma_of_type_ansiabma112014_results(self) -> '_2058.ANSIABMA112014Results':
        """ANSIABMA112014Results: 'ANSIABMA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ANSIABMA
        if _2058.ANSIABMA112014Results.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast ansiabma to ANSIABMA112014Results. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ansiabma_of_type_ansiabma92015_results(self) -> '_2059.ANSIABMA92015Results':
        """ANSIABMA92015Results: 'ANSIABMA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ANSIABMA
        if _2059.ANSIABMA92015Results.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast ansiabma to ANSIABMA92015Results. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def din732(self) -> '_1917.DIN732Results':
        """DIN732Results: 'DIN732' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DIN732
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def iso2812007(self) -> '_2047.ISO2812007Results':
        """ISO2812007Results: 'ISO2812007' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO2812007
        if _2047.ISO2812007Results.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast iso2812007 to ISO2812007Results. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def iso2812007_of_type_ball_iso2812007_results(self) -> '_2045.BallISO2812007Results':
        """BallISO2812007Results: 'ISO2812007' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO2812007
        if _2045.BallISO2812007Results.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast iso2812007 to BallISO2812007Results. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def iso2812007_of_type_roller_iso2812007_results(self) -> '_2051.RollerISO2812007Results':
        """RollerISO2812007Results: 'ISO2812007' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO2812007
        if _2051.RollerISO2812007Results.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast iso2812007 to RollerISO2812007Results. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def iso762006(self) -> '_2048.ISO762006Results':
        """ISO762006Results: 'ISO762006' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO762006
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def isots162812008(self) -> '_2050.ISOTS162812008Results':
        """ISOTS162812008Results: 'ISOTS162812008' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISOTS162812008
        if _2050.ISOTS162812008Results.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast isots162812008 to ISOTS162812008Results. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def isots162812008_of_type_ball_isots162812008_results(self) -> '_2046.BallISOTS162812008Results':
        """BallISOTS162812008Results: 'ISOTS162812008' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISOTS162812008
        if _2046.BallISOTS162812008Results.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast isots162812008 to BallISOTS162812008Results. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def isots162812008_of_type_roller_isots162812008_results(self) -> '_2052.RollerISOTS162812008Results':
        """RollerISOTS162812008Results: 'ISOTS162812008' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISOTS162812008
        if _2052.RollerISOTS162812008Results.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast isots162812008 to RollerISOTS162812008Results. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_ring_fitting_at_assembly(self) -> '_2054.InnerRingFittingThermalResults':
        """InnerRingFittingThermalResults: 'InnerRingFittingAtAssembly' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRingFittingAtAssembly
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_ring_fitting_at_operating_conditions(self) -> '_2054.InnerRingFittingThermalResults':
        """InnerRingFittingThermalResults: 'InnerRingFittingAtOperatingConditions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRingFittingAtOperatingConditions
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def maximum_operating_internal_clearance(self) -> '_1921.InternalClearance':
        """InternalClearance: 'MaximumOperatingInternalClearance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumOperatingInternalClearance
        if _1921.InternalClearance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast maximum_operating_internal_clearance to InternalClearance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def maximum_static_contact_stress(self) -> '_2004.MaximumStaticContactStress':
        """MaximumStaticContactStress: 'MaximumStaticContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumStaticContactStress
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def minimum_operating_internal_clearance(self) -> '_1921.InternalClearance':
        """InternalClearance: 'MinimumOperatingInternalClearance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumOperatingInternalClearance
        if _1921.InternalClearance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast minimum_operating_internal_clearance to InternalClearance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_ring_fitting_at_assembly(self) -> '_2056.OuterRingFittingThermalResults':
        """OuterRingFittingThermalResults: 'OuterRingFittingAtAssembly' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRingFittingAtAssembly
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_ring_fitting_at_operating_conditions(self) -> '_2056.OuterRingFittingThermalResults':
        """OuterRingFittingThermalResults: 'OuterRingFittingAtOperatingConditions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRingFittingAtOperatingConditions
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def skf_module_results(self) -> '_2042.SKFModuleResults':
        """SKFModuleResults: 'SKFModuleResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SKFModuleResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def all_mounting_results(self) -> 'List[_2057.RingFittingThermalResults]':
        """List[RingFittingThermalResults]: 'AllMountingResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllMountingResults
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def rows(self) -> 'List[_1978.LoadedRollingBearingRow]':
        """List[LoadedRollingBearingRow]: 'Rows' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rows
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

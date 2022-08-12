"""_2070.py

LoadedTiltingPadJournalBearingResults
"""


from mastapy._internal import constructor
from mastapy.bearings.bearing_results.fluid_film import _2064
from mastapy._internal.python_net import python_net_import

_LOADED_TILTING_PAD_JOURNAL_BEARING_RESULTS = python_net_import('SMT.MastaAPI.Bearings.BearingResults.FluidFilm', 'LoadedTiltingPadJournalBearingResults')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedTiltingPadJournalBearingResults',)


class LoadedTiltingPadJournalBearingResults(_2064.LoadedPadFluidFilmBearingResults):
    """LoadedTiltingPadJournalBearingResults

    This is a mastapy class.
    """

    TYPE = _LOADED_TILTING_PAD_JOURNAL_BEARING_RESULTS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'LoadedTiltingPadJournalBearingResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angular_position_of_the_minimum_film_thickness_from_the_x_axis(self) -> 'float':
        """float: 'AngularPositionOfTheMinimumFilmThicknessFromTheXAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngularPositionOfTheMinimumFilmThicknessFromTheXAxis
        return temp

    @property
    def critical_reynolds_number(self) -> 'float':
        """float: 'CriticalReynoldsNumber' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CriticalReynoldsNumber
        return temp

    @property
    def eccentricity_ratio(self) -> 'float':
        """float: 'EccentricityRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EccentricityRatio
        return temp

    @property
    def effective_film_temperature(self) -> 'float':
        """float: 'EffectiveFilmTemperature' is the original name of this property."""

        temp = self.wrapped.EffectiveFilmTemperature
        return temp

    @effective_film_temperature.setter
    def effective_film_temperature(self, value: 'float'):
        self.wrapped.EffectiveFilmTemperature = float(value) if value else 0.0

    @property
    def exit_flow(self) -> 'float':
        """float: 'ExitFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExitFlow
        return temp

    @property
    def feed_flow_rate(self) -> 'float':
        """float: 'FeedFlowRate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FeedFlowRate
        return temp

    @property
    def force_in_direction_of_eccentricity(self) -> 'float':
        """float: 'ForceInDirectionOfEccentricity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceInDirectionOfEccentricity
        return temp

    @property
    def hydrodynamic_preload_factor(self) -> 'float':
        """float: 'HydrodynamicPreloadFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HydrodynamicPreloadFactor
        return temp

    @property
    def inlet_flow(self) -> 'float':
        """float: 'InletFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InletFlow
        return temp

    @property
    def lubricant_density(self) -> 'float':
        """float: 'LubricantDensity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LubricantDensity
        return temp

    @property
    def lubricant_dynamic_viscosity(self) -> 'float':
        """float: 'LubricantDynamicViscosity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LubricantDynamicViscosity
        return temp

    @property
    def maximum_pad_eccentricity_ratio(self) -> 'float':
        """float: 'MaximumPadEccentricityRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumPadEccentricityRatio
        return temp

    @property
    def maximum_pressure(self) -> 'float':
        """float: 'MaximumPressure' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumPressure
        return temp

    @property
    def maximum_pressure_velocity(self) -> 'float':
        """float: 'MaximumPressureVelocity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumPressureVelocity
        return temp

    @property
    def minimum_film_thickness(self) -> 'float':
        """float: 'MinimumFilmThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumFilmThickness
        return temp

    @property
    def non_dimensional_friction(self) -> 'float':
        """float: 'NonDimensionalFriction' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NonDimensionalFriction
        return temp

    @property
    def non_dimensional_maximum_pressure(self) -> 'float':
        """float: 'NonDimensionalMaximumPressure' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NonDimensionalMaximumPressure
        return temp

    @property
    def non_dimensional_minimum_film_thickness(self) -> 'float':
        """float: 'NonDimensionalMinimumFilmThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NonDimensionalMinimumFilmThickness
        return temp

    @property
    def non_dimensional_out_flow(self) -> 'float':
        """float: 'NonDimensionalOutFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NonDimensionalOutFlow
        return temp

    @property
    def non_dimensional_side_flow(self) -> 'float':
        """float: 'NonDimensionalSideFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NonDimensionalSideFlow
        return temp

    @property
    def pad_shape_factor(self) -> 'float':
        """float: 'PadShapeFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PadShapeFactor
        return temp

    @property
    def relative_clearance(self) -> 'float':
        """float: 'RelativeClearance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeClearance
        return temp

    @property
    def reynolds_number(self) -> 'float':
        """float: 'ReynoldsNumber' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReynoldsNumber
        return temp

    @property
    def side_flow(self) -> 'float':
        """float: 'SideFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SideFlow
        return temp

    @property
    def sommerfeld_number(self) -> 'float':
        """float: 'SommerfeldNumber' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SommerfeldNumber
        return temp

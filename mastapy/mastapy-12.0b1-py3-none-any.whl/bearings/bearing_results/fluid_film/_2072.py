"""_2072.py

LoadedTiltingThrustPad
"""


from mastapy._internal import constructor
from mastapy.bearings.bearing_results.fluid_film import _2061
from mastapy._internal.python_net import python_net_import

_LOADED_TILTING_THRUST_PAD = python_net_import('SMT.MastaAPI.Bearings.BearingResults.FluidFilm', 'LoadedTiltingThrustPad')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedTiltingThrustPad',)


class LoadedTiltingThrustPad(_2061.LoadedFluidFilmBearingPad):
    """LoadedTiltingThrustPad

    This is a mastapy class.
    """

    TYPE = _LOADED_TILTING_THRUST_PAD

    __hash__ = None

    def __init__(self, instance_to_wrap: 'LoadedTiltingThrustPad.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def effective_film_kinematic_viscosity(self) -> 'float':
        """float: 'EffectiveFilmKinematicViscosity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EffectiveFilmKinematicViscosity
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
    def film_thickness_minimum(self) -> 'float':
        """float: 'FilmThicknessMinimum' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FilmThicknessMinimum
        return temp

    @property
    def film_thickness_at_pivot(self) -> 'float':
        """float: 'FilmThicknessAtPivot' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FilmThicknessAtPivot
        return temp

    @property
    def force(self) -> 'float':
        """float: 'Force' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Force
        return temp

    @property
    def lubricant_flow_at_leading_edge(self) -> 'float':
        """float: 'LubricantFlowAtLeadingEdge' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LubricantFlowAtLeadingEdge
        return temp

    @property
    def lubricant_flow_at_trailing_edge(self) -> 'float':
        """float: 'LubricantFlowAtTrailingEdge' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LubricantFlowAtTrailingEdge
        return temp

    @property
    def lubricant_side_flow(self) -> 'float':
        """float: 'LubricantSideFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LubricantSideFlow
        return temp

    @property
    def lubricant_temperature_at_leading_edge(self) -> 'float':
        """float: 'LubricantTemperatureAtLeadingEdge' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LubricantTemperatureAtLeadingEdge
        return temp

    @property
    def lubricant_temperature_at_trailing_edge(self) -> 'float':
        """float: 'LubricantTemperatureAtTrailingEdge' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LubricantTemperatureAtTrailingEdge
        return temp

    @property
    def power_loss(self) -> 'float':
        """float: 'PowerLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLoss
        return temp

    @property
    def pressure_velocity(self) -> 'float':
        """float: 'PressureVelocity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PressureVelocity
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
    def tilt(self) -> 'float':
        """float: 'Tilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Tilt
        return temp

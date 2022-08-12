"""_2067.py

LoadedPlainOilFedJournalBearing
"""


from mastapy._internal import constructor
from mastapy.bearings.bearing_results.fluid_film import _2065
from mastapy._internal.python_net import python_net_import

_LOADED_PLAIN_OIL_FED_JOURNAL_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingResults.FluidFilm', 'LoadedPlainOilFedJournalBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedPlainOilFedJournalBearing',)


class LoadedPlainOilFedJournalBearing(_2065.LoadedPlainJournalBearingResults):
    """LoadedPlainOilFedJournalBearing

    This is a mastapy class.
    """

    TYPE = _LOADED_PLAIN_OIL_FED_JOURNAL_BEARING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'LoadedPlainOilFedJournalBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_between_oil_feed_inlet_and_minimum_film_thickness(self) -> 'float':
        """float: 'AngleBetweenOilFeedInletAndMinimumFilmThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngleBetweenOilFeedInletAndMinimumFilmThickness
        return temp

    @property
    def angle_between_oil_feed_inlet_and_point_of_loading(self) -> 'float':
        """float: 'AngleBetweenOilFeedInletAndPointOfLoading' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngleBetweenOilFeedInletAndPointOfLoading
        return temp

    @property
    def combined_flow_rate(self) -> 'float':
        """float: 'CombinedFlowRate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CombinedFlowRate
        return temp

    @property
    def current_oil_inlet_angular_position_from_the_x_axis(self) -> 'float':
        """float: 'CurrentOilInletAngularPositionFromTheXAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentOilInletAngularPositionFromTheXAxis
        return temp

    @property
    def ideal_oil_inlet_angular_position_from_the_x_axis(self) -> 'float':
        """float: 'IdealOilInletAngularPositionFromTheXAxis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IdealOilInletAngularPositionFromTheXAxis
        return temp

    @property
    def oil_exit_temperature(self) -> 'float':
        """float: 'OilExitTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OilExitTemperature
        return temp

    @property
    def pressure_flow_rate(self) -> 'float':
        """float: 'PressureFlowRate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PressureFlowRate
        return temp

    @property
    def side_flow_rate(self) -> 'float':
        """float: 'SideFlowRate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SideFlowRate
        return temp

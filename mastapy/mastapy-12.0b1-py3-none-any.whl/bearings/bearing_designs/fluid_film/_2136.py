"""_2136.py

PlainOilFedJournalBearing
"""


from mastapy.bearings import _1836
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.bearings.bearing_designs.fluid_film import (
    _2125, _2126, _2127, _2134
)
from mastapy._internal.python_net import python_net_import

_PLAIN_OIL_FED_JOURNAL_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.FluidFilm', 'PlainOilFedJournalBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('PlainOilFedJournalBearing',)


class PlainOilFedJournalBearing(_2134.PlainJournalBearing):
    """PlainOilFedJournalBearing

    This is a mastapy class.
    """

    TYPE = _PLAIN_OIL_FED_JOURNAL_BEARING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PlainOilFedJournalBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def feed_type(self) -> '_1836.JournalOilFeedType':
        """JournalOilFeedType: 'FeedType' is the original name of this property."""

        temp = self.wrapped.FeedType
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1836.JournalOilFeedType)(value) if value is not None else None

    @feed_type.setter
    def feed_type(self, value: '_1836.JournalOilFeedType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.FeedType = value

    @property
    def land_width(self) -> 'float':
        """float: 'LandWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LandWidth
        return temp

    @property
    def number_of_axial_points_for_pressure_distribution(self) -> 'overridable.Overridable_int':
        """overridable.Overridable_int: 'NumberOfAxialPointsForPressureDistribution' is the original name of this property."""

        temp = self.wrapped.NumberOfAxialPointsForPressureDistribution
        return constructor.new_from_mastapy_type(overridable.Overridable_int)(temp) if temp is not None else None

    @number_of_axial_points_for_pressure_distribution.setter
    def number_of_axial_points_for_pressure_distribution(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0, is_overridden)
        self.wrapped.NumberOfAxialPointsForPressureDistribution = value

    @property
    def number_of_circumferential_points_for_pressure_distribution(self) -> 'overridable.Overridable_int':
        """overridable.Overridable_int: 'NumberOfCircumferentialPointsForPressureDistribution' is the original name of this property."""

        temp = self.wrapped.NumberOfCircumferentialPointsForPressureDistribution
        return constructor.new_from_mastapy_type(overridable.Overridable_int)(temp) if temp is not None else None

    @number_of_circumferential_points_for_pressure_distribution.setter
    def number_of_circumferential_points_for_pressure_distribution(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0, is_overridden)
        self.wrapped.NumberOfCircumferentialPointsForPressureDistribution = value

    @property
    def axial_groove_oil_feed(self) -> '_2125.AxialGrooveJournalBearing':
        """AxialGrooveJournalBearing: 'AxialGrooveOilFeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialGrooveOilFeed
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def axial_hole_oil_feed(self) -> '_2126.AxialHoleJournalBearing':
        """AxialHoleJournalBearing: 'AxialHoleOilFeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialHoleOilFeed
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def circumferential_groove_oil_feed(self) -> '_2127.CircumferentialFeedJournalBearing':
        """CircumferentialFeedJournalBearing: 'CircumferentialGrooveOilFeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CircumferentialGrooveOilFeed
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

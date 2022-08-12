"""_1928.py

LoadedAngularContactBallBearingRow
"""


from mastapy.bearings.bearing_results.rolling import _1927, _1930, _1947
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_ANGULAR_CONTACT_BALL_BEARING_ROW = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedAngularContactBallBearingRow')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedAngularContactBallBearingRow',)


class LoadedAngularContactBallBearingRow(_1947.LoadedBallBearingRow):
    """LoadedAngularContactBallBearingRow

    This is a mastapy class.
    """

    TYPE = _LOADED_ANGULAR_CONTACT_BALL_BEARING_ROW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'LoadedAngularContactBallBearingRow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def loaded_bearing(self) -> '_1927.LoadedAngularContactBallBearingResults':
        """LoadedAngularContactBallBearingResults: 'LoadedBearing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedBearing
        if _1927.LoadedAngularContactBallBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast loaded_bearing to LoadedAngularContactBallBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

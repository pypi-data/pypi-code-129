"""_5773.py

DatapointForResponseOfANodeAtAFrequencyOnAHarmonic
"""


from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_DATAPOINT_FOR_RESPONSE_OF_A_NODE_AT_A_FREQUENCY_ON_A_HARMONIC = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults', 'DatapointForResponseOfANodeAtAFrequencyOnAHarmonic')


__docformat__ = 'restructuredtext en'
__all__ = ('DatapointForResponseOfANodeAtAFrequencyOnAHarmonic',)


class DatapointForResponseOfANodeAtAFrequencyOnAHarmonic(_0.APIBase):
    """DatapointForResponseOfANodeAtAFrequencyOnAHarmonic

    This is a mastapy class.
    """

    TYPE = _DATAPOINT_FOR_RESPONSE_OF_A_NODE_AT_A_FREQUENCY_ON_A_HARMONIC

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DatapointForResponseOfANodeAtAFrequencyOnAHarmonic.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angular_magnitude(self) -> 'float':
        """float: 'AngularMagnitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngularMagnitude
        return temp

    @property
    def angular_radial_magnitude(self) -> 'float':
        """float: 'AngularRadialMagnitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngularRadialMagnitude
        return temp

    @property
    def frequency(self) -> 'float':
        """float: 'Frequency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Frequency
        return temp

    @property
    def linear_magnitude(self) -> 'float':
        """float: 'LinearMagnitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LinearMagnitude
        return temp

    @property
    def radial_magnitude(self) -> 'float':
        """float: 'RadialMagnitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadialMagnitude
        return temp

    @property
    def speed(self) -> 'float':
        """float: 'Speed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Speed
        return temp

    @property
    def theta_x(self) -> 'complex':
        """complex: 'ThetaX' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ThetaX
        value = conversion.pn_to_mp_complex(temp)
        return value

    @property
    def theta_y(self) -> 'complex':
        """complex: 'ThetaY' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ThetaY
        value = conversion.pn_to_mp_complex(temp)
        return value

    @property
    def theta_z(self) -> 'complex':
        """complex: 'ThetaZ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ThetaZ
        value = conversion.pn_to_mp_complex(temp)
        return value

    @property
    def x(self) -> 'complex':
        """complex: 'X' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.X
        value = conversion.pn_to_mp_complex(temp)
        return value

    @property
    def y(self) -> 'complex':
        """complex: 'Y' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Y
        value = conversion.pn_to_mp_complex(temp)
        return value

    @property
    def z(self) -> 'complex':
        """complex: 'Z' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Z
        value = conversion.pn_to_mp_complex(temp)
        return value

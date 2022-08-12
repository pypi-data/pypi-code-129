"""_1131.py

ISO1328AccuracyGrader
"""


from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1132
from mastapy._internal.python_net import python_net_import

_ISO1328_ACCURACY_GRADER = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances', 'ISO1328AccuracyGrader')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO1328AccuracyGrader',)


class ISO1328AccuracyGrader(_1132.ISO1328AccuracyGraderCommon):
    """ISO1328AccuracyGrader

    This is a mastapy class.
    """

    TYPE = _ISO1328_ACCURACY_GRADER

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ISO1328AccuracyGrader.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cumulative_pitch_deviation(self) -> 'float':
        """float: 'CumulativePitchDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CumulativePitchDeviation
        return temp

    @property
    def helix_form_deviation(self) -> 'float':
        """float: 'HelixFormDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixFormDeviation
        return temp

    @property
    def helix_slope_deviation(self) -> 'float':
        """float: 'HelixSlopeDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixSlopeDeviation
        return temp

    @property
    def profile_form_deviation(self) -> 'float':
        """float: 'ProfileFormDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileFormDeviation
        return temp

    @property
    def profile_slope_deviation(self) -> 'float':
        """float: 'ProfileSlopeDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileSlopeDeviation
        return temp

    @property
    def runout(self) -> 'float':
        """float: 'Runout' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Runout
        return temp

    @property
    def single_pitch_deviation_iso(self) -> 'float':
        """float: 'SinglePitchDeviationISO' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SinglePitchDeviationISO
        return temp

    @property
    def toothto_tooth_radial_composite_deviation(self) -> 'float':
        """float: 'ToothtoToothRadialCompositeDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothtoToothRadialCompositeDeviation
        return temp

    @property
    def total_cumulative_pitch_deviation(self) -> 'float':
        """float: 'TotalCumulativePitchDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalCumulativePitchDeviation
        return temp

    @property
    def total_helix_deviation(self) -> 'float':
        """float: 'TotalHelixDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalHelixDeviation
        return temp

    @property
    def total_profile_deviation(self) -> 'float':
        """float: 'TotalProfileDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalProfileDeviation
        return temp

    @property
    def total_radial_composite_deviation(self) -> 'float':
        """float: 'TotalRadialCompositeDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalRadialCompositeDeviation
        return temp

"""_1130.py

ISO13282013AccuracyGrader
"""


from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical.accuracy_and_tolerances import _1132
from mastapy._internal.python_net import python_net_import

_ISO13282013_ACCURACY_GRADER = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.AccuracyAndTolerances', 'ISO13282013AccuracyGrader')


__docformat__ = 'restructuredtext en'
__all__ = ('ISO13282013AccuracyGrader',)


class ISO13282013AccuracyGrader(_1132.ISO1328AccuracyGraderCommon):
    """ISO13282013AccuracyGrader

    This is a mastapy class.
    """

    TYPE = _ISO13282013_ACCURACY_GRADER

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ISO13282013AccuracyGrader.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def adjacent_pitch_difference_tolerance(self) -> 'float':
        """float: 'AdjacentPitchDifferenceTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdjacentPitchDifferenceTolerance
        return temp

    @property
    def cumulative_pitch_index_tolerance(self) -> 'float':
        """float: 'CumulativePitchIndexTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CumulativePitchIndexTolerance
        return temp

    @property
    def helix_form_tolerance(self) -> 'float':
        """float: 'HelixFormTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixFormTolerance
        return temp

    @property
    def helix_slope_tolerance(self) -> 'float':
        """float: 'HelixSlopeTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixSlopeTolerance
        return temp

    @property
    def profile_form_tolerance(self) -> 'float':
        """float: 'ProfileFormTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileFormTolerance
        return temp

    @property
    def profile_slope_tolerance(self) -> 'float':
        """float: 'ProfileSlopeTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileSlopeTolerance
        return temp

    @property
    def runout_tolerance(self) -> 'float':
        """float: 'RunoutTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RunoutTolerance
        return temp

    @property
    def sector_pitch_deviation_tolerance(self) -> 'float':
        """float: 'SectorPitchDeviationTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SectorPitchDeviationTolerance
        return temp

    @property
    def single_pitch_tolerance(self) -> 'float':
        """float: 'SinglePitchTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SinglePitchTolerance
        return temp

    @property
    def toothto_tooth_radial_composite_tolerance(self) -> 'float':
        """float: 'ToothtoToothRadialCompositeTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothtoToothRadialCompositeTolerance
        return temp

    @property
    def total_helix_tolerance(self) -> 'float':
        """float: 'TotalHelixTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalHelixTolerance
        return temp

    @property
    def total_profile_tolerance(self) -> 'float':
        """float: 'TotalProfileTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalProfileTolerance
        return temp

    @property
    def total_radial_composite_tolerance(self) -> 'float':
        """float: 'TotalRadialCompositeTolerance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalRadialCompositeTolerance
        return temp

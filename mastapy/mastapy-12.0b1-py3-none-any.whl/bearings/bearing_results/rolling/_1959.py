"""_1959.py

LoadedFourPointContactBallBearingElement
"""


from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _1963
from mastapy._internal.python_net import python_net_import

_LOADED_FOUR_POINT_CONTACT_BALL_BEARING_ELEMENT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedFourPointContactBallBearingElement')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedFourPointContactBallBearingElement',)


class LoadedFourPointContactBallBearingElement(_1963.LoadedMultiPointContactBallBearingElement):
    """LoadedFourPointContactBallBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_FOUR_POINT_CONTACT_BALL_BEARING_ELEMENT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'LoadedFourPointContactBallBearingElement.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def approximate_percentage_of_friction_used_outer_left(self) -> 'float':
        """float: 'ApproximatePercentageOfFrictionUsedOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ApproximatePercentageOfFrictionUsedOuterLeft
        return temp

    @property
    def approximate_percentage_of_friction_used_outer_right(self) -> 'float':
        """float: 'ApproximatePercentageOfFrictionUsedOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ApproximatePercentageOfFrictionUsedOuterRight
        return temp

    @property
    def contact_angle_outer_left(self) -> 'float':
        """float: 'ContactAngleOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactAngleOuterLeft
        return temp

    @property
    def contact_angle_outer_right(self) -> 'float':
        """float: 'ContactAngleOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactAngleOuterRight
        return temp

    @property
    def curvature_moment_outer_left(self) -> 'float':
        """float: 'CurvatureMomentOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurvatureMomentOuterLeft
        return temp

    @property
    def curvature_moment_outer_right(self) -> 'float':
        """float: 'CurvatureMomentOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurvatureMomentOuterRight
        return temp

    @property
    def hertzian_semi_major_dimension_outer_left(self) -> 'float':
        """float: 'HertzianSemiMajorDimensionOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianSemiMajorDimensionOuterLeft
        return temp

    @property
    def hertzian_semi_major_dimension_outer_right(self) -> 'float':
        """float: 'HertzianSemiMajorDimensionOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianSemiMajorDimensionOuterRight
        return temp

    @property
    def hertzian_semi_minor_dimension_outer_left(self) -> 'float':
        """float: 'HertzianSemiMinorDimensionOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianSemiMinorDimensionOuterLeft
        return temp

    @property
    def hertzian_semi_minor_dimension_outer_right(self) -> 'float':
        """float: 'HertzianSemiMinorDimensionOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianSemiMinorDimensionOuterRight
        return temp

    @property
    def hydrodynamic_rolling_resistance_force_outer_left(self) -> 'float':
        """float: 'HydrodynamicRollingResistanceForceOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HydrodynamicRollingResistanceForceOuterLeft
        return temp

    @property
    def hydrodynamic_rolling_resistance_force_outer_right(self) -> 'float':
        """float: 'HydrodynamicRollingResistanceForceOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HydrodynamicRollingResistanceForceOuterRight
        return temp

    @property
    def maximum_normal_stress_outer_left(self) -> 'float':
        """float: 'MaximumNormalStressOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalStressOuterLeft
        return temp

    @property
    def maximum_normal_stress_outer_right(self) -> 'float':
        """float: 'MaximumNormalStressOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalStressOuterRight
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
    def maximum_shear_stress_outer_left(self) -> 'float':
        """float: 'MaximumShearStressOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumShearStressOuterLeft
        return temp

    @property
    def maximum_shear_stress_outer_right(self) -> 'float':
        """float: 'MaximumShearStressOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumShearStressOuterRight
        return temp

    @property
    def maximum_smearing_intensity_outer(self) -> 'float':
        """float: 'MaximumSmearingIntensityOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumSmearingIntensityOuter
        return temp

    @property
    def minimum_lubricating_film_thickness_outer_left(self) -> 'float':
        """float: 'MinimumLubricatingFilmThicknessOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumLubricatingFilmThicknessOuterLeft
        return temp

    @property
    def minimum_lubricating_film_thickness_outer_right(self) -> 'float':
        """float: 'MinimumLubricatingFilmThicknessOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumLubricatingFilmThicknessOuterRight
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
    def normal_load_outer_left(self) -> 'float':
        """float: 'NormalLoadOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalLoadOuterLeft
        return temp

    @property
    def normal_load_outer_right(self) -> 'float':
        """float: 'NormalLoadOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalLoadOuterRight
        return temp

    @property
    def pivoting_moment_outer_left(self) -> 'float':
        """float: 'PivotingMomentOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PivotingMomentOuterLeft
        return temp

    @property
    def pivoting_moment_outer_right(self) -> 'float':
        """float: 'PivotingMomentOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PivotingMomentOuterRight
        return temp

    @property
    def power_loss_outer_left(self) -> 'float':
        """float: 'PowerLossOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossOuterLeft
        return temp

    @property
    def power_loss_outer_right(self) -> 'float':
        """float: 'PowerLossOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossOuterRight
        return temp

    @property
    def sliding_force_parallel_to_the_major_axis_outer_left(self) -> 'float':
        """float: 'SlidingForceParallelToTheMajorAxisOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingForceParallelToTheMajorAxisOuterLeft
        return temp

    @property
    def sliding_force_parallel_to_the_major_axis_outer_right(self) -> 'float':
        """float: 'SlidingForceParallelToTheMajorAxisOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingForceParallelToTheMajorAxisOuterRight
        return temp

    @property
    def sliding_force_parallel_to_the_minor_axis_outer_left(self) -> 'float':
        """float: 'SlidingForceParallelToTheMinorAxisOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingForceParallelToTheMinorAxisOuterLeft
        return temp

    @property
    def sliding_force_parallel_to_the_minor_axis_outer_right(self) -> 'float':
        """float: 'SlidingForceParallelToTheMinorAxisOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingForceParallelToTheMinorAxisOuterRight
        return temp

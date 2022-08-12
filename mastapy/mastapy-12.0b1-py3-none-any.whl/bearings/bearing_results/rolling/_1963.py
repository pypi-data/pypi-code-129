"""_1963.py

LoadedMultiPointContactBallBearingElement
"""


from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling import _1944
from mastapy._internal.python_net import python_net_import

_LOADED_MULTI_POINT_CONTACT_BALL_BEARING_ELEMENT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedMultiPointContactBallBearingElement')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedMultiPointContactBallBearingElement',)


class LoadedMultiPointContactBallBearingElement(_1944.LoadedBallBearingElement):
    """LoadedMultiPointContactBallBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_MULTI_POINT_CONTACT_BALL_BEARING_ELEMENT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'LoadedMultiPointContactBallBearingElement.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def approximate_percentage_of_friction_used_inner_left(self) -> 'float':
        """float: 'ApproximatePercentageOfFrictionUsedInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ApproximatePercentageOfFrictionUsedInnerLeft
        return temp

    @property
    def approximate_percentage_of_friction_used_inner_right(self) -> 'float':
        """float: 'ApproximatePercentageOfFrictionUsedInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ApproximatePercentageOfFrictionUsedInnerRight
        return temp

    @property
    def contact_angle_inner_left(self) -> 'float':
        """float: 'ContactAngleInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactAngleInnerLeft
        return temp

    @property
    def contact_angle_inner_right(self) -> 'float':
        """float: 'ContactAngleInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactAngleInnerRight
        return temp

    @property
    def curvature_moment_inner_left(self) -> 'float':
        """float: 'CurvatureMomentInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurvatureMomentInnerLeft
        return temp

    @property
    def curvature_moment_inner_right(self) -> 'float':
        """float: 'CurvatureMomentInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurvatureMomentInnerRight
        return temp

    @property
    def hertzian_semi_major_dimension_inner_left(self) -> 'float':
        """float: 'HertzianSemiMajorDimensionInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianSemiMajorDimensionInnerLeft
        return temp

    @property
    def hertzian_semi_major_dimension_inner_right(self) -> 'float':
        """float: 'HertzianSemiMajorDimensionInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianSemiMajorDimensionInnerRight
        return temp

    @property
    def hertzian_semi_minor_dimension_inner_left(self) -> 'float':
        """float: 'HertzianSemiMinorDimensionInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianSemiMinorDimensionInnerLeft
        return temp

    @property
    def hertzian_semi_minor_dimension_inner_right(self) -> 'float':
        """float: 'HertzianSemiMinorDimensionInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianSemiMinorDimensionInnerRight
        return temp

    @property
    def hydrodynamic_rolling_resistance_force_inner_left(self) -> 'float':
        """float: 'HydrodynamicRollingResistanceForceInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HydrodynamicRollingResistanceForceInnerLeft
        return temp

    @property
    def hydrodynamic_rolling_resistance_force_inner_right(self) -> 'float':
        """float: 'HydrodynamicRollingResistanceForceInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HydrodynamicRollingResistanceForceInnerRight
        return temp

    @property
    def maximum_normal_stress_inner_left(self) -> 'float':
        """float: 'MaximumNormalStressInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalStressInnerLeft
        return temp

    @property
    def maximum_normal_stress_inner_right(self) -> 'float':
        """float: 'MaximumNormalStressInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalStressInnerRight
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
    def maximum_shear_stress_inner_left(self) -> 'float':
        """float: 'MaximumShearStressInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumShearStressInnerLeft
        return temp

    @property
    def maximum_shear_stress_inner_right(self) -> 'float':
        """float: 'MaximumShearStressInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumShearStressInnerRight
        return temp

    @property
    def maximum_smearing_intensity_inner(self) -> 'float':
        """float: 'MaximumSmearingIntensityInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumSmearingIntensityInner
        return temp

    @property
    def minimum_lubricating_film_thickness_inner_left(self) -> 'float':
        """float: 'MinimumLubricatingFilmThicknessInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumLubricatingFilmThicknessInnerLeft
        return temp

    @property
    def minimum_lubricating_film_thickness_inner_right(self) -> 'float':
        """float: 'MinimumLubricatingFilmThicknessInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumLubricatingFilmThicknessInnerRight
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
    def normal_load_inner_left(self) -> 'float':
        """float: 'NormalLoadInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalLoadInnerLeft
        return temp

    @property
    def normal_load_inner_right(self) -> 'float':
        """float: 'NormalLoadInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalLoadInnerRight
        return temp

    @property
    def pivoting_moment_inner_left(self) -> 'float':
        """float: 'PivotingMomentInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PivotingMomentInnerLeft
        return temp

    @property
    def pivoting_moment_inner_right(self) -> 'float':
        """float: 'PivotingMomentInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PivotingMomentInnerRight
        return temp

    @property
    def power_loss_inner_left(self) -> 'float':
        """float: 'PowerLossInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossInnerLeft
        return temp

    @property
    def power_loss_inner_right(self) -> 'float':
        """float: 'PowerLossInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossInnerRight
        return temp

    @property
    def sliding_force_parallel_to_the_major_axis_inner_left(self) -> 'float':
        """float: 'SlidingForceParallelToTheMajorAxisInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingForceParallelToTheMajorAxisInnerLeft
        return temp

    @property
    def sliding_force_parallel_to_the_major_axis_inner_right(self) -> 'float':
        """float: 'SlidingForceParallelToTheMajorAxisInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingForceParallelToTheMajorAxisInnerRight
        return temp

    @property
    def sliding_force_parallel_to_the_minor_axis_inner_left(self) -> 'float':
        """float: 'SlidingForceParallelToTheMinorAxisInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingForceParallelToTheMinorAxisInnerLeft
        return temp

    @property
    def sliding_force_parallel_to_the_minor_axis_inner_right(self) -> 'float':
        """float: 'SlidingForceParallelToTheMinorAxisInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingForceParallelToTheMinorAxisInnerRight
        return temp

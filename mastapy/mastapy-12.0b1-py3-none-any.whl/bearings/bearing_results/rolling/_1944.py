"""_1944.py

LoadedBallBearingElement
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_results.rolling import _1916, _1958
from mastapy._internal.python_net import python_net_import

_LOADED_BALL_BEARING_ELEMENT = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling', 'LoadedBallBearingElement')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedBallBearingElement',)


class LoadedBallBearingElement(_1958.LoadedElement):
    """LoadedBallBearingElement

    This is a mastapy class.
    """

    TYPE = _LOADED_BALL_BEARING_ELEMENT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'LoadedBallBearingElement.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angular_velocity(self) -> 'float':
        """float: 'AngularVelocity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngularVelocity
        return temp

    @property
    def approximate_percentage_of_friction_used_inner(self) -> 'float':
        """float: 'ApproximatePercentageOfFrictionUsedInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ApproximatePercentageOfFrictionUsedInner
        return temp

    @property
    def approximate_percentage_of_friction_used_outer(self) -> 'float':
        """float: 'ApproximatePercentageOfFrictionUsedOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ApproximatePercentageOfFrictionUsedOuter
        return temp

    @property
    def arc_distance_of_inner_left_raceway_inside_edge_to_hertzian_contact(self) -> 'float':
        """float: 'ArcDistanceOfInnerLeftRacewayInsideEdgeToHertzianContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ArcDistanceOfInnerLeftRacewayInsideEdgeToHertzianContact
        return temp

    @property
    def arc_distance_of_inner_raceway_inner_edge_to_hertzian_contact(self) -> 'float':
        """float: 'ArcDistanceOfInnerRacewayInnerEdgeToHertzianContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ArcDistanceOfInnerRacewayInnerEdgeToHertzianContact
        return temp

    @property
    def arc_distance_of_inner_raceway_left_edge_to_hertzian_contact(self) -> 'float':
        """float: 'ArcDistanceOfInnerRacewayLeftEdgeToHertzianContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ArcDistanceOfInnerRacewayLeftEdgeToHertzianContact
        return temp

    @property
    def arc_distance_of_inner_raceway_outer_edge_to_hertzian_contact(self) -> 'float':
        """float: 'ArcDistanceOfInnerRacewayOuterEdgeToHertzianContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ArcDistanceOfInnerRacewayOuterEdgeToHertzianContact
        return temp

    @property
    def arc_distance_of_inner_raceway_right_edge_to_hertzian_contact(self) -> 'float':
        """float: 'ArcDistanceOfInnerRacewayRightEdgeToHertzianContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ArcDistanceOfInnerRacewayRightEdgeToHertzianContact
        return temp

    @property
    def arc_distance_of_inner_right_raceway_inside_edge_to_hertzian_contact(self) -> 'float':
        """float: 'ArcDistanceOfInnerRightRacewayInsideEdgeToHertzianContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ArcDistanceOfInnerRightRacewayInsideEdgeToHertzianContact
        return temp

    @property
    def arc_distance_of_outer_left_raceway_inside_edge_to_hertzian_contact(self) -> 'float':
        """float: 'ArcDistanceOfOuterLeftRacewayInsideEdgeToHertzianContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ArcDistanceOfOuterLeftRacewayInsideEdgeToHertzianContact
        return temp

    @property
    def arc_distance_of_outer_raceway_inner_edge_to_hertzian_contact(self) -> 'float':
        """float: 'ArcDistanceOfOuterRacewayInnerEdgeToHertzianContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ArcDistanceOfOuterRacewayInnerEdgeToHertzianContact
        return temp

    @property
    def arc_distance_of_outer_raceway_left_edge_to_hertzian_contact(self) -> 'float':
        """float: 'ArcDistanceOfOuterRacewayLeftEdgeToHertzianContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ArcDistanceOfOuterRacewayLeftEdgeToHertzianContact
        return temp

    @property
    def arc_distance_of_outer_raceway_outer_edge_to_hertzian_contact(self) -> 'float':
        """float: 'ArcDistanceOfOuterRacewayOuterEdgeToHertzianContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ArcDistanceOfOuterRacewayOuterEdgeToHertzianContact
        return temp

    @property
    def arc_distance_of_outer_raceway_right_edge_to_hertzian_contact(self) -> 'float':
        """float: 'ArcDistanceOfOuterRacewayRightEdgeToHertzianContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ArcDistanceOfOuterRacewayRightEdgeToHertzianContact
        return temp

    @property
    def arc_distance_of_outer_right_raceway_inside_edge_to_hertzian_contact(self) -> 'float':
        """float: 'ArcDistanceOfOuterRightRacewayInsideEdgeToHertzianContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ArcDistanceOfOuterRightRacewayInsideEdgeToHertzianContact
        return temp

    @property
    def centrifugal_force(self) -> 'float':
        """float: 'CentrifugalForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CentrifugalForce
        return temp

    @property
    def contact_angle_inner(self) -> 'float':
        """float: 'ContactAngleInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactAngleInner
        return temp

    @property
    def contact_angle_outer(self) -> 'float':
        """float: 'ContactAngleOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactAngleOuter
        return temp

    @property
    def curvature_moment_inner(self) -> 'float':
        """float: 'CurvatureMomentInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurvatureMomentInner
        return temp

    @property
    def curvature_moment_outer(self) -> 'float':
        """float: 'CurvatureMomentOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurvatureMomentOuter
        return temp

    @property
    def depth_of_maximum_shear_stress_inner(self) -> 'float':
        """float: 'DepthOfMaximumShearStressInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DepthOfMaximumShearStressInner
        return temp

    @property
    def depth_of_maximum_shear_stress_outer(self) -> 'float':
        """float: 'DepthOfMaximumShearStressOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DepthOfMaximumShearStressOuter
        return temp

    @property
    def difference_between_cage_speed_and_orbit_speed(self) -> 'float':
        """float: 'DifferenceBetweenCageSpeedAndOrbitSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DifferenceBetweenCageSpeedAndOrbitSpeed
        return temp

    @property
    def gyroscopic_moment(self) -> 'float':
        """float: 'GyroscopicMoment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GyroscopicMoment
        return temp

    @property
    def gyroscopic_moment_about_radial_direction(self) -> 'float':
        """float: 'GyroscopicMomentAboutRadialDirection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GyroscopicMomentAboutRadialDirection
        return temp

    @property
    def gyroscopic_speed(self) -> 'float':
        """float: 'GyroscopicSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GyroscopicSpeed
        return temp

    @property
    def hertzian_ellipse_major_2b_track_truncation_inner_left_race_inside_edge(self) -> 'float':
        """float: 'HertzianEllipseMajor2bTrackTruncationInnerLeftRaceInsideEdge' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianEllipseMajor2bTrackTruncationInnerLeftRaceInsideEdge
        return temp

    @property
    def hertzian_ellipse_major_2b_track_truncation_inner_left(self) -> 'float':
        """float: 'HertzianEllipseMajor2bTrackTruncationInnerLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianEllipseMajor2bTrackTruncationInnerLeft
        return temp

    @property
    def hertzian_ellipse_major_2b_track_truncation_inner_race_inner_edge(self) -> 'float':
        """float: 'HertzianEllipseMajor2bTrackTruncationInnerRaceInnerEdge' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianEllipseMajor2bTrackTruncationInnerRaceInnerEdge
        return temp

    @property
    def hertzian_ellipse_major_2b_track_truncation_inner_race_outer_edge(self) -> 'float':
        """float: 'HertzianEllipseMajor2bTrackTruncationInnerRaceOuterEdge' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianEllipseMajor2bTrackTruncationInnerRaceOuterEdge
        return temp

    @property
    def hertzian_ellipse_major_2b_track_truncation_inner_right_race_inside_edge(self) -> 'float':
        """float: 'HertzianEllipseMajor2bTrackTruncationInnerRightRaceInsideEdge' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianEllipseMajor2bTrackTruncationInnerRightRaceInsideEdge
        return temp

    @property
    def hertzian_ellipse_major_2b_track_truncation_inner_right(self) -> 'float':
        """float: 'HertzianEllipseMajor2bTrackTruncationInnerRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianEllipseMajor2bTrackTruncationInnerRight
        return temp

    @property
    def hertzian_ellipse_major_2b_track_truncation_outer_left_race_inside_edge(self) -> 'float':
        """float: 'HertzianEllipseMajor2bTrackTruncationOuterLeftRaceInsideEdge' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianEllipseMajor2bTrackTruncationOuterLeftRaceInsideEdge
        return temp

    @property
    def hertzian_ellipse_major_2b_track_truncation_outer_left(self) -> 'float':
        """float: 'HertzianEllipseMajor2bTrackTruncationOuterLeft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianEllipseMajor2bTrackTruncationOuterLeft
        return temp

    @property
    def hertzian_ellipse_major_2b_track_truncation_outer_race_inner_edge(self) -> 'float':
        """float: 'HertzianEllipseMajor2bTrackTruncationOuterRaceInnerEdge' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianEllipseMajor2bTrackTruncationOuterRaceInnerEdge
        return temp

    @property
    def hertzian_ellipse_major_2b_track_truncation_outer_race_outer_edge(self) -> 'float':
        """float: 'HertzianEllipseMajor2bTrackTruncationOuterRaceOuterEdge' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianEllipseMajor2bTrackTruncationOuterRaceOuterEdge
        return temp

    @property
    def hertzian_ellipse_major_2b_track_truncation_outer_right_race_inside_edge(self) -> 'float':
        """float: 'HertzianEllipseMajor2bTrackTruncationOuterRightRaceInsideEdge' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianEllipseMajor2bTrackTruncationOuterRightRaceInsideEdge
        return temp

    @property
    def hertzian_ellipse_major_2b_track_truncation_outer_right(self) -> 'float':
        """float: 'HertzianEllipseMajor2bTrackTruncationOuterRight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianEllipseMajor2bTrackTruncationOuterRight
        return temp

    @property
    def hertzian_semi_major_dimension_inner(self) -> 'float':
        """float: 'HertzianSemiMajorDimensionInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianSemiMajorDimensionInner
        return temp

    @property
    def hertzian_semi_major_dimension_outer(self) -> 'float':
        """float: 'HertzianSemiMajorDimensionOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianSemiMajorDimensionOuter
        return temp

    @property
    def hertzian_semi_minor_dimension_inner(self) -> 'float':
        """float: 'HertzianSemiMinorDimensionInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianSemiMinorDimensionInner
        return temp

    @property
    def hertzian_semi_minor_dimension_outer(self) -> 'float':
        """float: 'HertzianSemiMinorDimensionOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HertzianSemiMinorDimensionOuter
        return temp

    @property
    def hydrodynamic_rolling_resistance_force_inner(self) -> 'float':
        """float: 'HydrodynamicRollingResistanceForceInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HydrodynamicRollingResistanceForceInner
        return temp

    @property
    def hydrodynamic_rolling_resistance_force_outer(self) -> 'float':
        """float: 'HydrodynamicRollingResistanceForceOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HydrodynamicRollingResistanceForceOuter
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
    def maximum_normal_stress_outer(self) -> 'float':
        """float: 'MaximumNormalStressOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumNormalStressOuter
        return temp

    @property
    def maximum_shear_stress_inner(self) -> 'float':
        """float: 'MaximumShearStressInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumShearStressInner
        return temp

    @property
    def maximum_shear_stress_outer(self) -> 'float':
        """float: 'MaximumShearStressOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumShearStressOuter
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
    def maximum_smearing_intensity_outer(self) -> 'float':
        """float: 'MaximumSmearingIntensityOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumSmearingIntensityOuter
        return temp

    @property
    def number_of_contact_points(self) -> 'int':
        """int: 'NumberOfContactPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfContactPoints
        return temp

    @property
    def orbit_speed_ignoring_cage(self) -> 'float':
        """float: 'OrbitSpeedIgnoringCage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OrbitSpeedIgnoringCage
        return temp

    @property
    def pitch_angle(self) -> 'float':
        """float: 'PitchAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PitchAngle
        return temp

    @property
    def pivoting_moment_inner(self) -> 'float':
        """float: 'PivotingMomentInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PivotingMomentInner
        return temp

    @property
    def pivoting_moment_outer(self) -> 'float':
        """float: 'PivotingMomentOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PivotingMomentOuter
        return temp

    @property
    def power_loss_inner(self) -> 'float':
        """float: 'PowerLossInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossInner
        return temp

    @property
    def power_loss_outer(self) -> 'float':
        """float: 'PowerLossOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossOuter
        return temp

    @property
    def power_loss_total(self) -> 'float':
        """float: 'PowerLossTotal' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLossTotal
        return temp

    @property
    def sliding_force_parallel_to_the_major_axis_inner(self) -> 'float':
        """float: 'SlidingForceParallelToTheMajorAxisInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingForceParallelToTheMajorAxisInner
        return temp

    @property
    def sliding_force_parallel_to_the_major_axis_outer(self) -> 'float':
        """float: 'SlidingForceParallelToTheMajorAxisOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingForceParallelToTheMajorAxisOuter
        return temp

    @property
    def sliding_force_parallel_to_the_minor_axis_inner(self) -> 'float':
        """float: 'SlidingForceParallelToTheMinorAxisInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingForceParallelToTheMinorAxisInner
        return temp

    @property
    def sliding_force_parallel_to_the_minor_axis_outer(self) -> 'float':
        """float: 'SlidingForceParallelToTheMinorAxisOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingForceParallelToTheMinorAxisOuter
        return temp

    @property
    def smallest_arc_distance_of_raceway_edge_to_hertzian_contact(self) -> 'float':
        """float: 'SmallestArcDistanceOfRacewayEdgeToHertzianContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmallestArcDistanceOfRacewayEdgeToHertzianContact
        return temp

    @property
    def smearing_safety_factor(self) -> 'float':
        """float: 'SmearingSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmearingSafetyFactor
        return temp

    @property
    def spinto_roll_ratio_inner(self) -> 'float':
        """float: 'SpintoRollRatioInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpintoRollRatioInner
        return temp

    @property
    def spinto_roll_ratio_outer(self) -> 'float':
        """float: 'SpintoRollRatioOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpintoRollRatioOuter
        return temp

    @property
    def surface_velocity(self) -> 'float':
        """float: 'SurfaceVelocity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SurfaceVelocity
        return temp

    @property
    def track_truncation_occurring_beyond_permissible_limit(self) -> 'bool':
        """bool: 'TrackTruncationOccurringBeyondPermissibleLimit' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TrackTruncationOccurringBeyondPermissibleLimit
        return temp

    @property
    def worst_hertzian_ellipse_major_2b_track_truncation(self) -> 'float':
        """float: 'WorstHertzianEllipseMajor2bTrackTruncation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorstHertzianEllipseMajor2bTrackTruncation
        return temp

    @property
    def yaw_angle(self) -> 'float':
        """float: 'YawAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.YawAngle
        return temp

    @property
    def inner_race_contact_geometries(self) -> 'List[_1916.BallBearingRaceContactGeometry]':
        """List[BallBearingRaceContactGeometry]: 'InnerRaceContactGeometries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRaceContactGeometries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def outer_race_contact_geometries(self) -> 'List[_1916.BallBearingRaceContactGeometry]':
        """List[BallBearingRaceContactGeometry]: 'OuterRaceContactGeometries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRaceContactGeometries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

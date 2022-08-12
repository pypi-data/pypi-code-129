"""_2632.py

BearingSystemDeflection
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy._math.vector_2d import Vector2D
from mastapy._math.vector_3d import Vector3D
from mastapy.utility_gui.charts import (
    _1815, _1805, _1810, _1812
)
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model import _2380, _2381
from mastapy.bearings.bearing_results import (
    _1897, _1899, _1900, _1901,
    _1902, _1903, _1905, _1890
)
from mastapy.bearings.bearing_results.rolling import (
    _1927, _1930, _1933, _1938,
    _1941, _1946, _1949, _1953,
    _1956, _1961, _1965, _1968,
    _1973, _1977, _1980, _1984,
    _1987, _1992, _1995, _1998,
    _2001
)
from mastapy.bearings.bearing_results.fluid_film import (
    _2062, _2063, _2064, _2065,
    _2067, _2070, _2071
)
from mastapy.system_model.analyses_and_results.static_loads import _6734
from mastapy.system_model.analyses_and_results.power_flows import _3972
from mastapy.math_utility.measured_vectors import _1520
from mastapy.system_model.analyses_and_results.system_deflections import _2662
from mastapy._internal.python_net import python_net_import

_BEARING_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'BearingSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingSystemDeflection',)


class BearingSystemDeflection(_2662.ConnectorSystemDeflection):
    """BearingSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEARING_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BearingSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_stiffness(self) -> 'float':
        """float: 'AxialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialStiffness
        return temp

    @property
    def component_angular_displacements(self) -> 'List[Vector2D]':
        """List[Vector2D]: 'ComponentAngularDisplacements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAngularDisplacements
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_axial_displacements(self) -> 'List[float]':
        """List[float]: 'ComponentAxialDisplacements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAxialDisplacements
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def component_radial_displacements(self) -> 'List[Vector2D]':
        """List[Vector2D]: 'ComponentRadialDisplacements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentRadialDisplacements
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def element_axial_displacements(self) -> 'List[float]':
        """List[float]: 'ElementAxialDisplacements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementAxialDisplacements
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def element_radial_displacements(self) -> 'List[float]':
        """List[float]: 'ElementRadialDisplacements' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementRadialDisplacements
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def element_tilts(self) -> 'List[float]':
        """List[float]: 'ElementTilts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementTilts
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def elements_in_contact(self) -> 'int':
        """int: 'ElementsInContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElementsInContact
        return temp

    @property
    def inner_left_mounting_axial_stiffness(self) -> 'float':
        """float: 'InnerLeftMountingAxialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerLeftMountingAxialStiffness
        return temp

    @property
    def inner_left_mounting_displacement(self) -> 'Vector3D':
        """Vector3D: 'InnerLeftMountingDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerLeftMountingDisplacement
        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def inner_left_mounting_maximum_tilt_stiffness(self) -> 'float':
        """float: 'InnerLeftMountingMaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerLeftMountingMaximumTiltStiffness
        return temp

    @property
    def inner_left_mounting_tilt(self) -> 'Vector2D':
        """Vector2D: 'InnerLeftMountingTilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerLeftMountingTilt
        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def inner_radial_mounting_linear_displacement(self) -> 'Vector2D':
        """Vector2D: 'InnerRadialMountingLinearDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRadialMountingLinearDisplacement
        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def inner_radial_mounting_maximum_tilt_stiffness(self) -> 'float':
        """float: 'InnerRadialMountingMaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRadialMountingMaximumTiltStiffness
        return temp

    @property
    def inner_radial_mounting_tilt(self) -> 'Vector2D':
        """Vector2D: 'InnerRadialMountingTilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRadialMountingTilt
        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def inner_right_mounting_axial_stiffness(self) -> 'float':
        """float: 'InnerRightMountingAxialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRightMountingAxialStiffness
        return temp

    @property
    def inner_right_mounting_displacement(self) -> 'Vector3D':
        """Vector3D: 'InnerRightMountingDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRightMountingDisplacement
        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def inner_right_mounting_maximum_tilt_stiffness(self) -> 'float':
        """float: 'InnerRightMountingMaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRightMountingMaximumTiltStiffness
        return temp

    @property
    def inner_right_mounting_tilt(self) -> 'Vector2D':
        """Vector2D: 'InnerRightMountingTilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRightMountingTilt
        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def internal_force(self) -> 'Vector3D':
        """Vector3D: 'InternalForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InternalForce
        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def internal_moment(self) -> 'Vector3D':
        """Vector3D: 'InternalMoment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InternalMoment
        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def is_loaded(self) -> 'bool':
        """bool: 'IsLoaded' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsLoaded
        return temp

    @property
    def maximum_radial_stiffness(self) -> 'float':
        """float: 'MaximumRadialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumRadialStiffness
        return temp

    @property
    def maximum_tilt_stiffness(self) -> 'float':
        """float: 'MaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumTiltStiffness
        return temp

    @property
    def outer_left_mounting_axial_stiffness(self) -> 'float':
        """float: 'OuterLeftMountingAxialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterLeftMountingAxialStiffness
        return temp

    @property
    def outer_left_mounting_displacement(self) -> 'Vector3D':
        """Vector3D: 'OuterLeftMountingDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterLeftMountingDisplacement
        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def outer_left_mounting_maximum_tilt_stiffness(self) -> 'float':
        """float: 'OuterLeftMountingMaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterLeftMountingMaximumTiltStiffness
        return temp

    @property
    def outer_left_mounting_tilt(self) -> 'Vector2D':
        """Vector2D: 'OuterLeftMountingTilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterLeftMountingTilt
        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def outer_radial_mounting_linear_displacement(self) -> 'Vector2D':
        """Vector2D: 'OuterRadialMountingLinearDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRadialMountingLinearDisplacement
        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def outer_radial_mounting_maximum_tilt_stiffness(self) -> 'float':
        """float: 'OuterRadialMountingMaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRadialMountingMaximumTiltStiffness
        return temp

    @property
    def outer_radial_mounting_tilt(self) -> 'Vector2D':
        """Vector2D: 'OuterRadialMountingTilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRadialMountingTilt
        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def outer_right_mounting_axial_stiffness(self) -> 'float':
        """float: 'OuterRightMountingAxialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRightMountingAxialStiffness
        return temp

    @property
    def outer_right_mounting_displacement(self) -> 'Vector3D':
        """Vector3D: 'OuterRightMountingDisplacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRightMountingDisplacement
        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def outer_right_mounting_maximum_tilt_stiffness(self) -> 'float':
        """float: 'OuterRightMountingMaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRightMountingMaximumTiltStiffness
        return temp

    @property
    def outer_right_mounting_tilt(self) -> 'Vector2D':
        """Vector2D: 'OuterRightMountingTilt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRightMountingTilt
        value = conversion.pn_to_mp_vector2d(temp)
        return value

    @property
    def percentage_preload_spring_compression(self) -> 'float':
        """float: 'PercentagePreloadSpringCompression' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PercentagePreloadSpringCompression
        return temp

    @property
    def preload_spring_compression(self) -> 'float':
        """float: 'PreloadSpringCompression' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PreloadSpringCompression
        return temp

    @property
    def spring_preload_chart(self) -> '_1815.TwoDChartDefinition':
        """TwoDChartDefinition: 'SpringPreloadChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpringPreloadChart
        if _1815.TwoDChartDefinition.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast spring_preload_chart to TwoDChartDefinition. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design(self) -> '_2380.Bearing':
        """Bearing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_1897.LoadedBearingResults':
        """LoadedBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1897.LoadedBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_concept_axial_clearance_bearing_results(self) -> '_1899.LoadedConceptAxialClearanceBearingResults':
        """LoadedConceptAxialClearanceBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1899.LoadedConceptAxialClearanceBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedConceptAxialClearanceBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_concept_clearance_bearing_results(self) -> '_1900.LoadedConceptClearanceBearingResults':
        """LoadedConceptClearanceBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1900.LoadedConceptClearanceBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedConceptClearanceBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_concept_radial_clearance_bearing_results(self) -> '_1901.LoadedConceptRadialClearanceBearingResults':
        """LoadedConceptRadialClearanceBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1901.LoadedConceptRadialClearanceBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedConceptRadialClearanceBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_detailed_bearing_results(self) -> '_1902.LoadedDetailedBearingResults':
        """LoadedDetailedBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1902.LoadedDetailedBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedDetailedBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_linear_bearing_results(self) -> '_1903.LoadedLinearBearingResults':
        """LoadedLinearBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1903.LoadedLinearBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedLinearBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_non_linear_bearing_results(self) -> '_1905.LoadedNonLinearBearingResults':
        """LoadedNonLinearBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1905.LoadedNonLinearBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedNonLinearBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_angular_contact_ball_bearing_results(self) -> '_1927.LoadedAngularContactBallBearingResults':
        """LoadedAngularContactBallBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1927.LoadedAngularContactBallBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedAngularContactBallBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_angular_contact_thrust_ball_bearing_results(self) -> '_1930.LoadedAngularContactThrustBallBearingResults':
        """LoadedAngularContactThrustBallBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1930.LoadedAngularContactThrustBallBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedAngularContactThrustBallBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_asymmetric_spherical_roller_bearing_results(self) -> '_1933.LoadedAsymmetricSphericalRollerBearingResults':
        """LoadedAsymmetricSphericalRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1933.LoadedAsymmetricSphericalRollerBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedAsymmetricSphericalRollerBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_axial_thrust_cylindrical_roller_bearing_results(self) -> '_1938.LoadedAxialThrustCylindricalRollerBearingResults':
        """LoadedAxialThrustCylindricalRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1938.LoadedAxialThrustCylindricalRollerBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedAxialThrustCylindricalRollerBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_axial_thrust_needle_roller_bearing_results(self) -> '_1941.LoadedAxialThrustNeedleRollerBearingResults':
        """LoadedAxialThrustNeedleRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1941.LoadedAxialThrustNeedleRollerBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedAxialThrustNeedleRollerBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_ball_bearing_results(self) -> '_1946.LoadedBallBearingResults':
        """LoadedBallBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1946.LoadedBallBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedBallBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_crossed_roller_bearing_results(self) -> '_1949.LoadedCrossedRollerBearingResults':
        """LoadedCrossedRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1949.LoadedCrossedRollerBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedCrossedRollerBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_cylindrical_roller_bearing_results(self) -> '_1953.LoadedCylindricalRollerBearingResults':
        """LoadedCylindricalRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1953.LoadedCylindricalRollerBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedCylindricalRollerBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_deep_groove_ball_bearing_results(self) -> '_1956.LoadedDeepGrooveBallBearingResults':
        """LoadedDeepGrooveBallBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1956.LoadedDeepGrooveBallBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedDeepGrooveBallBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_four_point_contact_ball_bearing_results(self) -> '_1961.LoadedFourPointContactBallBearingResults':
        """LoadedFourPointContactBallBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1961.LoadedFourPointContactBallBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedFourPointContactBallBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_needle_roller_bearing_results(self) -> '_1965.LoadedNeedleRollerBearingResults':
        """LoadedNeedleRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1965.LoadedNeedleRollerBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedNeedleRollerBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_non_barrel_roller_bearing_results(self) -> '_1968.LoadedNonBarrelRollerBearingResults':
        """LoadedNonBarrelRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1968.LoadedNonBarrelRollerBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedNonBarrelRollerBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_roller_bearing_results(self) -> '_1973.LoadedRollerBearingResults':
        """LoadedRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1973.LoadedRollerBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedRollerBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_rolling_bearing_results(self) -> '_1977.LoadedRollingBearingResults':
        """LoadedRollingBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1977.LoadedRollingBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedRollingBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_self_aligning_ball_bearing_results(self) -> '_1980.LoadedSelfAligningBallBearingResults':
        """LoadedSelfAligningBallBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1980.LoadedSelfAligningBallBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedSelfAligningBallBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_spherical_roller_radial_bearing_results(self) -> '_1984.LoadedSphericalRollerRadialBearingResults':
        """LoadedSphericalRollerRadialBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1984.LoadedSphericalRollerRadialBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedSphericalRollerRadialBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_spherical_roller_thrust_bearing_results(self) -> '_1987.LoadedSphericalRollerThrustBearingResults':
        """LoadedSphericalRollerThrustBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1987.LoadedSphericalRollerThrustBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedSphericalRollerThrustBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_taper_roller_bearing_results(self) -> '_1992.LoadedTaperRollerBearingResults':
        """LoadedTaperRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1992.LoadedTaperRollerBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedTaperRollerBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_three_point_contact_ball_bearing_results(self) -> '_1995.LoadedThreePointContactBallBearingResults':
        """LoadedThreePointContactBallBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1995.LoadedThreePointContactBallBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedThreePointContactBallBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_thrust_ball_bearing_results(self) -> '_1998.LoadedThrustBallBearingResults':
        """LoadedThrustBallBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1998.LoadedThrustBallBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedThrustBallBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_toroidal_roller_bearing_results(self) -> '_2001.LoadedToroidalRollerBearingResults':
        """LoadedToroidalRollerBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _2001.LoadedToroidalRollerBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedToroidalRollerBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_fluid_film_bearing_results(self) -> '_2062.LoadedFluidFilmBearingResults':
        """LoadedFluidFilmBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _2062.LoadedFluidFilmBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedFluidFilmBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_grease_filled_journal_bearing_results(self) -> '_2063.LoadedGreaseFilledJournalBearingResults':
        """LoadedGreaseFilledJournalBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _2063.LoadedGreaseFilledJournalBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedGreaseFilledJournalBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_pad_fluid_film_bearing_results(self) -> '_2064.LoadedPadFluidFilmBearingResults':
        """LoadedPadFluidFilmBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _2064.LoadedPadFluidFilmBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedPadFluidFilmBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_plain_journal_bearing_results(self) -> '_2065.LoadedPlainJournalBearingResults':
        """LoadedPlainJournalBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _2065.LoadedPlainJournalBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedPlainJournalBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_plain_oil_fed_journal_bearing(self) -> '_2067.LoadedPlainOilFedJournalBearing':
        """LoadedPlainOilFedJournalBearing: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _2067.LoadedPlainOilFedJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedPlainOilFedJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_tilting_pad_journal_bearing_results(self) -> '_2070.LoadedTiltingPadJournalBearingResults':
        """LoadedTiltingPadJournalBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _2070.LoadedTiltingPadJournalBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedTiltingPadJournalBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_loaded_tilting_pad_thrust_bearing_results(self) -> '_2071.LoadedTiltingPadThrustBearingResults':
        """LoadedTiltingPadThrustBearingResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _2071.LoadedTiltingPadThrustBearingResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedTiltingPadThrustBearingResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6734.BearingLoadCase':
        """BearingLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_left_mounting_stiffness(self) -> '_1890.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'InnerLeftMountingStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerLeftMountingStiffness
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_radial_mounting_stiffness(self) -> '_1890.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'InnerRadialMountingStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRadialMountingStiffness
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_right_mounting_stiffness(self) -> '_1890.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'InnerRightMountingStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerRightMountingStiffness
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_left_mounting_stiffness(self) -> '_1890.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'OuterLeftMountingStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterLeftMountingStiffness
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_radial_mounting_stiffness(self) -> '_1890.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'OuterRadialMountingStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRadialMountingStiffness
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_right_mounting_stiffness(self) -> '_1890.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'OuterRightMountingStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterRightMountingStiffness
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_3972.BearingPowerFlow':
        """BearingPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def preload_spring_stiffness(self) -> '_1890.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'PreloadSpringStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PreloadSpringStiffness
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stiffness_between_rings(self) -> '_1890.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'StiffnessBetweenRings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessBetweenRings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stiffness_matrix(self) -> '_1890.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'StiffnessMatrix' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessMatrix
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def forces_at_zero_displacement_for_inner_and_outer_nodes(self) -> 'List[_1520.ForceResults]':
        """List[ForceResults]: 'ForcesAtZeroDisplacementForInnerAndOuterNodes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForcesAtZeroDisplacementForInnerAndOuterNodes
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[BearingSystemDeflection]':
        """List[BearingSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def race_mounting_options_for_analysis(self) -> 'List[_2381.BearingRaceMountingOptions]':
        """List[BearingRaceMountingOptions]: 'RaceMountingOptionsForAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RaceMountingOptionsForAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def stiffness_between_each_ring(self) -> 'List[_1890.BearingStiffnessMatrixReporter]':
        """List[BearingStiffnessMatrixReporter]: 'StiffnessBetweenEachRing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessBetweenEachRing
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

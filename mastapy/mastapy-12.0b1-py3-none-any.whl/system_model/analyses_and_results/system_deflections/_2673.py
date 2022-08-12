"""_2673.py

CylindricalGearMeshSystemDeflection
"""


from typing import List

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.utility.report import _1744
from mastapy.gears.rating.cylindrical import _449
from mastapy.system_model.connections_and_sockets.gears import _2249
from mastapy.system_model.analyses_and_results.static_loads import _6777
from mastapy.system_model.analyses_and_results.system_deflections import (
    _2679, _2680, _2681, _2684,
    _2683, _2693
)
from mastapy._internal.cast_exception import CastException
from mastapy.nodal_analysis import _55
from mastapy.system_model.analyses_and_results.power_flows import _4012
from mastapy.system_model.analyses_and_results.system_deflections.reporting import _2779
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'CylindricalGearMeshSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMeshSystemDeflection',)


class CylindricalGearMeshSystemDeflection(_2693.GearMeshSystemDeflection):
    """CylindricalGearMeshSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearMeshSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angular_misalignment_for_harmonic_analysis(self) -> 'float':
        """float: 'AngularMisalignmentForHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngularMisalignmentForHarmonicAnalysis
        return temp

    @property
    def average_interference_normal_to_the_flank(self) -> 'float':
        """float: 'AverageInterferenceNormalToTheFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageInterferenceNormalToTheFlank
        return temp

    @property
    def average_operating_backlash(self) -> 'float':
        """float: 'AverageOperatingBacklash' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageOperatingBacklash
        return temp

    @property
    def calculated_load_sharing_factor(self) -> 'float':
        """float: 'CalculatedLoadSharingFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedLoadSharingFactor
        return temp

    @property
    def calculated_worst_load_sharing_factor(self) -> 'float':
        """float: 'CalculatedWorstLoadSharingFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedWorstLoadSharingFactor
        return temp

    @property
    def change_in_backlash_due_to_tooth_expansion(self) -> 'float':
        """float: 'ChangeInBacklashDueToToothExpansion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ChangeInBacklashDueToToothExpansion
        return temp

    @property
    def change_in_operating_backlash_due_to_thermal_effects(self) -> 'float':
        """float: 'ChangeInOperatingBacklashDueToThermalEffects' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ChangeInOperatingBacklashDueToThermalEffects
        return temp

    @property
    def chart_of_effective_change_in_operating_centre_distance(self) -> 'Image':
        """Image: 'ChartOfEffectiveChangeInOperatingCentreDistance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ChartOfEffectiveChangeInOperatingCentreDistance
        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def chart_of_misalignment_in_transverse_line_of_action(self) -> '_1744.LegacyChartDefinition':
        """LegacyChartDefinition: 'ChartOfMisalignmentInTransverseLineOfAction' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ChartOfMisalignmentInTransverseLineOfAction
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def crowning_for_tilt_stiffness_gear_a(self) -> 'float':
        """float: 'CrowningForTiltStiffnessGearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CrowningForTiltStiffnessGearA
        return temp

    @property
    def crowning_for_tilt_stiffness_gear_b(self) -> 'float':
        """float: 'CrowningForTiltStiffnessGearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CrowningForTiltStiffnessGearB
        return temp

    @property
    def estimated_operating_tooth_temperature(self) -> 'float':
        """float: 'EstimatedOperatingToothTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EstimatedOperatingToothTemperature
        return temp

    @property
    def gear_mesh_tilt_stiffness_method(self) -> 'str':
        """str: 'GearMeshTiltStiffnessMethod' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshTiltStiffnessMethod
        return temp

    @property
    def is_in_contact(self) -> 'bool':
        """bool: 'IsInContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsInContact
        return temp

    @property
    def linear_relief_for_tilt_stiffness_gear_a(self) -> 'float':
        """float: 'LinearReliefForTiltStiffnessGearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LinearReliefForTiltStiffnessGearA
        return temp

    @property
    def linear_relief_for_tilt_stiffness_gear_b(self) -> 'float':
        """float: 'LinearReliefForTiltStiffnessGearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LinearReliefForTiltStiffnessGearB
        return temp

    @property
    def load_in_loa_from_ltca(self) -> 'float':
        """float: 'LoadInLOAFromLTCA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadInLOAFromLTCA
        return temp

    @property
    def maximum_change_in_centre_distance(self) -> 'float':
        """float: 'MaximumChangeInCentreDistance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumChangeInCentreDistance
        return temp

    @property
    def maximum_change_in_centre_distance_due_to_misalignment(self) -> 'float':
        """float: 'MaximumChangeInCentreDistanceDueToMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumChangeInCentreDistanceDueToMisalignment
        return temp

    @property
    def maximum_operating_backlash(self) -> 'float':
        """float: 'MaximumOperatingBacklash' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumOperatingBacklash
        return temp

    @property
    def maximum_operating_centre_distance(self) -> 'float':
        """float: 'MaximumOperatingCentreDistance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumOperatingCentreDistance
        return temp

    @property
    def maximum_operating_transverse_contact_ratio(self) -> 'float':
        """float: 'MaximumOperatingTransverseContactRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumOperatingTransverseContactRatio
        return temp

    @property
    def minimum_change_in_centre_distance(self) -> 'float':
        """float: 'MinimumChangeInCentreDistance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumChangeInCentreDistance
        return temp

    @property
    def minimum_change_in_centre_distance_due_to_misalignment(self) -> 'float':
        """float: 'MinimumChangeInCentreDistanceDueToMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumChangeInCentreDistanceDueToMisalignment
        return temp

    @property
    def minimum_operating_backlash(self) -> 'float':
        """float: 'MinimumOperatingBacklash' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumOperatingBacklash
        return temp

    @property
    def minimum_operating_centre_distance(self) -> 'float':
        """float: 'MinimumOperatingCentreDistance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumOperatingCentreDistance
        return temp

    @property
    def minimum_operating_transverse_contact_ratio(self) -> 'float':
        """float: 'MinimumOperatingTransverseContactRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumOperatingTransverseContactRatio
        return temp

    @property
    def node_pair_changes_in_operating_centre_distance_due_to_misalignment(self) -> 'List[float]':
        """List[float]: 'NodePairChangesInOperatingCentreDistanceDueToMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairChangesInOperatingCentreDistanceDueToMisalignment
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def node_pair_transverse_separations_for_ltca(self) -> 'List[float]':
        """List[float]: 'NodePairTransverseSeparationsForLTCA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairTransverseSeparationsForLTCA
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def pinion_torque_for_ltca(self) -> 'float':
        """float: 'PinionTorqueForLTCA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionTorqueForLTCA
        return temp

    @property
    def separation(self) -> 'float':
        """float: 'Separation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Separation
        return temp

    @property
    def separation_to_inactive_flank(self) -> 'float':
        """float: 'SeparationToInactiveFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SeparationToInactiveFlank
        return temp

    @property
    def signed_root_mean_square_planetary_equivalent_misalignment(self) -> 'float':
        """float: 'SignedRootMeanSquarePlanetaryEquivalentMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SignedRootMeanSquarePlanetaryEquivalentMisalignment
        return temp

    @property
    def smallest_effective_operating_centre_distance(self) -> 'float':
        """float: 'SmallestEffectiveOperatingCentreDistance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmallestEffectiveOperatingCentreDistance
        return temp

    @property
    def transmission_error_including_backlash(self) -> 'float':
        """float: 'TransmissionErrorIncludingBacklash' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransmissionErrorIncludingBacklash
        return temp

    @property
    def transmission_error_no_backlash(self) -> 'float':
        """float: 'TransmissionErrorNoBacklash' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransmissionErrorNoBacklash
        return temp

    @property
    def worst_planetary_misalignment(self) -> 'float':
        """float: 'WorstPlanetaryMisalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorstPlanetaryMisalignment
        return temp

    @property
    def rating(self) -> '_449.CylindricalGearMeshRating':
        """CylindricalGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_449.CylindricalGearMeshRating':
        """CylindricalGearMeshRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2249.CylindricalGearMesh':
        """CylindricalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6777.CylindricalGearMeshLoadCase':
        """CylindricalGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a(self) -> '_2679.CylindricalGearSystemDeflection':
        """CylindricalGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2679.CylindricalGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_system_deflection_timestep(self) -> '_2680.CylindricalGearSystemDeflectionTimestep':
        """CylindricalGearSystemDeflectionTimestep: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2680.CylindricalGearSystemDeflectionTimestep.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearSystemDeflectionTimestep. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_system_deflection_with_ltca_results(self) -> '_2681.CylindricalGearSystemDeflectionWithLTCAResults':
        """CylindricalGearSystemDeflectionWithLTCAResults: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2681.CylindricalGearSystemDeflectionWithLTCAResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearSystemDeflectionWithLTCAResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_planet_gear_system_deflection(self) -> '_2684.CylindricalPlanetGearSystemDeflection':
        """CylindricalPlanetGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2684.CylindricalPlanetGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalPlanetGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b(self) -> '_2679.CylindricalGearSystemDeflection':
        """CylindricalGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2679.CylindricalGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_system_deflection_timestep(self) -> '_2680.CylindricalGearSystemDeflectionTimestep':
        """CylindricalGearSystemDeflectionTimestep: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2680.CylindricalGearSystemDeflectionTimestep.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearSystemDeflectionTimestep. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_system_deflection_with_ltca_results(self) -> '_2681.CylindricalGearSystemDeflectionWithLTCAResults':
        """CylindricalGearSystemDeflectionWithLTCAResults: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2681.CylindricalGearSystemDeflectionWithLTCAResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearSystemDeflectionWithLTCAResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_planet_gear_system_deflection(self) -> '_2684.CylindricalPlanetGearSystemDeflection':
        """CylindricalPlanetGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2684.CylindricalPlanetGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalPlanetGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def misalignment_data(self) -> '_55.CylindricalMisalignmentCalculator':
        """CylindricalMisalignmentCalculator: 'MisalignmentData' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MisalignmentData
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def misalignment_data_left_flank(self) -> '_55.CylindricalMisalignmentCalculator':
        """CylindricalMisalignmentCalculator: 'MisalignmentDataLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MisalignmentDataLeftFlank
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def misalignment_data_right_flank(self) -> '_55.CylindricalMisalignmentCalculator':
        """CylindricalMisalignmentCalculator: 'MisalignmentDataRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MisalignmentDataRightFlank
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4012.CylindricalGearMeshPowerFlow':
        """CylindricalGearMeshPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gears(self) -> 'List[_2679.CylindricalGearSystemDeflection]':
        """List[CylindricalGearSystemDeflection]: 'CylindricalGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_meshed_gear_system_deflections(self) -> 'List[_2683.CylindricalMeshedGearSystemDeflection]':
        """List[CylindricalMeshedGearSystemDeflection]: 'CylindricalMeshedGearSystemDeflections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalMeshedGearSystemDeflections
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def mesh_deflections_left_flank(self) -> 'List[_2779.MeshDeflectionResults]':
        """List[MeshDeflectionResults]: 'MeshDeflectionsLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshDeflectionsLeftFlank
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def mesh_deflections_right_flank(self) -> 'List[_2779.MeshDeflectionResults]':
        """List[MeshDeflectionResults]: 'MeshDeflectionsRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshDeflectionsRightFlank
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[CylindricalGearMeshSystemDeflection]':
        """List[CylindricalGearMeshSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

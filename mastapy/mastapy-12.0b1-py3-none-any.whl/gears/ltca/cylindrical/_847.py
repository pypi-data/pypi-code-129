"""_847.py

CylindricalGearMeshLoadDistributionAnalysis
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.load_case.cylindrical import _874
from mastapy.gears.ltca import _822, _831
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1088
from mastapy.gears.cylindrical import _1200
from mastapy.gears.rating.cylindrical import _449
from mastapy.gears.ltca.cylindrical import _851
from mastapy._math.vector_2d import Vector2D
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_LOAD_DISTRIBUTION_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.LTCA.Cylindrical', 'CylindricalGearMeshLoadDistributionAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMeshLoadDistributionAnalysis',)


class CylindricalGearMeshLoadDistributionAnalysis(_831.GearMeshLoadDistributionAnalysis):
    """CylindricalGearMeshLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_LOAD_DISTRIBUTION_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearMeshLoadDistributionAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_flash_temperature(self) -> 'float':
        """float: 'AverageFlashTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageFlashTemperature
        return temp

    @property
    def calculated_face_load_factor_contact(self) -> 'float':
        """float: 'CalculatedFaceLoadFactorContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedFaceLoadFactorContact
        return temp

    @property
    def din_scuffing_bulk_tooth_temperature(self) -> 'float':
        """float: 'DINScuffingBulkToothTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DINScuffingBulkToothTemperature
        return temp

    @property
    def iso63362006_mesh_stiffness(self) -> 'float':
        """float: 'ISO63362006MeshStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO63362006MeshStiffness
        return temp

    @property
    def iso63362006_mesh_stiffness_across_face_width(self) -> 'float':
        """float: 'ISO63362006MeshStiffnessAcrossFaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO63362006MeshStiffnessAcrossFaceWidth
        return temp

    @property
    def iso63362006_single_stiffness(self) -> 'float':
        """float: 'ISO63362006SingleStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO63362006SingleStiffness
        return temp

    @property
    def iso63362006_single_stiffness_across_face_width(self) -> 'float':
        """float: 'ISO63362006SingleStiffnessAcrossFaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO63362006SingleStiffnessAcrossFaceWidth
        return temp

    @property
    def iso_scuffing_bulk_tooth_temperature(self) -> 'float':
        """float: 'ISOScuffingBulkToothTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISOScuffingBulkToothTemperature
        return temp

    @property
    def maximum_edge_pressure(self) -> 'float':
        """float: 'MaximumEdgePressure' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumEdgePressure
        return temp

    @property
    def mean_te(self) -> 'float':
        """float: 'MeanTE' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanTE
        return temp

    @property
    def misalignment(self) -> 'float':
        """float: 'Misalignment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Misalignment
        return temp

    @property
    def peak_to_peak_te(self) -> 'float':
        """float: 'PeakToPeakTE' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakToPeakTE
        return temp

    @property
    def strip_loads_deviation(self) -> 'float':
        """float: 'StripLoadsDeviation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StripLoadsDeviation
        return temp

    @property
    def strip_loads_maximum(self) -> 'float':
        """float: 'StripLoadsMaximum' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StripLoadsMaximum
        return temp

    @property
    def strip_loads_minimum(self) -> 'float':
        """float: 'StripLoadsMinimum' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StripLoadsMinimum
        return temp

    @property
    def theoretical_total_contact_ratio(self) -> 'float':
        """float: 'TheoreticalTotalContactRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TheoreticalTotalContactRatio
        return temp

    @property
    def tooth_temperature(self) -> 'float':
        """float: 'ToothTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothTemperature
        return temp

    @property
    def utilization_force_per_unit_length_cutoff_value(self) -> 'float':
        """float: 'UtilizationForcePerUnitLengthCutoffValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UtilizationForcePerUnitLengthCutoffValue
        return temp

    @property
    def cylindrical_mesh_load_case(self) -> '_874.CylindricalMeshLoadCase':
        """CylindricalMeshLoadCase: 'CylindricalMeshLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalMeshLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_in_mesh(self) -> '_822.CylindricalMeshedGearLoadDistributionAnalysis':
        """CylindricalMeshedGearLoadDistributionAnalysis: 'GearAInMesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearAInMesh
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_in_mesh(self) -> '_822.CylindricalMeshedGearLoadDistributionAnalysis':
        """CylindricalMeshedGearLoadDistributionAnalysis: 'GearBInMesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBInMesh
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_micro_geometry(self) -> '_1088.CylindricalGearMeshMicroGeometry':
        """CylindricalGearMeshMicroGeometry: 'MeshMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshMicroGeometry
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def points_with_worst_results(self) -> '_1200.PointsWithWorstResults':
        """PointsWithWorstResults: 'PointsWithWorstResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PointsWithWorstResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def load_distribution_analyses_at_single_rotation(self) -> 'List[_851.CylindricalMeshLoadDistributionAtRotation]':
        """List[CylindricalMeshLoadDistributionAtRotation]: 'LoadDistributionAnalysesAtSingleRotation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadDistributionAnalysesAtSingleRotation
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshed_gears(self) -> 'List[_822.CylindricalMeshedGearLoadDistributionAnalysis]':
        """List[CylindricalMeshedGearLoadDistributionAnalysis]: 'MeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshedGears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def transmission_error_against_rotation(self) -> 'List[Vector2D]':
        """List[Vector2D]: 'TransmissionErrorAgainstRotation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransmissionErrorAgainstRotation
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

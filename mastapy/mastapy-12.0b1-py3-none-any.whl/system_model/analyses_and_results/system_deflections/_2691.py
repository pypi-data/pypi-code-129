"""_2691.py

FEPartSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model import _2393
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6801
from mastapy.nodal_analysis.component_mode_synthesis import _226
from mastapy.nodal_analysis import _78
from mastapy.system_model.analyses_and_results.power_flows import _4021
from mastapy.math_utility.measured_vectors import _1523, _1519
from mastapy.system_model.fe import _2349
from mastapy.system_model.analyses_and_results.system_deflections import _2625
from mastapy._internal.python_net import python_net_import

_FE_PART_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'FEPartSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('FEPartSystemDeflection',)


class FEPartSystemDeflection(_2625.AbstractShaftOrHousingSystemDeflection):
    """FEPartSystemDeflection

    This is a mastapy class.
    """

    TYPE = _FE_PART_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FEPartSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2393.FEPart':
        """FEPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6801.FEPartLoadCase':
        """FEPartLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def full_fe_results(self) -> '_226.StaticCMSResults':
        """StaticCMSResults: 'FullFEResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FullFEResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mass_in_world_coordinate_system_mn_rad_s_kg(self) -> '_78.NodalMatrix':
        """NodalMatrix: 'MassInWorldCoordinateSystemMNRadSKg' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassInWorldCoordinateSystemMNRadSKg
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4021.FEPartPowerFlow':
        """FEPartPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stiffness_in_world_coordinate_system_mn_rad(self) -> '_78.NodalMatrix':
        """NodalMatrix: 'StiffnessInWorldCoordinateSystemMNRad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessInWorldCoordinateSystemMNRad
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def applied_internal_forces_in_world_coordinate_system(self) -> 'List[_1523.VectorWithLinearAndAngularComponents]':
        """List[VectorWithLinearAndAngularComponents]: 'AppliedInternalForcesInWorldCoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AppliedInternalForcesInWorldCoordinateSystem
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def node_results_in_shaft_coordinate_system(self) -> 'List[_1519.ForceAndDisplacementResults]':
        """List[ForceAndDisplacementResults]: 'NodeResultsInShaftCoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodeResultsInShaftCoordinateSystem
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[FEPartSystemDeflection]':
        """List[FEPartSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def export(self) -> '_2349.SystemDeflectionFEExportOptions':
        """SystemDeflectionFEExportOptions: 'Export' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Export
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def export_displacements(self):
        """ 'ExportDisplacements' is the original name of this method."""

        self.wrapped.ExportDisplacements()

    def export_forces(self):
        """ 'ExportForces' is the original name of this method."""

        self.wrapped.ExportForces()

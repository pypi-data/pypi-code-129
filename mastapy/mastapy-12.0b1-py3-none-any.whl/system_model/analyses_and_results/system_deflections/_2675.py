"""_2675.py

CylindricalGearMeshSystemDeflectionWithLTCAResults
"""


from mastapy.gears.ltca.cylindrical import _847
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2673
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_SYSTEM_DEFLECTION_WITH_LTCA_RESULTS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'CylindricalGearMeshSystemDeflectionWithLTCAResults')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMeshSystemDeflectionWithLTCAResults',)


class CylindricalGearMeshSystemDeflectionWithLTCAResults(_2673.CylindricalGearMeshSystemDeflection):
    """CylindricalGearMeshSystemDeflectionWithLTCAResults

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_SYSTEM_DEFLECTION_WITH_LTCA_RESULTS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearMeshSystemDeflectionWithLTCAResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def advanced_ltca_results(self) -> '_847.CylindricalGearMeshLoadDistributionAnalysis':
        """CylindricalGearMeshLoadDistributionAnalysis: 'AdvancedLTCAResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdvancedLTCAResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def advanced_ltca_results_only_first_planetary_mesh(self) -> '_847.CylindricalGearMeshLoadDistributionAnalysis':
        """CylindricalGearMeshLoadDistributionAnalysis: 'AdvancedLTCAResultsOnlyFirstPlanetaryMesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdvancedLTCAResultsOnlyFirstPlanetaryMesh
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def basic_ltca_results(self) -> '_847.CylindricalGearMeshLoadDistributionAnalysis':
        """CylindricalGearMeshLoadDistributionAnalysis: 'BasicLTCAResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicLTCAResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def basic_ltca_results_only_first_planetary_mesh(self) -> '_847.CylindricalGearMeshLoadDistributionAnalysis':
        """CylindricalGearMeshLoadDistributionAnalysis: 'BasicLTCAResultsOnlyFirstPlanetaryMesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicLTCAResultsOnlyFirstPlanetaryMesh
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

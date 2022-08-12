"""_3726.py

ConceptGearMeshStabilityAnalysis
"""


from mastapy.system_model.connections_and_sockets.gears import _2245
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6756
from mastapy.system_model.analyses_and_results.stability_analyses import _3756
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'ConceptGearMeshStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearMeshStabilityAnalysis',)


class ConceptGearMeshStabilityAnalysis(_3756.GearMeshStabilityAnalysis):
    """ConceptGearMeshStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearMeshStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2245.ConceptGearMesh':
        """ConceptGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6756.ConceptGearMeshLoadCase':
        """ConceptGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

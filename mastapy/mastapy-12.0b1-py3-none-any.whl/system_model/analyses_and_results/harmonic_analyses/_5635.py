"""_5635.py

ConceptGearSetHarmonicAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2461
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6757
from mastapy.system_model.analyses_and_results.system_deflections import _2655
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5633, _5634, _5680
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'ConceptGearSetHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetHarmonicAnalysis',)


class ConceptGearSetHarmonicAnalysis(_5680.GearSetHarmonicAnalysis):
    """ConceptGearSetHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearSetHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2461.ConceptGearSet':
        """ConceptGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6757.ConceptGearSetLoadCase':
        """ConceptGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2655.ConceptGearSetSystemDeflection':
        """ConceptGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gears_harmonic_analysis(self) -> 'List[_5633.ConceptGearHarmonicAnalysis]':
        """List[ConceptGearHarmonicAnalysis]: 'GearsHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearsHarmonicAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_gears_harmonic_analysis(self) -> 'List[_5633.ConceptGearHarmonicAnalysis]':
        """List[ConceptGearHarmonicAnalysis]: 'ConceptGearsHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearsHarmonicAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshes_harmonic_analysis(self) -> 'List[_5634.ConceptGearMeshHarmonicAnalysis]':
        """List[ConceptGearMeshHarmonicAnalysis]: 'MeshesHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshesHarmonicAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_meshes_harmonic_analysis(self) -> 'List[_5634.ConceptGearMeshHarmonicAnalysis]':
        """List[ConceptGearMeshHarmonicAnalysis]: 'ConceptMeshesHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptMeshesHarmonicAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

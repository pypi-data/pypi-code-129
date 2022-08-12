"""_5757.py

WormGearSetHarmonicAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2491
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6898
from mastapy.system_model.analyses_and_results.system_deflections import _2771
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5755, _5756, _5680
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'WormGearSetHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetHarmonicAnalysis',)


class WormGearSetHarmonicAnalysis(_5680.GearSetHarmonicAnalysis):
    """WormGearSetHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2491.WormGearSet':
        """WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6898.WormGearSetLoadCase':
        """WormGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2771.WormGearSetSystemDeflection':
        """WormGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gears_harmonic_analysis(self) -> 'List[_5755.WormGearHarmonicAnalysis]':
        """List[WormGearHarmonicAnalysis]: 'GearsHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearsHarmonicAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_gears_harmonic_analysis(self) -> 'List[_5755.WormGearHarmonicAnalysis]':
        """List[WormGearHarmonicAnalysis]: 'WormGearsHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearsHarmonicAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshes_harmonic_analysis(self) -> 'List[_5756.WormGearMeshHarmonicAnalysis]':
        """List[WormGearMeshHarmonicAnalysis]: 'MeshesHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshesHarmonicAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_meshes_harmonic_analysis(self) -> 'List[_5756.WormGearMeshHarmonicAnalysis]':
        """List[WormGearMeshHarmonicAnalysis]: 'WormMeshesHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormMeshesHarmonicAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

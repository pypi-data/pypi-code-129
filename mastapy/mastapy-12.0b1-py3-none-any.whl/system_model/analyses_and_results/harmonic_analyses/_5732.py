"""_5732.py

SpiralBevelGearSetHarmonicAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2483
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6869
from mastapy.system_model.analyses_and_results.system_deflections import _2742
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5730, _5731, _5621
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'SpiralBevelGearSetHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetHarmonicAnalysis',)


class SpiralBevelGearSetHarmonicAnalysis(_5621.BevelGearSetHarmonicAnalysis):
    """SpiralBevelGearSetHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2483.SpiralBevelGearSet':
        """SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6869.SpiralBevelGearSetLoadCase':
        """SpiralBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2742.SpiralBevelGearSetSystemDeflection':
        """SpiralBevelGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gears_harmonic_analysis(self) -> 'List[_5730.SpiralBevelGearHarmonicAnalysis]':
        """List[SpiralBevelGearHarmonicAnalysis]: 'GearsHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearsHarmonicAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_gears_harmonic_analysis(self) -> 'List[_5730.SpiralBevelGearHarmonicAnalysis]':
        """List[SpiralBevelGearHarmonicAnalysis]: 'SpiralBevelGearsHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGearsHarmonicAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshes_harmonic_analysis(self) -> 'List[_5731.SpiralBevelGearMeshHarmonicAnalysis]':
        """List[SpiralBevelGearMeshHarmonicAnalysis]: 'MeshesHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshesHarmonicAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_meshes_harmonic_analysis(self) -> 'List[_5731.SpiralBevelGearMeshHarmonicAnalysis]':
        """List[SpiralBevelGearMeshHarmonicAnalysis]: 'SpiralBevelMeshesHarmonicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelMeshesHarmonicAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

"""_6051.py

WormGearSetHarmonicAnalysisOfSingleExcitation
"""


from typing import List

from mastapy.system_model.part_model.gears import _2491
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6898
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6049, _6050, _5985
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'WormGearSetHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetHarmonicAnalysisOfSingleExcitation',)


class WormGearSetHarmonicAnalysisOfSingleExcitation(_5985.GearSetHarmonicAnalysisOfSingleExcitation):
    """WormGearSetHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetHarmonicAnalysisOfSingleExcitation.TYPE'):
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
    def worm_gears_harmonic_analysis_of_single_excitation(self) -> 'List[_6049.WormGearHarmonicAnalysisOfSingleExcitation]':
        """List[WormGearHarmonicAnalysisOfSingleExcitation]: 'WormGearsHarmonicAnalysisOfSingleExcitation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearsHarmonicAnalysisOfSingleExcitation
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_meshes_harmonic_analysis_of_single_excitation(self) -> 'List[_6050.WormGearMeshHarmonicAnalysisOfSingleExcitation]':
        """List[WormGearMeshHarmonicAnalysisOfSingleExcitation]: 'WormMeshesHarmonicAnalysisOfSingleExcitation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormMeshesHarmonicAnalysisOfSingleExcitation
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

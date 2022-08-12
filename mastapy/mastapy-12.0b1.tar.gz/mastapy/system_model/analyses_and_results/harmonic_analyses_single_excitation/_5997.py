"""_5997.py

KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation
"""


from typing import List

from mastapy.system_model.part_model.gears import _2478
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6831
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5995, _5996, _5994
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation',)


class KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation(_5994.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysisOfSingleExcitation):
    """KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2478.KlingelnbergCycloPalloidHypoidGearSet':
        """KlingelnbergCycloPalloidHypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6831.KlingelnbergCycloPalloidHypoidGearSetLoadCase':
        """KlingelnbergCycloPalloidHypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_harmonic_analysis_of_single_excitation(self) -> 'List[_5995.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation]':
        """List[KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation]: 'KlingelnbergCycloPalloidHypoidGearsHarmonicAnalysisOfSingleExcitation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsHarmonicAnalysisOfSingleExcitation
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_harmonic_analysis_of_single_excitation(self) -> 'List[_5996.KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation]':
        """List[KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation]: 'KlingelnbergCycloPalloidHypoidMeshesHarmonicAnalysisOfSingleExcitation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshesHarmonicAnalysisOfSingleExcitation
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

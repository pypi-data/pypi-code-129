"""_6061.py

AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
"""


from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5931
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6089
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation',)


class AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation(_6089.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation):
    """AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_5931.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation]':
        """List[AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5931.AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation]':
        """List[AGMAGleasonConicalGearSetHarmonicAnalysisOfSingleExcitation]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

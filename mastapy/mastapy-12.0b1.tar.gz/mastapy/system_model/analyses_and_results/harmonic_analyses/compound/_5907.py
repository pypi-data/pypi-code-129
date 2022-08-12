"""_5907.py

StraightBevelPlanetGearCompoundHarmonicAnalysis
"""


from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5742
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5901
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'StraightBevelPlanetGearCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelPlanetGearCompoundHarmonicAnalysis',)


class StraightBevelPlanetGearCompoundHarmonicAnalysis(_5901.StraightBevelDiffGearCompoundHarmonicAnalysis):
    """StraightBevelPlanetGearCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelPlanetGearCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(self) -> 'List[_5742.StraightBevelPlanetGearHarmonicAnalysis]':
        """List[StraightBevelPlanetGearHarmonicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5742.StraightBevelPlanetGearHarmonicAnalysis]':
        """List[StraightBevelPlanetGearHarmonicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

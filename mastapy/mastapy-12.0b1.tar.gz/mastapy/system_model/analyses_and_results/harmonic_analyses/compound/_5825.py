"""_5825.py

ConceptGearCompoundHarmonicAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2460
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5633
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5854
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'ConceptGearCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearCompoundHarmonicAnalysis',)


class ConceptGearCompoundHarmonicAnalysis(_5854.GearCompoundHarmonicAnalysis):
    """ConceptGearCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_COMPOUND_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2460.ConceptGear':
        """ConceptGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5633.ConceptGearHarmonicAnalysis]':
        """List[ConceptGearHarmonicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5633.ConceptGearHarmonicAnalysis]':
        """List[ConceptGearHarmonicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

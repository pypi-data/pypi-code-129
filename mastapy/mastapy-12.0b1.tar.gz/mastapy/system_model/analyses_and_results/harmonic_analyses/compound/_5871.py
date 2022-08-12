"""_5871.py

MassDiscCompoundHarmonicAnalysis
"""


from typing import List

from mastapy.system_model.part_model import _2402
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5702
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5918
from mastapy._internal.python_net import python_net_import

_MASS_DISC_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'MassDiscCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('MassDiscCompoundHarmonicAnalysis',)


class MassDiscCompoundHarmonicAnalysis(_5918.VirtualComponentCompoundHarmonicAnalysis):
    """MassDiscCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_COMPOUND_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MassDiscCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2402.MassDisc':
        """MassDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5702.MassDiscHarmonicAnalysis]':
        """List[MassDiscHarmonicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[MassDiscCompoundHarmonicAnalysis]':
        """List[MassDiscCompoundHarmonicAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5702.MassDiscHarmonicAnalysis]':
        """List[MassDiscHarmonicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

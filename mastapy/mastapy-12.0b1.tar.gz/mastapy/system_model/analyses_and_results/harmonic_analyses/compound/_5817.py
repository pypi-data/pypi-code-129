"""_5817.py

ClutchCompoundHarmonicAnalysis
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2517
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5626
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5833
from mastapy._internal.python_net import python_net_import

_CLUTCH_COMPOUND_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound', 'ClutchCompoundHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchCompoundHarmonicAnalysis',)


class ClutchCompoundHarmonicAnalysis(_5833.CouplingCompoundHarmonicAnalysis):
    """ClutchCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_COMPOUND_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchCompoundHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2517.Clutch':
        """Clutch: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2517.Clutch':
        """Clutch: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5626.ClutchHarmonicAnalysis]':
        """List[ClutchHarmonicAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5626.ClutchHarmonicAnalysis]':
        """List[ClutchHarmonicAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

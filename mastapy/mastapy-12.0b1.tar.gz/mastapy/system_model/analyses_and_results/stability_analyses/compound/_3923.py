"""_3923.py

RootAssemblyCompoundStabilityAnalysis
"""


from typing import List

from mastapy.system_model.analyses_and_results.stability_analyses import _3792
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3836
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'RootAssemblyCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyCompoundStabilityAnalysis',)


class RootAssemblyCompoundStabilityAnalysis(_3836.AssemblyCompoundStabilityAnalysis):
    """RootAssemblyCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RootAssemblyCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3792.RootAssemblyStabilityAnalysis]':
        """List[RootAssemblyStabilityAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3792.RootAssemblyStabilityAnalysis]':
        """List[RootAssemblyStabilityAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

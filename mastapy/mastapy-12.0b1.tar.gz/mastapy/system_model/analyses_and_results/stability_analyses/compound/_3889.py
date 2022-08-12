"""_3889.py

GearSetCompoundStabilityAnalysis
"""


from typing import List

from mastapy.system_model.analyses_and_results.stability_analyses import _3757
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3927
from mastapy._internal.python_net import python_net_import

_GEAR_SET_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'GearSetCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetCompoundStabilityAnalysis',)


class GearSetCompoundStabilityAnalysis(_3927.SpecialisedAssemblyCompoundStabilityAnalysis):
    """GearSetCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_COMPOUND_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearSetCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_3757.GearSetStabilityAnalysis]':
        """List[GearSetStabilityAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3757.GearSetStabilityAnalysis]':
        """List[GearSetStabilityAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

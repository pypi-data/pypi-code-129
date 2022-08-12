"""_3906.py

MountableComponentCompoundStabilityAnalysis
"""


from typing import List

from mastapy.system_model.analyses_and_results.stability_analyses import _3775
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3854
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'MountableComponentCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('MountableComponentCompoundStabilityAnalysis',)


class MountableComponentCompoundStabilityAnalysis(_3854.ComponentCompoundStabilityAnalysis):
    """MountableComponentCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MountableComponentCompoundStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_3775.MountableComponentStabilityAnalysis]':
        """List[MountableComponentStabilityAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_3775.MountableComponentStabilityAnalysis]':
        """List[MountableComponentStabilityAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

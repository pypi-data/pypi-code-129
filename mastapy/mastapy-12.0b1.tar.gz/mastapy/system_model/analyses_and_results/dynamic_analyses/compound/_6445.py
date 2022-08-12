"""_6445.py

VirtualComponentCompoundDynamicAnalysis
"""


from typing import List

from mastapy.system_model.analyses_and_results.dynamic_analyses import _6316
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6400
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'VirtualComponentCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualComponentCompoundDynamicAnalysis',)


class VirtualComponentCompoundDynamicAnalysis(_6400.MountableComponentCompoundDynamicAnalysis):
    """VirtualComponentCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'VirtualComponentCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_6316.VirtualComponentDynamicAnalysis]':
        """List[VirtualComponentDynamicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_6316.VirtualComponentDynamicAnalysis]':
        """List[VirtualComponentDynamicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

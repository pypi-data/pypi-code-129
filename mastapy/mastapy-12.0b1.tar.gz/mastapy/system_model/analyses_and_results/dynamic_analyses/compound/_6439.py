"""_6439.py

SynchroniserSleeveCompoundDynamicAnalysis
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2545
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6438
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'SynchroniserSleeveCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserSleeveCompoundDynamicAnalysis',)


class SynchroniserSleeveCompoundDynamicAnalysis(_6438.SynchroniserPartCompoundDynamicAnalysis):
    """SynchroniserSleeveCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_COMPOUND_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SynchroniserSleeveCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2545.SynchroniserSleeve':
        """SynchroniserSleeve: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_6310.SynchroniserSleeveDynamicAnalysis]':
        """List[SynchroniserSleeveDynamicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_6310.SynchroniserSleeveDynamicAnalysis]':
        """List[SynchroniserSleeveDynamicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

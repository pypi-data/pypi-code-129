"""_6401.py

OilSealCompoundDynamicAnalysis
"""


from typing import List

from mastapy.system_model.part_model import _2406
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6272
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6359
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'OilSealCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('OilSealCompoundDynamicAnalysis',)


class OilSealCompoundDynamicAnalysis(_6359.ConnectorCompoundDynamicAnalysis):
    """OilSealCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_COMPOUND_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'OilSealCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2406.OilSeal':
        """OilSeal: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_6272.OilSealDynamicAnalysis]':
        """List[OilSealDynamicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_6272.OilSealDynamicAnalysis]':
        """List[OilSealDynamicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

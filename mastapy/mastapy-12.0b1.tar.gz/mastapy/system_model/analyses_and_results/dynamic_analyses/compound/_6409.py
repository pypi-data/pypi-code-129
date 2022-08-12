"""_6409.py

PointLoadCompoundDynamicAnalysis
"""


from typing import List

from mastapy.system_model.part_model import _2411
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6280
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6445
from mastapy._internal.python_net import python_net_import

_POINT_LOAD_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'PointLoadCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PointLoadCompoundDynamicAnalysis',)


class PointLoadCompoundDynamicAnalysis(_6445.VirtualComponentCompoundDynamicAnalysis):
    """PointLoadCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _POINT_LOAD_COMPOUND_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PointLoadCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2411.PointLoad':
        """PointLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_6280.PointLoadDynamicAnalysis]':
        """List[PointLoadDynamicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_6280.PointLoadDynamicAnalysis]':
        """List[PointLoadDynamicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

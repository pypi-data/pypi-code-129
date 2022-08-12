"""_6374.py

DatumCompoundDynamicAnalysis
"""


from typing import List

from mastapy.system_model.part_model import _2388
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6244
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6348
from mastapy._internal.python_net import python_net_import

_DATUM_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'DatumCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('DatumCompoundDynamicAnalysis',)


class DatumCompoundDynamicAnalysis(_6348.ComponentCompoundDynamicAnalysis):
    """DatumCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _DATUM_COMPOUND_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DatumCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2388.Datum':
        """Datum: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_6244.DatumDynamicAnalysis]':
        """List[DatumDynamicAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_6244.DatumDynamicAnalysis]':
        """List[DatumDynamicAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

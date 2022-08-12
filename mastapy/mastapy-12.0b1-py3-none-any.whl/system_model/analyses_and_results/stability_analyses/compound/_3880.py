"""_3880.py

DatumCompoundStabilityAnalysis
"""


from typing import List

from mastapy.system_model.part_model import _2388
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3749
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3854
from mastapy._internal.python_net import python_net_import

_DATUM_COMPOUND_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound', 'DatumCompoundStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('DatumCompoundStabilityAnalysis',)


class DatumCompoundStabilityAnalysis(_3854.ComponentCompoundStabilityAnalysis):
    """DatumCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _DATUM_COMPOUND_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DatumCompoundStabilityAnalysis.TYPE'):
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
    def component_analysis_cases_ready(self) -> 'List[_3749.DatumStabilityAnalysis]':
        """List[DatumStabilityAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3749.DatumStabilityAnalysis]':
        """List[DatumStabilityAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

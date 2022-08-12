"""_6650.py

GuideDxfModelCompoundCriticalSpeedAnalysis
"""


from typing import List

from mastapy.system_model.part_model import _2395
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6521
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6614
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'GuideDxfModelCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GuideDxfModelCompoundCriticalSpeedAnalysis',)


class GuideDxfModelCompoundCriticalSpeedAnalysis(_6614.ComponentCompoundCriticalSpeedAnalysis):
    """GuideDxfModelCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_COMPOUND_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GuideDxfModelCompoundCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2395.GuideDxfModel':
        """GuideDxfModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_6521.GuideDxfModelCriticalSpeedAnalysis]':
        """List[GuideDxfModelCriticalSpeedAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_6521.GuideDxfModelCriticalSpeedAnalysis]':
        """List[GuideDxfModelCriticalSpeedAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

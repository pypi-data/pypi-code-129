"""_6640.py

DatumCompoundCriticalSpeedAnalysis
"""


from typing import List

from mastapy.system_model.part_model import _2388
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6511
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import _6614
from mastapy._internal.python_net import python_net_import

_DATUM_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound', 'DatumCompoundCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('DatumCompoundCriticalSpeedAnalysis',)


class DatumCompoundCriticalSpeedAnalysis(_6614.ComponentCompoundCriticalSpeedAnalysis):
    """DatumCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _DATUM_COMPOUND_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DatumCompoundCriticalSpeedAnalysis.TYPE'):
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
    def component_analysis_cases_ready(self) -> 'List[_6511.DatumCriticalSpeedAnalysis]':
        """List[DatumCriticalSpeedAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_6511.DatumCriticalSpeedAnalysis]':
        """List[DatumCriticalSpeedAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

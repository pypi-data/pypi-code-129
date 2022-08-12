"""_4697.py

CVTPulleyCompoundModalAnalysis
"""


from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses import _4545
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4743
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'CVTPulleyCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTPulleyCompoundModalAnalysis',)


class CVTPulleyCompoundModalAnalysis(_4743.PulleyCompoundModalAnalysis):
    """CVTPulleyCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_COMPOUND_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CVTPulleyCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(self) -> 'List[_4545.CVTPulleyModalAnalysis]':
        """List[CVTPulleyModalAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4545.CVTPulleyModalAnalysis]':
        """List[CVTPulleyModalAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

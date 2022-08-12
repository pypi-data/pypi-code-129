"""_4706.py

DatumCompoundModalAnalysis
"""


from typing import List

from mastapy.system_model.part_model import _2388
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4554
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4680
from mastapy._internal.python_net import python_net_import

_DATUM_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'DatumCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('DatumCompoundModalAnalysis',)


class DatumCompoundModalAnalysis(_4680.ComponentCompoundModalAnalysis):
    """DatumCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _DATUM_COMPOUND_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DatumCompoundModalAnalysis.TYPE'):
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
    def component_analysis_cases_ready(self) -> 'List[_4554.DatumModalAnalysis]':
        """List[DatumModalAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4554.DatumModalAnalysis]':
        """List[DatumModalAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

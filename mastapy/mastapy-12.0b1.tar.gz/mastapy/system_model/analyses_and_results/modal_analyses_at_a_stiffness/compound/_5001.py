"""_5001.py

PowerLoadCompoundModalAnalysisAtAStiffness
"""


from typing import List

from mastapy.system_model.part_model import _2412
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4872
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _5036
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'PowerLoadCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('PowerLoadCompoundModalAnalysisAtAStiffness',)


class PowerLoadCompoundModalAnalysisAtAStiffness(_5036.VirtualComponentCompoundModalAnalysisAtAStiffness):
    """PowerLoadCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PowerLoadCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2412.PowerLoad':
        """PowerLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4872.PowerLoadModalAnalysisAtAStiffness]':
        """List[PowerLoadModalAnalysisAtAStiffness]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4872.PowerLoadModalAnalysisAtAStiffness]':
        """List[PowerLoadModalAnalysisAtAStiffness]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

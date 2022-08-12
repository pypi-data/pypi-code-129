"""_4948.py

ConicalGearSetCompoundModalAnalysisAtAStiffness
"""


from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4818
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import _4974
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound', 'ConicalGearSetCompoundModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearSetCompoundModalAnalysisAtAStiffness',)


class ConicalGearSetCompoundModalAnalysisAtAStiffness(_4974.GearSetCompoundModalAnalysisAtAStiffness):
    """ConicalGearSetCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalGearSetCompoundModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_4818.ConicalGearSetModalAnalysisAtAStiffness]':
        """List[ConicalGearSetModalAnalysisAtAStiffness]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4818.ConicalGearSetModalAnalysisAtAStiffness]':
        """List[ConicalGearSetModalAnalysisAtAStiffness]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

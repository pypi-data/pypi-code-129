"""_4689.py

ConicalGearSetCompoundModalAnalysis
"""


from typing import List

from mastapy.system_model.analyses_and_results.modal_analyses import _4536
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4715
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'ConicalGearSetCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearSetCompoundModalAnalysis',)


class ConicalGearSetCompoundModalAnalysis(_4715.GearSetCompoundModalAnalysis):
    """ConicalGearSetCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_COMPOUND_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalGearSetCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_4536.ConicalGearSetModalAnalysis]':
        """List[ConicalGearSetModalAnalysis]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4536.ConicalGearSetModalAnalysis]':
        """List[ConicalGearSetModalAnalysis]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

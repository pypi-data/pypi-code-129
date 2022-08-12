"""_4747.py

RollingRingCompoundModalAnalysis
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2535
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4603
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4694
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'RollingRingCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingCompoundModalAnalysis',)


class RollingRingCompoundModalAnalysis(_4694.CouplingHalfCompoundModalAnalysis):
    """RollingRingCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_COMPOUND_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RollingRingCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2535.RollingRing':
        """RollingRing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4603.RollingRingModalAnalysis]':
        """List[RollingRingModalAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[RollingRingCompoundModalAnalysis]':
        """List[RollingRingCompoundModalAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4603.RollingRingModalAnalysis]':
        """List[RollingRingModalAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

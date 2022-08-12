"""_4717.py

HypoidGearCompoundModalAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2473
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4569
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4659
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'HypoidGearCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearCompoundModalAnalysis',)


class HypoidGearCompoundModalAnalysis(_4659.AGMAGleasonConicalGearCompoundModalAnalysis):
    """HypoidGearCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_COMPOUND_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2473.HypoidGear':
        """HypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4569.HypoidGearModalAnalysis]':
        """List[HypoidGearModalAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4569.HypoidGearModalAnalysis]':
        """List[HypoidGearModalAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

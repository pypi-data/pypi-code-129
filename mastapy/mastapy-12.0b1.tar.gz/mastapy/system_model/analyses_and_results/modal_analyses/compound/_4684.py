"""_4684.py

ConceptGearCompoundModalAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2460
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4532
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4713
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_COMPOUND_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound', 'ConceptGearCompoundModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearCompoundModalAnalysis',)


class ConceptGearCompoundModalAnalysis(_4713.GearCompoundModalAnalysis):
    """ConceptGearCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_COMPOUND_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearCompoundModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2460.ConceptGear':
        """ConceptGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4532.ConceptGearModalAnalysis]':
        """List[ConceptGearModalAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4532.ConceptGearModalAnalysis]':
        """List[ConceptGearModalAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

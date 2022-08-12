"""_5203.py

ConceptGearSetCompoundModalAnalysisAtASpeed
"""


from typing import List

from mastapy.system_model.part_model.gears import _2461
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5074
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed.compound import _5201, _5202, _5232
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed.Compound', 'ConceptGearSetCompoundModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetCompoundModalAnalysisAtASpeed',)


class ConceptGearSetCompoundModalAnalysisAtASpeed(_5232.GearSetCompoundModalAnalysisAtASpeed):
    """ConceptGearSetCompoundModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_COMPOUND_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearSetCompoundModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2461.ConceptGearSet':
        """ConceptGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2461.ConceptGearSet':
        """ConceptGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_5074.ConceptGearSetModalAnalysisAtASpeed]':
        """List[ConceptGearSetModalAnalysisAtASpeed]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_gears_compound_modal_analysis_at_a_speed(self) -> 'List[_5201.ConceptGearCompoundModalAnalysisAtASpeed]':
        """List[ConceptGearCompoundModalAnalysisAtASpeed]: 'ConceptGearsCompoundModalAnalysisAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearsCompoundModalAnalysisAtASpeed
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_meshes_compound_modal_analysis_at_a_speed(self) -> 'List[_5202.ConceptGearMeshCompoundModalAnalysisAtASpeed]':
        """List[ConceptGearMeshCompoundModalAnalysisAtASpeed]: 'ConceptMeshesCompoundModalAnalysisAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptMeshesCompoundModalAnalysisAtASpeed
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_5074.ConceptGearSetModalAnalysisAtASpeed]':
        """List[ConceptGearSetModalAnalysisAtASpeed]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

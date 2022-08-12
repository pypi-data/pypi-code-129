"""_4401.py

ConceptCouplingHalfCompoundParametricStudyTool
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2521
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4253
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4412
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'ConceptCouplingHalfCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingHalfCompoundParametricStudyTool',)


class ConceptCouplingHalfCompoundParametricStudyTool(_4412.CouplingHalfCompoundParametricStudyTool):
    """ConceptCouplingHalfCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF_COMPOUND_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingHalfCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2521.ConceptCouplingHalf':
        """ConceptCouplingHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4253.ConceptCouplingHalfParametricStudyTool]':
        """List[ConceptCouplingHalfParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4253.ConceptCouplingHalfParametricStudyTool]':
        """List[ConceptCouplingHalfParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

"""_4429.py

FEPartCompoundParametricStudyTool
"""


from typing import List

from mastapy.system_model.part_model import _2393
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4289
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4375
from mastapy._internal.python_net import python_net_import

_FE_PART_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'FEPartCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('FEPartCompoundParametricStudyTool',)


class FEPartCompoundParametricStudyTool(_4375.AbstractShaftOrHousingCompoundParametricStudyTool):
    """FEPartCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _FE_PART_COMPOUND_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FEPartCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2393.FEPart':
        """FEPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4289.FEPartParametricStudyTool]':
        """List[FEPartParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[FEPartCompoundParametricStudyTool]':
        """List[FEPartCompoundParametricStudyTool]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4289.FEPartParametricStudyTool]':
        """List[FEPartParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

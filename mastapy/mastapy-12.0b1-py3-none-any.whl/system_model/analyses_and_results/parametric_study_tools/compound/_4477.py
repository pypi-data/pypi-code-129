"""_4477.py

SpringDamperHalfCompoundParametricStudyTool
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2540
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4347
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4412
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_HALF_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'SpringDamperHalfCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperHalfCompoundParametricStudyTool',)


class SpringDamperHalfCompoundParametricStudyTool(_4412.CouplingHalfCompoundParametricStudyTool):
    """SpringDamperHalfCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_HALF_COMPOUND_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperHalfCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2540.SpringDamperHalf':
        """SpringDamperHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4347.SpringDamperHalfParametricStudyTool]':
        """List[SpringDamperHalfParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4347.SpringDamperHalfParametricStudyTool]':
        """List[SpringDamperHalfParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

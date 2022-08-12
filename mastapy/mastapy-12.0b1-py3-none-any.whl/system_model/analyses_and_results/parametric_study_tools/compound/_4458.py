"""_4458.py

PlanetCarrierCompoundParametricStudyTool
"""


from typing import List

from mastapy.system_model.part_model import _2409
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4329
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4450
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'PlanetCarrierCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetCarrierCompoundParametricStudyTool',)


class PlanetCarrierCompoundParametricStudyTool(_4450.MountableComponentCompoundParametricStudyTool):
    """PlanetCarrierCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_COMPOUND_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PlanetCarrierCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2409.PlanetCarrier':
        """PlanetCarrier: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4329.PlanetCarrierParametricStudyTool]':
        """List[PlanetCarrierParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4329.PlanetCarrierParametricStudyTool]':
        """List[PlanetCarrierParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

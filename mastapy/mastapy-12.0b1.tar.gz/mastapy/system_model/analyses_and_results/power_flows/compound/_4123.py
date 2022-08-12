"""_4123.py

ConceptCouplingCompoundPowerFlow
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2520
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _3992
from mastapy.system_model.analyses_and_results.power_flows.compound import _4134
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'ConceptCouplingCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingCompoundPowerFlow',)


class ConceptCouplingCompoundPowerFlow(_4134.CouplingCompoundPowerFlow):
    """ConceptCouplingCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2520.ConceptCoupling':
        """ConceptCoupling: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2520.ConceptCoupling':
        """ConceptCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3992.ConceptCouplingPowerFlow]':
        """List[ConceptCouplingPowerFlow]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3992.ConceptCouplingPowerFlow]':
        """List[ConceptCouplingPowerFlow]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

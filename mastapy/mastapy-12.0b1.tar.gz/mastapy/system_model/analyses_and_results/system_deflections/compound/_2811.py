"""_2811.py

ConceptCouplingCompoundSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2520
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2653
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2822
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'ConceptCouplingCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingCompoundSystemDeflection',)


class ConceptCouplingCompoundSystemDeflection(_2822.CouplingCompoundSystemDeflection):
    """ConceptCouplingCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingCompoundSystemDeflection.TYPE'):
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
    def assembly_analysis_cases_ready(self) -> 'List[_2653.ConceptCouplingSystemDeflection]':
        """List[ConceptCouplingSystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_2653.ConceptCouplingSystemDeflection]':
        """List[ConceptCouplingSystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

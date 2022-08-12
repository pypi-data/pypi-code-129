"""_7213.py

ConceptCouplingHalfAdvancedSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2521
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6753
from mastapy.system_model.analyses_and_results.system_deflections import _2652
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7225
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_HALF_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'ConceptCouplingHalfAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingHalfAdvancedSystemDeflection',)


class ConceptCouplingHalfAdvancedSystemDeflection(_7225.CouplingHalfAdvancedSystemDeflection):
    """ConceptCouplingHalfAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_HALF_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingHalfAdvancedSystemDeflection.TYPE'):
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
    def component_load_case(self) -> '_6753.ConceptCouplingHalfLoadCase':
        """ConceptCouplingHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_system_deflection_results(self) -> 'List[_2652.ConceptCouplingHalfSystemDeflection]':
        """List[ConceptCouplingHalfSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentSystemDeflectionResults
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

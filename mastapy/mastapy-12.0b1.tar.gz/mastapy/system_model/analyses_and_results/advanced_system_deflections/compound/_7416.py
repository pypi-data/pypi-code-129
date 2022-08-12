"""_7416.py

SpecialisedAssemblyCompoundAdvancedSystemDeflection
"""


from typing import List

from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7286
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7318
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'SpecialisedAssemblyCompoundAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('SpecialisedAssemblyCompoundAdvancedSystemDeflection',)


class SpecialisedAssemblyCompoundAdvancedSystemDeflection(_7318.AbstractAssemblyCompoundAdvancedSystemDeflection):
    """SpecialisedAssemblyCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpecialisedAssemblyCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_7286.SpecialisedAssemblyAdvancedSystemDeflection]':
        """List[SpecialisedAssemblyAdvancedSystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_7286.SpecialisedAssemblyAdvancedSystemDeflection]':
        """List[SpecialisedAssemblyAdvancedSystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

"""_7405.py

PowerLoadCompoundAdvancedSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model import _2412
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7275
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import _7440
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound', 'PowerLoadCompoundAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('PowerLoadCompoundAdvancedSystemDeflection',)


class PowerLoadCompoundAdvancedSystemDeflection(_7440.VirtualComponentCompoundAdvancedSystemDeflection):
    """PowerLoadCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_COMPOUND_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PowerLoadCompoundAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2412.PowerLoad':
        """PowerLoad: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_7275.PowerLoadAdvancedSystemDeflection]':
        """List[PowerLoadAdvancedSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_7275.PowerLoadAdvancedSystemDeflection]':
        """List[PowerLoadAdvancedSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

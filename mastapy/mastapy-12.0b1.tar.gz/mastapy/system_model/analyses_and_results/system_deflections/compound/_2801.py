"""_2801.py

BevelGearCompoundSystemDeflection
"""


from typing import List

from mastapy.system_model.analyses_and_results.system_deflections import _2642
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2789
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'BevelGearCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearCompoundSystemDeflection',)


class BevelGearCompoundSystemDeflection(_2789.AGMAGleasonConicalGearCompoundSystemDeflection):
    """BevelGearCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelGearCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_2642.BevelGearSystemDeflection]':
        """List[BevelGearSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_2642.BevelGearSystemDeflection]':
        """List[BevelGearSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

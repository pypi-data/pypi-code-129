"""_2855.py

KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model.gears import _2477
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2707
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2852
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection',)


class KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection(_2852.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection):
    """KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2477.KlingelnbergCycloPalloidHypoidGear':
        """KlingelnbergCycloPalloidHypoidGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_2707.KlingelnbergCycloPalloidHypoidGearSystemDeflection]':
        """List[KlingelnbergCycloPalloidHypoidGearSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_2707.KlingelnbergCycloPalloidHypoidGearSystemDeflection]':
        """List[KlingelnbergCycloPalloidHypoidGearSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

"""_2817.py

ConicalGearCompoundSystemDeflection
"""


from typing import List

from mastapy.gears.rating.conical import _528
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2660
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2844
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'ConicalGearCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearCompoundSystemDeflection',)


class ConicalGearCompoundSystemDeflection(_2844.GearCompoundSystemDeflection):
    """ConicalGearCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalGearCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duty_cycle_rating(self) -> '_528.ConicalGearDutyCycleRating':
        """ConicalGearDutyCycleRating: 'DutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DutyCycleRating
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_duty_cycle_rating(self) -> '_528.ConicalGearDutyCycleRating':
        """ConicalGearDutyCycleRating: 'ConicalDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalDutyCycleRating
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[ConicalGearCompoundSystemDeflection]':
        """List[ConicalGearCompoundSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_2660.ConicalGearSystemDeflection]':
        """List[ConicalGearSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_2660.ConicalGearSystemDeflection]':
        """List[ConicalGearSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

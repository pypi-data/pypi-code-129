"""_4129.py

ConicalGearCompoundPowerFlow
"""


from typing import List

from mastapy.gears.rating.conical import _528
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _3997
from mastapy.system_model.analyses_and_results.power_flows.compound import _4155
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'ConicalGearCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearCompoundPowerFlow',)


class ConicalGearCompoundPowerFlow(_4155.GearCompoundPowerFlow):
    """ConicalGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalGearCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_duty_cycle_rating(self) -> '_528.ConicalGearDutyCycleRating':
        """ConicalGearDutyCycleRating: 'GearDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleRating
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gear_duty_cycle_rating(self) -> '_528.ConicalGearDutyCycleRating':
        """ConicalGearDutyCycleRating: 'ConicalGearDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearDutyCycleRating
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases(self) -> 'List[_3997.ConicalGearPowerFlow]':
        """List[ConicalGearPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_3997.ConicalGearPowerFlow]':
        """List[ConicalGearPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

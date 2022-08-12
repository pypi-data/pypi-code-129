"""_4131.py

ConicalGearSetCompoundPowerFlow
"""


from typing import List

from mastapy.gears.rating.conical import _531
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _3998
from mastapy.system_model.analyses_and_results.power_flows.compound import _4157
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'ConicalGearSetCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearSetCompoundPowerFlow',)


class ConicalGearSetCompoundPowerFlow(_4157.GearSetCompoundPowerFlow):
    """ConicalGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalGearSetCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_set_duty_cycle_rating(self) -> '_531.ConicalGearSetDutyCycleRating':
        """ConicalGearSetDutyCycleRating: 'GearSetDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDutyCycleRating
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gear_set_duty_cycle_rating(self) -> '_531.ConicalGearSetDutyCycleRating':
        """ConicalGearSetDutyCycleRating: 'ConicalGearSetDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearSetDutyCycleRating
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases(self) -> 'List[_3998.ConicalGearSetPowerFlow]':
        """List[ConicalGearSetPowerFlow]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3998.ConicalGearSetPowerFlow]':
        """List[ConicalGearSetPowerFlow]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

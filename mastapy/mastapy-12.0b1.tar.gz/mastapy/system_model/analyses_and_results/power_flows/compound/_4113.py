"""_4113.py

BevelGearCompoundPowerFlow
"""


from typing import List

from mastapy.system_model.analyses_and_results.power_flows import _3981
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4101
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'BevelGearCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearCompoundPowerFlow',)


class BevelGearCompoundPowerFlow(_4101.AGMAGleasonConicalGearCompoundPowerFlow):
    """BevelGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelGearCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_3981.BevelGearPowerFlow]':
        """List[BevelGearPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_3981.BevelGearPowerFlow]':
        """List[BevelGearPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

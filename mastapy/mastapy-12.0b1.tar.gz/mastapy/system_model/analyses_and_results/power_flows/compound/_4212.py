"""_4212.py

SynchroniserPartCompoundPowerFlow
"""


from typing import List

from mastapy.system_model.analyses_and_results.power_flows import _4081
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4136
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'SynchroniserPartCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserPartCompoundPowerFlow',)


class SynchroniserPartCompoundPowerFlow(_4136.CouplingHalfCompoundPowerFlow):
    """SynchroniserPartCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SynchroniserPartCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_4081.SynchroniserPartPowerFlow]':
        """List[SynchroniserPartPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4081.SynchroniserPartPowerFlow]':
        """List[SynchroniserPartPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

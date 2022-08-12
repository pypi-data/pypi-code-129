"""_4115.py

BevelGearSetCompoundPowerFlow
"""


from typing import List

from mastapy.system_model.analyses_and_results.power_flows import _3982
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4103
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'BevelGearSetCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelGearSetCompoundPowerFlow',)


class BevelGearSetCompoundPowerFlow(_4103.AGMAGleasonConicalGearSetCompoundPowerFlow):
    """BevelGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelGearSetCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(self) -> 'List[_3982.BevelGearSetPowerFlow]':
        """List[BevelGearSetPowerFlow]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3982.BevelGearSetPowerFlow]':
        """List[BevelGearSetPowerFlow]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

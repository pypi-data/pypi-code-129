"""_4116.py

BoltCompoundPowerFlow
"""


from typing import List

from mastapy.system_model.part_model import _2382
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _3984
from mastapy.system_model.analyses_and_results.power_flows.compound import _4122
from mastapy._internal.python_net import python_net_import

_BOLT_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'BoltCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltCompoundPowerFlow',)


class BoltCompoundPowerFlow(_4122.ComponentCompoundPowerFlow):
    """BoltCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _BOLT_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BoltCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2382.Bolt':
        """Bolt: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_3984.BoltPowerFlow]':
        """List[BoltPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_3984.BoltPowerFlow]':
        """List[BoltPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

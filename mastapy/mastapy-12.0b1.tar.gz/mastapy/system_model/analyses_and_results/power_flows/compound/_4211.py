"""_4211.py

SynchroniserHalfCompoundPowerFlow
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2543
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4080
from mastapy.system_model.analyses_and_results.power_flows.compound import _4212
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'SynchroniserHalfCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserHalfCompoundPowerFlow',)


class SynchroniserHalfCompoundPowerFlow(_4212.SynchroniserPartCompoundPowerFlow):
    """SynchroniserHalfCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SynchroniserHalfCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2543.SynchroniserHalf':
        """SynchroniserHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4080.SynchroniserHalfPowerFlow]':
        """List[SynchroniserHalfPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4080.SynchroniserHalfPowerFlow]':
        """List[SynchroniserHalfPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

"""_4175.py

OilSealCompoundPowerFlow
"""


from typing import List

from mastapy.system_model.part_model import _2406
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4043
from mastapy.system_model.analyses_and_results.power_flows.compound import _4133
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'OilSealCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('OilSealCompoundPowerFlow',)


class OilSealCompoundPowerFlow(_4133.ConnectorCompoundPowerFlow):
    """OilSealCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'OilSealCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2406.OilSeal':
        """OilSeal: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4043.OilSealPowerFlow]':
        """List[OilSealPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4043.OilSealPowerFlow]':
        """List[OilSealPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

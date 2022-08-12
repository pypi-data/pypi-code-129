"""_4169.py

KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
"""


from typing import List

from mastapy.system_model.part_model.gears import _2479
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4038
from mastapy.system_model.analyses_and_results.power_flows.compound import _4163
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow',)


class KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow(_4163.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow):
    """KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2479.KlingelnbergCycloPalloidSpiralBevelGear':
        """KlingelnbergCycloPalloidSpiralBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4038.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4038.KlingelnbergCycloPalloidSpiralBevelGearPowerFlow]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

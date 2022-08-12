"""_4147.py

CylindricalPlanetGearCompoundPowerFlow
"""


from typing import List

from mastapy.system_model.analyses_and_results.power_flows import _4015
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4144
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'CylindricalPlanetGearCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalPlanetGearCompoundPowerFlow',)


class CylindricalPlanetGearCompoundPowerFlow(_4144.CylindricalGearCompoundPowerFlow):
    """CylindricalPlanetGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalPlanetGearCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(self) -> 'List[_4015.CylindricalPlanetGearPowerFlow]':
        """List[CylindricalPlanetGearPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4015.CylindricalPlanetGearPowerFlow]':
        """List[CylindricalPlanetGearPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

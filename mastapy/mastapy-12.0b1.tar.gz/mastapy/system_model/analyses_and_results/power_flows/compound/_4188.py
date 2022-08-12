"""_4188.py

RollingRingAssemblyCompoundPowerFlow
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2536
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _4058
from mastapy.system_model.analyses_and_results.power_flows.compound import _4195
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'RollingRingAssemblyCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingAssemblyCompoundPowerFlow',)


class RollingRingAssemblyCompoundPowerFlow(_4195.SpecialisedAssemblyCompoundPowerFlow):
    """RollingRingAssemblyCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RollingRingAssemblyCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2536.RollingRingAssembly':
        """RollingRingAssembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2536.RollingRingAssembly':
        """RollingRingAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4058.RollingRingAssemblyPowerFlow]':
        """List[RollingRingAssemblyPowerFlow]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4058.RollingRingAssemblyPowerFlow]':
        """List[RollingRingAssemblyPowerFlow]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

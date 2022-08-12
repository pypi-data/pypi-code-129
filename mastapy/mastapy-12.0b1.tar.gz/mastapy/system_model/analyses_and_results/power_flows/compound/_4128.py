"""_4128.py

ConceptGearSetCompoundPowerFlow
"""


from typing import List

from mastapy.system_model.part_model.gears import _2461
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows import _3995
from mastapy.system_model.analyses_and_results.power_flows.compound import _4126, _4127, _4157
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'ConceptGearSetCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetCompoundPowerFlow',)


class ConceptGearSetCompoundPowerFlow(_4157.GearSetCompoundPowerFlow):
    """ConceptGearSetCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearSetCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2461.ConceptGearSet':
        """ConceptGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2461.ConceptGearSet':
        """ConceptGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_3995.ConceptGearSetPowerFlow]':
        """List[ConceptGearSetPowerFlow]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_gears_compound_power_flow(self) -> 'List[_4126.ConceptGearCompoundPowerFlow]':
        """List[ConceptGearCompoundPowerFlow]: 'ConceptGearsCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearsCompoundPowerFlow
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_meshes_compound_power_flow(self) -> 'List[_4127.ConceptGearMeshCompoundPowerFlow]':
        """List[ConceptGearMeshCompoundPowerFlow]: 'ConceptMeshesCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptMeshesCompoundPowerFlow
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_3995.ConceptGearSetPowerFlow]':
        """List[ConceptGearSetPowerFlow]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

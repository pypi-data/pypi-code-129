"""_7181.py

ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation
"""


from typing import List

from mastapy.system_model.part_model.gears import _2493
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7052
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import _7179, _7180, _7071
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound', 'ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation',)


class ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation(_7071.BevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation):
    """ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2493.ZerolBevelGearSet':
        """ZerolBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2493.ZerolBevelGearSet':
        """ZerolBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_7052.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation]':
        """List[ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_gears_compound_advanced_time_stepping_analysis_for_modulation(self) -> 'List[_7179.ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation]: 'ZerolBevelGearsCompoundAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearsCompoundAdvancedTimeSteppingAnalysisForModulation
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_meshes_compound_advanced_time_stepping_analysis_for_modulation(self) -> 'List[_7180.ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[ZerolBevelGearMeshCompoundAdvancedTimeSteppingAnalysisForModulation]: 'ZerolBevelMeshesCompoundAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelMeshesCompoundAdvancedTimeSteppingAnalysisForModulation
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_7052.ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation]':
        """List[ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

"""_7052.py

ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation
"""


from typing import List

from mastapy.system_model.part_model.gears import _2493
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6901
from mastapy.system_model.analyses_and_results.system_deflections import _2774
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _7050, _7051, _6941
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation',)


class ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation(_6941.BevelGearSetAdvancedTimeSteppingAnalysisForModulation):
    """ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSetAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def assembly_load_case(self) -> '_6901.ZerolBevelGearSetLoadCase':
        """ZerolBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2774.ZerolBevelGearSetSystemDeflection':
        """ZerolBevelGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def zerol_bevel_gears_advanced_time_stepping_analysis_for_modulation(self) -> 'List[_7050.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation]':
        """List[ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation]: 'ZerolBevelGearsAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearsAdvancedTimeSteppingAnalysisForModulation
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_meshes_advanced_time_stepping_analysis_for_modulation(self) -> 'List[_7051.ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation]':
        """List[ZerolBevelGearMeshAdvancedTimeSteppingAnalysisForModulation]: 'ZerolBevelMeshesAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelMeshesAdvancedTimeSteppingAnalysisForModulation
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

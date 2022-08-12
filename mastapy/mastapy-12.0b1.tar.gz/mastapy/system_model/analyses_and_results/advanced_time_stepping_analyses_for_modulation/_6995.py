"""_6995.py

KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation
"""


from typing import List

from mastapy.system_model.part_model.gears import _2478
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6831
from mastapy.system_model.analyses_and_results.system_deflections import _2706
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6993, _6994, _6992
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation',)


class KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation(_6992.KlingelnbergCycloPalloidConicalGearSetAdvancedTimeSteppingAnalysisForModulation):
    """KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2478.KlingelnbergCycloPalloidHypoidGearSet':
        """KlingelnbergCycloPalloidHypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6831.KlingelnbergCycloPalloidHypoidGearSetLoadCase':
        """KlingelnbergCycloPalloidHypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2706.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection':
        """KlingelnbergCycloPalloidHypoidGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_advanced_time_stepping_analysis_for_modulation(self) -> 'List[_6993.KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation]':
        """List[KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation]: 'KlingelnbergCycloPalloidHypoidGearsAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsAdvancedTimeSteppingAnalysisForModulation
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_advanced_time_stepping_analysis_for_modulation(self) -> 'List[_6994.KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation]':
        """List[KlingelnbergCycloPalloidHypoidGearMeshAdvancedTimeSteppingAnalysisForModulation]: 'KlingelnbergCycloPalloidHypoidMeshesAdvancedTimeSteppingAnalysisForModulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshesAdvancedTimeSteppingAnalysisForModulation
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

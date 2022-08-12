"""_7261.py

KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model.gears import _2480
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6834
from mastapy.gears.rating.klingelnberg_spiral_bevel import _398
from mastapy.system_model.analyses_and_results.system_deflections import _2709
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7259, _7260, _7255
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection',)


class KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection(_7255.KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection):
    """KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2480.KlingelnbergCycloPalloidSpiralBevelGearSet':
        """KlingelnbergCycloPalloidSpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6834.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase':
        """KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_398.KlingelnbergCycloPalloidSpiralBevelGearSetRating':
        """KlingelnbergCycloPalloidSpiralBevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_398.KlingelnbergCycloPalloidSpiralBevelGearSetRating':
        """KlingelnbergCycloPalloidSpiralBevelGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2709.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblySystemDeflectionResults
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_advanced_system_deflection(self) -> 'List[_7259.KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearAdvancedSystemDeflection]: 'KlingelnbergCycloPalloidSpiralBevelGearsAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsAdvancedSystemDeflection
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_advanced_system_deflection(self) -> 'List[_7260.KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearMeshAdvancedSystemDeflection]: 'KlingelnbergCycloPalloidSpiralBevelMeshesAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesAdvancedSystemDeflection
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

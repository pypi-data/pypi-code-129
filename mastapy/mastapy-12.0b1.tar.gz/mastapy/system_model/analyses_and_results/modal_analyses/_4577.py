"""_4577.py

KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2478
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6831
from mastapy.system_model.analyses_and_results.system_deflections import _2706
from mastapy.system_model.analyses_and_results.modal_analyses import _4576, _4575, _4574
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'KlingelnbergCycloPalloidHypoidGearSetModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearSetModalAnalysis',)


class KlingelnbergCycloPalloidHypoidGearSetModalAnalysis(_4574.KlingelnbergCycloPalloidConicalGearSetModalAnalysis):
    """KlingelnbergCycloPalloidHypoidGearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearSetModalAnalysis.TYPE'):
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
    def klingelnberg_cyclo_palloid_hypoid_gears_modal_analysis(self) -> 'List[_4576.KlingelnbergCycloPalloidHypoidGearModalAnalysis]':
        """List[KlingelnbergCycloPalloidHypoidGearModalAnalysis]: 'KlingelnbergCycloPalloidHypoidGearsModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearsModalAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_modal_analysis(self) -> 'List[_4575.KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis]':
        """List[KlingelnbergCycloPalloidHypoidGearMeshModalAnalysis]: 'KlingelnbergCycloPalloidHypoidMeshesModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshesModalAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

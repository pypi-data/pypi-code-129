"""_5383.py

KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2480
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6834
from mastapy.system_model.analyses_and_results.mbd_analyses import _5382, _5381, _5377
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis',)


class KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis(_5377.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis):
    """KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis.TYPE'):
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
    def gears(self) -> 'List[_5382.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gears_multibody_dynamics_analysis(self) -> 'List[_5382.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelGearsMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearsMultibodyDynamicsAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_meshes_multibody_dynamics_analysis(self) -> 'List[_5381.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis]: 'KlingelnbergCycloPalloidSpiralBevelMeshesMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelMeshesMultibodyDynamicsAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

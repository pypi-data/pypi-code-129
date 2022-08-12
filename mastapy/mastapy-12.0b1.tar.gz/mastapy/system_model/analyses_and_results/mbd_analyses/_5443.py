"""_5443.py

WormGearSetMultibodyDynamicsAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2491
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6898
from mastapy.system_model.analyses_and_results.mbd_analyses import _5442, _5441, _5365
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'WormGearSetMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetMultibodyDynamicsAnalysis',)


class WormGearSetMultibodyDynamicsAnalysis(_5365.GearSetMultibodyDynamicsAnalysis):
    """WormGearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2491.WormGearSet':
        """WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6898.WormGearSetLoadCase':
        """WormGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gears(self) -> 'List[_5442.WormGearMultibodyDynamicsAnalysis]':
        """List[WormGearMultibodyDynamicsAnalysis]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_gears_multibody_dynamics_analysis(self) -> 'List[_5442.WormGearMultibodyDynamicsAnalysis]':
        """List[WormGearMultibodyDynamicsAnalysis]: 'WormGearsMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearsMultibodyDynamicsAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_meshes_multibody_dynamics_analysis(self) -> 'List[_5441.WormGearMeshMultibodyDynamicsAnalysis]':
        """List[WormGearMeshMultibodyDynamicsAnalysis]: 'WormMeshesMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormMeshesMultibodyDynamicsAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

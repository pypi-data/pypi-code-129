"""_5425.py

StraightBevelGearSetMultibodyDynamicsAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2487
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6878
from mastapy.system_model.analyses_and_results.mbd_analyses import _5424, _5423, _5321
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'StraightBevelGearSetMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSetMultibodyDynamicsAnalysis',)


class StraightBevelGearSetMultibodyDynamicsAnalysis(_5321.BevelGearSetMultibodyDynamicsAnalysis):
    """StraightBevelGearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelGearSetMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2487.StraightBevelGearSet':
        """StraightBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6878.StraightBevelGearSetLoadCase':
        """StraightBevelGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gears(self) -> 'List[_5424.StraightBevelGearMultibodyDynamicsAnalysis]':
        """List[StraightBevelGearMultibodyDynamicsAnalysis]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_gears_multibody_dynamics_analysis(self) -> 'List[_5424.StraightBevelGearMultibodyDynamicsAnalysis]':
        """List[StraightBevelGearMultibodyDynamicsAnalysis]: 'StraightBevelGearsMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearsMultibodyDynamicsAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_meshes_multibody_dynamics_analysis(self) -> 'List[_5423.StraightBevelGearMeshMultibodyDynamicsAnalysis]':
        """List[StraightBevelGearMeshMultibodyDynamicsAnalysis]: 'StraightBevelMeshesMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelMeshesMultibodyDynamicsAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

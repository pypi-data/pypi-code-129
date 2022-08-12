"""_6570.py

StraightBevelGearSetCriticalSpeedAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2487
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6878
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6568, _6569, _6476
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'StraightBevelGearSetCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSetCriticalSpeedAnalysis',)


class StraightBevelGearSetCriticalSpeedAnalysis(_6476.BevelGearSetCriticalSpeedAnalysis):
    """StraightBevelGearSetCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelGearSetCriticalSpeedAnalysis.TYPE'):
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
    def straight_bevel_gears_critical_speed_analysis(self) -> 'List[_6568.StraightBevelGearCriticalSpeedAnalysis]':
        """List[StraightBevelGearCriticalSpeedAnalysis]: 'StraightBevelGearsCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearsCriticalSpeedAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_meshes_critical_speed_analysis(self) -> 'List[_6569.StraightBevelGearMeshCriticalSpeedAnalysis]':
        """List[StraightBevelGearMeshCriticalSpeedAnalysis]: 'StraightBevelMeshesCriticalSpeedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelMeshesCriticalSpeedAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

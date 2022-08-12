"""_3827.py

ZerolBevelGearSetStabilityAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2493
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6901
from mastapy.system_model.analyses_and_results.stability_analyses import _3828, _3826, _3714
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'ZerolBevelGearSetStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSetStabilityAnalysis',)


class ZerolBevelGearSetStabilityAnalysis(_3714.BevelGearSetStabilityAnalysis):
    """ZerolBevelGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSetStabilityAnalysis.TYPE'):
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
    def zerol_bevel_gears_stability_analysis(self) -> 'List[_3828.ZerolBevelGearStabilityAnalysis]':
        """List[ZerolBevelGearStabilityAnalysis]: 'ZerolBevelGearsStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearsStabilityAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_meshes_stability_analysis(self) -> 'List[_3826.ZerolBevelGearMeshStabilityAnalysis]':
        """List[ZerolBevelGearMeshStabilityAnalysis]: 'ZerolBevelMeshesStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelMeshesStabilityAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

"""_3824.py

WormGearSetStabilityAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2491
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6898
from mastapy.system_model.analyses_and_results.stability_analyses import _3825, _3823, _3757
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'WormGearSetStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetStabilityAnalysis',)


class WormGearSetStabilityAnalysis(_3757.GearSetStabilityAnalysis):
    """WormGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetStabilityAnalysis.TYPE'):
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
    def worm_gears_stability_analysis(self) -> 'List[_3825.WormGearStabilityAnalysis]':
        """List[WormGearStabilityAnalysis]: 'WormGearsStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearsStabilityAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_meshes_stability_analysis(self) -> 'List[_3823.WormGearMeshStabilityAnalysis]':
        """List[WormGearMeshStabilityAnalysis]: 'WormMeshesStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormMeshesStabilityAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

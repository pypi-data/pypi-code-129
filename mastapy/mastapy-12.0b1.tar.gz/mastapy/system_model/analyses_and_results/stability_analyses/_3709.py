"""_3709.py

BevelDifferentialGearSetStabilityAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2455
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6739
from mastapy.system_model.analyses_and_results.stability_analyses import _3710, _3708, _3714
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'BevelDifferentialGearSetStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSetStabilityAnalysis',)


class BevelDifferentialGearSetStabilityAnalysis(_3714.BevelGearSetStabilityAnalysis):
    """BevelDifferentialGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSetStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2455.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6739.BevelDifferentialGearSetLoadCase':
        """BevelDifferentialGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_differential_gears_stability_analysis(self) -> 'List[_3710.BevelDifferentialGearStabilityAnalysis]':
        """List[BevelDifferentialGearStabilityAnalysis]: 'BevelDifferentialGearsStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialGearsStabilityAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_meshes_stability_analysis(self) -> 'List[_3708.BevelDifferentialGearMeshStabilityAnalysis]':
        """List[BevelDifferentialGearMeshStabilityAnalysis]: 'BevelDifferentialMeshesStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialMeshesStabilityAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

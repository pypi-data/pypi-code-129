"""_6301.py

StraightBevelDiffGearSetDynamicAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2485
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6875
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6299, _6300, _6211
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'StraightBevelDiffGearSetDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSetDynamicAnalysis',)


class StraightBevelDiffGearSetDynamicAnalysis(_6211.BevelGearSetDynamicAnalysis):
    """StraightBevelDiffGearSetDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSetDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2485.StraightBevelDiffGearSet':
        """StraightBevelDiffGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6875.StraightBevelDiffGearSetLoadCase':
        """StraightBevelDiffGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def straight_bevel_diff_gears_dynamic_analysis(self) -> 'List[_6299.StraightBevelDiffGearDynamicAnalysis]':
        """List[StraightBevelDiffGearDynamicAnalysis]: 'StraightBevelDiffGearsDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGearsDynamicAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_meshes_dynamic_analysis(self) -> 'List[_6300.StraightBevelDiffGearMeshDynamicAnalysis]':
        """List[StraightBevelDiffGearMeshDynamicAnalysis]: 'StraightBevelDiffMeshesDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffMeshesDynamicAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

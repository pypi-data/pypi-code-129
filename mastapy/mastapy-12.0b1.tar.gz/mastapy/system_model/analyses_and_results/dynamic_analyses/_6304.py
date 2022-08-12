"""_6304.py

StraightBevelGearSetDynamicAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2487
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6878
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302, _6303, _6211
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'StraightBevelGearSetDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSetDynamicAnalysis',)


class StraightBevelGearSetDynamicAnalysis(_6211.BevelGearSetDynamicAnalysis):
    """StraightBevelGearSetDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelGearSetDynamicAnalysis.TYPE'):
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
    def straight_bevel_gears_dynamic_analysis(self) -> 'List[_6302.StraightBevelGearDynamicAnalysis]':
        """List[StraightBevelGearDynamicAnalysis]: 'StraightBevelGearsDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearsDynamicAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_meshes_dynamic_analysis(self) -> 'List[_6303.StraightBevelGearMeshDynamicAnalysis]':
        """List[StraightBevelGearMeshDynamicAnalysis]: 'StraightBevelMeshesDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelMeshesDynamicAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

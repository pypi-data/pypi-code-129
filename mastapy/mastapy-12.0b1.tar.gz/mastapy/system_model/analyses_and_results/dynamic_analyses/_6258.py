"""_6258.py

HypoidGearSetDynamicAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2474
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6821
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6256, _6257, _6199
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'HypoidGearSetDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetDynamicAnalysis',)


class HypoidGearSetDynamicAnalysis(_6199.AGMAGleasonConicalGearSetDynamicAnalysis):
    """HypoidGearSetDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSetDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2474.HypoidGearSet':
        """HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6821.HypoidGearSetLoadCase':
        """HypoidGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hypoid_gears_dynamic_analysis(self) -> 'List[_6256.HypoidGearDynamicAnalysis]':
        """List[HypoidGearDynamicAnalysis]: 'HypoidGearsDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearsDynamicAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_meshes_dynamic_analysis(self) -> 'List[_6257.HypoidGearMeshDynamicAnalysis]':
        """List[HypoidGearMeshDynamicAnalysis]: 'HypoidMeshesDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidMeshesDynamicAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

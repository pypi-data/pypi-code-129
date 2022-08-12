"""_5107.py

HypoidGearSetModalAnalysisAtASpeed
"""


from typing import List

from mastapy.system_model.part_model.gears import _2474
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6821
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5106, _5105, _5049
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'HypoidGearSetModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetModalAnalysisAtASpeed',)


class HypoidGearSetModalAnalysisAtASpeed(_5049.AGMAGleasonConicalGearSetModalAnalysisAtASpeed):
    """HypoidGearSetModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSetModalAnalysisAtASpeed.TYPE'):
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
    def hypoid_gears_modal_analysis_at_a_speed(self) -> 'List[_5106.HypoidGearModalAnalysisAtASpeed]':
        """List[HypoidGearModalAnalysisAtASpeed]: 'HypoidGearsModalAnalysisAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearsModalAnalysisAtASpeed
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_meshes_modal_analysis_at_a_speed(self) -> 'List[_5105.HypoidGearMeshModalAnalysisAtASpeed]':
        """List[HypoidGearMeshModalAnalysisAtASpeed]: 'HypoidMeshesModalAnalysisAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidMeshesModalAnalysisAtASpeed
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

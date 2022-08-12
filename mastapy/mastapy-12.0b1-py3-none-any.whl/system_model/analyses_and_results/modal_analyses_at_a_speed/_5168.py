"""_5168.py

WormGearSetModalAnalysisAtASpeed
"""


from typing import List

from mastapy.system_model.part_model.gears import _2491
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6898
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5167, _5166, _5103
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'WormGearSetModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetModalAnalysisAtASpeed',)


class WormGearSetModalAnalysisAtASpeed(_5103.GearSetModalAnalysisAtASpeed):
    """WormGearSetModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetModalAnalysisAtASpeed.TYPE'):
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
    def worm_gears_modal_analysis_at_a_speed(self) -> 'List[_5167.WormGearModalAnalysisAtASpeed]':
        """List[WormGearModalAnalysisAtASpeed]: 'WormGearsModalAnalysisAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearsModalAnalysisAtASpeed
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_meshes_modal_analysis_at_a_speed(self) -> 'List[_5166.WormGearMeshModalAnalysisAtASpeed]':
        """List[WormGearMeshModalAnalysisAtASpeed]: 'WormMeshesModalAnalysisAtASpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormMeshesModalAnalysisAtASpeed
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

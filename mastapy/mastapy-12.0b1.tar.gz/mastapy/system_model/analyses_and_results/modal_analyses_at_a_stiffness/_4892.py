"""_4892.py

StraightBevelDiffGearSetModalAnalysisAtAStiffness
"""


from typing import List

from mastapy.system_model.part_model.gears import _2485
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6875
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4891, _4890, _4802
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'StraightBevelDiffGearSetModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSetModalAnalysisAtAStiffness',)


class StraightBevelDiffGearSetModalAnalysisAtAStiffness(_4802.BevelGearSetModalAnalysisAtAStiffness):
    """StraightBevelDiffGearSetModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET_MODAL_ANALYSIS_AT_A_STIFFNESS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSetModalAnalysisAtAStiffness.TYPE'):
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
    def straight_bevel_diff_gears_modal_analysis_at_a_stiffness(self) -> 'List[_4891.StraightBevelDiffGearModalAnalysisAtAStiffness]':
        """List[StraightBevelDiffGearModalAnalysisAtAStiffness]: 'StraightBevelDiffGearsModalAnalysisAtAStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGearsModalAnalysisAtAStiffness
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_meshes_modal_analysis_at_a_stiffness(self) -> 'List[_4890.StraightBevelDiffGearMeshModalAnalysisAtAStiffness]':
        """List[StraightBevelDiffGearMeshModalAnalysisAtAStiffness]: 'StraightBevelDiffMeshesModalAnalysisAtAStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffMeshesModalAnalysisAtAStiffness
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

"""_6869.py

SpiralBevelGearSetLoadCase
"""


from typing import List

from mastapy.system_model.part_model.gears import _2483
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6867, _6868, _6744
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'SpiralBevelGearSetLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetLoadCase',)


class SpiralBevelGearSetLoadCase(_6744.BevelGearSetLoadCase):
    """SpiralBevelGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2483.SpiralBevelGearSet':
        """SpiralBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gears(self) -> 'List[_6867.SpiralBevelGearLoadCase]':
        """List[SpiralBevelGearLoadCase]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_gears_load_case(self) -> 'List[_6867.SpiralBevelGearLoadCase]':
        """List[SpiralBevelGearLoadCase]: 'SpiralBevelGearsLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGearsLoadCase
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_meshes_load_case(self) -> 'List[_6868.SpiralBevelGearMeshLoadCase]':
        """List[SpiralBevelGearMeshLoadCase]: 'SpiralBevelMeshesLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelMeshesLoadCase
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

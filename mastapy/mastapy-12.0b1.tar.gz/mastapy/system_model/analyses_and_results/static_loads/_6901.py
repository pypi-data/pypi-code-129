"""_6901.py

ZerolBevelGearSetLoadCase
"""


from typing import List

from mastapy.system_model.part_model.gears import _2493
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6899, _6900, _6744
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ZerolBevelGearSetLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSetLoadCase',)


class ZerolBevelGearSetLoadCase(_6744.BevelGearSetLoadCase):
    """ZerolBevelGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSetLoadCase.TYPE'):
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
    def gears(self) -> 'List[_6899.ZerolBevelGearLoadCase]':
        """List[ZerolBevelGearLoadCase]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_gears_load_case(self) -> 'List[_6899.ZerolBevelGearLoadCase]':
        """List[ZerolBevelGearLoadCase]: 'ZerolBevelGearsLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearsLoadCase
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_meshes_load_case(self) -> 'List[_6900.ZerolBevelGearMeshLoadCase]':
        """List[ZerolBevelGearMeshLoadCase]: 'ZerolBevelMeshesLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelMeshesLoadCase
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

"""_6821.py

HypoidGearSetLoadCase
"""


from typing import List

from mastapy.system_model.part_model.gears import _2474
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6819, _6820, _6730
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'HypoidGearSetLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetLoadCase',)


class HypoidGearSetLoadCase(_6730.AGMAGleasonConicalGearSetLoadCase):
    """HypoidGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSetLoadCase.TYPE'):
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
    def gears(self) -> 'List[_6819.HypoidGearLoadCase]':
        """List[HypoidGearLoadCase]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_gears_load_case(self) -> 'List[_6819.HypoidGearLoadCase]':
        """List[HypoidGearLoadCase]: 'HypoidGearsLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearsLoadCase
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_meshes_load_case(self) -> 'List[_6820.HypoidGearMeshLoadCase]':
        """List[HypoidGearMeshLoadCase]: 'HypoidMeshesLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidMeshesLoadCase
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

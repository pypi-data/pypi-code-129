"""_6739.py

BevelDifferentialGearSetLoadCase
"""


from typing import List

from mastapy.system_model.part_model.gears import _2455
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6737, _6738, _6744
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BevelDifferentialGearSetLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSetLoadCase',)


class BevelDifferentialGearSetLoadCase(_6744.BevelGearSetLoadCase):
    """BevelDifferentialGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSetLoadCase.TYPE'):
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
    def gears(self) -> 'List[_6737.BevelDifferentialGearLoadCase]':
        """List[BevelDifferentialGearLoadCase]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_gears_load_case(self) -> 'List[_6737.BevelDifferentialGearLoadCase]':
        """List[BevelDifferentialGearLoadCase]: 'BevelDifferentialGearsLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialGearsLoadCase
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_meshes_load_case(self) -> 'List[_6738.BevelDifferentialGearMeshLoadCase]':
        """List[BevelDifferentialGearMeshLoadCase]: 'BevelDifferentialMeshesLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialMeshesLoadCase
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

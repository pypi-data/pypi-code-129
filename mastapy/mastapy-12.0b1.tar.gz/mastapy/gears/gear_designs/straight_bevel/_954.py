"""_954.py

StraightBevelGearSetDesign
"""


from typing import List

from mastapy.gears.gear_designs.straight_bevel import _952, _953
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.bevel import _1170
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.StraightBevel', 'StraightBevelGearSetDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSetDesign',)


class StraightBevelGearSetDesign(_1170.BevelGearSetDesign):
    """StraightBevelGearSetDesign

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelGearSetDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gears(self) -> 'List[_952.StraightBevelGearDesign]':
        """List[StraightBevelGearDesign]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_gears(self) -> 'List[_952.StraightBevelGearDesign]':
        """List[StraightBevelGearDesign]: 'StraightBevelGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_meshes(self) -> 'List[_953.StraightBevelGearMeshDesign]':
        """List[StraightBevelGearMeshDesign]: 'StraightBevelMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelMeshes
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

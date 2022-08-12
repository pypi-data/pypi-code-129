"""_395.py

SpiralBevelGearSetRating
"""


from typing import List

from mastapy.gears.gear_designs.spiral_bevel import _962
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.spiral_bevel import _394, _393
from mastapy.gears.rating.bevel import _546
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.SpiralBevel', 'SpiralBevelGearSetRating')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSetRating',)


class SpiralBevelGearSetRating(_546.BevelGearSetRating):
    """SpiralBevelGearSetRating

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SET_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSetRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def spiral_bevel_gear_set(self) -> '_962.SpiralBevelGearSetDesign':
        """SpiralBevelGearSetDesign: 'SpiralBevelGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGearSet
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def spiral_bevel_gear_ratings(self) -> 'List[_394.SpiralBevelGearRating]':
        """List[SpiralBevelGearRating]: 'SpiralBevelGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGearRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_mesh_ratings(self) -> 'List[_393.SpiralBevelGearMeshRating]':
        """List[SpiralBevelGearMeshRating]: 'SpiralBevelMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelMeshRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

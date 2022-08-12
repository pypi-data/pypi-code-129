"""_386.py

StraightBevelGearMeshRating
"""


from typing import List

from mastapy.gears.gear_designs.straight_bevel import _953
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.straight_bevel import _387
from mastapy.gears.rating.bevel import _544
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.StraightBevel', 'StraightBevelGearMeshRating')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearMeshRating',)


class StraightBevelGearMeshRating(_544.BevelGearMeshRating):
    """StraightBevelGearMeshRating

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelGearMeshRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def straight_bevel_gear_mesh(self) -> '_953.StraightBevelGearMeshDesign':
        """StraightBevelGearMeshDesign: 'StraightBevelGearMesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearMesh
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def straight_bevel_gear_ratings(self) -> 'List[_387.StraightBevelGearRating]':
        """List[StraightBevelGearRating]: 'StraightBevelGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

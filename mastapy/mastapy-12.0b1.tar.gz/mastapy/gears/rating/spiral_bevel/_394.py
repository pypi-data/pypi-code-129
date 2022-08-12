"""_394.py

SpiralBevelGearRating
"""


from mastapy.gears.gear_designs.spiral_bevel import _960
from mastapy._internal import constructor
from mastapy.gears.rating.bevel import _545
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.SpiralBevel', 'SpiralBevelGearRating')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearRating',)


class SpiralBevelGearRating(_545.BevelGearRating):
    """SpiralBevelGearRating

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def spiral_bevel_gear(self) -> '_960.SpiralBevelGearDesign':
        """SpiralBevelGearDesign: 'SpiralBevelGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGear
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

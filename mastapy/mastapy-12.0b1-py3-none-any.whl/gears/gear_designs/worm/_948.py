"""_948.py

WormGearDesign
"""


from mastapy.gears import _324
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.gears.gear_designs import _938
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Worm', 'WormGearDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearDesign',)


class WormGearDesign(_938.GearDesign):
    """WormGearDesign

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hand(self) -> '_324.Hand':
        """Hand: 'Hand' is the original name of this property."""

        temp = self.wrapped.Hand
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_324.Hand)(value) if value is not None else None

    @hand.setter
    def hand(self, value: '_324.Hand'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.Hand = value

    @property
    def root_diameter(self) -> 'float':
        """float: 'RootDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RootDiameter
        return temp

    @property
    def whole_depth(self) -> 'float':
        """float: 'WholeDepth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WholeDepth
        return temp

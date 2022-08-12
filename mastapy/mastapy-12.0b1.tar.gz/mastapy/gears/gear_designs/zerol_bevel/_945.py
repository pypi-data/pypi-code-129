"""_945.py

ZerolBevelGearSetDesign
"""


from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears import _343
from mastapy.gears.gear_designs.zerol_bevel import _943, _944
from mastapy.gears.gear_designs.bevel import _1170
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.ZerolBevel', 'ZerolBevelGearSetDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSetDesign',)


class ZerolBevelGearSetDesign(_1170.BevelGearSetDesign):
    """ZerolBevelGearSetDesign

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSetDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def minimum_number_of_teeth_for_recommended_tooth_proportions(self) -> 'int':
        """int: 'MinimumNumberOfTeethForRecommendedToothProportions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumNumberOfTeethForRecommendedToothProportions
        return temp

    @property
    def tooth_taper_zerol(self) -> '_343.ZerolBevelGleasonToothTaperOption':
        """ZerolBevelGleasonToothTaperOption: 'ToothTaperZerol' is the original name of this property."""

        temp = self.wrapped.ToothTaperZerol
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_343.ZerolBevelGleasonToothTaperOption)(value) if value is not None else None

    @tooth_taper_zerol.setter
    def tooth_taper_zerol(self, value: '_343.ZerolBevelGleasonToothTaperOption'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ToothTaperZerol = value

    @property
    def gears(self) -> 'List[_943.ZerolBevelGearDesign]':
        """List[ZerolBevelGearDesign]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_gears(self) -> 'List[_943.ZerolBevelGearDesign]':
        """List[ZerolBevelGearDesign]: 'ZerolBevelGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_meshes(self) -> 'List[_944.ZerolBevelGearMeshDesign]':
        """List[ZerolBevelGearMeshDesign]: 'ZerolBevelMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelMeshes
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

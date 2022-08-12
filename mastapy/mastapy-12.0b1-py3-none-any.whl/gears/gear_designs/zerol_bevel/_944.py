"""_944.py

ZerolBevelGearMeshDesign
"""


from typing import List

from mastapy.gears.gear_designs.zerol_bevel import _945, _943, _946
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.bevel import _1169
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.ZerolBevel', 'ZerolBevelGearMeshDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearMeshDesign',)


class ZerolBevelGearMeshDesign(_1169.BevelGearMeshDesign):
    """ZerolBevelGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearMeshDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def zerol_bevel_gear_set(self) -> '_945.ZerolBevelGearSetDesign':
        """ZerolBevelGearSetDesign: 'ZerolBevelGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearSet
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def zerol_bevel_meshed_gears(self) -> 'List[_946.ZerolBevelMeshedGearDesign]':
        """List[ZerolBevelMeshedGearDesign]: 'ZerolBevelMeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelMeshedGears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

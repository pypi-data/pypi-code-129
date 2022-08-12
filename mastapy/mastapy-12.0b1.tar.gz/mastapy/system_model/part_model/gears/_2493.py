"""_2493.py

ZerolBevelGearSet
"""


from typing import List

from mastapy.gears.gear_designs.zerol_bevel import _945
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2492, _2459
from mastapy.system_model.connections_and_sockets.gears import _2271
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ZerolBevelGearSet')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearSet',)


class ZerolBevelGearSet(_2459.BevelGearSet):
    """ZerolBevelGearSet

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_set_design(self) -> '_945.ZerolBevelGearSetDesign':
        """ZerolBevelGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearSetDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def zerol_bevel_gear_set_design(self) -> '_945.ZerolBevelGearSetDesign':
        """ZerolBevelGearSetDesign: 'ZerolBevelGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearSetDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def zerol_bevel_gears(self) -> 'List[_2492.ZerolBevelGear]':
        """List[ZerolBevelGear]: 'ZerolBevelGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_meshes(self) -> 'List[_2271.ZerolBevelGearMesh]':
        """List[ZerolBevelGearMesh]: 'ZerolBevelMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelMeshes
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

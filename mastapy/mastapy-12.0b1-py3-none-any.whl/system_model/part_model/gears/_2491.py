"""_2491.py

WormGearSet
"""


from typing import List

from mastapy.gears.gear_designs.worm import _950
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2490, _2471
from mastapy.system_model.connections_and_sockets.gears import _2269
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'WormGearSet')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSet',)


class WormGearSet(_2471.GearSet):
    """WormGearSet

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_set_design(self) -> '_950.WormGearSetDesign':
        """WormGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearSetDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def worm_gear_set_design(self) -> '_950.WormGearSetDesign':
        """WormGearSetDesign: 'WormGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearSetDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def worm_gears(self) -> 'List[_2490.WormGear]':
        """List[WormGear]: 'WormGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_meshes(self) -> 'List[_2269.WormGearMesh]':
        """List[WormGearMesh]: 'WormMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormMeshes
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

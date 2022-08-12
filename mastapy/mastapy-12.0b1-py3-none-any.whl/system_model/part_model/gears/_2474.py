"""_2474.py

HypoidGearSet
"""


from typing import List

from mastapy.gears.gear_designs.hypoid import _978
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2473, _2453
from mastapy.system_model.connections_and_sockets.gears import _2255
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'HypoidGearSet')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSet',)


class HypoidGearSet(_2453.AGMAGleasonConicalGearSet):
    """HypoidGearSet

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_set_design(self) -> '_978.HypoidGearSetDesign':
        """HypoidGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearSetDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hypoid_gear_set_design(self) -> '_978.HypoidGearSetDesign':
        """HypoidGearSetDesign: 'HypoidGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearSetDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hypoid_gears(self) -> 'List[_2473.HypoidGear]':
        """List[HypoidGear]: 'HypoidGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_meshes(self) -> 'List[_2255.HypoidGearMesh]':
        """List[HypoidGearMesh]: 'HypoidMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidMeshes
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

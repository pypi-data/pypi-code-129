"""_2485.py

StraightBevelDiffGearSet
"""


from typing import List

from mastapy.gears.gear_designs.straight_bevel_diff import _958
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2484, _2459
from mastapy.system_model.connections_and_sockets.gears import _2265
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'StraightBevelDiffGearSet')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearSet',)


class StraightBevelDiffGearSet(_2459.BevelGearSet):
    """StraightBevelDiffGearSet

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_SET

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_set_design(self) -> '_958.StraightBevelDiffGearSetDesign':
        """StraightBevelDiffGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearSetDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def straight_bevel_diff_gear_set_design(self) -> '_958.StraightBevelDiffGearSetDesign':
        """StraightBevelDiffGearSetDesign: 'StraightBevelDiffGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGearSetDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def straight_bevel_diff_gears(self) -> 'List[_2484.StraightBevelDiffGear]':
        """List[StraightBevelDiffGear]: 'StraightBevelDiffGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_meshes(self) -> 'List[_2265.StraightBevelDiffGearMesh]':
        """List[StraightBevelDiffGearMesh]: 'StraightBevelDiffMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffMeshes
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

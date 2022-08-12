"""_957.py

StraightBevelDiffGearMeshDesign
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.straight_bevel_diff import _958, _956, _959
from mastapy.gears.gear_designs.bevel import _1169
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.StraightBevelDiff', 'StraightBevelDiffGearMeshDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelDiffGearMeshDesign',)


class StraightBevelDiffGearMeshDesign(_1169.BevelGearMeshDesign):
    """StraightBevelDiffGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelDiffGearMeshDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pinion_performance_torque(self) -> 'float':
        """float: 'PinionPerformanceTorque' is the original name of this property."""

        temp = self.wrapped.PinionPerformanceTorque
        return temp

    @pinion_performance_torque.setter
    def pinion_performance_torque(self, value: 'float'):
        self.wrapped.PinionPerformanceTorque = float(value) if value else 0.0

    @property
    def straight_bevel_diff_gear_set(self) -> '_958.StraightBevelDiffGearSetDesign':
        """StraightBevelDiffGearSetDesign: 'StraightBevelDiffGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGearSet
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def straight_bevel_diff_gears(self) -> 'List[_956.StraightBevelDiffGearDesign]':
        """List[StraightBevelDiffGearDesign]: 'StraightBevelDiffGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_meshed_gears(self) -> 'List[_959.StraightBevelDiffMeshedGearDesign]':
        """List[StraightBevelDiffMeshedGearDesign]: 'StraightBevelDiffMeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffMeshedGears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

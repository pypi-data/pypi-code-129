"""_5600.py

GearSetStaticLoadCaseGroup
"""


from typing import List, Generic, TypeVar

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import _5597, _5598, _5601
from mastapy.system_model.part_model.gears import _2471, _2469
from mastapy.system_model.analyses_and_results.static_loads import _6804, _6806, _6809
from mastapy.system_model.connections_and_sockets.gears import _2253
from mastapy._internal.python_net import python_net_import

_GEAR_SET_STATIC_LOAD_CASE_GROUP = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.DesignEntityStaticLoadCaseGroups', 'GearSetStaticLoadCaseGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetStaticLoadCaseGroup',)


TGearSet = TypeVar('TGearSet', bound='_2471.GearSet')
TGear = TypeVar('TGear', bound='_2469.Gear')
TGearStaticLoad = TypeVar('TGearStaticLoad', bound='_6804.GearLoadCase')
TGearMesh = TypeVar('TGearMesh', bound='_2253.GearMesh')
TGearMeshStaticLoad = TypeVar('TGearMeshStaticLoad', bound='_6806.GearMeshLoadCase')
TGearSetStaticLoad = TypeVar('TGearSetStaticLoad', bound='_6809.GearSetLoadCase')


class GearSetStaticLoadCaseGroup(_5601.PartStaticLoadCaseGroup, Generic[TGearSet, TGear, TGearStaticLoad, TGearMesh, TGearMeshStaticLoad, TGearSetStaticLoad]):
    """GearSetStaticLoadCaseGroup

    This is a mastapy class.

    Generic Types:
        TGearSet
        TGear
        TGearStaticLoad
        TGearMesh
        TGearMeshStaticLoad
        TGearSetStaticLoad
    """

    TYPE = _GEAR_SET_STATIC_LOAD_CASE_GROUP

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearSetStaticLoadCaseGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def part(self) -> 'TGearSet':
        """TGearSet: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set(self) -> 'TGearSet':
        """TGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_load_cases(self) -> 'List[TGearSetStaticLoad]':
        """List[TGearSetStaticLoad]: 'PartLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PartLoadCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_set_load_cases(self) -> 'List[TGearSetStaticLoad]':
        """List[TGearSetStaticLoad]: 'GearSetLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetLoadCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gears_load_cases(self) -> 'List[_5597.ComponentStaticLoadCaseGroup[TGear, TGearStaticLoad]]':
        """List[ComponentStaticLoadCaseGroup[TGear, TGearStaticLoad]]: 'GearsLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearsLoadCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def meshes_load_cases(self) -> 'List[_5598.ConnectionStaticLoadCaseGroup[TGearMesh, TGearMeshStaticLoad]]':
        """List[ConnectionStaticLoadCaseGroup[TGearMesh, TGearMeshStaticLoad]]: 'MeshesLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshesLoadCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

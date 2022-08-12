"""_2461.py

ConceptGearSet
"""


from typing import List

from mastapy.gears.gear_designs.concept import _1166
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2460, _2471
from mastapy.system_model.connections_and_sockets.gears import _2245
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ConceptGearSet')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSet',)


class ConceptGearSet(_2471.GearSet):
    """ConceptGearSet

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_set_design(self) -> '_1166.ConceptGearSetDesign':
        """ConceptGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearSetDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def concept_gear_set_design(self) -> '_1166.ConceptGearSetDesign':
        """ConceptGearSetDesign: 'ConceptGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearSetDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def concept_gears(self) -> 'List[_2460.ConceptGear]':
        """List[ConceptGear]: 'ConceptGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_meshes(self) -> 'List[_2245.ConceptGearMesh]':
        """List[ConceptGearMesh]: 'ConceptMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptMeshes
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

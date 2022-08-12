"""_5596.py

AbstractAssemblyStaticLoadCaseGroup
"""


from typing import List, Generic, TypeVar

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.load_case_groups.design_entity_static_load_case_groups import _5601
from mastapy.system_model.part_model import _2375
from mastapy.system_model.analyses_and_results.static_loads import _6721
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_STATIC_LOAD_CASE_GROUP = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups.DesignEntityStaticLoadCaseGroups', 'AbstractAssemblyStaticLoadCaseGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractAssemblyStaticLoadCaseGroup',)


TAssembly = TypeVar('TAssembly', bound='_2375.AbstractAssembly')
TAssemblyStaticLoad = TypeVar('TAssemblyStaticLoad', bound='_6721.AbstractAssemblyLoadCase')


class AbstractAssemblyStaticLoadCaseGroup(_5601.PartStaticLoadCaseGroup, Generic[TAssembly, TAssemblyStaticLoad]):
    """AbstractAssemblyStaticLoadCaseGroup

    This is a mastapy class.

    Generic Types:
        TAssembly
        TAssemblyStaticLoad
    """

    TYPE = _ABSTRACT_ASSEMBLY_STATIC_LOAD_CASE_GROUP

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AbstractAssemblyStaticLoadCaseGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def part(self) -> 'TAssembly':
        """TAssembly: 'Part' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Part
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly(self) -> 'TAssembly':
        """TAssembly: 'Assembly' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Assembly
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_load_cases(self) -> 'List[TAssemblyStaticLoad]':
        """List[TAssemblyStaticLoad]: 'PartLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PartLoadCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_load_cases(self) -> 'List[TAssemblyStaticLoad]':
        """List[TAssemblyStaticLoad]: 'AssemblyLoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

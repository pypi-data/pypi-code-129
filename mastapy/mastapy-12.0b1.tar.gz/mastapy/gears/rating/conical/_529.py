"""_529.py

ConicalGearMeshRating
"""


from typing import List

from mastapy.gears.load_case.conical import _877
from mastapy._internal import constructor, conversion
from mastapy.gears.load_case.bevel import _882
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.conical import _535
from mastapy.gears.rating import _351
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Conical', 'ConicalGearMeshRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearMeshRating',)


class ConicalGearMeshRating(_351.GearMeshRating):
    """ConicalGearMeshRating

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalGearMeshRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mesh_load_case(self) -> '_877.ConicalMeshLoadCase':
        """ConicalMeshLoadCase: 'MeshLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshLoadCase
        if _877.ConicalMeshLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh_load_case to ConicalMeshLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_mesh_load_case(self) -> '_877.ConicalMeshLoadCase':
        """ConicalMeshLoadCase: 'ConicalMeshLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalMeshLoadCase
        if _877.ConicalMeshLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast conical_mesh_load_case to ConicalMeshLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def meshed_gears(self) -> 'List[_535.ConicalMeshedGearRating]':
        """List[ConicalMeshedGearRating]: 'MeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshedGears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

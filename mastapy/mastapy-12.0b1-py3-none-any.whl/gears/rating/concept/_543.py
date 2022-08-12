"""_543.py

ConceptGearSetRating
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.concept import _1166
from mastapy.gears.rating.concept import _541, _540
from mastapy.gears.rating import _354
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SET_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Concept', 'ConceptGearSetRating')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSetRating',)


class ConceptGearSetRating(_354.GearSetRating):
    """ConceptGearSetRating

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SET_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearSetRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self) -> 'str':
        """str: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        return temp

    @property
    def concept_gear_set(self) -> '_1166.ConceptGearSetDesign':
        """ConceptGearSetDesign: 'ConceptGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearSet
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_ratings(self) -> 'List[_541.ConceptGearRating]':
        """List[ConceptGearRating]: 'GearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_gear_ratings(self) -> 'List[_541.ConceptGearRating]':
        """List[ConceptGearRating]: 'ConceptGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_mesh_ratings(self) -> 'List[_540.ConceptGearMeshRating]':
        """List[ConceptGearMeshRating]: 'ConceptMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptMeshRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

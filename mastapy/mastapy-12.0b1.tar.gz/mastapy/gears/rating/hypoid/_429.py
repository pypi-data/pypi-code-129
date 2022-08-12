"""_429.py

HypoidGearMeshRating
"""


from typing import List

from mastapy.gears.rating.hypoid.standards import _434
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.hypoid import _977
from mastapy.gears.rating.iso_10300 import _416, _415
from mastapy.gears.rating.conical import _535
from mastapy.gears.rating.hypoid import _430
from mastapy.gears.rating.agma_gleason_conical import _555
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Hypoid', 'HypoidGearMeshRating')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearMeshRating',)


class HypoidGearMeshRating(_555.AGMAGleasonConicalGearMeshRating):
    """HypoidGearMeshRating

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearMeshRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gleason_hypoid_mesh_single_flank_rating(self) -> '_434.GleasonHypoidMeshSingleFlankRating':
        """GleasonHypoidMeshSingleFlankRating: 'GleasonHypoidMeshSingleFlankRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GleasonHypoidMeshSingleFlankRating
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hypoid_gear_mesh(self) -> '_977.HypoidGearMeshDesign':
        """HypoidGearMeshDesign: 'HypoidGearMesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearMesh
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def iso10300_hypoid_mesh_single_flank_rating_method_b1(self) -> '_416.ISO10300MeshSingleFlankRatingMethodB1':
        """ISO10300MeshSingleFlankRatingMethodB1: 'ISO10300HypoidMeshSingleFlankRatingMethodB1' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO10300HypoidMeshSingleFlankRatingMethodB1
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def iso10300_hypoid_mesh_single_flank_rating_method_b2(self) -> '_415.Iso10300MeshSingleFlankRatingHypoidMethodB2':
        """Iso10300MeshSingleFlankRatingHypoidMethodB2: 'ISO10300HypoidMeshSingleFlankRatingMethodB2' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO10300HypoidMeshSingleFlankRatingMethodB2
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

    @property
    def gears_in_mesh(self) -> 'List[_535.ConicalMeshedGearRating]':
        """List[ConicalMeshedGearRating]: 'GearsInMesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearsInMesh
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_gear_ratings(self) -> 'List[_430.HypoidGearRating]':
        """List[HypoidGearRating]: 'HypoidGearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

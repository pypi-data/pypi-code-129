"""_353.py

GearSetDutyCycleRating
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs import _941
from mastapy.gears.gear_designs.zerol_bevel import _945
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.worm import _950
from mastapy.gears.gear_designs.straight_bevel import _954
from mastapy.gears.gear_designs.straight_bevel_diff import _958
from mastapy.gears.gear_designs.spiral_bevel import _962
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _966
from mastapy.gears.gear_designs.klingelnberg_hypoid import _970
from mastapy.gears.gear_designs.klingelnberg_conical import _974
from mastapy.gears.gear_designs.hypoid import _978
from mastapy.gears.gear_designs.face import _986
from mastapy.gears.gear_designs.cylindrical import _1019, _1031
from mastapy.gears.gear_designs.conical import _1144
from mastapy.gears.gear_designs.concept import _1166
from mastapy.gears.gear_designs.bevel import _1170
from mastapy.gears.gear_designs.agma_gleason_conical import _1183
from mastapy.gears.rating import _349, _356, _346
from mastapy._internal.python_net import python_net_import

_GEAR_SET_DUTY_CYCLE_RATING = python_net_import('SMT.MastaAPI.Gears.Rating', 'GearSetDutyCycleRating')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetDutyCycleRating',)


class GearSetDutyCycleRating(_346.AbstractGearSetRating):
    """GearSetDutyCycleRating

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_DUTY_CYCLE_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearSetDutyCycleRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duty_cycle_name(self) -> 'str':
        """str: 'DutyCycleName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DutyCycleName
        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property."""

        temp = self.wrapped.Name
        return temp

    @name.setter
    def name(self, value: 'str'):
        self.wrapped.Name = str(value) if value else ''

    @property
    def total_duty_cycle_gear_set_reliability(self) -> 'float':
        """float: 'TotalDutyCycleGearSetReliability' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalDutyCycleGearSetReliability
        return temp

    @property
    def gear_set_design(self) -> '_941.GearSetDesign':
        """GearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign
        if _941.GearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to GearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_zerol_bevel_gear_set_design(self) -> '_945.ZerolBevelGearSetDesign':
        """ZerolBevelGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign
        if _945.ZerolBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to ZerolBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_worm_gear_set_design(self) -> '_950.WormGearSetDesign':
        """WormGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign
        if _950.WormGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to WormGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_straight_bevel_gear_set_design(self) -> '_954.StraightBevelGearSetDesign':
        """StraightBevelGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign
        if _954.StraightBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to StraightBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_straight_bevel_diff_gear_set_design(self) -> '_958.StraightBevelDiffGearSetDesign':
        """StraightBevelDiffGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign
        if _958.StraightBevelDiffGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to StraightBevelDiffGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_spiral_bevel_gear_set_design(self) -> '_962.SpiralBevelGearSetDesign':
        """SpiralBevelGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign
        if _962.SpiralBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to SpiralBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(self) -> '_966.KlingelnbergCycloPalloidSpiralBevelGearSetDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign
        if _966.KlingelnbergCycloPalloidSpiralBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to KlingelnbergCycloPalloidSpiralBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_design(self) -> '_970.KlingelnbergCycloPalloidHypoidGearSetDesign':
        """KlingelnbergCycloPalloidHypoidGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign
        if _970.KlingelnbergCycloPalloidHypoidGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to KlingelnbergCycloPalloidHypoidGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_klingelnberg_conical_gear_set_design(self) -> '_974.KlingelnbergConicalGearSetDesign':
        """KlingelnbergConicalGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign
        if _974.KlingelnbergConicalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to KlingelnbergConicalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_hypoid_gear_set_design(self) -> '_978.HypoidGearSetDesign':
        """HypoidGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign
        if _978.HypoidGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to HypoidGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_face_gear_set_design(self) -> '_986.FaceGearSetDesign':
        """FaceGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign
        if _986.FaceGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to FaceGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_cylindrical_gear_set_design(self) -> '_1019.CylindricalGearSetDesign':
        """CylindricalGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign
        if _1019.CylindricalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to CylindricalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_cylindrical_planetary_gear_set_design(self) -> '_1031.CylindricalPlanetaryGearSetDesign':
        """CylindricalPlanetaryGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign
        if _1031.CylindricalPlanetaryGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to CylindricalPlanetaryGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_conical_gear_set_design(self) -> '_1144.ConicalGearSetDesign':
        """ConicalGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign
        if _1144.ConicalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to ConicalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_concept_gear_set_design(self) -> '_1166.ConceptGearSetDesign':
        """ConceptGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign
        if _1166.ConceptGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to ConceptGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_bevel_gear_set_design(self) -> '_1170.BevelGearSetDesign':
        """BevelGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign
        if _1170.BevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to BevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_design_of_type_agma_gleason_conical_gear_set_design(self) -> '_1183.AGMAGleasonConicalGearSetDesign':
        """AGMAGleasonConicalGearSetDesign: 'GearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesign
        if _1183.AGMAGleasonConicalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_design to AGMAGleasonConicalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_ratings(self) -> 'List[_349.GearDutyCycleRating]':
        """List[GearDutyCycleRating]: 'GearRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_duty_cycle_ratings(self) -> 'List[_349.GearDutyCycleRating]':
        """List[GearDutyCycleRating]: 'GearDutyCycleRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_mesh_ratings(self) -> 'List[_356.MeshDutyCycleRating]':
        """List[MeshDutyCycleRating]: 'GearMeshRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_mesh_duty_cycle_ratings(self) -> 'List[_356.MeshDutyCycleRating]':
        """List[MeshDutyCycleRating]: 'GearMeshDutyCycleRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshDutyCycleRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def set_face_widths_for_specified_safety_factors(self):
        """ 'SetFaceWidthsForSpecifiedSafetyFactors' is the original name of this method."""

        self.wrapped.SetFaceWidthsForSpecifiedSafetyFactors()

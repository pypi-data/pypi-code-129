"""_321.py

GearSetOptimisationResult
"""


from mastapy.gears.gear_designs import _941
from mastapy._internal import constructor
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
from mastapy.math_utility.optimisation import _1502
from mastapy.gears.rating import _346, _353, _354
from mastapy.gears.rating.zerol_bevel import _362
from mastapy.gears.rating.worm import _366, _367
from mastapy.gears.rating.straight_bevel import _388
from mastapy.gears.rating.straight_bevel_diff import _391
from mastapy.gears.rating.spiral_bevel import _395
from mastapy.gears.rating.klingelnberg_spiral_bevel import _398
from mastapy.gears.rating.klingelnberg_hypoid import _401
from mastapy.gears.rating.klingelnberg_conical import _404
from mastapy.gears.rating.hypoid import _431
from mastapy.gears.rating.face import _440, _441
from mastapy.gears.rating.cylindrical import _454, _455
from mastapy.gears.rating.conical import _531, _532
from mastapy.gears.rating.concept import _542, _543
from mastapy.gears.rating.bevel import _546
from mastapy.gears.rating.agma_gleason_conical import _557
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_GEAR_SET_OPTIMISATION_RESULT = python_net_import('SMT.MastaAPI.Gears', 'GearSetOptimisationResult')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetOptimisationResult',)


class GearSetOptimisationResult(_0.APIBase):
    """GearSetOptimisationResult

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_OPTIMISATION_RESULT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearSetOptimisationResult.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_set(self) -> '_941.GearSetDesign':
        """GearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _941.GearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to GearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_zerol_bevel_gear_set_design(self) -> '_945.ZerolBevelGearSetDesign':
        """ZerolBevelGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _945.ZerolBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to ZerolBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_worm_gear_set_design(self) -> '_950.WormGearSetDesign':
        """WormGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _950.WormGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to WormGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_straight_bevel_gear_set_design(self) -> '_954.StraightBevelGearSetDesign':
        """StraightBevelGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _954.StraightBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to StraightBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_straight_bevel_diff_gear_set_design(self) -> '_958.StraightBevelDiffGearSetDesign':
        """StraightBevelDiffGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _958.StraightBevelDiffGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to StraightBevelDiffGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_spiral_bevel_gear_set_design(self) -> '_962.SpiralBevelGearSetDesign':
        """SpiralBevelGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _962.SpiralBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to SpiralBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(self) -> '_966.KlingelnbergCycloPalloidSpiralBevelGearSetDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _966.KlingelnbergCycloPalloidSpiralBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to KlingelnbergCycloPalloidSpiralBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_design(self) -> '_970.KlingelnbergCycloPalloidHypoidGearSetDesign':
        """KlingelnbergCycloPalloidHypoidGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _970.KlingelnbergCycloPalloidHypoidGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to KlingelnbergCycloPalloidHypoidGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_klingelnberg_conical_gear_set_design(self) -> '_974.KlingelnbergConicalGearSetDesign':
        """KlingelnbergConicalGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _974.KlingelnbergConicalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to KlingelnbergConicalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_hypoid_gear_set_design(self) -> '_978.HypoidGearSetDesign':
        """HypoidGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _978.HypoidGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to HypoidGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_face_gear_set_design(self) -> '_986.FaceGearSetDesign':
        """FaceGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _986.FaceGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to FaceGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_cylindrical_gear_set_design(self) -> '_1019.CylindricalGearSetDesign':
        """CylindricalGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _1019.CylindricalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to CylindricalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_cylindrical_planetary_gear_set_design(self) -> '_1031.CylindricalPlanetaryGearSetDesign':
        """CylindricalPlanetaryGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _1031.CylindricalPlanetaryGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to CylindricalPlanetaryGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_conical_gear_set_design(self) -> '_1144.ConicalGearSetDesign':
        """ConicalGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _1144.ConicalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to ConicalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_concept_gear_set_design(self) -> '_1166.ConceptGearSetDesign':
        """ConceptGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _1166.ConceptGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to ConceptGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_bevel_gear_set_design(self) -> '_1170.BevelGearSetDesign':
        """BevelGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _1170.BevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to BevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_agma_gleason_conical_gear_set_design(self) -> '_1183.AGMAGleasonConicalGearSetDesign':
        """AGMAGleasonConicalGearSetDesign: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _1183.AGMAGleasonConicalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to AGMAGleasonConicalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def is_optimized(self) -> 'bool':
        """bool: 'IsOptimized' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsOptimized
        return temp

    @property
    def optimisation_history(self) -> '_1502.OptimisationHistory':
        """OptimisationHistory: 'OptimisationHistory' is the original name of this property."""

        temp = self.wrapped.OptimisationHistory
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @optimisation_history.setter
    def optimisation_history(self, value: '_1502.OptimisationHistory'):
        value = value.wrapped if value else None
        self.wrapped.OptimisationHistory = value

    @property
    def rating(self) -> '_346.AbstractGearSetRating':
        """AbstractGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _346.AbstractGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to AbstractGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_gear_set_duty_cycle_rating(self) -> '_353.GearSetDutyCycleRating':
        """GearSetDutyCycleRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _353.GearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to GearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_gear_set_rating(self) -> '_354.GearSetRating':
        """GearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _354.GearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to GearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_zerol_bevel_gear_set_rating(self) -> '_362.ZerolBevelGearSetRating':
        """ZerolBevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _362.ZerolBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to ZerolBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_worm_gear_set_duty_cycle_rating(self) -> '_366.WormGearSetDutyCycleRating':
        """WormGearSetDutyCycleRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _366.WormGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to WormGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_worm_gear_set_rating(self) -> '_367.WormGearSetRating':
        """WormGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _367.WormGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to WormGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_straight_bevel_gear_set_rating(self) -> '_388.StraightBevelGearSetRating':
        """StraightBevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _388.StraightBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to StraightBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_straight_bevel_diff_gear_set_rating(self) -> '_391.StraightBevelDiffGearSetRating':
        """StraightBevelDiffGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _391.StraightBevelDiffGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to StraightBevelDiffGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_spiral_bevel_gear_set_rating(self) -> '_395.SpiralBevelGearSetRating':
        """SpiralBevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _395.SpiralBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to SpiralBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(self) -> '_398.KlingelnbergCycloPalloidSpiralBevelGearSetRating':
        """KlingelnbergCycloPalloidSpiralBevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _398.KlingelnbergCycloPalloidSpiralBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to KlingelnbergCycloPalloidSpiralBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_rating(self) -> '_401.KlingelnbergCycloPalloidHypoidGearSetRating':
        """KlingelnbergCycloPalloidHypoidGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _401.KlingelnbergCycloPalloidHypoidGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to KlingelnbergCycloPalloidHypoidGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_klingelnberg_cyclo_palloid_conical_gear_set_rating(self) -> '_404.KlingelnbergCycloPalloidConicalGearSetRating':
        """KlingelnbergCycloPalloidConicalGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _404.KlingelnbergCycloPalloidConicalGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to KlingelnbergCycloPalloidConicalGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_hypoid_gear_set_rating(self) -> '_431.HypoidGearSetRating':
        """HypoidGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _431.HypoidGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to HypoidGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_face_gear_set_duty_cycle_rating(self) -> '_440.FaceGearSetDutyCycleRating':
        """FaceGearSetDutyCycleRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _440.FaceGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to FaceGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_face_gear_set_rating(self) -> '_441.FaceGearSetRating':
        """FaceGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _441.FaceGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to FaceGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_cylindrical_gear_set_duty_cycle_rating(self) -> '_454.CylindricalGearSetDutyCycleRating':
        """CylindricalGearSetDutyCycleRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _454.CylindricalGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to CylindricalGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_cylindrical_gear_set_rating(self) -> '_455.CylindricalGearSetRating':
        """CylindricalGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _455.CylindricalGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to CylindricalGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_conical_gear_set_duty_cycle_rating(self) -> '_531.ConicalGearSetDutyCycleRating':
        """ConicalGearSetDutyCycleRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _531.ConicalGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to ConicalGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_conical_gear_set_rating(self) -> '_532.ConicalGearSetRating':
        """ConicalGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _532.ConicalGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to ConicalGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_concept_gear_set_duty_cycle_rating(self) -> '_542.ConceptGearSetDutyCycleRating':
        """ConceptGearSetDutyCycleRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _542.ConceptGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to ConceptGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_concept_gear_set_rating(self) -> '_543.ConceptGearSetRating':
        """ConceptGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _543.ConceptGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to ConceptGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_bevel_gear_set_rating(self) -> '_546.BevelGearSetRating':
        """BevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _546.BevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to BevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_agma_gleason_conical_gear_set_rating(self) -> '_557.AGMAGleasonConicalGearSetRating':
        """AGMAGleasonConicalGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _557.AGMAGleasonConicalGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to AGMAGleasonConicalGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

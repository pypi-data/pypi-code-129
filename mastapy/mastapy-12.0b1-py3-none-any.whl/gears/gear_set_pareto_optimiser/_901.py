"""_901.py

GearSetOptimiserCandidate
"""


from mastapy.gears.rating import _346, _353, _354
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
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
from mastapy.gears.gear_set_pareto_optimiser import _897
from mastapy._internal.python_net import python_net_import

_GEAR_SET_OPTIMISER_CANDIDATE = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'GearSetOptimiserCandidate')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetOptimiserCandidate',)


class GearSetOptimiserCandidate(_897.DesignSpaceSearchCandidateBase['_346.AbstractGearSetRating', 'GearSetOptimiserCandidate']):
    """GearSetOptimiserCandidate

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_OPTIMISER_CANDIDATE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearSetOptimiserCandidate.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def candidate(self) -> '_346.AbstractGearSetRating':
        """AbstractGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate
        if _346.AbstractGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to AbstractGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_gear_set_duty_cycle_rating(self) -> '_353.GearSetDutyCycleRating':
        """GearSetDutyCycleRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate
        if _353.GearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to GearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_gear_set_rating(self) -> '_354.GearSetRating':
        """GearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate
        if _354.GearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to GearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_zerol_bevel_gear_set_rating(self) -> '_362.ZerolBevelGearSetRating':
        """ZerolBevelGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate
        if _362.ZerolBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to ZerolBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_worm_gear_set_duty_cycle_rating(self) -> '_366.WormGearSetDutyCycleRating':
        """WormGearSetDutyCycleRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate
        if _366.WormGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to WormGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_worm_gear_set_rating(self) -> '_367.WormGearSetRating':
        """WormGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate
        if _367.WormGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to WormGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_straight_bevel_gear_set_rating(self) -> '_388.StraightBevelGearSetRating':
        """StraightBevelGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate
        if _388.StraightBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to StraightBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_straight_bevel_diff_gear_set_rating(self) -> '_391.StraightBevelDiffGearSetRating':
        """StraightBevelDiffGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate
        if _391.StraightBevelDiffGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to StraightBevelDiffGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_spiral_bevel_gear_set_rating(self) -> '_395.SpiralBevelGearSetRating':
        """SpiralBevelGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate
        if _395.SpiralBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to SpiralBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_rating(self) -> '_398.KlingelnbergCycloPalloidSpiralBevelGearSetRating':
        """KlingelnbergCycloPalloidSpiralBevelGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate
        if _398.KlingelnbergCycloPalloidSpiralBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to KlingelnbergCycloPalloidSpiralBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_rating(self) -> '_401.KlingelnbergCycloPalloidHypoidGearSetRating':
        """KlingelnbergCycloPalloidHypoidGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate
        if _401.KlingelnbergCycloPalloidHypoidGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to KlingelnbergCycloPalloidHypoidGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_klingelnberg_cyclo_palloid_conical_gear_set_rating(self) -> '_404.KlingelnbergCycloPalloidConicalGearSetRating':
        """KlingelnbergCycloPalloidConicalGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate
        if _404.KlingelnbergCycloPalloidConicalGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to KlingelnbergCycloPalloidConicalGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_hypoid_gear_set_rating(self) -> '_431.HypoidGearSetRating':
        """HypoidGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate
        if _431.HypoidGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to HypoidGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_face_gear_set_duty_cycle_rating(self) -> '_440.FaceGearSetDutyCycleRating':
        """FaceGearSetDutyCycleRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate
        if _440.FaceGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to FaceGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_face_gear_set_rating(self) -> '_441.FaceGearSetRating':
        """FaceGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate
        if _441.FaceGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to FaceGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_cylindrical_gear_set_duty_cycle_rating(self) -> '_454.CylindricalGearSetDutyCycleRating':
        """CylindricalGearSetDutyCycleRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate
        if _454.CylindricalGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to CylindricalGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_cylindrical_gear_set_rating(self) -> '_455.CylindricalGearSetRating':
        """CylindricalGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate
        if _455.CylindricalGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to CylindricalGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_conical_gear_set_duty_cycle_rating(self) -> '_531.ConicalGearSetDutyCycleRating':
        """ConicalGearSetDutyCycleRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate
        if _531.ConicalGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to ConicalGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_conical_gear_set_rating(self) -> '_532.ConicalGearSetRating':
        """ConicalGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate
        if _532.ConicalGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to ConicalGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_concept_gear_set_duty_cycle_rating(self) -> '_542.ConceptGearSetDutyCycleRating':
        """ConceptGearSetDutyCycleRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate
        if _542.ConceptGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to ConceptGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_concept_gear_set_rating(self) -> '_543.ConceptGearSetRating':
        """ConceptGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate
        if _543.ConceptGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to ConceptGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_bevel_gear_set_rating(self) -> '_546.BevelGearSetRating':
        """BevelGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate
        if _546.BevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to BevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def candidate_of_type_agma_gleason_conical_gear_set_rating(self) -> '_557.AGMAGleasonConicalGearSetRating':
        """AGMAGleasonConicalGearSetRating: 'Candidate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Candidate
        if _557.AGMAGleasonConicalGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast candidate to AGMAGleasonConicalGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def add_design(self):
        """ 'AddDesign' is the original name of this method."""

        self.wrapped.AddDesign()

"""_940.py

GearMeshDesign
"""


from mastapy._internal import constructor
from mastapy.gears.gear_designs import _938, _939
from mastapy.gears.gear_designs.zerol_bevel import _943
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.worm import _947, _948, _951
from mastapy.gears.gear_designs.straight_bevel import _952
from mastapy.gears.gear_designs.straight_bevel_diff import _956
from mastapy.gears.gear_designs.spiral_bevel import _960
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _964
from mastapy.gears.gear_designs.klingelnberg_hypoid import _968
from mastapy.gears.gear_designs.klingelnberg_conical import _972
from mastapy.gears.gear_designs.hypoid import _976
from mastapy.gears.gear_designs.face import _980, _985, _988
from mastapy.gears.gear_designs.cylindrical import _1003, _1032
from mastapy.gears.gear_designs.conical import _1142
from mastapy.gears.gear_designs.concept import _1164
from mastapy.gears.gear_designs.bevel import _1168
from mastapy.gears.gear_designs.agma_gleason_conical import _1181
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns', 'GearMeshDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshDesign',)


class GearMeshDesign(_939.GearDesignComponent):
    """GearMeshDesign

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearMeshDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_contact_ratio_rating_for_nvh(self) -> 'float':
        """float: 'AxialContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialContactRatioRatingForNVH
        return temp

    @property
    def has_hunting_ratio(self) -> 'bool':
        """bool: 'HasHuntingRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HasHuntingRatio
        return temp

    @property
    def highest_common_factor_of_teeth_numbers(self) -> 'int':
        """int: 'HighestCommonFactorOfTeethNumbers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HighestCommonFactorOfTeethNumbers
        return temp

    @property
    def hunting_tooth_factor(self) -> 'float':
        """float: 'HuntingToothFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HuntingToothFactor
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
    def speed_ratio_a_to_b(self) -> 'float':
        """float: 'SpeedRatioAToB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpeedRatioAToB
        return temp

    @property
    def torque_ratio_a_to_b(self) -> 'float':
        """float: 'TorqueRatioAToB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueRatioAToB
        return temp

    @property
    def transverse_contact_ratio_rating_for_nvh(self) -> 'float':
        """float: 'TransverseContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseContactRatioRatingForNVH
        return temp

    @property
    def transverse_and_axial_contact_ratio_rating_for_nvh(self) -> 'float':
        """float: 'TransverseAndAxialContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseAndAxialContactRatioRatingForNVH
        return temp

    @property
    def gear_a(self) -> '_938.GearDesign':
        """GearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _938.GearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to GearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_zerol_bevel_gear_design(self) -> '_943.ZerolBevelGearDesign':
        """ZerolBevelGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _943.ZerolBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ZerolBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_worm_design(self) -> '_947.WormDesign':
        """WormDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _947.WormDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to WormDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_worm_gear_design(self) -> '_948.WormGearDesign':
        """WormGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _948.WormGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to WormGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_worm_wheel_design(self) -> '_951.WormWheelDesign':
        """WormWheelDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _951.WormWheelDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to WormWheelDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_straight_bevel_gear_design(self) -> '_952.StraightBevelGearDesign':
        """StraightBevelGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _952.StraightBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to StraightBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_straight_bevel_diff_gear_design(self) -> '_956.StraightBevelDiffGearDesign':
        """StraightBevelDiffGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _956.StraightBevelDiffGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to StraightBevelDiffGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_spiral_bevel_gear_design(self) -> '_960.SpiralBevelGearDesign':
        """SpiralBevelGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _960.SpiralBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to SpiralBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_design(self) -> '_964.KlingelnbergCycloPalloidSpiralBevelGearDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _964.KlingelnbergCycloPalloidSpiralBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to KlingelnbergCycloPalloidSpiralBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_klingelnberg_cyclo_palloid_hypoid_gear_design(self) -> '_968.KlingelnbergCycloPalloidHypoidGearDesign':
        """KlingelnbergCycloPalloidHypoidGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _968.KlingelnbergCycloPalloidHypoidGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to KlingelnbergCycloPalloidHypoidGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_klingelnberg_conical_gear_design(self) -> '_972.KlingelnbergConicalGearDesign':
        """KlingelnbergConicalGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _972.KlingelnbergConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to KlingelnbergConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_hypoid_gear_design(self) -> '_976.HypoidGearDesign':
        """HypoidGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _976.HypoidGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to HypoidGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_face_gear_design(self) -> '_980.FaceGearDesign':
        """FaceGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _980.FaceGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to FaceGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_face_gear_pinion_design(self) -> '_985.FaceGearPinionDesign':
        """FaceGearPinionDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _985.FaceGearPinionDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to FaceGearPinionDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_face_gear_wheel_design(self) -> '_988.FaceGearWheelDesign':
        """FaceGearWheelDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _988.FaceGearWheelDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to FaceGearWheelDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_design(self) -> '_1003.CylindricalGearDesign':
        """CylindricalGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _1003.CylindricalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_planet_gear_design(self) -> '_1032.CylindricalPlanetGearDesign':
        """CylindricalPlanetGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _1032.CylindricalPlanetGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalPlanetGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_conical_gear_design(self) -> '_1142.ConicalGearDesign':
        """ConicalGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _1142.ConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_concept_gear_design(self) -> '_1164.ConceptGearDesign':
        """ConceptGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _1164.ConceptGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConceptGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_bevel_gear_design(self) -> '_1168.BevelGearDesign':
        """BevelGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _1168.BevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to BevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_agma_gleason_conical_gear_design(self) -> '_1181.AGMAGleasonConicalGearDesign':
        """AGMAGleasonConicalGearDesign: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _1181.AGMAGleasonConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to AGMAGleasonConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b(self) -> '_938.GearDesign':
        """GearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _938.GearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to GearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_zerol_bevel_gear_design(self) -> '_943.ZerolBevelGearDesign':
        """ZerolBevelGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _943.ZerolBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ZerolBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_worm_design(self) -> '_947.WormDesign':
        """WormDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _947.WormDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to WormDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_worm_gear_design(self) -> '_948.WormGearDesign':
        """WormGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _948.WormGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to WormGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_worm_wheel_design(self) -> '_951.WormWheelDesign':
        """WormWheelDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _951.WormWheelDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to WormWheelDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_straight_bevel_gear_design(self) -> '_952.StraightBevelGearDesign':
        """StraightBevelGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _952.StraightBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to StraightBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_straight_bevel_diff_gear_design(self) -> '_956.StraightBevelDiffGearDesign':
        """StraightBevelDiffGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _956.StraightBevelDiffGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to StraightBevelDiffGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_spiral_bevel_gear_design(self) -> '_960.SpiralBevelGearDesign':
        """SpiralBevelGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _960.SpiralBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to SpiralBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_design(self) -> '_964.KlingelnbergCycloPalloidSpiralBevelGearDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _964.KlingelnbergCycloPalloidSpiralBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to KlingelnbergCycloPalloidSpiralBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_klingelnberg_cyclo_palloid_hypoid_gear_design(self) -> '_968.KlingelnbergCycloPalloidHypoidGearDesign':
        """KlingelnbergCycloPalloidHypoidGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _968.KlingelnbergCycloPalloidHypoidGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to KlingelnbergCycloPalloidHypoidGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_klingelnberg_conical_gear_design(self) -> '_972.KlingelnbergConicalGearDesign':
        """KlingelnbergConicalGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _972.KlingelnbergConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to KlingelnbergConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_hypoid_gear_design(self) -> '_976.HypoidGearDesign':
        """HypoidGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _976.HypoidGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to HypoidGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_face_gear_design(self) -> '_980.FaceGearDesign':
        """FaceGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _980.FaceGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to FaceGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_face_gear_pinion_design(self) -> '_985.FaceGearPinionDesign':
        """FaceGearPinionDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _985.FaceGearPinionDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to FaceGearPinionDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_face_gear_wheel_design(self) -> '_988.FaceGearWheelDesign':
        """FaceGearWheelDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _988.FaceGearWheelDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to FaceGearWheelDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_design(self) -> '_1003.CylindricalGearDesign':
        """CylindricalGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _1003.CylindricalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_planet_gear_design(self) -> '_1032.CylindricalPlanetGearDesign':
        """CylindricalPlanetGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _1032.CylindricalPlanetGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalPlanetGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_conical_gear_design(self) -> '_1142.ConicalGearDesign':
        """ConicalGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _1142.ConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_concept_gear_design(self) -> '_1164.ConceptGearDesign':
        """ConceptGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _1164.ConceptGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConceptGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_bevel_gear_design(self) -> '_1168.BevelGearDesign':
        """BevelGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _1168.BevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to BevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_agma_gleason_conical_gear_design(self) -> '_1181.AGMAGleasonConicalGearDesign':
        """AGMAGleasonConicalGearDesign: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _1181.AGMAGleasonConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to AGMAGleasonConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

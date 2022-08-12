"""_2469.py

Gear
"""


from mastapy._internal import constructor
from mastapy.gears.gear_designs import _938
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
from mastapy.system_model.part_model.gears import (
    _2471, _2453, _2455, _2459,
    _2461, _2463, _2465, _2468,
    _2474, _2476, _2478, _2480,
    _2481, _2483, _2485, _2487,
    _2491, _2493
)
from mastapy.system_model.part_model.shaft_model import _2422
from mastapy.system_model.part_model import _2404
from mastapy._internal.python_net import python_net_import

_GEAR = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'Gear')


__docformat__ = 'restructuredtext en'
__all__ = ('Gear',)


class Gear(_2404.MountableComponent):
    """Gear

    This is a mastapy class.
    """

    TYPE = _GEAR

    __hash__ = None

    def __init__(self, instance_to_wrap: 'Gear.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cloned_from(self) -> 'str':
        """str: 'ClonedFrom' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ClonedFrom
        return temp

    @property
    def is_clone_gear(self) -> 'bool':
        """bool: 'IsCloneGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsCloneGear
        return temp

    @property
    def length(self) -> 'float':
        """float: 'Length' is the original name of this property."""

        temp = self.wrapped.Length
        return temp

    @length.setter
    def length(self, value: 'float'):
        self.wrapped.Length = float(value) if value else 0.0

    @property
    def maximum_number_of_teeth(self) -> 'int':
        """int: 'MaximumNumberOfTeeth' is the original name of this property."""

        temp = self.wrapped.MaximumNumberOfTeeth
        return temp

    @maximum_number_of_teeth.setter
    def maximum_number_of_teeth(self, value: 'int'):
        self.wrapped.MaximumNumberOfTeeth = int(value) if value else 0

    @property
    def minimum_number_of_teeth(self) -> 'int':
        """int: 'MinimumNumberOfTeeth' is the original name of this property."""

        temp = self.wrapped.MinimumNumberOfTeeth
        return temp

    @minimum_number_of_teeth.setter
    def minimum_number_of_teeth(self, value: 'int'):
        self.wrapped.MinimumNumberOfTeeth = int(value) if value else 0

    @property
    def active_gear_design(self) -> '_938.GearDesign':
        """GearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign
        if _938.GearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to GearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_zerol_bevel_gear_design(self) -> '_943.ZerolBevelGearDesign':
        """ZerolBevelGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign
        if _943.ZerolBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to ZerolBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_worm_design(self) -> '_947.WormDesign':
        """WormDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign
        if _947.WormDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to WormDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_worm_gear_design(self) -> '_948.WormGearDesign':
        """WormGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign
        if _948.WormGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to WormGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_worm_wheel_design(self) -> '_951.WormWheelDesign':
        """WormWheelDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign
        if _951.WormWheelDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to WormWheelDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_straight_bevel_gear_design(self) -> '_952.StraightBevelGearDesign':
        """StraightBevelGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign
        if _952.StraightBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to StraightBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_straight_bevel_diff_gear_design(self) -> '_956.StraightBevelDiffGearDesign':
        """StraightBevelDiffGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign
        if _956.StraightBevelDiffGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to StraightBevelDiffGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_spiral_bevel_gear_design(self) -> '_960.SpiralBevelGearDesign':
        """SpiralBevelGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign
        if _960.SpiralBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to SpiralBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_design(self) -> '_964.KlingelnbergCycloPalloidSpiralBevelGearDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign
        if _964.KlingelnbergCycloPalloidSpiralBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to KlingelnbergCycloPalloidSpiralBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_design(self) -> '_968.KlingelnbergCycloPalloidHypoidGearDesign':
        """KlingelnbergCycloPalloidHypoidGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign
        if _968.KlingelnbergCycloPalloidHypoidGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to KlingelnbergCycloPalloidHypoidGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_klingelnberg_conical_gear_design(self) -> '_972.KlingelnbergConicalGearDesign':
        """KlingelnbergConicalGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign
        if _972.KlingelnbergConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to KlingelnbergConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_hypoid_gear_design(self) -> '_976.HypoidGearDesign':
        """HypoidGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign
        if _976.HypoidGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to HypoidGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_face_gear_design(self) -> '_980.FaceGearDesign':
        """FaceGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign
        if _980.FaceGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to FaceGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_face_gear_pinion_design(self) -> '_985.FaceGearPinionDesign':
        """FaceGearPinionDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign
        if _985.FaceGearPinionDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to FaceGearPinionDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_face_gear_wheel_design(self) -> '_988.FaceGearWheelDesign':
        """FaceGearWheelDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign
        if _988.FaceGearWheelDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to FaceGearWheelDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_cylindrical_gear_design(self) -> '_1003.CylindricalGearDesign':
        """CylindricalGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign
        if _1003.CylindricalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to CylindricalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_cylindrical_planet_gear_design(self) -> '_1032.CylindricalPlanetGearDesign':
        """CylindricalPlanetGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign
        if _1032.CylindricalPlanetGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to CylindricalPlanetGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_conical_gear_design(self) -> '_1142.ConicalGearDesign':
        """ConicalGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign
        if _1142.ConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to ConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_concept_gear_design(self) -> '_1164.ConceptGearDesign':
        """ConceptGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign
        if _1164.ConceptGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to ConceptGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_bevel_gear_design(self) -> '_1168.BevelGearDesign':
        """BevelGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign
        if _1168.BevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to BevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_design_of_type_agma_gleason_conical_gear_design(self) -> '_1181.AGMAGleasonConicalGearDesign':
        """AGMAGleasonConicalGearDesign: 'ActiveGearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearDesign
        if _1181.AGMAGleasonConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_design to AGMAGleasonConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def face_width(self) -> 'float':
        """float: 'FaceWidth' is the original name of this property."""

        temp = self.wrapped.FaceWidth
        return temp

    @face_width.setter
    def face_width(self, value: 'float'):
        self.wrapped.FaceWidth = float(value) if value else 0.0

    @property
    def gear_set(self) -> '_2471.GearSet':
        """GearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _2471.GearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to GearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_agma_gleason_conical_gear_set(self) -> '_2453.AGMAGleasonConicalGearSet':
        """AGMAGleasonConicalGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _2453.AGMAGleasonConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to AGMAGleasonConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_bevel_differential_gear_set(self) -> '_2455.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _2455.BevelDifferentialGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to BevelDifferentialGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_bevel_gear_set(self) -> '_2459.BevelGearSet':
        """BevelGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _2459.BevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to BevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_concept_gear_set(self) -> '_2461.ConceptGearSet':
        """ConceptGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _2461.ConceptGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to ConceptGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_conical_gear_set(self) -> '_2463.ConicalGearSet':
        """ConicalGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _2463.ConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to ConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_cylindrical_gear_set(self) -> '_2465.CylindricalGearSet':
        """CylindricalGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _2465.CylindricalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to CylindricalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_face_gear_set(self) -> '_2468.FaceGearSet':
        """FaceGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _2468.FaceGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to FaceGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_hypoid_gear_set(self) -> '_2474.HypoidGearSet':
        """HypoidGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _2474.HypoidGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to HypoidGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_klingelnberg_cyclo_palloid_conical_gear_set(self) -> '_2476.KlingelnbergCycloPalloidConicalGearSet':
        """KlingelnbergCycloPalloidConicalGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _2476.KlingelnbergCycloPalloidConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to KlingelnbergCycloPalloidConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self) -> '_2478.KlingelnbergCycloPalloidHypoidGearSet':
        """KlingelnbergCycloPalloidHypoidGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _2478.KlingelnbergCycloPalloidHypoidGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to KlingelnbergCycloPalloidHypoidGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> '_2480.KlingelnbergCycloPalloidSpiralBevelGearSet':
        """KlingelnbergCycloPalloidSpiralBevelGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _2480.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to KlingelnbergCycloPalloidSpiralBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_planetary_gear_set(self) -> '_2481.PlanetaryGearSet':
        """PlanetaryGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _2481.PlanetaryGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to PlanetaryGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_spiral_bevel_gear_set(self) -> '_2483.SpiralBevelGearSet':
        """SpiralBevelGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _2483.SpiralBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to SpiralBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_straight_bevel_diff_gear_set(self) -> '_2485.StraightBevelDiffGearSet':
        """StraightBevelDiffGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _2485.StraightBevelDiffGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to StraightBevelDiffGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_straight_bevel_gear_set(self) -> '_2487.StraightBevelGearSet':
        """StraightBevelGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _2487.StraightBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to StraightBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_worm_gear_set(self) -> '_2491.WormGearSet':
        """WormGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _2491.WormGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to WormGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_of_type_zerol_bevel_gear_set(self) -> '_2493.ZerolBevelGearSet':
        """ZerolBevelGearSet: 'GearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSet
        if _2493.ZerolBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set to ZerolBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def number_of_teeth(self) -> 'int':
        """int: 'NumberOfTeeth' is the original name of this property."""

        temp = self.wrapped.NumberOfTeeth
        return temp

    @number_of_teeth.setter
    def number_of_teeth(self, value: 'int'):
        self.wrapped.NumberOfTeeth = int(value) if value else 0

    @property
    def shaft(self) -> '_2422.Shaft':
        """Shaft: 'Shaft' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Shaft
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def connect_to(self, other_gear: 'Gear'):
        """ 'ConnectTo' is the original name of this method.

        Args:
            other_gear (mastapy.system_model.part_model.gears.Gear)
        """

        self.wrapped.ConnectTo(other_gear.wrapped if other_gear else None)

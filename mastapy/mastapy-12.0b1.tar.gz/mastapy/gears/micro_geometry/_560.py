"""_560.py

FlankMicroGeometry
"""


from mastapy.gears import _327
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
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
from mastapy.utility.scripting import _1700
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_FLANK_MICRO_GEOMETRY = python_net_import('SMT.MastaAPI.Gears.MicroGeometry', 'FlankMicroGeometry')


__docformat__ = 'restructuredtext en'
__all__ = ('FlankMicroGeometry',)


class FlankMicroGeometry(_0.APIBase):
    """FlankMicroGeometry

    This is a mastapy class.
    """

    TYPE = _FLANK_MICRO_GEOMETRY

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FlankMicroGeometry.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def micro_geometry_input_type(self) -> '_327.MicroGeometryInputTypes':
        """MicroGeometryInputTypes: 'MicroGeometryInputType' is the original name of this property."""

        temp = self.wrapped.MicroGeometryInputType
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_327.MicroGeometryInputTypes)(value) if value is not None else None

    @micro_geometry_input_type.setter
    def micro_geometry_input_type(self, value: '_327.MicroGeometryInputTypes'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.MicroGeometryInputType = value

    @property
    def gear_design(self) -> '_938.GearDesign':
        """GearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDesign
        if _938.GearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_design to GearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_design_of_type_zerol_bevel_gear_design(self) -> '_943.ZerolBevelGearDesign':
        """ZerolBevelGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDesign
        if _943.ZerolBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_design to ZerolBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_design_of_type_worm_design(self) -> '_947.WormDesign':
        """WormDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDesign
        if _947.WormDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_design to WormDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_design_of_type_worm_gear_design(self) -> '_948.WormGearDesign':
        """WormGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDesign
        if _948.WormGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_design to WormGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_design_of_type_worm_wheel_design(self) -> '_951.WormWheelDesign':
        """WormWheelDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDesign
        if _951.WormWheelDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_design to WormWheelDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_design_of_type_straight_bevel_gear_design(self) -> '_952.StraightBevelGearDesign':
        """StraightBevelGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDesign
        if _952.StraightBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_design to StraightBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_design_of_type_straight_bevel_diff_gear_design(self) -> '_956.StraightBevelDiffGearDesign':
        """StraightBevelDiffGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDesign
        if _956.StraightBevelDiffGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_design to StraightBevelDiffGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_design_of_type_spiral_bevel_gear_design(self) -> '_960.SpiralBevelGearDesign':
        """SpiralBevelGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDesign
        if _960.SpiralBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_design to SpiralBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_design(self) -> '_964.KlingelnbergCycloPalloidSpiralBevelGearDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDesign
        if _964.KlingelnbergCycloPalloidSpiralBevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_design to KlingelnbergCycloPalloidSpiralBevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_design(self) -> '_968.KlingelnbergCycloPalloidHypoidGearDesign':
        """KlingelnbergCycloPalloidHypoidGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDesign
        if _968.KlingelnbergCycloPalloidHypoidGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_design to KlingelnbergCycloPalloidHypoidGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_design_of_type_klingelnberg_conical_gear_design(self) -> '_972.KlingelnbergConicalGearDesign':
        """KlingelnbergConicalGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDesign
        if _972.KlingelnbergConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_design to KlingelnbergConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_design_of_type_hypoid_gear_design(self) -> '_976.HypoidGearDesign':
        """HypoidGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDesign
        if _976.HypoidGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_design to HypoidGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_design_of_type_face_gear_design(self) -> '_980.FaceGearDesign':
        """FaceGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDesign
        if _980.FaceGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_design to FaceGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_design_of_type_face_gear_pinion_design(self) -> '_985.FaceGearPinionDesign':
        """FaceGearPinionDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDesign
        if _985.FaceGearPinionDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_design to FaceGearPinionDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_design_of_type_face_gear_wheel_design(self) -> '_988.FaceGearWheelDesign':
        """FaceGearWheelDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDesign
        if _988.FaceGearWheelDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_design to FaceGearWheelDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_design_of_type_cylindrical_gear_design(self) -> '_1003.CylindricalGearDesign':
        """CylindricalGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDesign
        if _1003.CylindricalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_design to CylindricalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_design_of_type_cylindrical_planet_gear_design(self) -> '_1032.CylindricalPlanetGearDesign':
        """CylindricalPlanetGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDesign
        if _1032.CylindricalPlanetGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_design to CylindricalPlanetGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_design_of_type_conical_gear_design(self) -> '_1142.ConicalGearDesign':
        """ConicalGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDesign
        if _1142.ConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_design to ConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_design_of_type_concept_gear_design(self) -> '_1164.ConceptGearDesign':
        """ConceptGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDesign
        if _1164.ConceptGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_design to ConceptGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_design_of_type_bevel_gear_design(self) -> '_1168.BevelGearDesign':
        """BevelGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDesign
        if _1168.BevelGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_design to BevelGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_design_of_type_agma_gleason_conical_gear_design(self) -> '_1181.AGMAGleasonConicalGearDesign':
        """AGMAGleasonConicalGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDesign
        if _1181.AGMAGleasonConicalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_design to AGMAGleasonConicalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def user_specified_data(self) -> '_1700.UserSpecifiedData':
        """UserSpecifiedData: 'UserSpecifiedData' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UserSpecifiedData
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

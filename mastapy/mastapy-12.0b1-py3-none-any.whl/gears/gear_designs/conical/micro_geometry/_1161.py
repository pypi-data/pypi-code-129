"""_1161.py

ConicalGearFlankMicroGeometry
"""


from mastapy.gears import _327
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.gears.gear_designs.conical.micro_geometry import _1160, _1162, _1163
from mastapy.gears.gear_designs.conical import _1142
from mastapy.gears.gear_designs.zerol_bevel import _943
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.straight_bevel import _952
from mastapy.gears.gear_designs.straight_bevel_diff import _956
from mastapy.gears.gear_designs.spiral_bevel import _960
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _964
from mastapy.gears.gear_designs.klingelnberg_hypoid import _968
from mastapy.gears.gear_designs.klingelnberg_conical import _972
from mastapy.gears.gear_designs.hypoid import _976
from mastapy.gears.gear_designs.bevel import _1168
from mastapy.gears.gear_designs.agma_gleason_conical import _1181
from mastapy.gears.micro_geometry import _560
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_FLANK_MICRO_GEOMETRY = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Conical.MicroGeometry', 'ConicalGearFlankMicroGeometry')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearFlankMicroGeometry',)


class ConicalGearFlankMicroGeometry(_560.FlankMicroGeometry):
    """ConicalGearFlankMicroGeometry

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_FLANK_MICRO_GEOMETRY

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalGearFlankMicroGeometry.TYPE'):
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
    def bias(self) -> '_1160.ConicalGearBiasModification':
        """ConicalGearBiasModification: 'Bias' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bias
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def lead_relief(self) -> '_1162.ConicalGearLeadModification':
        """ConicalGearLeadModification: 'LeadRelief' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeadRelief
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def profile_relief(self) -> '_1163.ConicalGearProfileModification':
        """ConicalGearProfileModification: 'ProfileRelief' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileRelief
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_design(self) -> '_1142.ConicalGearDesign':
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

"""_777.py

ConicalMeshMicroGeometryConfigBase
"""


from mastapy.gears.gear_designs.conical import _1143
from mastapy._internal import constructor
from mastapy.gears.gear_designs.zerol_bevel import _944
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.straight_bevel import _953
from mastapy.gears.gear_designs.straight_bevel_diff import _957
from mastapy.gears.gear_designs.spiral_bevel import _961
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _965
from mastapy.gears.gear_designs.klingelnberg_hypoid import _969
from mastapy.gears.gear_designs.klingelnberg_conical import _973
from mastapy.gears.gear_designs.hypoid import _977
from mastapy.gears.gear_designs.bevel import _1169
from mastapy.gears.gear_designs.agma_gleason_conical import _1182
from mastapy.gears.manufacturing.bevel import (
    _768, _766, _767, _778,
    _779, _784
)
from mastapy.gears.analysis import _1211
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_MICRO_GEOMETRY_CONFIG_BASE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalMeshMicroGeometryConfigBase')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshMicroGeometryConfigBase',)


class ConicalMeshMicroGeometryConfigBase(_1211.GearMeshImplementationDetail):
    """ConicalMeshMicroGeometryConfigBase

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_MICRO_GEOMETRY_CONFIG_BASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalMeshMicroGeometryConfigBase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mesh(self) -> '_1143.ConicalGearMeshDesign':
        """ConicalGearMeshDesign: 'Mesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mesh
        if _1143.ConicalGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh to ConicalGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_of_type_zerol_bevel_gear_mesh_design(self) -> '_944.ZerolBevelGearMeshDesign':
        """ZerolBevelGearMeshDesign: 'Mesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mesh
        if _944.ZerolBevelGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh to ZerolBevelGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_of_type_straight_bevel_gear_mesh_design(self) -> '_953.StraightBevelGearMeshDesign':
        """StraightBevelGearMeshDesign: 'Mesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mesh
        if _953.StraightBevelGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh to StraightBevelGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_of_type_straight_bevel_diff_gear_mesh_design(self) -> '_957.StraightBevelDiffGearMeshDesign':
        """StraightBevelDiffGearMeshDesign: 'Mesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mesh
        if _957.StraightBevelDiffGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh to StraightBevelDiffGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_of_type_spiral_bevel_gear_mesh_design(self) -> '_961.SpiralBevelGearMeshDesign':
        """SpiralBevelGearMeshDesign: 'Mesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mesh
        if _961.SpiralBevelGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh to SpiralBevelGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_design(self) -> '_965.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearMeshDesign: 'Mesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mesh
        if _965.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh to KlingelnbergCycloPalloidSpiralBevelGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh_design(self) -> '_969.KlingelnbergCycloPalloidHypoidGearMeshDesign':
        """KlingelnbergCycloPalloidHypoidGearMeshDesign: 'Mesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mesh
        if _969.KlingelnbergCycloPalloidHypoidGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh to KlingelnbergCycloPalloidHypoidGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_of_type_klingelnberg_conical_gear_mesh_design(self) -> '_973.KlingelnbergConicalGearMeshDesign':
        """KlingelnbergConicalGearMeshDesign: 'Mesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mesh
        if _973.KlingelnbergConicalGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh to KlingelnbergConicalGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_of_type_hypoid_gear_mesh_design(self) -> '_977.HypoidGearMeshDesign':
        """HypoidGearMeshDesign: 'Mesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mesh
        if _977.HypoidGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh to HypoidGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_of_type_bevel_gear_mesh_design(self) -> '_1169.BevelGearMeshDesign':
        """BevelGearMeshDesign: 'Mesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mesh
        if _1169.BevelGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh to BevelGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_of_type_agma_gleason_conical_gear_mesh_design(self) -> '_1182.AGMAGleasonConicalGearMeshDesign':
        """AGMAGleasonConicalGearMeshDesign: 'Mesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mesh
        if _1182.AGMAGleasonConicalGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh to AGMAGleasonConicalGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def wheel_config(self) -> '_768.ConicalGearMicroGeometryConfigBase':
        """ConicalGearMicroGeometryConfigBase: 'WheelConfig' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelConfig
        if _768.ConicalGearMicroGeometryConfigBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast wheel_config to ConicalGearMicroGeometryConfigBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def wheel_config_of_type_conical_gear_manufacturing_config(self) -> '_766.ConicalGearManufacturingConfig':
        """ConicalGearManufacturingConfig: 'WheelConfig' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelConfig
        if _766.ConicalGearManufacturingConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast wheel_config to ConicalGearManufacturingConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def wheel_config_of_type_conical_gear_micro_geometry_config(self) -> '_767.ConicalGearMicroGeometryConfig':
        """ConicalGearMicroGeometryConfig: 'WheelConfig' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelConfig
        if _767.ConicalGearMicroGeometryConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast wheel_config to ConicalGearMicroGeometryConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def wheel_config_of_type_conical_pinion_manufacturing_config(self) -> '_778.ConicalPinionManufacturingConfig':
        """ConicalPinionManufacturingConfig: 'WheelConfig' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelConfig
        if _778.ConicalPinionManufacturingConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast wheel_config to ConicalPinionManufacturingConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def wheel_config_of_type_conical_pinion_micro_geometry_config(self) -> '_779.ConicalPinionMicroGeometryConfig':
        """ConicalPinionMicroGeometryConfig: 'WheelConfig' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelConfig
        if _779.ConicalPinionMicroGeometryConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast wheel_config to ConicalPinionMicroGeometryConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def wheel_config_of_type_conical_wheel_manufacturing_config(self) -> '_784.ConicalWheelManufacturingConfig':
        """ConicalWheelManufacturingConfig: 'WheelConfig' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelConfig
        if _784.ConicalWheelManufacturingConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast wheel_config to ConicalWheelManufacturingConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

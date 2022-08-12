"""_2253.py

GearMesh
"""


from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.gears.gear_designs import _940
from mastapy.gears.gear_designs.zerol_bevel import _944
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.worm import _949
from mastapy.gears.gear_designs.straight_bevel import _953
from mastapy.gears.gear_designs.straight_bevel_diff import _957
from mastapy.gears.gear_designs.spiral_bevel import _961
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _965
from mastapy.gears.gear_designs.klingelnberg_hypoid import _969
from mastapy.gears.gear_designs.klingelnberg_conical import _973
from mastapy.gears.gear_designs.hypoid import _977
from mastapy.gears.gear_designs.face import _982
from mastapy.gears.gear_designs.cylindrical import _1009
from mastapy.gears.gear_designs.conical import _1143
from mastapy.gears.gear_designs.concept import _1165
from mastapy.gears.gear_designs.bevel import _1169
from mastapy.gears.gear_designs.agma_gleason_conical import _1182
from mastapy.system_model.connections_and_sockets import _2221
from mastapy._internal.python_net import python_net_import

_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'GearMesh')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMesh',)


class GearMesh(_2221.InterMountableComponentConnection):
    """GearMesh

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mesh_efficiency(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'MeshEfficiency' is the original name of this property."""

        temp = self.wrapped.MeshEfficiency
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @mesh_efficiency.setter
    def mesh_efficiency(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.MeshEfficiency = value

    @property
    def use_specified_mesh_stiffness(self) -> 'bool':
        """bool: 'UseSpecifiedMeshStiffness' is the original name of this property."""

        temp = self.wrapped.UseSpecifiedMeshStiffness
        return temp

    @use_specified_mesh_stiffness.setter
    def use_specified_mesh_stiffness(self, value: 'bool'):
        self.wrapped.UseSpecifiedMeshStiffness = bool(value) if value else False

    @property
    def user_specified_mesh_stiffness(self) -> 'float':
        """float: 'UserSpecifiedMeshStiffness' is the original name of this property."""

        temp = self.wrapped.UserSpecifiedMeshStiffness
        return temp

    @user_specified_mesh_stiffness.setter
    def user_specified_mesh_stiffness(self, value: 'float'):
        self.wrapped.UserSpecifiedMeshStiffness = float(value) if value else 0.0

    @property
    def active_gear_mesh_design(self) -> '_940.GearMeshDesign':
        """GearMeshDesign: 'ActiveGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearMeshDesign
        if _940.GearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_mesh_design to GearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_mesh_design_of_type_zerol_bevel_gear_mesh_design(self) -> '_944.ZerolBevelGearMeshDesign':
        """ZerolBevelGearMeshDesign: 'ActiveGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearMeshDesign
        if _944.ZerolBevelGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_mesh_design to ZerolBevelGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_mesh_design_of_type_worm_gear_mesh_design(self) -> '_949.WormGearMeshDesign':
        """WormGearMeshDesign: 'ActiveGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearMeshDesign
        if _949.WormGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_mesh_design to WormGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_mesh_design_of_type_straight_bevel_gear_mesh_design(self) -> '_953.StraightBevelGearMeshDesign':
        """StraightBevelGearMeshDesign: 'ActiveGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearMeshDesign
        if _953.StraightBevelGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_mesh_design to StraightBevelGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_mesh_design_of_type_straight_bevel_diff_gear_mesh_design(self) -> '_957.StraightBevelDiffGearMeshDesign':
        """StraightBevelDiffGearMeshDesign: 'ActiveGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearMeshDesign
        if _957.StraightBevelDiffGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_mesh_design to StraightBevelDiffGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_mesh_design_of_type_spiral_bevel_gear_mesh_design(self) -> '_961.SpiralBevelGearMeshDesign':
        """SpiralBevelGearMeshDesign: 'ActiveGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearMeshDesign
        if _961.SpiralBevelGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_mesh_design to SpiralBevelGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_mesh_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_design(self) -> '_965.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearMeshDesign: 'ActiveGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearMeshDesign
        if _965.KlingelnbergCycloPalloidSpiralBevelGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_mesh_design to KlingelnbergCycloPalloidSpiralBevelGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_mesh_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh_design(self) -> '_969.KlingelnbergCycloPalloidHypoidGearMeshDesign':
        """KlingelnbergCycloPalloidHypoidGearMeshDesign: 'ActiveGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearMeshDesign
        if _969.KlingelnbergCycloPalloidHypoidGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_mesh_design to KlingelnbergCycloPalloidHypoidGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_mesh_design_of_type_klingelnberg_conical_gear_mesh_design(self) -> '_973.KlingelnbergConicalGearMeshDesign':
        """KlingelnbergConicalGearMeshDesign: 'ActiveGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearMeshDesign
        if _973.KlingelnbergConicalGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_mesh_design to KlingelnbergConicalGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_mesh_design_of_type_hypoid_gear_mesh_design(self) -> '_977.HypoidGearMeshDesign':
        """HypoidGearMeshDesign: 'ActiveGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearMeshDesign
        if _977.HypoidGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_mesh_design to HypoidGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_mesh_design_of_type_face_gear_mesh_design(self) -> '_982.FaceGearMeshDesign':
        """FaceGearMeshDesign: 'ActiveGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearMeshDesign
        if _982.FaceGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_mesh_design to FaceGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_mesh_design_of_type_cylindrical_gear_mesh_design(self) -> '_1009.CylindricalGearMeshDesign':
        """CylindricalGearMeshDesign: 'ActiveGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearMeshDesign
        if _1009.CylindricalGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_mesh_design to CylindricalGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_mesh_design_of_type_conical_gear_mesh_design(self) -> '_1143.ConicalGearMeshDesign':
        """ConicalGearMeshDesign: 'ActiveGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearMeshDesign
        if _1143.ConicalGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_mesh_design to ConicalGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_mesh_design_of_type_concept_gear_mesh_design(self) -> '_1165.ConceptGearMeshDesign':
        """ConceptGearMeshDesign: 'ActiveGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearMeshDesign
        if _1165.ConceptGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_mesh_design to ConceptGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_mesh_design_of_type_bevel_gear_mesh_design(self) -> '_1169.BevelGearMeshDesign':
        """BevelGearMeshDesign: 'ActiveGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearMeshDesign
        if _1169.BevelGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_mesh_design to BevelGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_mesh_design_of_type_agma_gleason_conical_gear_mesh_design(self) -> '_1182.AGMAGleasonConicalGearMeshDesign':
        """AGMAGleasonConicalGearMeshDesign: 'ActiveGearMeshDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearMeshDesign
        if _1182.AGMAGleasonConicalGearMeshDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_mesh_design to AGMAGleasonConicalGearMeshDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

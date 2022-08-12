"""_2471.py

GearSet
"""


from typing import List

from mastapy._internal.implicit import list_with_selected_item, overridable
from mastapy.gears.gear_designs import _941
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
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
from mastapy.system_model.part_model import _2416
from mastapy._internal.python_net import python_net_import

_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'GearSet')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSet',)


class GearSet(_2416.SpecialisedAssembly):
    """GearSet

    This is a mastapy class.
    """

    TYPE = _GEAR_SET

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_design(self) -> 'list_with_selected_item.ListWithSelectedItem_GearSetDesign':
        """list_with_selected_item.ListWithSelectedItem_GearSetDesign: 'ActiveDesign' is the original name of this property."""

        temp = self.wrapped.ActiveDesign
        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_GearSetDesign)(temp) if temp is not None else None

    @active_design.setter
    def active_design(self, value: 'list_with_selected_item.ListWithSelectedItem_GearSetDesign.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_GearSetDesign.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_GearSetDesign.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.ActiveDesign = value

    @property
    def maximum_mesh_ratio(self) -> 'float':
        """float: 'MaximumMeshRatio' is the original name of this property."""

        temp = self.wrapped.MaximumMeshRatio
        return temp

    @maximum_mesh_ratio.setter
    def maximum_mesh_ratio(self, value: 'float'):
        self.wrapped.MaximumMeshRatio = float(value) if value else 0.0

    @property
    def maximum_number_of_teeth_in_mesh(self) -> 'int':
        """int: 'MaximumNumberOfTeethInMesh' is the original name of this property."""

        temp = self.wrapped.MaximumNumberOfTeethInMesh
        return temp

    @maximum_number_of_teeth_in_mesh.setter
    def maximum_number_of_teeth_in_mesh(self, value: 'int'):
        self.wrapped.MaximumNumberOfTeethInMesh = int(value) if value else 0

    @property
    def minimum_number_of_teeth_in_mesh(self) -> 'int':
        """int: 'MinimumNumberOfTeethInMesh' is the original name of this property."""

        temp = self.wrapped.MinimumNumberOfTeethInMesh
        return temp

    @minimum_number_of_teeth_in_mesh.setter
    def minimum_number_of_teeth_in_mesh(self, value: 'int'):
        self.wrapped.MinimumNumberOfTeethInMesh = int(value) if value else 0

    @property
    def required_safety_factor_for_bending(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RequiredSafetyFactorForBending' is the original name of this property."""

        temp = self.wrapped.RequiredSafetyFactorForBending
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @required_safety_factor_for_bending.setter
    def required_safety_factor_for_bending(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RequiredSafetyFactorForBending = value

    @property
    def required_safety_factor_for_contact(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RequiredSafetyFactorForContact' is the original name of this property."""

        temp = self.wrapped.RequiredSafetyFactorForContact
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @required_safety_factor_for_contact.setter
    def required_safety_factor_for_contact(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RequiredSafetyFactorForContact = value

    @property
    def required_safety_factor_for_static_bending(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RequiredSafetyFactorForStaticBending' is the original name of this property."""

        temp = self.wrapped.RequiredSafetyFactorForStaticBending
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @required_safety_factor_for_static_bending.setter
    def required_safety_factor_for_static_bending(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RequiredSafetyFactorForStaticBending = value

    @property
    def required_safety_factor_for_static_contact(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'RequiredSafetyFactorForStaticContact' is the original name of this property."""

        temp = self.wrapped.RequiredSafetyFactorForStaticContact
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @required_safety_factor_for_static_contact.setter
    def required_safety_factor_for_static_contact(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.RequiredSafetyFactorForStaticContact = value

    @property
    def active_gear_set_design(self) -> '_941.GearSetDesign':
        """GearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearSetDesign
        if _941.GearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to GearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_set_design_of_type_zerol_bevel_gear_set_design(self) -> '_945.ZerolBevelGearSetDesign':
        """ZerolBevelGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearSetDesign
        if _945.ZerolBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to ZerolBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_set_design_of_type_worm_gear_set_design(self) -> '_950.WormGearSetDesign':
        """WormGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearSetDesign
        if _950.WormGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to WormGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_set_design_of_type_straight_bevel_gear_set_design(self) -> '_954.StraightBevelGearSetDesign':
        """StraightBevelGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearSetDesign
        if _954.StraightBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to StraightBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_set_design_of_type_straight_bevel_diff_gear_set_design(self) -> '_958.StraightBevelDiffGearSetDesign':
        """StraightBevelDiffGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearSetDesign
        if _958.StraightBevelDiffGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to StraightBevelDiffGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_set_design_of_type_spiral_bevel_gear_set_design(self) -> '_962.SpiralBevelGearSetDesign':
        """SpiralBevelGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearSetDesign
        if _962.SpiralBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to SpiralBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_set_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(self) -> '_966.KlingelnbergCycloPalloidSpiralBevelGearSetDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearSetDesign
        if _966.KlingelnbergCycloPalloidSpiralBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to KlingelnbergCycloPalloidSpiralBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_set_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_design(self) -> '_970.KlingelnbergCycloPalloidHypoidGearSetDesign':
        """KlingelnbergCycloPalloidHypoidGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearSetDesign
        if _970.KlingelnbergCycloPalloidHypoidGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to KlingelnbergCycloPalloidHypoidGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_set_design_of_type_klingelnberg_conical_gear_set_design(self) -> '_974.KlingelnbergConicalGearSetDesign':
        """KlingelnbergConicalGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearSetDesign
        if _974.KlingelnbergConicalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to KlingelnbergConicalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_set_design_of_type_hypoid_gear_set_design(self) -> '_978.HypoidGearSetDesign':
        """HypoidGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearSetDesign
        if _978.HypoidGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to HypoidGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_set_design_of_type_face_gear_set_design(self) -> '_986.FaceGearSetDesign':
        """FaceGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearSetDesign
        if _986.FaceGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to FaceGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_set_design_of_type_cylindrical_gear_set_design(self) -> '_1019.CylindricalGearSetDesign':
        """CylindricalGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearSetDesign
        if _1019.CylindricalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to CylindricalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_set_design_of_type_cylindrical_planetary_gear_set_design(self) -> '_1031.CylindricalPlanetaryGearSetDesign':
        """CylindricalPlanetaryGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearSetDesign
        if _1031.CylindricalPlanetaryGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to CylindricalPlanetaryGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_set_design_of_type_conical_gear_set_design(self) -> '_1144.ConicalGearSetDesign':
        """ConicalGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearSetDesign
        if _1144.ConicalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to ConicalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_set_design_of_type_concept_gear_set_design(self) -> '_1166.ConceptGearSetDesign':
        """ConceptGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearSetDesign
        if _1166.ConceptGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to ConceptGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_set_design_of_type_bevel_gear_set_design(self) -> '_1170.BevelGearSetDesign':
        """BevelGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearSetDesign
        if _1170.BevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to BevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def active_gear_set_design_of_type_agma_gleason_conical_gear_set_design(self) -> '_1183.AGMAGleasonConicalGearSetDesign':
        """AGMAGleasonConicalGearSetDesign: 'ActiveGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActiveGearSetDesign
        if _1183.AGMAGleasonConicalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast active_gear_set_design to AGMAGleasonConicalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_designs(self) -> 'List[_941.GearSetDesign]':
        """List[GearSetDesign]: 'GearSetDesigns' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDesigns
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def add_gear_set_design(self, design: '_941.GearSetDesign'):
        """ 'AddGearSetDesign' is the original name of this method.

        Args:
            design (mastapy.gears.gear_designs.GearSetDesign)
        """

        self.wrapped.AddGearSetDesign(design.wrapped if design else None)

    def set_active_gear_set_design(self, gear_set_design: '_941.GearSetDesign'):
        """ 'SetActiveGearSetDesign' is the original name of this method.

        Args:
            gear_set_design (mastapy.gears.gear_designs.GearSetDesign)
        """

        self.wrapped.SetActiveGearSetDesign(gear_set_design.wrapped if gear_set_design else None)

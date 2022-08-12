"""_6775.py

CylindricalGearLoadCase
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.system_model.part_model.gears import _2464, _2466
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6776, _6804
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1091, _1090, _1094
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'CylindricalGearLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearLoadCase',)


class CylindricalGearLoadCase(_6804.GearLoadCase):
    """CylindricalGearLoadCase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_reaction_force(self) -> 'float':
        """float: 'AxialReactionForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialReactionForce
        return temp

    @property
    def lateral_reaction_force(self) -> 'float':
        """float: 'LateralReactionForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LateralReactionForce
        return temp

    @property
    def lateral_reaction_moment(self) -> 'float':
        """float: 'LateralReactionMoment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LateralReactionMoment
        return temp

    @property
    def override_micro_geometry(self) -> 'bool':
        """bool: 'OverrideMicroGeometry' is the original name of this property."""

        temp = self.wrapped.OverrideMicroGeometry
        return temp

    @override_micro_geometry.setter
    def override_micro_geometry(self, value: 'bool'):
        self.wrapped.OverrideMicroGeometry = bool(value) if value else False

    @property
    def power(self) -> 'float':
        """float: 'Power' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Power
        return temp

    @property
    def reversed_bending_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ReversedBendingFactor' is the original name of this property."""

        temp = self.wrapped.ReversedBendingFactor
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @reversed_bending_factor.setter
    def reversed_bending_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.ReversedBendingFactor = value

    @property
    def speed(self) -> 'float':
        """float: 'Speed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Speed
        return temp

    @property
    def torque(self) -> 'float':
        """float: 'Torque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Torque
        return temp

    @property
    def vertical_reaction_force(self) -> 'float':
        """float: 'VerticalReactionForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VerticalReactionForce
        return temp

    @property
    def vertical_reaction_moment(self) -> 'float':
        """float: 'VerticalReactionMoment' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VerticalReactionMoment
        return temp

    @property
    def component_design(self) -> '_2464.CylindricalGear':
        """CylindricalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        if _2464.CylindricalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CylindricalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_manufacture_errors(self) -> '_6776.CylindricalGearManufactureError':
        """CylindricalGearManufactureError: 'GearManufactureErrors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearManufactureErrors
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def overridden_micro_geometry(self) -> '_1091.CylindricalGearMicroGeometryBase':
        """CylindricalGearMicroGeometryBase: 'OverriddenMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OverriddenMicroGeometry
        if _1091.CylindricalGearMicroGeometryBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast overridden_micro_geometry to CylindricalGearMicroGeometryBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def overridden_micro_geometry_of_type_cylindrical_gear_micro_geometry(self) -> '_1090.CylindricalGearMicroGeometry':
        """CylindricalGearMicroGeometry: 'OverriddenMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OverriddenMicroGeometry
        if _1090.CylindricalGearMicroGeometry.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast overridden_micro_geometry to CylindricalGearMicroGeometry. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def overridden_micro_geometry_of_type_cylindrical_gear_micro_geometry_per_tooth(self) -> '_1094.CylindricalGearMicroGeometryPerTooth':
        """CylindricalGearMicroGeometryPerTooth: 'OverriddenMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OverriddenMicroGeometry
        if _1094.CylindricalGearMicroGeometryPerTooth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast overridden_micro_geometry to CylindricalGearMicroGeometryPerTooth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[CylindricalGearLoadCase]':
        """List[CylindricalGearLoadCase]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

"""_1088.py

CylindricalGearMeshMicroGeometry
"""


from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.utility_gui.charts import (
    _1815, _1805, _1810, _1812
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.gear_designs.cylindrical import _1017, _1009
from mastapy.gears.gear_designs.cylindrical.micro_geometry import (
    _1097, _1091, _1094, _1090
)
from mastapy.gears.analysis import _1211
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_MICRO_GEOMETRY = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'CylindricalGearMeshMicroGeometry')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMeshMicroGeometry',)


class CylindricalGearMeshMicroGeometry(_1211.GearMeshImplementationDetail):
    """CylindricalGearMeshMicroGeometry

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_MICRO_GEOMETRY

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearMeshMicroGeometry.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def has_gears_specifying_micro_geometry_per_tooth(self) -> 'bool':
        """bool: 'HasGearsSpecifyingMicroGeometryPerTooth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HasGearsSpecifyingMicroGeometryPerTooth
        return temp

    @property
    def left_flank_lead_modification_chart(self) -> '_1815.TwoDChartDefinition':
        """TwoDChartDefinition: 'LeftFlankLeadModificationChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlankLeadModificationChart
        if _1815.TwoDChartDefinition.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast left_flank_lead_modification_chart to TwoDChartDefinition. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def left_flank_profile_modification_chart(self) -> '_1815.TwoDChartDefinition':
        """TwoDChartDefinition: 'LeftFlankProfileModificationChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlankProfileModificationChart
        if _1815.TwoDChartDefinition.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast left_flank_profile_modification_chart to TwoDChartDefinition. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def number_of_tooth_passes_for_ltca(self) -> 'overridable.Overridable_int':
        """overridable.Overridable_int: 'NumberOfToothPassesForLTCA' is the original name of this property."""

        temp = self.wrapped.NumberOfToothPassesForLTCA
        return constructor.new_from_mastapy_type(overridable.Overridable_int)(temp) if temp is not None else None

    @number_of_tooth_passes_for_ltca.setter
    def number_of_tooth_passes_for_ltca(self, value: 'overridable.Overridable_int.implicit_type()'):
        wrapper_type = overridable.Overridable_int.wrapper_type()
        enclosed_type = overridable.Overridable_int.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0, is_overridden)
        self.wrapped.NumberOfToothPassesForLTCA = value

    @property
    def profile_measured_as(self) -> '_1017.CylindricalGearProfileMeasurementType':
        """CylindricalGearProfileMeasurementType: 'ProfileMeasuredAs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileMeasuredAs
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1017.CylindricalGearProfileMeasurementType)(value) if value is not None else None

    @property
    def right_flank_lead_modification_chart(self) -> '_1815.TwoDChartDefinition':
        """TwoDChartDefinition: 'RightFlankLeadModificationChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlankLeadModificationChart
        if _1815.TwoDChartDefinition.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast right_flank_lead_modification_chart to TwoDChartDefinition. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def right_flank_profile_modification_chart(self) -> '_1815.TwoDChartDefinition':
        """TwoDChartDefinition: 'RightFlankProfileModificationChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlankProfileModificationChart
        if _1815.TwoDChartDefinition.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast right_flank_profile_modification_chart to TwoDChartDefinition. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_set_micro_geometry(self) -> '_1097.CylindricalGearSetMicroGeometry':
        """CylindricalGearSetMicroGeometry: 'CylindricalGearSetMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSetMicroGeometry
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_mesh(self) -> '_1009.CylindricalGearMeshDesign':
        """CylindricalGearMeshDesign: 'CylindricalMesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalMesh
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_micro_geometries(self) -> 'List[_1091.CylindricalGearMicroGeometryBase]':
        """List[CylindricalGearMicroGeometryBase]: 'CylindricalGearMicroGeometries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearMicroGeometries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_gear_micro_geometries_specified_per_tooth(self) -> 'List[_1094.CylindricalGearMicroGeometryPerTooth]':
        """List[CylindricalGearMicroGeometryPerTooth]: 'CylindricalGearMicroGeometriesSpecifiedPerTooth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearMicroGeometriesSpecifiedPerTooth
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_a(self) -> '_1091.CylindricalGearMicroGeometryBase':
        """CylindricalGearMicroGeometryBase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _1091.CylindricalGearMicroGeometryBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearMicroGeometryBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_micro_geometry(self) -> '_1090.CylindricalGearMicroGeometry':
        """CylindricalGearMicroGeometry: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _1090.CylindricalGearMicroGeometry.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearMicroGeometry. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_micro_geometry_per_tooth(self) -> '_1094.CylindricalGearMicroGeometryPerTooth':
        """CylindricalGearMicroGeometryPerTooth: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _1094.CylindricalGearMicroGeometryPerTooth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearMicroGeometryPerTooth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b(self) -> '_1091.CylindricalGearMicroGeometryBase':
        """CylindricalGearMicroGeometryBase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _1091.CylindricalGearMicroGeometryBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearMicroGeometryBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_micro_geometry(self) -> '_1090.CylindricalGearMicroGeometry':
        """CylindricalGearMicroGeometry: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _1090.CylindricalGearMicroGeometry.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearMicroGeometry. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_micro_geometry_per_tooth(self) -> '_1094.CylindricalGearMicroGeometryPerTooth':
        """CylindricalGearMicroGeometryPerTooth: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _1094.CylindricalGearMicroGeometryPerTooth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearMicroGeometryPerTooth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

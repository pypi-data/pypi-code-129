"""_1284.py

UShapedLayerSpecification
"""


from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.electric_machines import _1257, _1259, _1271
from mastapy._internal.python_net import python_net_import

_U_SHAPED_LAYER_SPECIFICATION = python_net_import('SMT.MastaAPI.ElectricMachines', 'UShapedLayerSpecification')


__docformat__ = 'restructuredtext en'
__all__ = ('UShapedLayerSpecification',)


class UShapedLayerSpecification(_1271.RotorInternalLayerSpecification):
    """UShapedLayerSpecification

    This is a mastapy class.
    """

    TYPE = _U_SHAPED_LAYER_SPECIFICATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'UShapedLayerSpecification.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_between_inner_and_outer_sections(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'AngleBetweenInnerAndOuterSections' is the original name of this property."""

        temp = self.wrapped.AngleBetweenInnerAndOuterSections
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @angle_between_inner_and_outer_sections.setter
    def angle_between_inner_and_outer_sections(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.AngleBetweenInnerAndOuterSections = value

    @property
    def bridge_offset_at_layer_bend(self) -> 'float':
        """float: 'BridgeOffsetAtLayerBend' is the original name of this property."""

        temp = self.wrapped.BridgeOffsetAtLayerBend
        return temp

    @bridge_offset_at_layer_bend.setter
    def bridge_offset_at_layer_bend(self, value: 'float'):
        self.wrapped.BridgeOffsetAtLayerBend = float(value) if value else 0.0

    @property
    def bridge_thickness_at_layer_bend(self) -> 'float':
        """float: 'BridgeThicknessAtLayerBend' is the original name of this property."""

        temp = self.wrapped.BridgeThicknessAtLayerBend
        return temp

    @bridge_thickness_at_layer_bend.setter
    def bridge_thickness_at_layer_bend(self, value: 'float'):
        self.wrapped.BridgeThicknessAtLayerBend = float(value) if value else 0.0

    @property
    def distance_to_layer(self) -> 'float':
        """float: 'DistanceToLayer' is the original name of this property."""

        temp = self.wrapped.DistanceToLayer
        return temp

    @distance_to_layer.setter
    def distance_to_layer(self, value: 'float'):
        self.wrapped.DistanceToLayer = float(value) if value else 0.0

    @property
    def magnet_configuration(self) -> '_1257.MagnetConfiguration':
        """MagnetConfiguration: 'MagnetConfiguration' is the original name of this property."""

        temp = self.wrapped.MagnetConfiguration
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1257.MagnetConfiguration)(value) if value is not None else None

    @magnet_configuration.setter
    def magnet_configuration(self, value: '_1257.MagnetConfiguration'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.MagnetConfiguration = value

    @property
    def thickness_of_inner_flux_barriers(self) -> 'float':
        """float: 'ThicknessOfInnerFluxBarriers' is the original name of this property."""

        temp = self.wrapped.ThicknessOfInnerFluxBarriers
        return temp

    @thickness_of_inner_flux_barriers.setter
    def thickness_of_inner_flux_barriers(self, value: 'float'):
        self.wrapped.ThicknessOfInnerFluxBarriers = float(value) if value else 0.0

    @property
    def thickness_of_outer_flux_barriers(self) -> 'float':
        """float: 'ThicknessOfOuterFluxBarriers' is the original name of this property."""

        temp = self.wrapped.ThicknessOfOuterFluxBarriers
        return temp

    @thickness_of_outer_flux_barriers.setter
    def thickness_of_outer_flux_barriers(self, value: 'float'):
        self.wrapped.ThicknessOfOuterFluxBarriers = float(value) if value else 0.0

    @property
    def web_thickness(self) -> 'float':
        """float: 'WebThickness' is the original name of this property."""

        temp = self.wrapped.WebThickness
        return temp

    @web_thickness.setter
    def web_thickness(self, value: 'float'):
        self.wrapped.WebThickness = float(value) if value else 0.0

    @property
    def outer_magnets(self) -> '_1259.MagnetForLayer':
        """MagnetForLayer: 'OuterMagnets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterMagnets
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

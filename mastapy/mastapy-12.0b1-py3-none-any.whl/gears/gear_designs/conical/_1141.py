"""_1141.py

ConicalGearCutter
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears.gear_designs.conical import (
    _1149, _1150, _1159, _1158
)
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_CUTTER = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Conical', 'ConicalGearCutter')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearCutter',)


class ConicalGearCutter(_0.APIBase):
    """ConicalGearCutter

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_CUTTER

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalGearCutter.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def calculated_point_width(self) -> 'float':
        """float: 'CalculatedPointWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedPointWidth
        return temp

    @property
    def cutter_blade_type(self) -> '_1149.CutterBladeType':
        """CutterBladeType: 'CutterBladeType' is the original name of this property."""

        temp = self.wrapped.CutterBladeType
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1149.CutterBladeType)(value) if value is not None else None

    @cutter_blade_type.setter
    def cutter_blade_type(self, value: '_1149.CutterBladeType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.CutterBladeType = value

    @property
    def cutter_gauge_length(self) -> '_1150.CutterGaugeLengths':
        """CutterGaugeLengths: 'CutterGaugeLength' is the original name of this property."""

        temp = self.wrapped.CutterGaugeLength
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1150.CutterGaugeLengths)(value) if value is not None else None

    @cutter_gauge_length.setter
    def cutter_gauge_length(self, value: '_1150.CutterGaugeLengths'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.CutterGaugeLength = value

    @property
    def inner_blade_angle_convex(self) -> 'float':
        """float: 'InnerBladeAngleConvex' is the original name of this property."""

        temp = self.wrapped.InnerBladeAngleConvex
        return temp

    @inner_blade_angle_convex.setter
    def inner_blade_angle_convex(self, value: 'float'):
        self.wrapped.InnerBladeAngleConvex = float(value) if value else 0.0

    @property
    def inner_blade_point_radius_convex(self) -> 'float':
        """float: 'InnerBladePointRadiusConvex' is the original name of this property."""

        temp = self.wrapped.InnerBladePointRadiusConvex
        return temp

    @inner_blade_point_radius_convex.setter
    def inner_blade_point_radius_convex(self, value: 'float'):
        self.wrapped.InnerBladePointRadiusConvex = float(value) if value else 0.0

    @property
    def inner_edge_radius_convex(self) -> 'float':
        """float: 'InnerEdgeRadiusConvex' is the original name of this property."""

        temp = self.wrapped.InnerEdgeRadiusConvex
        return temp

    @inner_edge_radius_convex.setter
    def inner_edge_radius_convex(self, value: 'float'):
        self.wrapped.InnerEdgeRadiusConvex = float(value) if value else 0.0

    @property
    def inner_parabolic_apex_location_convex(self) -> 'float':
        """float: 'InnerParabolicApexLocationConvex' is the original name of this property."""

        temp = self.wrapped.InnerParabolicApexLocationConvex
        return temp

    @inner_parabolic_apex_location_convex.setter
    def inner_parabolic_apex_location_convex(self, value: 'float'):
        self.wrapped.InnerParabolicApexLocationConvex = float(value) if value else 0.0

    @property
    def inner_parabolic_coefficient_convex(self) -> 'float':
        """float: 'InnerParabolicCoefficientConvex' is the original name of this property."""

        temp = self.wrapped.InnerParabolicCoefficientConvex
        return temp

    @inner_parabolic_coefficient_convex.setter
    def inner_parabolic_coefficient_convex(self, value: 'float'):
        self.wrapped.InnerParabolicCoefficientConvex = float(value) if value else 0.0

    @property
    def inner_spherical_radius_convex(self) -> 'float':
        """float: 'InnerSphericalRadiusConvex' is the original name of this property."""

        temp = self.wrapped.InnerSphericalRadiusConvex
        return temp

    @inner_spherical_radius_convex.setter
    def inner_spherical_radius_convex(self, value: 'float'):
        self.wrapped.InnerSphericalRadiusConvex = float(value) if value else 0.0

    @property
    def inner_toprem_angle_convex(self) -> 'float':
        """float: 'InnerTopremAngleConvex' is the original name of this property."""

        temp = self.wrapped.InnerTopremAngleConvex
        return temp

    @inner_toprem_angle_convex.setter
    def inner_toprem_angle_convex(self, value: 'float'):
        self.wrapped.InnerTopremAngleConvex = float(value) if value else 0.0

    @property
    def inner_toprem_length_convex(self) -> 'float':
        """float: 'InnerTopremLengthConvex' is the original name of this property."""

        temp = self.wrapped.InnerTopremLengthConvex
        return temp

    @inner_toprem_length_convex.setter
    def inner_toprem_length_convex(self, value: 'float'):
        self.wrapped.InnerTopremLengthConvex = float(value) if value else 0.0

    @property
    def inner_toprem_letter_convex(self) -> '_1159.TopremLetter':
        """TopremLetter: 'InnerTopremLetterConvex' is the original name of this property."""

        temp = self.wrapped.InnerTopremLetterConvex
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1159.TopremLetter)(value) if value is not None else None

    @inner_toprem_letter_convex.setter
    def inner_toprem_letter_convex(self, value: '_1159.TopremLetter'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.InnerTopremLetterConvex = value

    @property
    def input_toprem_as(self) -> '_1158.TopremEntryType':
        """TopremEntryType: 'InputTopremAs' is the original name of this property."""

        temp = self.wrapped.InputTopremAs
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1158.TopremEntryType)(value) if value is not None else None

    @input_toprem_as.setter
    def input_toprem_as(self, value: '_1158.TopremEntryType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.InputTopremAs = value

    @property
    def outer_blade_angle_concave(self) -> 'float':
        """float: 'OuterBladeAngleConcave' is the original name of this property."""

        temp = self.wrapped.OuterBladeAngleConcave
        return temp

    @outer_blade_angle_concave.setter
    def outer_blade_angle_concave(self, value: 'float'):
        self.wrapped.OuterBladeAngleConcave = float(value) if value else 0.0

    @property
    def outer_blade_point_radius_concave(self) -> 'float':
        """float: 'OuterBladePointRadiusConcave' is the original name of this property."""

        temp = self.wrapped.OuterBladePointRadiusConcave
        return temp

    @outer_blade_point_radius_concave.setter
    def outer_blade_point_radius_concave(self, value: 'float'):
        self.wrapped.OuterBladePointRadiusConcave = float(value) if value else 0.0

    @property
    def outer_edge_radius_concave(self) -> 'float':
        """float: 'OuterEdgeRadiusConcave' is the original name of this property."""

        temp = self.wrapped.OuterEdgeRadiusConcave
        return temp

    @outer_edge_radius_concave.setter
    def outer_edge_radius_concave(self, value: 'float'):
        self.wrapped.OuterEdgeRadiusConcave = float(value) if value else 0.0

    @property
    def outer_parabolic_apex_location_concave(self) -> 'float':
        """float: 'OuterParabolicApexLocationConcave' is the original name of this property."""

        temp = self.wrapped.OuterParabolicApexLocationConcave
        return temp

    @outer_parabolic_apex_location_concave.setter
    def outer_parabolic_apex_location_concave(self, value: 'float'):
        self.wrapped.OuterParabolicApexLocationConcave = float(value) if value else 0.0

    @property
    def outer_parabolic_coefficient_concave(self) -> 'float':
        """float: 'OuterParabolicCoefficientConcave' is the original name of this property."""

        temp = self.wrapped.OuterParabolicCoefficientConcave
        return temp

    @outer_parabolic_coefficient_concave.setter
    def outer_parabolic_coefficient_concave(self, value: 'float'):
        self.wrapped.OuterParabolicCoefficientConcave = float(value) if value else 0.0

    @property
    def outer_spherical_radius_concave(self) -> 'float':
        """float: 'OuterSphericalRadiusConcave' is the original name of this property."""

        temp = self.wrapped.OuterSphericalRadiusConcave
        return temp

    @outer_spherical_radius_concave.setter
    def outer_spherical_radius_concave(self, value: 'float'):
        self.wrapped.OuterSphericalRadiusConcave = float(value) if value else 0.0

    @property
    def outer_toprem_angle_concave(self) -> 'float':
        """float: 'OuterTopremAngleConcave' is the original name of this property."""

        temp = self.wrapped.OuterTopremAngleConcave
        return temp

    @outer_toprem_angle_concave.setter
    def outer_toprem_angle_concave(self, value: 'float'):
        self.wrapped.OuterTopremAngleConcave = float(value) if value else 0.0

    @property
    def outer_toprem_length_concave(self) -> 'float':
        """float: 'OuterTopremLengthConcave' is the original name of this property."""

        temp = self.wrapped.OuterTopremLengthConcave
        return temp

    @outer_toprem_length_concave.setter
    def outer_toprem_length_concave(self, value: 'float'):
        self.wrapped.OuterTopremLengthConcave = float(value) if value else 0.0

    @property
    def outer_toprem_letter_concave(self) -> '_1159.TopremLetter':
        """TopremLetter: 'OuterTopremLetterConcave' is the original name of this property."""

        temp = self.wrapped.OuterTopremLetterConcave
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1159.TopremLetter)(value) if value is not None else None

    @outer_toprem_letter_concave.setter
    def outer_toprem_letter_concave(self, value: '_1159.TopremLetter'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.OuterTopremLetterConcave = value

    @property
    def protuberance_at_concave_blade(self) -> 'float':
        """float: 'ProtuberanceAtConcaveBlade' is the original name of this property."""

        temp = self.wrapped.ProtuberanceAtConcaveBlade
        return temp

    @protuberance_at_concave_blade.setter
    def protuberance_at_concave_blade(self, value: 'float'):
        self.wrapped.ProtuberanceAtConcaveBlade = float(value) if value else 0.0

    @property
    def protuberance_at_convex_blade(self) -> 'float':
        """float: 'ProtuberanceAtConvexBlade' is the original name of this property."""

        temp = self.wrapped.ProtuberanceAtConvexBlade
        return temp

    @protuberance_at_convex_blade.setter
    def protuberance_at_convex_blade(self, value: 'float'):
        self.wrapped.ProtuberanceAtConvexBlade = float(value) if value else 0.0

    @property
    def radius(self) -> 'float':
        """float: 'Radius' is the original name of this property."""

        temp = self.wrapped.Radius
        return temp

    @radius.setter
    def radius(self, value: 'float'):
        self.wrapped.Radius = float(value) if value else 0.0

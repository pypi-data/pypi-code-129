"""_699.py

CylindricalGearHobDesign
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears.manufacturing.cylindrical import _621
from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _715, _720, _718
from mastapy._internal.cast_exception import CastException
from mastapy.gears.manufacturing.cylindrical.cutters import _702
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_HOB_DESIGN = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters', 'CylindricalGearHobDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearHobDesign',)


class CylindricalGearHobDesign(_702.CylindricalGearRackDesign):
    """CylindricalGearHobDesign

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_HOB_DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearHobDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def addendum_tolerance(self) -> 'float':
        """float: 'AddendumTolerance' is the original name of this property."""

        temp = self.wrapped.AddendumTolerance
        return temp

    @addendum_tolerance.setter
    def addendum_tolerance(self, value: 'float'):
        self.wrapped.AddendumTolerance = float(value) if value else 0.0

    @property
    def blade_control_distance(self) -> 'float':
        """float: 'BladeControlDistance' is the original name of this property."""

        temp = self.wrapped.BladeControlDistance
        return temp

    @blade_control_distance.setter
    def blade_control_distance(self, value: 'float'):
        self.wrapped.BladeControlDistance = float(value) if value else 0.0

    @property
    def blade_relief(self) -> 'float':
        """float: 'BladeRelief' is the original name of this property."""

        temp = self.wrapped.BladeRelief
        return temp

    @blade_relief.setter
    def blade_relief(self, value: 'float'):
        self.wrapped.BladeRelief = float(value) if value else 0.0

    @property
    def edge_height(self) -> 'float':
        """float: 'EdgeHeight' is the original name of this property."""

        temp = self.wrapped.EdgeHeight
        return temp

    @edge_height.setter
    def edge_height(self, value: 'float'):
        self.wrapped.EdgeHeight = float(value) if value else 0.0

    @property
    def edge_radius_tolerance(self) -> 'float':
        """float: 'EdgeRadiusTolerance' is the original name of this property."""

        temp = self.wrapped.EdgeRadiusTolerance
        return temp

    @edge_radius_tolerance.setter
    def edge_radius_tolerance(self, value: 'float'):
        self.wrapped.EdgeRadiusTolerance = float(value) if value else 0.0

    @property
    def flat_tip_width(self) -> 'float':
        """float: 'FlatTipWidth' is the original name of this property."""

        temp = self.wrapped.FlatTipWidth
        return temp

    @flat_tip_width.setter
    def flat_tip_width(self, value: 'float'):
        self.wrapped.FlatTipWidth = float(value) if value else 0.0

    @property
    def has_protuberance(self) -> 'bool':
        """bool: 'HasProtuberance' is the original name of this property."""

        temp = self.wrapped.HasProtuberance
        return temp

    @has_protuberance.setter
    def has_protuberance(self, value: 'bool'):
        self.wrapped.HasProtuberance = bool(value) if value else False

    @property
    def has_semi_topping_blade(self) -> 'bool':
        """bool: 'HasSemiToppingBlade' is the original name of this property."""

        temp = self.wrapped.HasSemiToppingBlade
        return temp

    @has_semi_topping_blade.setter
    def has_semi_topping_blade(self, value: 'bool'):
        self.wrapped.HasSemiToppingBlade = bool(value) if value else False

    @property
    def hob_edge_type(self) -> '_621.HobEdgeTypes':
        """HobEdgeTypes: 'HobEdgeType' is the original name of this property."""

        temp = self.wrapped.HobEdgeType
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_621.HobEdgeTypes)(value) if value is not None else None

    @hob_edge_type.setter
    def hob_edge_type(self, value: '_621.HobEdgeTypes'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.HobEdgeType = value

    @property
    def normal_thickness_tolerance(self) -> 'float':
        """float: 'NormalThicknessTolerance' is the original name of this property."""

        temp = self.wrapped.NormalThicknessTolerance
        return temp

    @normal_thickness_tolerance.setter
    def normal_thickness_tolerance(self, value: 'float'):
        self.wrapped.NormalThicknessTolerance = float(value) if value else 0.0

    @property
    def number_of_gashes(self) -> 'int':
        """int: 'NumberOfGashes' is the original name of this property."""

        temp = self.wrapped.NumberOfGashes
        return temp

    @number_of_gashes.setter
    def number_of_gashes(self, value: 'int'):
        self.wrapped.NumberOfGashes = int(value) if value else 0

    @property
    def protuberance(self) -> 'float':
        """float: 'Protuberance' is the original name of this property."""

        temp = self.wrapped.Protuberance
        return temp

    @protuberance.setter
    def protuberance(self, value: 'float'):
        self.wrapped.Protuberance = float(value) if value else 0.0

    @property
    def protuberance_angle(self) -> 'float':
        """float: 'ProtuberanceAngle' is the original name of this property."""

        temp = self.wrapped.ProtuberanceAngle
        return temp

    @protuberance_angle.setter
    def protuberance_angle(self, value: 'float'):
        self.wrapped.ProtuberanceAngle = float(value) if value else 0.0

    @property
    def protuberance_factor(self) -> 'float':
        """float: 'ProtuberanceFactor' is the original name of this property."""

        temp = self.wrapped.ProtuberanceFactor
        return temp

    @protuberance_factor.setter
    def protuberance_factor(self, value: 'float'):
        self.wrapped.ProtuberanceFactor = float(value) if value else 0.0

    @property
    def protuberance_height(self) -> 'float':
        """float: 'ProtuberanceHeight' is the original name of this property."""

        temp = self.wrapped.ProtuberanceHeight
        return temp

    @protuberance_height.setter
    def protuberance_height(self, value: 'float'):
        self.wrapped.ProtuberanceHeight = float(value) if value else 0.0

    @property
    def protuberance_height_relative_to_edge_height(self) -> 'float':
        """float: 'ProtuberanceHeightRelativeToEdgeHeight' is the original name of this property."""

        temp = self.wrapped.ProtuberanceHeightRelativeToEdgeHeight
        return temp

    @protuberance_height_relative_to_edge_height.setter
    def protuberance_height_relative_to_edge_height(self, value: 'float'):
        self.wrapped.ProtuberanceHeightRelativeToEdgeHeight = float(value) if value else 0.0

    @property
    def protuberance_height_tolerance(self) -> 'float':
        """float: 'ProtuberanceHeightTolerance' is the original name of this property."""

        temp = self.wrapped.ProtuberanceHeightTolerance
        return temp

    @protuberance_height_tolerance.setter
    def protuberance_height_tolerance(self, value: 'float'):
        self.wrapped.ProtuberanceHeightTolerance = float(value) if value else 0.0

    @property
    def protuberance_length(self) -> 'float':
        """float: 'ProtuberanceLength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProtuberanceLength
        return temp

    @property
    def protuberance_tolerance(self) -> 'float':
        """float: 'ProtuberanceTolerance' is the original name of this property."""

        temp = self.wrapped.ProtuberanceTolerance
        return temp

    @protuberance_tolerance.setter
    def protuberance_tolerance(self, value: 'float'):
        self.wrapped.ProtuberanceTolerance = float(value) if value else 0.0

    @property
    def semi_topping_blade_height_tolerance(self) -> 'float':
        """float: 'SemiToppingBladeHeightTolerance' is the original name of this property."""

        temp = self.wrapped.SemiToppingBladeHeightTolerance
        return temp

    @semi_topping_blade_height_tolerance.setter
    def semi_topping_blade_height_tolerance(self, value: 'float'):
        self.wrapped.SemiToppingBladeHeightTolerance = float(value) if value else 0.0

    @property
    def semi_topping_height(self) -> 'float':
        """float: 'SemiToppingHeight' is the original name of this property."""

        temp = self.wrapped.SemiToppingHeight
        return temp

    @semi_topping_height.setter
    def semi_topping_height(self, value: 'float'):
        self.wrapped.SemiToppingHeight = float(value) if value else 0.0

    @property
    def semi_topping_pressure_angle(self) -> 'float':
        """float: 'SemiToppingPressureAngle' is the original name of this property."""

        temp = self.wrapped.SemiToppingPressureAngle
        return temp

    @semi_topping_pressure_angle.setter
    def semi_topping_pressure_angle(self, value: 'float'):
        self.wrapped.SemiToppingPressureAngle = float(value) if value else 0.0

    @property
    def semi_topping_pressure_angle_tolerance(self) -> 'float':
        """float: 'SemiToppingPressureAngleTolerance' is the original name of this property."""

        temp = self.wrapped.SemiToppingPressureAngleTolerance
        return temp

    @semi_topping_pressure_angle_tolerance.setter
    def semi_topping_pressure_angle_tolerance(self, value: 'float'):
        self.wrapped.SemiToppingPressureAngleTolerance = float(value) if value else 0.0

    @property
    def semi_topping_start(self) -> 'float':
        """float: 'SemiToppingStart' is the original name of this property."""

        temp = self.wrapped.SemiToppingStart
        return temp

    @semi_topping_start.setter
    def semi_topping_start(self, value: 'float'):
        self.wrapped.SemiToppingStart = float(value) if value else 0.0

    @property
    def tip_control_distance(self) -> 'float':
        """float: 'TipControlDistance' is the original name of this property."""

        temp = self.wrapped.TipControlDistance
        return temp

    @tip_control_distance.setter
    def tip_control_distance(self, value: 'float'):
        self.wrapped.TipControlDistance = float(value) if value else 0.0

    @property
    def maximum_hob_material_shape(self) -> '_715.CylindricalGearHobShape':
        """CylindricalGearHobShape: 'MaximumHobMaterialShape' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumHobMaterialShape
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def minimum_hob_material_shape(self) -> '_715.CylindricalGearHobShape':
        """CylindricalGearHobShape: 'MinimumHobMaterialShape' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumHobMaterialShape
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def nominal_hob_shape(self) -> '_715.CylindricalGearHobShape':
        """CylindricalGearHobShape: 'NominalHobShape' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalHobShape
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def nominal_rack_shape(self) -> '_720.RackShape':
        """RackShape: 'NominalRackShape' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalRackShape
        if _720.RackShape.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast nominal_rack_shape to RackShape. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def nominal_rack_shape_of_type_cylindrical_gear_hob_shape(self) -> '_715.CylindricalGearHobShape':
        """CylindricalGearHobShape: 'NominalRackShape' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalRackShape
        if _715.CylindricalGearHobShape.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast nominal_rack_shape to CylindricalGearHobShape. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def nominal_rack_shape_of_type_cylindrical_gear_worm_grinder_shape(self) -> '_718.CylindricalGearWormGrinderShape':
        """CylindricalGearWormGrinderShape: 'NominalRackShape' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalRackShape
        if _718.CylindricalGearWormGrinderShape.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast nominal_rack_shape to CylindricalGearWormGrinderShape. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

"""_716.py

CylindricalGearShaperTangible
"""


from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutters import _704
from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _713
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SHAPER_TANGIBLE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters.Tangibles', 'CylindricalGearShaperTangible')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearShaperTangible',)


class CylindricalGearShaperTangible(_713.CutterShapeDefinition):
    """CylindricalGearShaperTangible

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SHAPER_TANGIBLE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearShaperTangible.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def actual_protuberance(self) -> 'float':
        """float: 'ActualProtuberance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ActualProtuberance
        return temp

    @property
    def base_diameter(self) -> 'float':
        """float: 'BaseDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BaseDiameter
        return temp

    @property
    def edge_radius(self) -> 'float':
        """float: 'EdgeRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EdgeRadius
        return temp

    @property
    def helix_angle(self) -> 'float':
        """float: 'HelixAngle' is the original name of this property."""

        temp = self.wrapped.HelixAngle
        return temp

    @helix_angle.setter
    def helix_angle(self, value: 'float'):
        self.wrapped.HelixAngle = float(value) if value else 0.0

    @property
    def maximum_blade_control_distance(self) -> 'float':
        """float: 'MaximumBladeControlDistance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumBladeControlDistance
        return temp

    @property
    def maximum_protuberance(self) -> 'float':
        """float: 'MaximumProtuberance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumProtuberance
        return temp

    @property
    def maximum_protuberance_height_for_single_circle(self) -> 'float':
        """float: 'MaximumProtuberanceHeightForSingleCircle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumProtuberanceHeightForSingleCircle
        return temp

    @property
    def maximum_tip_control_distance_for_zero_protuberance(self) -> 'float':
        """float: 'MaximumTipControlDistanceForZeroProtuberance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumTipControlDistanceForZeroProtuberance
        return temp

    @property
    def maximum_tip_diameter_to_avoid_pointed_teeth_no_protuberance(self) -> 'float':
        """float: 'MaximumTipDiameterToAvoidPointedTeethNoProtuberance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumTipDiameterToAvoidPointedTeethNoProtuberance
        return temp

    @property
    def minimum_protuberance_having_pointed_teeth(self) -> 'float':
        """float: 'MinimumProtuberanceHavingPointedTeeth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumProtuberanceHavingPointedTeeth
        return temp

    @property
    def minimum_protuberance_height_for_single_circle(self) -> 'float':
        """float: 'MinimumProtuberanceHeightForSingleCircle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumProtuberanceHeightForSingleCircle
        return temp

    @property
    def normal_tooth_thickness(self) -> 'float':
        """float: 'NormalToothThickness' is the original name of this property."""

        temp = self.wrapped.NormalToothThickness
        return temp

    @normal_tooth_thickness.setter
    def normal_tooth_thickness(self, value: 'float'):
        self.wrapped.NormalToothThickness = float(value) if value else 0.0

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
    def protuberance_height(self) -> 'float':
        """float: 'ProtuberanceHeight' is the original name of this property."""

        temp = self.wrapped.ProtuberanceHeight
        return temp

    @protuberance_height.setter
    def protuberance_height(self, value: 'float'):
        self.wrapped.ProtuberanceHeight = float(value) if value else 0.0

    @property
    def root_diameter(self) -> 'float':
        """float: 'RootDiameter' is the original name of this property."""

        temp = self.wrapped.RootDiameter
        return temp

    @root_diameter.setter
    def root_diameter(self, value: 'float'):
        self.wrapped.RootDiameter = float(value) if value else 0.0

    @property
    def semi_topping_diameter(self) -> 'float':
        """float: 'SemiToppingDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SemiToppingDiameter
        return temp

    @property
    def semi_topping_pressure_angle(self) -> 'float':
        """float: 'SemiToppingPressureAngle' is the original name of this property."""

        temp = self.wrapped.SemiToppingPressureAngle
        return temp

    @semi_topping_pressure_angle.setter
    def semi_topping_pressure_angle(self, value: 'float'):
        self.wrapped.SemiToppingPressureAngle = float(value) if value else 0.0

    @property
    def single_circle_maximum_edge_radius(self) -> 'float':
        """float: 'SingleCircleMaximumEdgeRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SingleCircleMaximumEdgeRadius
        return temp

    @property
    def tip_diameter(self) -> 'float':
        """float: 'TipDiameter' is the original name of this property."""

        temp = self.wrapped.TipDiameter
        return temp

    @tip_diameter.setter
    def tip_diameter(self, value: 'float'):
        self.wrapped.TipDiameter = float(value) if value else 0.0

    @property
    def tip_thickness(self) -> 'float':
        """float: 'TipThickness' is the original name of this property."""

        temp = self.wrapped.TipThickness
        return temp

    @tip_thickness.setter
    def tip_thickness(self, value: 'float'):
        self.wrapped.TipThickness = float(value) if value else 0.0

    @property
    def design(self) -> '_704.CylindricalGearShaper':
        """CylindricalGearShaper: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

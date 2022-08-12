"""_2083.py

BallBearing
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.bearings.bearing_designs.rolling import _2084, _2108
from mastapy._internal.python_net import python_net_import

_BALL_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns.Rolling', 'BallBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('BallBearing',)


class BallBearing(_2108.RollingBearing):
    """BallBearing

    This is a mastapy class.
    """

    TYPE = _BALL_BEARING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BallBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact_radius_at_right_angle_to_rolling_direction_inner(self) -> 'float':
        """float: 'ContactRadiusAtRightAngleToRollingDirectionInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactRadiusAtRightAngleToRollingDirectionInner
        return temp

    @property
    def contact_radius_at_right_angle_to_rolling_direction_outer(self) -> 'float':
        """float: 'ContactRadiusAtRightAngleToRollingDirectionOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactRadiusAtRightAngleToRollingDirectionOuter
        return temp

    @property
    def curvature_sum_inner(self) -> 'float':
        """float: 'CurvatureSumInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurvatureSumInner
        return temp

    @property
    def curvature_sum_outer(self) -> 'float':
        """float: 'CurvatureSumOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurvatureSumOuter
        return temp

    @property
    def element_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'ElementDiameter' is the original name of this property."""

        temp = self.wrapped.ElementDiameter
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @element_diameter.setter
    def element_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.ElementDiameter = value

    @property
    def inner_groove_radius(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'InnerGrooveRadius' is the original name of this property."""

        temp = self.wrapped.InnerGrooveRadius
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @inner_groove_radius.setter
    def inner_groove_radius(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.InnerGrooveRadius = value

    @property
    def inner_groove_radius_as_percentage_of_element_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'InnerGrooveRadiusAsPercentageOfElementDiameter' is the original name of this property."""

        temp = self.wrapped.InnerGrooveRadiusAsPercentageOfElementDiameter
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @inner_groove_radius_as_percentage_of_element_diameter.setter
    def inner_groove_radius_as_percentage_of_element_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.InnerGrooveRadiusAsPercentageOfElementDiameter = value

    @property
    def inner_left_shoulder_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'InnerLeftShoulderDiameter' is the original name of this property."""

        temp = self.wrapped.InnerLeftShoulderDiameter
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @inner_left_shoulder_diameter.setter
    def inner_left_shoulder_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.InnerLeftShoulderDiameter = value

    @property
    def inner_race_osculation(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'InnerRaceOsculation' is the original name of this property."""

        temp = self.wrapped.InnerRaceOsculation
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @inner_race_osculation.setter
    def inner_race_osculation(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.InnerRaceOsculation = value

    @property
    def inner_right_shoulder_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'InnerRightShoulderDiameter' is the original name of this property."""

        temp = self.wrapped.InnerRightShoulderDiameter
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @inner_right_shoulder_diameter.setter
    def inner_right_shoulder_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.InnerRightShoulderDiameter = value

    @property
    def inner_ring_left_shoulder_height(self) -> 'float':
        """float: 'InnerRingLeftShoulderHeight' is the original name of this property."""

        temp = self.wrapped.InnerRingLeftShoulderHeight
        return temp

    @inner_ring_left_shoulder_height.setter
    def inner_ring_left_shoulder_height(self, value: 'float'):
        self.wrapped.InnerRingLeftShoulderHeight = float(value) if value else 0.0

    @property
    def inner_ring_right_shoulder_height(self) -> 'float':
        """float: 'InnerRingRightShoulderHeight' is the original name of this property."""

        temp = self.wrapped.InnerRingRightShoulderHeight
        return temp

    @inner_ring_right_shoulder_height.setter
    def inner_ring_right_shoulder_height(self, value: 'float'):
        self.wrapped.InnerRingRightShoulderHeight = float(value) if value else 0.0

    @property
    def inner_ring_shoulder_chamfer(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'InnerRingShoulderChamfer' is the original name of this property."""

        temp = self.wrapped.InnerRingShoulderChamfer
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @inner_ring_shoulder_chamfer.setter
    def inner_ring_shoulder_chamfer(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.InnerRingShoulderChamfer = value

    @property
    def outer_groove_radius(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'OuterGrooveRadius' is the original name of this property."""

        temp = self.wrapped.OuterGrooveRadius
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @outer_groove_radius.setter
    def outer_groove_radius(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.OuterGrooveRadius = value

    @property
    def outer_groove_radius_as_percentage_of_element_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'OuterGrooveRadiusAsPercentageOfElementDiameter' is the original name of this property."""

        temp = self.wrapped.OuterGrooveRadiusAsPercentageOfElementDiameter
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @outer_groove_radius_as_percentage_of_element_diameter.setter
    def outer_groove_radius_as_percentage_of_element_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.OuterGrooveRadiusAsPercentageOfElementDiameter = value

    @property
    def outer_left_shoulder_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'OuterLeftShoulderDiameter' is the original name of this property."""

        temp = self.wrapped.OuterLeftShoulderDiameter
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @outer_left_shoulder_diameter.setter
    def outer_left_shoulder_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.OuterLeftShoulderDiameter = value

    @property
    def outer_race_osculation(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'OuterRaceOsculation' is the original name of this property."""

        temp = self.wrapped.OuterRaceOsculation
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @outer_race_osculation.setter
    def outer_race_osculation(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.OuterRaceOsculation = value

    @property
    def outer_right_shoulder_diameter(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'OuterRightShoulderDiameter' is the original name of this property."""

        temp = self.wrapped.OuterRightShoulderDiameter
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @outer_right_shoulder_diameter.setter
    def outer_right_shoulder_diameter(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.OuterRightShoulderDiameter = value

    @property
    def outer_ring_left_shoulder_height(self) -> 'float':
        """float: 'OuterRingLeftShoulderHeight' is the original name of this property."""

        temp = self.wrapped.OuterRingLeftShoulderHeight
        return temp

    @outer_ring_left_shoulder_height.setter
    def outer_ring_left_shoulder_height(self, value: 'float'):
        self.wrapped.OuterRingLeftShoulderHeight = float(value) if value else 0.0

    @property
    def outer_ring_right_shoulder_height(self) -> 'float':
        """float: 'OuterRingRightShoulderHeight' is the original name of this property."""

        temp = self.wrapped.OuterRingRightShoulderHeight
        return temp

    @outer_ring_right_shoulder_height.setter
    def outer_ring_right_shoulder_height(self, value: 'float'):
        self.wrapped.OuterRingRightShoulderHeight = float(value) if value else 0.0

    @property
    def outer_ring_shoulder_chamfer(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'OuterRingShoulderChamfer' is the original name of this property."""

        temp = self.wrapped.OuterRingShoulderChamfer
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @outer_ring_shoulder_chamfer.setter
    def outer_ring_shoulder_chamfer(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.OuterRingShoulderChamfer = value

    @property
    def relative_curvature_difference_inner(self) -> 'float':
        """float: 'RelativeCurvatureDifferenceInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeCurvatureDifferenceInner
        return temp

    @property
    def relative_curvature_difference_outer(self) -> 'float':
        """float: 'RelativeCurvatureDifferenceOuter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeCurvatureDifferenceOuter
        return temp

    @property
    def shoulders(self) -> 'List[_2084.BallBearingShoulderDefinition]':
        """List[BallBearingShoulderDefinition]: 'Shoulders' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Shoulders
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

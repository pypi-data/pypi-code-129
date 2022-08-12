"""_1566.py

MeasurementSettings
"""


from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item, overridable
from mastapy.utility.units_and_measurements import _1565
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.utility.units_and_measurements.measurements import (
    _1572, _1573, _1574, _1575,
    _1576, _1577, _1578, _1579,
    _1580, _1581, _1582, _1583,
    _1584, _1585, _1586, _1587,
    _1588, _1589, _1590, _1591,
    _1592, _1593, _1594, _1595,
    _1596, _1597, _1598, _1599,
    _1600, _1601, _1602, _1603,
    _1604, _1605, _1606, _1607,
    _1608, _1609, _1610, _1611,
    _1612, _1613, _1614, _1615,
    _1616, _1617, _1618, _1619,
    _1620, _1621, _1622, _1623,
    _1624, _1625, _1626, _1627,
    _1628, _1629, _1630, _1631,
    _1632, _1633, _1634, _1635,
    _1636, _1637, _1638, _1639,
    _1640, _1641, _1642, _1643,
    _1644, _1645, _1646, _1647,
    _1648, _1649, _1650, _1651,
    _1652, _1653, _1654, _1655,
    _1656, _1657, _1658, _1659,
    _1660, _1661, _1662, _1663,
    _1664, _1665, _1666, _1667,
    _1668, _1669, _1670, _1671,
    _1672, _1673, _1674, _1675,
    _1676, _1677, _1678, _1679,
    _1680, _1681, _1682, _1683,
    _1684, _1685, _1686, _1687,
    _1688, _1689, _1690, _1691,
    _1692, _1693, _1694, _1695,
    _1696, _1697
)
from mastapy._internal.cast_exception import CastException
from mastapy.units_and_measurements import _7472
from mastapy.utility import _1554
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_SETTINGS = python_net_import('SMT.MastaAPI.Utility.UnitsAndMeasurements', 'MeasurementSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementSettings',)


class MeasurementSettings(_1554.PerMachineSettings):
    """MeasurementSettings

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_SETTINGS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MeasurementSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def large_number_cutoff(self) -> 'float':
        """float: 'LargeNumberCutoff' is the original name of this property."""

        temp = self.wrapped.LargeNumberCutoff
        return temp

    @large_number_cutoff.setter
    def large_number_cutoff(self, value: 'float'):
        self.wrapped.LargeNumberCutoff = float(value) if value else 0.0

    @property
    def number_decimal_separator(self) -> 'str':
        """str: 'NumberDecimalSeparator' is the original name of this property."""

        temp = self.wrapped.NumberDecimalSeparator
        return temp

    @number_decimal_separator.setter
    def number_decimal_separator(self, value: 'str'):
        self.wrapped.NumberDecimalSeparator = str(value) if value else ''

    @property
    def number_group_separator(self) -> 'str':
        """str: 'NumberGroupSeparator' is the original name of this property."""

        temp = self.wrapped.NumberGroupSeparator
        return temp

    @number_group_separator.setter
    def number_group_separator(self, value: 'str'):
        self.wrapped.NumberGroupSeparator = str(value) if value else ''

    @property
    def sample_input(self) -> 'str':
        """str: 'SampleInput' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SampleInput
        return temp

    @property
    def sample_output(self) -> 'str':
        """str: 'SampleOutput' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SampleOutput
        return temp

    @property
    def selected_measurement(self) -> 'list_with_selected_item.ListWithSelectedItem_MeasurementBase':
        """list_with_selected_item.ListWithSelectedItem_MeasurementBase: 'SelectedMeasurement' is the original name of this property."""

        temp = self.wrapped.SelectedMeasurement
        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_MeasurementBase)(temp) if temp is not None else None

    @selected_measurement.setter
    def selected_measurement(self, value: 'list_with_selected_item.ListWithSelectedItem_MeasurementBase.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_MeasurementBase.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_MeasurementBase.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.SelectedMeasurement = value

    @property
    def show_trailing_zeros(self) -> 'bool':
        """bool: 'ShowTrailingZeros' is the original name of this property."""

        temp = self.wrapped.ShowTrailingZeros
        return temp

    @show_trailing_zeros.setter
    def show_trailing_zeros(self, value: 'bool'):
        self.wrapped.ShowTrailingZeros = bool(value) if value else False

    @property
    def small_number_cutoff(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'SmallNumberCutoff' is the original name of this property."""

        temp = self.wrapped.SmallNumberCutoff
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @small_number_cutoff.setter
    def small_number_cutoff(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.SmallNumberCutoff = value

    @property
    def current_selected_measurement(self) -> '_1565.MeasurementBase':
        """MeasurementBase: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1565.MeasurementBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MeasurementBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_acceleration(self) -> '_1572.Acceleration':
        """Acceleration: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1572.Acceleration.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Acceleration. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angle(self) -> '_1573.Angle':
        """Angle: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1573.Angle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Angle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angle_per_unit_temperature(self) -> '_1574.AnglePerUnitTemperature':
        """AnglePerUnitTemperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1574.AnglePerUnitTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AnglePerUnitTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angle_small(self) -> '_1575.AngleSmall':
        """AngleSmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1575.AngleSmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngleSmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angle_very_small(self) -> '_1576.AngleVerySmall':
        """AngleVerySmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1576.AngleVerySmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngleVerySmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angular_acceleration(self) -> '_1577.AngularAcceleration':
        """AngularAcceleration: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1577.AngularAcceleration.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngularAcceleration. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angular_compliance(self) -> '_1578.AngularCompliance':
        """AngularCompliance: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1578.AngularCompliance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngularCompliance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angular_jerk(self) -> '_1579.AngularJerk':
        """AngularJerk: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1579.AngularJerk.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngularJerk. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angular_stiffness(self) -> '_1580.AngularStiffness':
        """AngularStiffness: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1580.AngularStiffness.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngularStiffness. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_angular_velocity(self) -> '_1581.AngularVelocity':
        """AngularVelocity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1581.AngularVelocity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AngularVelocity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_area(self) -> '_1582.Area':
        """Area: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1582.Area.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Area. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_area_small(self) -> '_1583.AreaSmall':
        """AreaSmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1583.AreaSmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to AreaSmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_current_density(self) -> '_1584.CurrentDensity':
        """CurrentDensity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1584.CurrentDensity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to CurrentDensity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_current_per_length(self) -> '_1585.CurrentPerLength':
        """CurrentPerLength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1585.CurrentPerLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to CurrentPerLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_cycles(self) -> '_1586.Cycles':
        """Cycles: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1586.Cycles.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Cycles. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_damage(self) -> '_1587.Damage':
        """Damage: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1587.Damage.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Damage. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_damage_rate(self) -> '_1588.DamageRate':
        """DamageRate: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1588.DamageRate.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to DamageRate. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_data_size(self) -> '_1589.DataSize':
        """DataSize: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1589.DataSize.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to DataSize. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_decibel(self) -> '_1590.Decibel':
        """Decibel: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1590.Decibel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Decibel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_density(self) -> '_1591.Density':
        """Density: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1591.Density.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Density. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_electrical_resistance(self) -> '_1592.ElectricalResistance':
        """ElectricalResistance: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1592.ElectricalResistance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ElectricalResistance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_electrical_resistivity(self) -> '_1593.ElectricalResistivity':
        """ElectricalResistivity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1593.ElectricalResistivity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ElectricalResistivity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_electric_current(self) -> '_1594.ElectricCurrent':
        """ElectricCurrent: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1594.ElectricCurrent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ElectricCurrent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_energy(self) -> '_1595.Energy':
        """Energy: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1595.Energy.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Energy. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_energy_per_unit_area(self) -> '_1596.EnergyPerUnitArea':
        """EnergyPerUnitArea: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1596.EnergyPerUnitArea.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to EnergyPerUnitArea. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_energy_per_unit_area_small(self) -> '_1597.EnergyPerUnitAreaSmall':
        """EnergyPerUnitAreaSmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1597.EnergyPerUnitAreaSmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to EnergyPerUnitAreaSmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_energy_small(self) -> '_1598.EnergySmall':
        """EnergySmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1598.EnergySmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to EnergySmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_enum(self) -> '_1599.Enum':
        """Enum: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1599.Enum.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Enum. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_flow_rate(self) -> '_1600.FlowRate':
        """FlowRate: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1600.FlowRate.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to FlowRate. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_force(self) -> '_1601.Force':
        """Force: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1601.Force.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Force. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_force_per_unit_length(self) -> '_1602.ForcePerUnitLength':
        """ForcePerUnitLength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1602.ForcePerUnitLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ForcePerUnitLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_force_per_unit_pressure(self) -> '_1603.ForcePerUnitPressure':
        """ForcePerUnitPressure: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1603.ForcePerUnitPressure.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ForcePerUnitPressure. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_force_per_unit_temperature(self) -> '_1604.ForcePerUnitTemperature':
        """ForcePerUnitTemperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1604.ForcePerUnitTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ForcePerUnitTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_fraction_measurement_base(self) -> '_1605.FractionMeasurementBase':
        """FractionMeasurementBase: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1605.FractionMeasurementBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to FractionMeasurementBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_fraction_per_temperature(self) -> '_1606.FractionPerTemperature':
        """FractionPerTemperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1606.FractionPerTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to FractionPerTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_frequency(self) -> '_1607.Frequency':
        """Frequency: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1607.Frequency.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Frequency. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_fuel_consumption_engine(self) -> '_1608.FuelConsumptionEngine':
        """FuelConsumptionEngine: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1608.FuelConsumptionEngine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to FuelConsumptionEngine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_fuel_efficiency_vehicle(self) -> '_1609.FuelEfficiencyVehicle':
        """FuelEfficiencyVehicle: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1609.FuelEfficiencyVehicle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to FuelEfficiencyVehicle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_gradient(self) -> '_1610.Gradient':
        """Gradient: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1610.Gradient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Gradient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_heat_conductivity(self) -> '_1611.HeatConductivity':
        """HeatConductivity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1611.HeatConductivity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to HeatConductivity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_heat_transfer(self) -> '_1612.HeatTransfer':
        """HeatTransfer: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1612.HeatTransfer.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to HeatTransfer. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_heat_transfer_coefficient_for_plastic_gear_tooth(self) -> '_1613.HeatTransferCoefficientForPlasticGearTooth':
        """HeatTransferCoefficientForPlasticGearTooth: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1613.HeatTransferCoefficientForPlasticGearTooth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to HeatTransferCoefficientForPlasticGearTooth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_heat_transfer_resistance(self) -> '_1614.HeatTransferResistance':
        """HeatTransferResistance: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1614.HeatTransferResistance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to HeatTransferResistance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_impulse(self) -> '_1615.Impulse':
        """Impulse: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1615.Impulse.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Impulse. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_index(self) -> '_1616.Index':
        """Index: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1616.Index.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Index. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_inductance(self) -> '_1617.Inductance':
        """Inductance: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1617.Inductance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Inductance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_integer(self) -> '_1618.Integer':
        """Integer: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1618.Integer.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Integer. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_inverse_short_length(self) -> '_1619.InverseShortLength':
        """InverseShortLength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1619.InverseShortLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to InverseShortLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_inverse_short_time(self) -> '_1620.InverseShortTime':
        """InverseShortTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1620.InverseShortTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to InverseShortTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_jerk(self) -> '_1621.Jerk':
        """Jerk: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1621.Jerk.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Jerk. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_kinematic_viscosity(self) -> '_1622.KinematicViscosity':
        """KinematicViscosity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1622.KinematicViscosity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to KinematicViscosity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_length_long(self) -> '_1623.LengthLong':
        """LengthLong: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1623.LengthLong.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthLong. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_length_medium(self) -> '_1624.LengthMedium':
        """LengthMedium: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1624.LengthMedium.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthMedium. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_length_per_unit_temperature(self) -> '_1625.LengthPerUnitTemperature':
        """LengthPerUnitTemperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1625.LengthPerUnitTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthPerUnitTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_length_short(self) -> '_1626.LengthShort':
        """LengthShort: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1626.LengthShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_length_to_the_fourth(self) -> '_1627.LengthToTheFourth':
        """LengthToTheFourth: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1627.LengthToTheFourth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthToTheFourth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_length_very_long(self) -> '_1628.LengthVeryLong':
        """LengthVeryLong: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1628.LengthVeryLong.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthVeryLong. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_length_very_short(self) -> '_1629.LengthVeryShort':
        """LengthVeryShort: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1629.LengthVeryShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthVeryShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_length_very_short_per_length_short(self) -> '_1630.LengthVeryShortPerLengthShort':
        """LengthVeryShortPerLengthShort: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1630.LengthVeryShortPerLengthShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LengthVeryShortPerLengthShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_linear_angular_damping(self) -> '_1631.LinearAngularDamping':
        """LinearAngularDamping: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1631.LinearAngularDamping.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LinearAngularDamping. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_linear_angular_stiffness_cross_term(self) -> '_1632.LinearAngularStiffnessCrossTerm':
        """LinearAngularStiffnessCrossTerm: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1632.LinearAngularStiffnessCrossTerm.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LinearAngularStiffnessCrossTerm. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_linear_damping(self) -> '_1633.LinearDamping':
        """LinearDamping: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1633.LinearDamping.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LinearDamping. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_linear_flexibility(self) -> '_1634.LinearFlexibility':
        """LinearFlexibility: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1634.LinearFlexibility.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LinearFlexibility. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_linear_stiffness(self) -> '_1635.LinearStiffness':
        """LinearStiffness: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1635.LinearStiffness.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to LinearStiffness. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_magnetic_field_strength(self) -> '_1636.MagneticFieldStrength':
        """MagneticFieldStrength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1636.MagneticFieldStrength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MagneticFieldStrength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_magnetic_flux(self) -> '_1637.MagneticFlux':
        """MagneticFlux: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1637.MagneticFlux.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MagneticFlux. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_magnetic_flux_density(self) -> '_1638.MagneticFluxDensity':
        """MagneticFluxDensity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1638.MagneticFluxDensity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MagneticFluxDensity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_magnetic_vector_potential(self) -> '_1639.MagneticVectorPotential':
        """MagneticVectorPotential: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1639.MagneticVectorPotential.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MagneticVectorPotential. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_magnetomotive_force(self) -> '_1640.MagnetomotiveForce':
        """MagnetomotiveForce: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1640.MagnetomotiveForce.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MagnetomotiveForce. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_mass(self) -> '_1641.Mass':
        """Mass: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1641.Mass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Mass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_mass_per_unit_length(self) -> '_1642.MassPerUnitLength':
        """MassPerUnitLength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1642.MassPerUnitLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MassPerUnitLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_mass_per_unit_time(self) -> '_1643.MassPerUnitTime':
        """MassPerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1643.MassPerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MassPerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_moment_of_inertia(self) -> '_1644.MomentOfInertia':
        """MomentOfInertia: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1644.MomentOfInertia.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MomentOfInertia. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_moment_of_inertia_per_unit_length(self) -> '_1645.MomentOfInertiaPerUnitLength':
        """MomentOfInertiaPerUnitLength: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1645.MomentOfInertiaPerUnitLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MomentOfInertiaPerUnitLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_moment_per_unit_pressure(self) -> '_1646.MomentPerUnitPressure':
        """MomentPerUnitPressure: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1646.MomentPerUnitPressure.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to MomentPerUnitPressure. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_number(self) -> '_1647.Number':
        """Number: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1647.Number.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Number. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_percentage(self) -> '_1648.Percentage':
        """Percentage: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1648.Percentage.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Percentage. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power(self) -> '_1649.Power':
        """Power: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1649.Power.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Power. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power_per_small_area(self) -> '_1650.PowerPerSmallArea':
        """PowerPerSmallArea: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1650.PowerPerSmallArea.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerPerSmallArea. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power_per_unit_time(self) -> '_1651.PowerPerUnitTime':
        """PowerPerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1651.PowerPerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerPerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power_small(self) -> '_1652.PowerSmall':
        """PowerSmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1652.PowerSmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power_small_per_area(self) -> '_1653.PowerSmallPerArea':
        """PowerSmallPerArea: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1653.PowerSmallPerArea.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmallPerArea. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power_small_per_mass(self) -> '_1654.PowerSmallPerMass':
        """PowerSmallPerMass: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1654.PowerSmallPerMass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmallPerMass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power_small_per_unit_area_per_unit_time(self) -> '_1655.PowerSmallPerUnitAreaPerUnitTime':
        """PowerSmallPerUnitAreaPerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1655.PowerSmallPerUnitAreaPerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmallPerUnitAreaPerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power_small_per_unit_time(self) -> '_1656.PowerSmallPerUnitTime':
        """PowerSmallPerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1656.PowerSmallPerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmallPerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_power_small_per_volume(self) -> '_1657.PowerSmallPerVolume':
        """PowerSmallPerVolume: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1657.PowerSmallPerVolume.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PowerSmallPerVolume. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_pressure(self) -> '_1658.Pressure':
        """Pressure: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1658.Pressure.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Pressure. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_pressure_per_unit_time(self) -> '_1659.PressurePerUnitTime':
        """PressurePerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1659.PressurePerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PressurePerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_pressure_velocity_product(self) -> '_1660.PressureVelocityProduct':
        """PressureVelocityProduct: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1660.PressureVelocityProduct.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PressureVelocityProduct. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_pressure_viscosity_coefficient(self) -> '_1661.PressureViscosityCoefficient':
        """PressureViscosityCoefficient: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1661.PressureViscosityCoefficient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PressureViscosityCoefficient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_price(self) -> '_1662.Price':
        """Price: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1662.Price.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Price. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_price_per_unit_mass(self) -> '_1663.PricePerUnitMass':
        """PricePerUnitMass: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1663.PricePerUnitMass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to PricePerUnitMass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_quadratic_angular_damping(self) -> '_1664.QuadraticAngularDamping':
        """QuadraticAngularDamping: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1664.QuadraticAngularDamping.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to QuadraticAngularDamping. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_quadratic_drag(self) -> '_1665.QuadraticDrag':
        """QuadraticDrag: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1665.QuadraticDrag.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to QuadraticDrag. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_rescaled_measurement(self) -> '_1666.RescaledMeasurement':
        """RescaledMeasurement: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1666.RescaledMeasurement.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to RescaledMeasurement. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_rotatum(self) -> '_1667.Rotatum':
        """Rotatum: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1667.Rotatum.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Rotatum. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_safety_factor(self) -> '_1668.SafetyFactor':
        """SafetyFactor: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1668.SafetyFactor.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to SafetyFactor. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_specific_acoustic_impedance(self) -> '_1669.SpecificAcousticImpedance':
        """SpecificAcousticImpedance: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1669.SpecificAcousticImpedance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to SpecificAcousticImpedance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_specific_heat(self) -> '_1670.SpecificHeat':
        """SpecificHeat: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1670.SpecificHeat.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to SpecificHeat. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_square_root_of_unit_force_per_unit_area(self) -> '_1671.SquareRootOfUnitForcePerUnitArea':
        """SquareRootOfUnitForcePerUnitArea: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1671.SquareRootOfUnitForcePerUnitArea.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to SquareRootOfUnitForcePerUnitArea. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_stiffness_per_unit_face_width(self) -> '_1672.StiffnessPerUnitFaceWidth':
        """StiffnessPerUnitFaceWidth: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1672.StiffnessPerUnitFaceWidth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to StiffnessPerUnitFaceWidth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_stress(self) -> '_1673.Stress':
        """Stress: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1673.Stress.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Stress. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_temperature(self) -> '_1674.Temperature':
        """Temperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1674.Temperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Temperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_temperature_difference(self) -> '_1675.TemperatureDifference':
        """TemperatureDifference: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1675.TemperatureDifference.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TemperatureDifference. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_temperature_per_unit_time(self) -> '_1676.TemperaturePerUnitTime':
        """TemperaturePerUnitTime: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1676.TemperaturePerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TemperaturePerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_text(self) -> '_1677.Text':
        """Text: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1677.Text.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Text. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_thermal_contact_coefficient(self) -> '_1678.ThermalContactCoefficient':
        """ThermalContactCoefficient: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1678.ThermalContactCoefficient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ThermalContactCoefficient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_thermal_expansion_coefficient(self) -> '_1679.ThermalExpansionCoefficient':
        """ThermalExpansionCoefficient: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1679.ThermalExpansionCoefficient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ThermalExpansionCoefficient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_thermo_elastic_factor(self) -> '_1680.ThermoElasticFactor':
        """ThermoElasticFactor: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1680.ThermoElasticFactor.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to ThermoElasticFactor. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_time(self) -> '_1681.Time':
        """Time: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1681.Time.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Time. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_time_short(self) -> '_1682.TimeShort':
        """TimeShort: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1682.TimeShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TimeShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_time_very_short(self) -> '_1683.TimeVeryShort':
        """TimeVeryShort: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1683.TimeVeryShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TimeVeryShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_torque(self) -> '_1684.Torque':
        """Torque: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1684.Torque.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Torque. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_torque_converter_inverse_k(self) -> '_1685.TorqueConverterInverseK':
        """TorqueConverterInverseK: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1685.TorqueConverterInverseK.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TorqueConverterInverseK. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_torque_converter_k(self) -> '_1686.TorqueConverterK':
        """TorqueConverterK: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1686.TorqueConverterK.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TorqueConverterK. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_torque_per_current(self) -> '_1687.TorquePerCurrent':
        """TorquePerCurrent: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1687.TorquePerCurrent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TorquePerCurrent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_torque_per_square_root_of_power(self) -> '_1688.TorquePerSquareRootOfPower':
        """TorquePerSquareRootOfPower: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1688.TorquePerSquareRootOfPower.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TorquePerSquareRootOfPower. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_torque_per_unit_temperature(self) -> '_1689.TorquePerUnitTemperature':
        """TorquePerUnitTemperature: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1689.TorquePerUnitTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to TorquePerUnitTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_velocity(self) -> '_1690.Velocity':
        """Velocity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1690.Velocity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Velocity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_velocity_small(self) -> '_1691.VelocitySmall':
        """VelocitySmall: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1691.VelocitySmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to VelocitySmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_viscosity(self) -> '_1692.Viscosity':
        """Viscosity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1692.Viscosity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Viscosity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_voltage(self) -> '_1693.Voltage':
        """Voltage: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1693.Voltage.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Voltage. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_voltage_per_angular_velocity(self) -> '_1694.VoltagePerAngularVelocity':
        """VoltagePerAngularVelocity: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1694.VoltagePerAngularVelocity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to VoltagePerAngularVelocity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_volume(self) -> '_1695.Volume':
        """Volume: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1695.Volume.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Volume. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_wear_coefficient(self) -> '_1696.WearCoefficient':
        """WearCoefficient: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1696.WearCoefficient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to WearCoefficient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def current_selected_measurement_of_type_yank(self) -> '_1697.Yank':
        """Yank: 'CurrentSelectedMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentSelectedMeasurement
        if _1697.Yank.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast current_selected_measurement to Yank. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def default_to_imperial(self):
        """ 'DefaultToImperial' is the original name of this method."""

        self.wrapped.DefaultToImperial()

    def default_to_metric(self):
        """ 'DefaultToMetric' is the original name of this method."""

        self.wrapped.DefaultToMetric()

    def find_measurement_by_name(self, name: 'str') -> '_1565.MeasurementBase':
        """ 'FindMeasurementByName' is the original name of this method.

        Args:
            name (str)

        Returns:
            mastapy.utility.units_and_measurements.MeasurementBase
        """

        name = str(name)
        method_result = self.wrapped.FindMeasurementByName(name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_measurement(self, measurement_type: '_7472.MeasurementType') -> '_1565.MeasurementBase':
        """ 'GetMeasurement' is the original name of this method.

        Args:
            measurement_type (mastapy.units_and_measurements.MeasurementType)

        Returns:
            mastapy.utility.units_and_measurements.MeasurementBase
        """

        measurement_type = conversion.mp_to_pn_enum(measurement_type)
        method_result = self.wrapped.GetMeasurement(measurement_type)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

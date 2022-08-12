"""_2502.py

SuperchargerRotorSet
"""


from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.utility_gui.charts import _1813
from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
    _2504, _2494, _2497, _2495,
    _2496, _2499, _2498
)
from mastapy.utility.databases import _1785
from mastapy._internal.python_net import python_net_import

_SUPERCHARGER_ROTOR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears.SuperchargerRotorSet', 'SuperchargerRotorSet')


__docformat__ = 'restructuredtext en'
__all__ = ('SuperchargerRotorSet',)


class SuperchargerRotorSet(_1785.NamedDatabaseItem):
    """SuperchargerRotorSet

    This is a mastapy class.
    """

    TYPE = _SUPERCHARGER_ROTOR_SET

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SuperchargerRotorSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_reaction_force(self) -> 'float':
        """float: 'AxialReactionForce' is the original name of this property."""

        temp = self.wrapped.AxialReactionForce
        return temp

    @axial_reaction_force.setter
    def axial_reaction_force(self, value: 'float'):
        self.wrapped.AxialReactionForce = float(value) if value else 0.0

    @property
    def dynamic_load_factor(self) -> 'float':
        """float: 'DynamicLoadFactor' is the original name of this property."""

        temp = self.wrapped.DynamicLoadFactor
        return temp

    @dynamic_load_factor.setter
    def dynamic_load_factor(self, value: 'float'):
        self.wrapped.DynamicLoadFactor = float(value) if value else 0.0

    @property
    def lateral_reaction_force(self) -> 'float':
        """float: 'LateralReactionForce' is the original name of this property."""

        temp = self.wrapped.LateralReactionForce
        return temp

    @lateral_reaction_force.setter
    def lateral_reaction_force(self, value: 'float'):
        self.wrapped.LateralReactionForce = float(value) if value else 0.0

    @property
    def lateral_reaction_moment(self) -> 'float':
        """float: 'LateralReactionMoment' is the original name of this property."""

        temp = self.wrapped.LateralReactionMoment
        return temp

    @lateral_reaction_moment.setter
    def lateral_reaction_moment(self, value: 'float'):
        self.wrapped.LateralReactionMoment = float(value) if value else 0.0

    @property
    def selected_file_name(self) -> 'str':
        """str: 'SelectedFileName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SelectedFileName
        return temp

    @property
    def supercharger_map_chart(self) -> '_1813.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'SuperchargerMapChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SuperchargerMapChart
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def vertical_reaction_force(self) -> 'float':
        """float: 'VerticalReactionForce' is the original name of this property."""

        temp = self.wrapped.VerticalReactionForce
        return temp

    @vertical_reaction_force.setter
    def vertical_reaction_force(self, value: 'float'):
        self.wrapped.VerticalReactionForce = float(value) if value else 0.0

    @property
    def vertical_reaction_moment(self) -> 'float':
        """float: 'VerticalReactionMoment' is the original name of this property."""

        temp = self.wrapped.VerticalReactionMoment
        return temp

    @vertical_reaction_moment.setter
    def vertical_reaction_moment(self, value: 'float'):
        self.wrapped.VerticalReactionMoment = float(value) if value else 0.0

    @property
    def y_variable_for_imported_data(self) -> '_2504.YVariableForImportedData':
        """YVariableForImportedData: 'YVariableForImportedData' is the original name of this property."""

        temp = self.wrapped.YVariableForImportedData
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_2504.YVariableForImportedData)(value) if value is not None else None

    @y_variable_for_imported_data.setter
    def y_variable_for_imported_data(self, value: '_2504.YVariableForImportedData'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.YVariableForImportedData = value

    @property
    def boost_pressure(self) -> '_2494.BoostPressureInputOptions':
        """BoostPressureInputOptions: 'BoostPressure' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoostPressure
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def file(self) -> '_2497.RotorSetDataInputFileOptions':
        """RotorSetDataInputFileOptions: 'File' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.File
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def input_power(self) -> '_2495.InputPowerInputOptions':
        """InputPowerInputOptions: 'InputPower' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InputPower
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pressure_ratio(self) -> '_2496.PressureRatioInputOptions':
        """PressureRatioInputOptions: 'PressureRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PressureRatio
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rotor_speed(self) -> '_2499.RotorSpeedInputOptions':
        """RotorSpeedInputOptions: 'RotorSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RotorSpeed
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def measured_points(self) -> 'List[_2498.RotorSetMeasuredPoint]':
        """List[RotorSetMeasuredPoint]: 'MeasuredPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeasuredPoints
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def select_different_file(self):
        """ 'SelectDifferentFile' is the original name of this method."""

        self.wrapped.SelectDifferentFile()

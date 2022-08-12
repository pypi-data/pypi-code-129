"""_758.py

ShavingDynamicsCalculationForHobbedGears
"""


from typing import List, Generic, TypeVar

from mastapy.utility_gui.charts import (
    _1815, _1805, _1810, _1812
)
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.gears.gear_designs.cylindrical import _1016
from mastapy._internal.python_net import python_net_import
from mastapy.gears.manufacturing.cylindrical.axial_and_plunge_shaving_dynamics import (
    _754, _740, _747, _751,
    _756, _755
)

_REPORTING_OVERRIDABLE = python_net_import('SMT.MastaAPI.Utility.Property', 'ReportingOverridable')
_SHAVING_DYNAMICS_CALCULATION_FOR_HOBBED_GEARS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.AxialAndPlungeShavingDynamics', 'ShavingDynamicsCalculationForHobbedGears')


__docformat__ = 'restructuredtext en'
__all__ = ('ShavingDynamicsCalculationForHobbedGears',)


T = TypeVar('T', bound='_755.ShavingDynamics')


class ShavingDynamicsCalculationForHobbedGears(_756.ShavingDynamicsCalculation['T'], Generic[T]):
    """ShavingDynamicsCalculationForHobbedGears

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _SHAVING_DYNAMICS_CALCULATION_FOR_HOBBED_GEARS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShavingDynamicsCalculationForHobbedGears.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def redressing_chart_maximum_start_and_end_of_shaving_profile(self) -> '_1815.TwoDChartDefinition':
        """TwoDChartDefinition: 'RedressingChartMaximumStartAndEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingChartMaximumStartAndEndOfShavingProfile
        if _1815.TwoDChartDefinition.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast redressing_chart_maximum_start_and_end_of_shaving_profile to TwoDChartDefinition. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def redressing_chart_maximum_start_and_minimum_end_of_shaving_profile(self) -> '_1815.TwoDChartDefinition':
        """TwoDChartDefinition: 'RedressingChartMaximumStartAndMinimumEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingChartMaximumStartAndMinimumEndOfShavingProfile
        if _1815.TwoDChartDefinition.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast redressing_chart_maximum_start_and_minimum_end_of_shaving_profile to TwoDChartDefinition. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def redressing_chart_minimum_start_and_end_of_shaving_profile(self) -> '_1815.TwoDChartDefinition':
        """TwoDChartDefinition: 'RedressingChartMinimumStartAndEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingChartMinimumStartAndEndOfShavingProfile
        if _1815.TwoDChartDefinition.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast redressing_chart_minimum_start_and_end_of_shaving_profile to TwoDChartDefinition. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def redressing_chart_minimum_start_and_maximum_end_of_shaving_profile(self) -> '_1815.TwoDChartDefinition':
        """TwoDChartDefinition: 'RedressingChartMinimumStartAndMaximumEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingChartMinimumStartAndMaximumEndOfShavingProfile
        if _1815.TwoDChartDefinition.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast redressing_chart_minimum_start_and_maximum_end_of_shaving_profile to TwoDChartDefinition. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_redressing(self) -> 'list_with_selected_item.ListWithSelectedItem_T':
        """list_with_selected_item.ListWithSelectedItem_T: 'SelectedRedressing' is the original name of this property."""

        temp = self.wrapped.SelectedRedressing
        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_T)(temp) if temp is not None else None

    @selected_redressing.setter
    def selected_redressing(self, value: 'list_with_selected_item.ListWithSelectedItem_T.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_T.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_T.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.SelectedRedressing = value

    @property
    def maximum_end_of_shaving_profile(self) -> '_1016.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'MaximumEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumEndOfShavingProfile.Value
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def maximum_start_of_shaving_profile(self) -> '_1016.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'MaximumStartOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumStartOfShavingProfile.Value
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def minimum_end_of_shaving_profile(self) -> '_1016.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'MinimumEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumEndOfShavingProfile.Value
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def minimum_start_of_shaving_profile(self) -> '_1016.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'MinimumStartOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumStartOfShavingProfile.Value
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def redressing_at_maximum_start_and_end_of_shaving_profile(self) -> '_754.ShaverRedressing[T]':
        """ShaverRedressing[T]: 'RedressingAtMaximumStartAndEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingAtMaximumStartAndEndOfShavingProfile
        if _754.ShaverRedressing[T].TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast redressing_at_maximum_start_and_end_of_shaving_profile to ShaverRedressing[T]. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[T](temp) if temp is not None else None

    @property
    def redressing_at_maximum_start_and_end_of_shaving_profile_of_type_axial_shaver_redressing(self) -> '_740.AxialShaverRedressing':
        """AxialShaverRedressing: 'RedressingAtMaximumStartAndEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingAtMaximumStartAndEndOfShavingProfile
        if _740.AxialShaverRedressing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast redressing_at_maximum_start_and_end_of_shaving_profile to AxialShaverRedressing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def redressing_at_maximum_start_and_end_of_shaving_profile_of_type_plunge_shaver_redressing(self) -> '_747.PlungeShaverRedressing':
        """PlungeShaverRedressing: 'RedressingAtMaximumStartAndEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingAtMaximumStartAndEndOfShavingProfile
        if _747.PlungeShaverRedressing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast redressing_at_maximum_start_and_end_of_shaving_profile to PlungeShaverRedressing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def redressing_at_maximum_start_and_minimum_end_of_shaving_profile(self) -> '_754.ShaverRedressing[T]':
        """ShaverRedressing[T]: 'RedressingAtMaximumStartAndMinimumEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingAtMaximumStartAndMinimumEndOfShavingProfile
        if _754.ShaverRedressing[T].TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast redressing_at_maximum_start_and_minimum_end_of_shaving_profile to ShaverRedressing[T]. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[T](temp) if temp is not None else None

    @property
    def redressing_at_maximum_start_and_minimum_end_of_shaving_profile_of_type_axial_shaver_redressing(self) -> '_740.AxialShaverRedressing':
        """AxialShaverRedressing: 'RedressingAtMaximumStartAndMinimumEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingAtMaximumStartAndMinimumEndOfShavingProfile
        if _740.AxialShaverRedressing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast redressing_at_maximum_start_and_minimum_end_of_shaving_profile to AxialShaverRedressing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def redressing_at_maximum_start_and_minimum_end_of_shaving_profile_of_type_plunge_shaver_redressing(self) -> '_747.PlungeShaverRedressing':
        """PlungeShaverRedressing: 'RedressingAtMaximumStartAndMinimumEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingAtMaximumStartAndMinimumEndOfShavingProfile
        if _747.PlungeShaverRedressing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast redressing_at_maximum_start_and_minimum_end_of_shaving_profile to PlungeShaverRedressing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def redressing_at_minimum_start_and_end_of_shaving_profile(self) -> '_754.ShaverRedressing[T]':
        """ShaverRedressing[T]: 'RedressingAtMinimumStartAndEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingAtMinimumStartAndEndOfShavingProfile
        if _754.ShaverRedressing[T].TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast redressing_at_minimum_start_and_end_of_shaving_profile to ShaverRedressing[T]. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[T](temp) if temp is not None else None

    @property
    def redressing_at_minimum_start_and_end_of_shaving_profile_of_type_axial_shaver_redressing(self) -> '_740.AxialShaverRedressing':
        """AxialShaverRedressing: 'RedressingAtMinimumStartAndEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingAtMinimumStartAndEndOfShavingProfile
        if _740.AxialShaverRedressing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast redressing_at_minimum_start_and_end_of_shaving_profile to AxialShaverRedressing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def redressing_at_minimum_start_and_end_of_shaving_profile_of_type_plunge_shaver_redressing(self) -> '_747.PlungeShaverRedressing':
        """PlungeShaverRedressing: 'RedressingAtMinimumStartAndEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingAtMinimumStartAndEndOfShavingProfile
        if _747.PlungeShaverRedressing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast redressing_at_minimum_start_and_end_of_shaving_profile to PlungeShaverRedressing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def redressing_at_minimum_start_and_maximum_end_of_shaving_profile(self) -> '_754.ShaverRedressing[T]':
        """ShaverRedressing[T]: 'RedressingAtMinimumStartAndMaximumEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingAtMinimumStartAndMaximumEndOfShavingProfile
        if _754.ShaverRedressing[T].TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast redressing_at_minimum_start_and_maximum_end_of_shaving_profile to ShaverRedressing[T]. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[T](temp) if temp is not None else None

    @property
    def redressing_at_minimum_start_and_maximum_end_of_shaving_profile_of_type_axial_shaver_redressing(self) -> '_740.AxialShaverRedressing':
        """AxialShaverRedressing: 'RedressingAtMinimumStartAndMaximumEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingAtMinimumStartAndMaximumEndOfShavingProfile
        if _740.AxialShaverRedressing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast redressing_at_minimum_start_and_maximum_end_of_shaving_profile to AxialShaverRedressing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def redressing_at_minimum_start_and_maximum_end_of_shaving_profile_of_type_plunge_shaver_redressing(self) -> '_747.PlungeShaverRedressing':
        """PlungeShaverRedressing: 'RedressingAtMinimumStartAndMaximumEndOfShavingProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingAtMinimumStartAndMaximumEndOfShavingProfile
        if _747.PlungeShaverRedressing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast redressing_at_minimum_start_and_maximum_end_of_shaving_profile to PlungeShaverRedressing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def redressing_settings(self) -> 'List[_751.RedressingSettings[T]]':
        """List[RedressingSettings[T]]: 'RedressingSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RedressingSettings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

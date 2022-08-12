"""_801.py

Wheel
"""


from mastapy.gears.manufacturing.bevel.basic_machine_settings import _811, _812, _813
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.gears.manufacturing.bevel.cutters import _805
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_WHEEL = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'Wheel')


__docformat__ = 'restructuredtext en'
__all__ = ('Wheel',)


class Wheel(_0.APIBase):
    """Wheel

    This is a mastapy class.
    """

    TYPE = _WHEEL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'Wheel.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def basic_conical_gear_machine_settings(self) -> '_811.BasicConicalGearMachineSettings':
        """BasicConicalGearMachineSettings: 'BasicConicalGearMachineSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicConicalGearMachineSettings
        if _811.BasicConicalGearMachineSettings.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast basic_conical_gear_machine_settings to BasicConicalGearMachineSettings. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def basic_conical_gear_machine_settings_of_type_basic_conical_gear_machine_settings_formate(self) -> '_812.BasicConicalGearMachineSettingsFormate':
        """BasicConicalGearMachineSettingsFormate: 'BasicConicalGearMachineSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicConicalGearMachineSettings
        if _812.BasicConicalGearMachineSettingsFormate.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast basic_conical_gear_machine_settings to BasicConicalGearMachineSettingsFormate. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def basic_conical_gear_machine_settings_of_type_basic_conical_gear_machine_settings_generated(self) -> '_813.BasicConicalGearMachineSettingsGenerated':
        """BasicConicalGearMachineSettingsGenerated: 'BasicConicalGearMachineSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicConicalGearMachineSettings
        if _813.BasicConicalGearMachineSettingsGenerated.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast basic_conical_gear_machine_settings to BasicConicalGearMachineSettingsGenerated. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def wheel_finish_cutter(self) -> '_805.WheelFinishCutter':
        """WheelFinishCutter: 'WheelFinishCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelFinishCutter
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

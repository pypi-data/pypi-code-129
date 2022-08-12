"""_814.py

CradleStyleConicalMachineSettingsGenerated
"""


from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_CRADLE_STYLE_CONICAL_MACHINE_SETTINGS_GENERATED = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel.BasicMachineSettings', 'CradleStyleConicalMachineSettingsGenerated')


__docformat__ = 'restructuredtext en'
__all__ = ('CradleStyleConicalMachineSettingsGenerated',)


class CradleStyleConicalMachineSettingsGenerated(_0.APIBase):
    """CradleStyleConicalMachineSettingsGenerated

    This is a mastapy class.
    """

    TYPE = _CRADLE_STYLE_CONICAL_MACHINE_SETTINGS_GENERATED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CradleStyleConicalMachineSettingsGenerated.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def blank_offset(self) -> 'float':
        """float: 'BlankOffset' is the original name of this property."""

        temp = self.wrapped.BlankOffset
        return temp

    @blank_offset.setter
    def blank_offset(self, value: 'float'):
        self.wrapped.BlankOffset = float(value) if value else 0.0

    @property
    def cradle_angle(self) -> 'float':
        """float: 'CradleAngle' is the original name of this property."""

        temp = self.wrapped.CradleAngle
        return temp

    @cradle_angle.setter
    def cradle_angle(self, value: 'float'):
        self.wrapped.CradleAngle = float(value) if value else 0.0

    @property
    def cutter_spindle_rotation_angle(self) -> 'float':
        """float: 'CutterSpindleRotationAngle' is the original name of this property."""

        temp = self.wrapped.CutterSpindleRotationAngle
        return temp

    @cutter_spindle_rotation_angle.setter
    def cutter_spindle_rotation_angle(self, value: 'float'):
        self.wrapped.CutterSpindleRotationAngle = float(value) if value else 0.0

    @property
    def decimal_ratio(self) -> 'float':
        """float: 'DecimalRatio' is the original name of this property."""

        temp = self.wrapped.DecimalRatio
        return temp

    @decimal_ratio.setter
    def decimal_ratio(self, value: 'float'):
        self.wrapped.DecimalRatio = float(value) if value else 0.0

    @property
    def eccentric_angle(self) -> 'float':
        """float: 'EccentricAngle' is the original name of this property."""

        temp = self.wrapped.EccentricAngle
        return temp

    @eccentric_angle.setter
    def eccentric_angle(self, value: 'float'):
        self.wrapped.EccentricAngle = float(value) if value else 0.0

    @property
    def machine_centre_to_back(self) -> 'float':
        """float: 'MachineCentreToBack' is the original name of this property."""

        temp = self.wrapped.MachineCentreToBack
        return temp

    @machine_centre_to_back.setter
    def machine_centre_to_back(self, value: 'float'):
        self.wrapped.MachineCentreToBack = float(value) if value else 0.0

    @property
    def machine_root_angle(self) -> 'float':
        """float: 'MachineRootAngle' is the original name of this property."""

        temp = self.wrapped.MachineRootAngle
        return temp

    @machine_root_angle.setter
    def machine_root_angle(self, value: 'float'):
        self.wrapped.MachineRootAngle = float(value) if value else 0.0

    @property
    def modified_roll_coefficient_c(self) -> 'float':
        """float: 'ModifiedRollCoefficientC' is the original name of this property."""

        temp = self.wrapped.ModifiedRollCoefficientC
        return temp

    @modified_roll_coefficient_c.setter
    def modified_roll_coefficient_c(self, value: 'float'):
        self.wrapped.ModifiedRollCoefficientC = float(value) if value else 0.0

    @property
    def modified_roll_coefficient_d(self) -> 'float':
        """float: 'ModifiedRollCoefficientD' is the original name of this property."""

        temp = self.wrapped.ModifiedRollCoefficientD
        return temp

    @modified_roll_coefficient_d.setter
    def modified_roll_coefficient_d(self, value: 'float'):
        self.wrapped.ModifiedRollCoefficientD = float(value) if value else 0.0

    @property
    def sliding_base(self) -> 'float':
        """float: 'SlidingBase' is the original name of this property."""

        temp = self.wrapped.SlidingBase
        return temp

    @sliding_base.setter
    def sliding_base(self, value: 'float'):
        self.wrapped.SlidingBase = float(value) if value else 0.0

    @property
    def swivel_angle(self) -> 'float':
        """float: 'SwivelAngle' is the original name of this property."""

        temp = self.wrapped.SwivelAngle
        return temp

    @swivel_angle.setter
    def swivel_angle(self, value: 'float'):
        self.wrapped.SwivelAngle = float(value) if value else 0.0

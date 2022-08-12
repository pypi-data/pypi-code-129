"""_485.py

PlasticSNCurveForTheSpecifiedOperatingConditions
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.materials import _279
from mastapy.gears.materials import _594
from mastapy._internal.python_net import python_net_import

_PLASTIC_SN_CURVE_FOR_THE_SPECIFIED_OPERATING_CONDITIONS = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.PlasticVDI2736', 'PlasticSNCurveForTheSpecifiedOperatingConditions')


__docformat__ = 'restructuredtext en'
__all__ = ('PlasticSNCurveForTheSpecifiedOperatingConditions',)


class PlasticSNCurveForTheSpecifiedOperatingConditions(_594.PlasticSNCurve):
    """PlasticSNCurveForTheSpecifiedOperatingConditions

    This is a mastapy class.
    """

    TYPE = _PLASTIC_SN_CURVE_FOR_THE_SPECIFIED_OPERATING_CONDITIONS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PlasticSNCurveForTheSpecifiedOperatingConditions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def flank_temperature(self) -> 'float':
        """float: 'FlankTemperature' is the original name of this property."""

        temp = self.wrapped.FlankTemperature
        return temp

    @flank_temperature.setter
    def flank_temperature(self, value: 'float'):
        self.wrapped.FlankTemperature = float(value) if value else 0.0

    @property
    def life_cycles(self) -> 'float':
        """float: 'LifeCycles' is the original name of this property."""

        temp = self.wrapped.LifeCycles
        return temp

    @life_cycles.setter
    def life_cycles(self, value: 'float'):
        self.wrapped.LifeCycles = float(value) if value else 0.0

    @property
    def lubricant(self) -> '_279.VDI2736LubricantType':
        """VDI2736LubricantType: 'Lubricant' is the original name of this property."""

        temp = self.wrapped.Lubricant
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_279.VDI2736LubricantType)(value) if value is not None else None

    @lubricant.setter
    def lubricant(self, value: '_279.VDI2736LubricantType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.Lubricant = value

    @property
    def root_temperature(self) -> 'float':
        """float: 'RootTemperature' is the original name of this property."""

        temp = self.wrapped.RootTemperature
        return temp

    @root_temperature.setter
    def root_temperature(self, value: 'float'):
        self.wrapped.RootTemperature = float(value) if value else 0.0

"""_1260.py

MagnetMaterial
"""


from mastapy._internal import constructor
from mastapy.materials import _260
from mastapy._internal.python_net import python_net_import

_MAGNET_MATERIAL = python_net_import('SMT.MastaAPI.ElectricMachines', 'MagnetMaterial')


__docformat__ = 'restructuredtext en'
__all__ = ('MagnetMaterial',)


class MagnetMaterial(_260.Material):
    """MagnetMaterial

    This is a mastapy class.
    """

    TYPE = _MAGNET_MATERIAL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MagnetMaterial.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def electrical_resistivity(self) -> 'float':
        """float: 'ElectricalResistivity' is the original name of this property."""

        temp = self.wrapped.ElectricalResistivity
        return temp

    @electrical_resistivity.setter
    def electrical_resistivity(self, value: 'float'):
        self.wrapped.ElectricalResistivity = float(value) if value else 0.0

    @property
    def relative_permeability(self) -> 'float':
        """float: 'RelativePermeability' is the original name of this property."""

        temp = self.wrapped.RelativePermeability
        return temp

    @relative_permeability.setter
    def relative_permeability(self, value: 'float'):
        self.wrapped.RelativePermeability = float(value) if value else 0.0

    @property
    def remanence_at_20_degrees_c(self) -> 'float':
        """float: 'RemanenceAt20DegreesC' is the original name of this property."""

        temp = self.wrapped.RemanenceAt20DegreesC
        return temp

    @remanence_at_20_degrees_c.setter
    def remanence_at_20_degrees_c(self, value: 'float'):
        self.wrapped.RemanenceAt20DegreesC = float(value) if value else 0.0

    @property
    def temperature_coefficient_for_remanence(self) -> 'float':
        """float: 'TemperatureCoefficientForRemanence' is the original name of this property."""

        temp = self.wrapped.TemperatureCoefficientForRemanence
        return temp

    @temperature_coefficient_for_remanence.setter
    def temperature_coefficient_for_remanence(self, value: 'float'):
        self.wrapped.TemperatureCoefficientForRemanence = float(value) if value else 0.0

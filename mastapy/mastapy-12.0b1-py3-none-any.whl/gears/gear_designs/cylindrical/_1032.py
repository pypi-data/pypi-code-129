"""_1032.py

CylindricalPlanetGearDesign
"""


from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.geometry.two_d import _303
from mastapy.gears import _331
from mastapy.gears.gear_designs.cylindrical import _1054, _1055, _1003
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalPlanetGearDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalPlanetGearDesign',)


class CylindricalPlanetGearDesign(_1003.CylindricalGearDesign):
    """CylindricalPlanetGearDesign

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalPlanetGearDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def has_factorising_annulus(self) -> 'bool':
        """bool: 'HasFactorisingAnnulus' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HasFactorisingAnnulus
        return temp

    @property
    def has_factorising_sun(self) -> 'bool':
        """bool: 'HasFactorisingSun' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HasFactorisingSun
        return temp

    @property
    def internal_external(self) -> '_303.InternalExternalType':
        """InternalExternalType: 'InternalExternal' is the original name of this property."""

        temp = self.wrapped.InternalExternal
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_303.InternalExternalType)(value) if value is not None else None

    @internal_external.setter
    def internal_external(self, value: '_303.InternalExternalType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.InternalExternal = value

    @property
    def planetary_details(self) -> '_331.PlanetaryDetail':
        """PlanetaryDetail: 'PlanetaryDetails' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetaryDetails
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planet_assembly_indices(self) -> 'List[_1054.NamedPlanetAssemblyIndex]':
        """List[NamedPlanetAssemblyIndex]: 'PlanetAssemblyIndices' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetAssemblyIndices
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetary_sidebands_amplitude_factors(self) -> 'List[_1055.NamedPlanetSideBandAmplitudeFactor]':
        """List[NamedPlanetSideBandAmplitudeFactor]: 'PlanetarySidebandsAmplitudeFactors' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetarySidebandsAmplitudeFactors
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

"""_1031.py

CylindricalPlanetaryGearSetDesign
"""


from mastapy._internal import constructor
from mastapy.utility_gui.charts import (
    _1815, _1805, _1810, _1812
)
from mastapy._internal.cast_exception import CastException
from mastapy.math_utility import _1471
from mastapy.gears.gear_designs.cylindrical import _1019
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANETARY_GEAR_SET_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalPlanetaryGearSetDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalPlanetaryGearSetDesign',)


class CylindricalPlanetaryGearSetDesign(_1019.CylindricalGearSetDesign):
    """CylindricalPlanetaryGearSetDesign

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANETARY_GEAR_SET_DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalPlanetaryGearSetDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def equally_spaced_planets_are_assemblable(self) -> 'bool':
        """bool: 'EquallySpacedPlanetsAreAssemblable' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EquallySpacedPlanetsAreAssemblable
        return temp

    @property
    def least_mesh_angle(self) -> 'float':
        """float: 'LeastMeshAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeastMeshAngle
        return temp

    @property
    def planet_gear_phasing_chart(self) -> '_1815.TwoDChartDefinition':
        """TwoDChartDefinition: 'PlanetGearPhasingChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetGearPhasingChart
        if _1815.TwoDChartDefinition.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast planet_gear_phasing_chart to TwoDChartDefinition. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetary_sideband_fourier_series_for_rotating_planet_carrier(self) -> '_1471.FourierSeries':
        """FourierSeries: 'PlanetarySidebandFourierSeriesForRotatingPlanetCarrier' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetarySidebandFourierSeriesForRotatingPlanetCarrier
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def add_new_micro_geometry_using_planetary_duplicates(self):
        """ 'AddNewMicroGeometryUsingPlanetaryDuplicates' is the original name of this method."""

        self.wrapped.AddNewMicroGeometryUsingPlanetaryDuplicates()

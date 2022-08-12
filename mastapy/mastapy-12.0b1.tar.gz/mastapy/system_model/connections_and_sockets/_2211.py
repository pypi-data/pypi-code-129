"""_2211.py

ComponentMeasurer
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import (
    _2384, _2376, _2377, _2380,
    _2382, _2387, _2388, _2392,
    _2393, _2395, _2402, _2403,
    _2404, _2406, _2409, _2411,
    _2412, _2417, _2419
)
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model.shaft_model import _2422
from mastapy.system_model.part_model.gears import (
    _2452, _2454, _2456, _2457,
    _2458, _2460, _2462, _2464,
    _2466, _2467, _2469, _2473,
    _2475, _2477, _2479, _2482,
    _2484, _2486, _2488, _2489,
    _2490, _2492
)
from mastapy.system_model.part_model.cycloidal import _2508, _2509
from mastapy.system_model.part_model.couplings import (
    _2518, _2521, _2523, _2526,
    _2528, _2529, _2535, _2537,
    _2540, _2543, _2544, _2545,
    _2547, _2549
)
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_COMPONENT_MEASURER = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'ComponentMeasurer')


__docformat__ = 'restructuredtext en'
__all__ = ('ComponentMeasurer',)


class ComponentMeasurer(_0.APIBase):
    """ComponentMeasurer

    This is a mastapy class.
    """

    TYPE = _COMPONENT_MEASURER

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ComponentMeasurer.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def offset_of_component(self) -> 'float':
        """float: 'OffsetOfComponent' is the original name of this property."""

        temp = self.wrapped.OffsetOfComponent
        return temp

    @offset_of_component.setter
    def offset_of_component(self, value: 'float'):
        self.wrapped.OffsetOfComponent = float(value) if value else 0.0

    @property
    def component(self) -> '_2384.Component':
        """Component: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2384.Component.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to Component. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_abstract_shaft(self) -> '_2376.AbstractShaft':
        """AbstractShaft: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2376.AbstractShaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to AbstractShaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_abstract_shaft_or_housing(self) -> '_2377.AbstractShaftOrHousing':
        """AbstractShaftOrHousing: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2377.AbstractShaftOrHousing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to AbstractShaftOrHousing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_bearing(self) -> '_2380.Bearing':
        """Bearing: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2380.Bearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to Bearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_bolt(self) -> '_2382.Bolt':
        """Bolt: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2382.Bolt.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to Bolt. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_connector(self) -> '_2387.Connector':
        """Connector: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2387.Connector.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to Connector. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_datum(self) -> '_2388.Datum':
        """Datum: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2388.Datum.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to Datum. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_external_cad_model(self) -> '_2392.ExternalCADModel':
        """ExternalCADModel: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2392.ExternalCADModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to ExternalCADModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_fe_part(self) -> '_2393.FEPart':
        """FEPart: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2393.FEPart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to FEPart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_guide_dxf_model(self) -> '_2395.GuideDxfModel':
        """GuideDxfModel: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2395.GuideDxfModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to GuideDxfModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_mass_disc(self) -> '_2402.MassDisc':
        """MassDisc: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2402.MassDisc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to MassDisc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_measurement_component(self) -> '_2403.MeasurementComponent':
        """MeasurementComponent: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2403.MeasurementComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to MeasurementComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_mountable_component(self) -> '_2404.MountableComponent':
        """MountableComponent: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2404.MountableComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to MountableComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_oil_seal(self) -> '_2406.OilSeal':
        """OilSeal: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2406.OilSeal.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to OilSeal. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_planet_carrier(self) -> '_2409.PlanetCarrier':
        """PlanetCarrier: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2409.PlanetCarrier.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to PlanetCarrier. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_point_load(self) -> '_2411.PointLoad':
        """PointLoad: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2411.PointLoad.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to PointLoad. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_power_load(self) -> '_2412.PowerLoad':
        """PowerLoad: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2412.PowerLoad.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to PowerLoad. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_unbalanced_mass(self) -> '_2417.UnbalancedMass':
        """UnbalancedMass: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2417.UnbalancedMass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to UnbalancedMass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_virtual_component(self) -> '_2419.VirtualComponent':
        """VirtualComponent: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2419.VirtualComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to VirtualComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_shaft(self) -> '_2422.Shaft':
        """Shaft: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2422.Shaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to Shaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_agma_gleason_conical_gear(self) -> '_2452.AGMAGleasonConicalGear':
        """AGMAGleasonConicalGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2452.AGMAGleasonConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to AGMAGleasonConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_bevel_differential_gear(self) -> '_2454.BevelDifferentialGear':
        """BevelDifferentialGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2454.BevelDifferentialGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to BevelDifferentialGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_bevel_differential_planet_gear(self) -> '_2456.BevelDifferentialPlanetGear':
        """BevelDifferentialPlanetGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2456.BevelDifferentialPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to BevelDifferentialPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_bevel_differential_sun_gear(self) -> '_2457.BevelDifferentialSunGear':
        """BevelDifferentialSunGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2457.BevelDifferentialSunGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to BevelDifferentialSunGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_bevel_gear(self) -> '_2458.BevelGear':
        """BevelGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2458.BevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to BevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_concept_gear(self) -> '_2460.ConceptGear':
        """ConceptGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2460.ConceptGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to ConceptGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_conical_gear(self) -> '_2462.ConicalGear':
        """ConicalGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2462.ConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to ConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_cylindrical_gear(self) -> '_2464.CylindricalGear':
        """CylindricalGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2464.CylindricalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to CylindricalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_cylindrical_planet_gear(self) -> '_2466.CylindricalPlanetGear':
        """CylindricalPlanetGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2466.CylindricalPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to CylindricalPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_face_gear(self) -> '_2467.FaceGear':
        """FaceGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2467.FaceGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to FaceGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_gear(self) -> '_2469.Gear':
        """Gear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2469.Gear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to Gear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_hypoid_gear(self) -> '_2473.HypoidGear':
        """HypoidGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2473.HypoidGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to HypoidGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> '_2475.KlingelnbergCycloPalloidConicalGear':
        """KlingelnbergCycloPalloidConicalGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2475.KlingelnbergCycloPalloidConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to KlingelnbergCycloPalloidConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> '_2477.KlingelnbergCycloPalloidHypoidGear':
        """KlingelnbergCycloPalloidHypoidGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2477.KlingelnbergCycloPalloidHypoidGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to KlingelnbergCycloPalloidHypoidGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> '_2479.KlingelnbergCycloPalloidSpiralBevelGear':
        """KlingelnbergCycloPalloidSpiralBevelGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2479.KlingelnbergCycloPalloidSpiralBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to KlingelnbergCycloPalloidSpiralBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_spiral_bevel_gear(self) -> '_2482.SpiralBevelGear':
        """SpiralBevelGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2482.SpiralBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to SpiralBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_straight_bevel_diff_gear(self) -> '_2484.StraightBevelDiffGear':
        """StraightBevelDiffGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2484.StraightBevelDiffGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to StraightBevelDiffGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_straight_bevel_gear(self) -> '_2486.StraightBevelGear':
        """StraightBevelGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2486.StraightBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to StraightBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_straight_bevel_planet_gear(self) -> '_2488.StraightBevelPlanetGear':
        """StraightBevelPlanetGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2488.StraightBevelPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to StraightBevelPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_straight_bevel_sun_gear(self) -> '_2489.StraightBevelSunGear':
        """StraightBevelSunGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2489.StraightBevelSunGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to StraightBevelSunGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_worm_gear(self) -> '_2490.WormGear':
        """WormGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2490.WormGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to WormGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_zerol_bevel_gear(self) -> '_2492.ZerolBevelGear':
        """ZerolBevelGear: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2492.ZerolBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to ZerolBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_cycloidal_disc(self) -> '_2508.CycloidalDisc':
        """CycloidalDisc: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2508.CycloidalDisc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to CycloidalDisc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_ring_pins(self) -> '_2509.RingPins':
        """RingPins: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2509.RingPins.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to RingPins. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_clutch_half(self) -> '_2518.ClutchHalf':
        """ClutchHalf: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2518.ClutchHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to ClutchHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_concept_coupling_half(self) -> '_2521.ConceptCouplingHalf':
        """ConceptCouplingHalf: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2521.ConceptCouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to ConceptCouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_coupling_half(self) -> '_2523.CouplingHalf':
        """CouplingHalf: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2523.CouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to CouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_cvt_pulley(self) -> '_2526.CVTPulley':
        """CVTPulley: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2526.CVTPulley.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to CVTPulley. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_part_to_part_shear_coupling_half(self) -> '_2528.PartToPartShearCouplingHalf':
        """PartToPartShearCouplingHalf: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2528.PartToPartShearCouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to PartToPartShearCouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_pulley(self) -> '_2529.Pulley':
        """Pulley: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2529.Pulley.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to Pulley. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_rolling_ring(self) -> '_2535.RollingRing':
        """RollingRing: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2535.RollingRing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to RollingRing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_shaft_hub_connection(self) -> '_2537.ShaftHubConnection':
        """ShaftHubConnection: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2537.ShaftHubConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to ShaftHubConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_spring_damper_half(self) -> '_2540.SpringDamperHalf':
        """SpringDamperHalf: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2540.SpringDamperHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to SpringDamperHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_synchroniser_half(self) -> '_2543.SynchroniserHalf':
        """SynchroniserHalf: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2543.SynchroniserHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to SynchroniserHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_synchroniser_part(self) -> '_2544.SynchroniserPart':
        """SynchroniserPart: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2544.SynchroniserPart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to SynchroniserPart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_synchroniser_sleeve(self) -> '_2545.SynchroniserSleeve':
        """SynchroniserSleeve: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2545.SynchroniserSleeve.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to SynchroniserSleeve. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_torque_converter_pump(self) -> '_2547.TorqueConverterPump':
        """TorqueConverterPump: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2547.TorqueConverterPump.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to TorqueConverterPump. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_of_type_torque_converter_turbine(self) -> '_2549.TorqueConverterTurbine':
        """TorqueConverterTurbine: 'Component' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Component
        if _2549.TorqueConverterTurbine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component to TorqueConverterTurbine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames
        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result

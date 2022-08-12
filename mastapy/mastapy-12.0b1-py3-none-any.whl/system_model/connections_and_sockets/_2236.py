"""_2236.py

Socket
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import (
    _2384, _2376, _2377, _2380,
    _2382, _2387, _2388, _2392,
    _2393, _2395, _2402, _2403,
    _2404, _2406, _2409, _2411,
    _2412, _2417, _2419, _2385
)
from mastapy.system_model.connections_and_sockets import _2212
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
from mastapy._internal.python_net import python_net_import
from mastapy import _0

_SOCKET = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets', 'Socket')
_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Component')


__docformat__ = 'restructuredtext en'
__all__ = ('Socket',)


class Socket(_0.APIBase):
    """Socket

    This is a mastapy class.
    """

    TYPE = _SOCKET

    __hash__ = None

    def __init__(self, instance_to_wrap: 'Socket.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name
        return temp

    @property
    def connected_components(self) -> 'List[_2384.Component]':
        """List[Component]: 'ConnectedComponents' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectedComponents
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connections(self) -> 'List[_2212.Connection]':
        """List[Connection]: 'Connections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connections
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def owner(self) -> '_2384.Component':
        """Component: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2384.Component.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to Component. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_abstract_shaft(self) -> '_2376.AbstractShaft':
        """AbstractShaft: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2376.AbstractShaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to AbstractShaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_abstract_shaft_or_housing(self) -> '_2377.AbstractShaftOrHousing':
        """AbstractShaftOrHousing: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2377.AbstractShaftOrHousing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to AbstractShaftOrHousing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_bearing(self) -> '_2380.Bearing':
        """Bearing: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2380.Bearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to Bearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_bolt(self) -> '_2382.Bolt':
        """Bolt: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2382.Bolt.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to Bolt. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_connector(self) -> '_2387.Connector':
        """Connector: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2387.Connector.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to Connector. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_datum(self) -> '_2388.Datum':
        """Datum: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2388.Datum.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to Datum. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_external_cad_model(self) -> '_2392.ExternalCADModel':
        """ExternalCADModel: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2392.ExternalCADModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to ExternalCADModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_fe_part(self) -> '_2393.FEPart':
        """FEPart: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2393.FEPart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to FEPart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_guide_dxf_model(self) -> '_2395.GuideDxfModel':
        """GuideDxfModel: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2395.GuideDxfModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to GuideDxfModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_mass_disc(self) -> '_2402.MassDisc':
        """MassDisc: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2402.MassDisc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to MassDisc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_measurement_component(self) -> '_2403.MeasurementComponent':
        """MeasurementComponent: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2403.MeasurementComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to MeasurementComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_mountable_component(self) -> '_2404.MountableComponent':
        """MountableComponent: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2404.MountableComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to MountableComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_oil_seal(self) -> '_2406.OilSeal':
        """OilSeal: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2406.OilSeal.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to OilSeal. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_planet_carrier(self) -> '_2409.PlanetCarrier':
        """PlanetCarrier: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2409.PlanetCarrier.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to PlanetCarrier. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_point_load(self) -> '_2411.PointLoad':
        """PointLoad: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2411.PointLoad.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to PointLoad. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_power_load(self) -> '_2412.PowerLoad':
        """PowerLoad: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2412.PowerLoad.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to PowerLoad. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_unbalanced_mass(self) -> '_2417.UnbalancedMass':
        """UnbalancedMass: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2417.UnbalancedMass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to UnbalancedMass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_virtual_component(self) -> '_2419.VirtualComponent':
        """VirtualComponent: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2419.VirtualComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to VirtualComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_shaft(self) -> '_2422.Shaft':
        """Shaft: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2422.Shaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to Shaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_agma_gleason_conical_gear(self) -> '_2452.AGMAGleasonConicalGear':
        """AGMAGleasonConicalGear: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2452.AGMAGleasonConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to AGMAGleasonConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_bevel_differential_gear(self) -> '_2454.BevelDifferentialGear':
        """BevelDifferentialGear: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2454.BevelDifferentialGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to BevelDifferentialGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_bevel_differential_planet_gear(self) -> '_2456.BevelDifferentialPlanetGear':
        """BevelDifferentialPlanetGear: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2456.BevelDifferentialPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to BevelDifferentialPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_bevel_differential_sun_gear(self) -> '_2457.BevelDifferentialSunGear':
        """BevelDifferentialSunGear: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2457.BevelDifferentialSunGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to BevelDifferentialSunGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_bevel_gear(self) -> '_2458.BevelGear':
        """BevelGear: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2458.BevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to BevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_concept_gear(self) -> '_2460.ConceptGear':
        """ConceptGear: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2460.ConceptGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to ConceptGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_conical_gear(self) -> '_2462.ConicalGear':
        """ConicalGear: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2462.ConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to ConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_cylindrical_gear(self) -> '_2464.CylindricalGear':
        """CylindricalGear: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2464.CylindricalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to CylindricalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_cylindrical_planet_gear(self) -> '_2466.CylindricalPlanetGear':
        """CylindricalPlanetGear: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2466.CylindricalPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to CylindricalPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_face_gear(self) -> '_2467.FaceGear':
        """FaceGear: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2467.FaceGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to FaceGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_gear(self) -> '_2469.Gear':
        """Gear: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2469.Gear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to Gear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_hypoid_gear(self) -> '_2473.HypoidGear':
        """HypoidGear: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2473.HypoidGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to HypoidGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> '_2475.KlingelnbergCycloPalloidConicalGear':
        """KlingelnbergCycloPalloidConicalGear: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2475.KlingelnbergCycloPalloidConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to KlingelnbergCycloPalloidConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> '_2477.KlingelnbergCycloPalloidHypoidGear':
        """KlingelnbergCycloPalloidHypoidGear: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2477.KlingelnbergCycloPalloidHypoidGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to KlingelnbergCycloPalloidHypoidGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> '_2479.KlingelnbergCycloPalloidSpiralBevelGear':
        """KlingelnbergCycloPalloidSpiralBevelGear: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2479.KlingelnbergCycloPalloidSpiralBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to KlingelnbergCycloPalloidSpiralBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_spiral_bevel_gear(self) -> '_2482.SpiralBevelGear':
        """SpiralBevelGear: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2482.SpiralBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to SpiralBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_straight_bevel_diff_gear(self) -> '_2484.StraightBevelDiffGear':
        """StraightBevelDiffGear: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2484.StraightBevelDiffGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to StraightBevelDiffGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_straight_bevel_gear(self) -> '_2486.StraightBevelGear':
        """StraightBevelGear: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2486.StraightBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to StraightBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_straight_bevel_planet_gear(self) -> '_2488.StraightBevelPlanetGear':
        """StraightBevelPlanetGear: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2488.StraightBevelPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to StraightBevelPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_straight_bevel_sun_gear(self) -> '_2489.StraightBevelSunGear':
        """StraightBevelSunGear: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2489.StraightBevelSunGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to StraightBevelSunGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_worm_gear(self) -> '_2490.WormGear':
        """WormGear: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2490.WormGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to WormGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_zerol_bevel_gear(self) -> '_2492.ZerolBevelGear':
        """ZerolBevelGear: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2492.ZerolBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to ZerolBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_cycloidal_disc(self) -> '_2508.CycloidalDisc':
        """CycloidalDisc: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2508.CycloidalDisc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to CycloidalDisc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_ring_pins(self) -> '_2509.RingPins':
        """RingPins: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2509.RingPins.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to RingPins. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_clutch_half(self) -> '_2518.ClutchHalf':
        """ClutchHalf: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2518.ClutchHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to ClutchHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_concept_coupling_half(self) -> '_2521.ConceptCouplingHalf':
        """ConceptCouplingHalf: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2521.ConceptCouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to ConceptCouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_coupling_half(self) -> '_2523.CouplingHalf':
        """CouplingHalf: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2523.CouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to CouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_cvt_pulley(self) -> '_2526.CVTPulley':
        """CVTPulley: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2526.CVTPulley.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to CVTPulley. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_part_to_part_shear_coupling_half(self) -> '_2528.PartToPartShearCouplingHalf':
        """PartToPartShearCouplingHalf: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2528.PartToPartShearCouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to PartToPartShearCouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_pulley(self) -> '_2529.Pulley':
        """Pulley: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2529.Pulley.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to Pulley. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_rolling_ring(self) -> '_2535.RollingRing':
        """RollingRing: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2535.RollingRing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to RollingRing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_shaft_hub_connection(self) -> '_2537.ShaftHubConnection':
        """ShaftHubConnection: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2537.ShaftHubConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to ShaftHubConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_spring_damper_half(self) -> '_2540.SpringDamperHalf':
        """SpringDamperHalf: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2540.SpringDamperHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to SpringDamperHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_synchroniser_half(self) -> '_2543.SynchroniserHalf':
        """SynchroniserHalf: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2543.SynchroniserHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to SynchroniserHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_synchroniser_part(self) -> '_2544.SynchroniserPart':
        """SynchroniserPart: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2544.SynchroniserPart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to SynchroniserPart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_synchroniser_sleeve(self) -> '_2545.SynchroniserSleeve':
        """SynchroniserSleeve: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2545.SynchroniserSleeve.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to SynchroniserSleeve. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_torque_converter_pump(self) -> '_2547.TorqueConverterPump':
        """TorqueConverterPump: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2547.TorqueConverterPump.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to TorqueConverterPump. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def owner_of_type_torque_converter_turbine(self) -> '_2549.TorqueConverterTurbine':
        """TorqueConverterTurbine: 'Owner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Owner
        if _2549.TorqueConverterTurbine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast owner to TorqueConverterTurbine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def connect_to_socket(self, socket: 'Socket') -> '_2385.ComponentsConnectedResult':
        """ 'ConnectTo' is the original name of this method.

        Args:
            socket (mastapy.system_model.connections_and_sockets.Socket)

        Returns:
            mastapy.system_model.part_model.ComponentsConnectedResult
        """

        method_result = self.wrapped.ConnectTo.Overloads[_SOCKET](socket.wrapped if socket else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def connect_to(self, component: '_2384.Component') -> '_2385.ComponentsConnectedResult':
        """ 'ConnectTo' is the original name of this method.

        Args:
            component (mastapy.system_model.part_model.Component)

        Returns:
            mastapy.system_model.part_model.ComponentsConnectedResult
        """

        method_result = self.wrapped.ConnectTo.Overloads[_COMPONENT](component.wrapped if component else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def connection_to(self, socket: 'Socket') -> '_2212.Connection':
        """ 'ConnectionTo' is the original name of this method.

        Args:
            socket (mastapy.system_model.connections_and_sockets.Socket)

        Returns:
            mastapy.system_model.connections_and_sockets.Connection
        """

        method_result = self.wrapped.ConnectionTo(socket.wrapped if socket else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def get_possible_sockets_to_connect_to(self, component_to_connect_to: '_2384.Component') -> 'List[Socket]':
        """ 'GetPossibleSocketsToConnectTo' is the original name of this method.

        Args:
            component_to_connect_to (mastapy.system_model.part_model.Component)

        Returns:
            List[mastapy.system_model.connections_and_sockets.Socket]
        """

        return conversion.pn_to_mp_objects_in_list(self.wrapped.GetPossibleSocketsToConnectTo(component_to_connect_to.wrapped if component_to_connect_to else None))

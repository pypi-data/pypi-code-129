"""_2386.py

ConnectedSockets
"""


from mastapy.system_model.connections_and_sockets import (
    _2212, _2205, _2208, _2209,
    _2213, _2221, _2227, _2232,
    _2235, _2236, _2206, _2207,
    _2214, _2216, _2218, _2219,
    _2220, _2222, _2223, _2224,
    _2225, _2226, _2228, _2229,
    _2230, _2233, _2234
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.connections_and_sockets.gears import (
    _2239, _2241, _2243, _2245,
    _2247, _2249, _2251, _2253,
    _2255, _2258, _2259, _2260,
    _2263, _2265, _2267, _2269,
    _2271, _2240, _2242, _2244,
    _2246, _2248, _2250, _2252,
    _2254, _2256, _2257, _2261,
    _2262, _2264, _2266, _2268,
    _2270, _2272
)
from mastapy.system_model.connections_and_sockets.cycloidal import (
    _2275, _2278, _2281, _2273,
    _2274, _2276, _2277, _2279,
    _2280
)
from mastapy.system_model.connections_and_sockets.couplings import (
    _2282, _2284, _2286, _2288,
    _2290, _2292, _2283, _2285,
    _2287, _2289, _2291, _2293,
    _2294
)
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_CONNECTED_SOCKETS = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'ConnectedSockets')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectedSockets',)


class ConnectedSockets(_0.APIBase):
    """ConnectedSockets

    This is a mastapy class.
    """

    TYPE = _CONNECTED_SOCKETS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConnectedSockets.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection(self) -> '_2212.Connection':
        """Connection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2212.Connection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to Connection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_abstract_shaft_to_mountable_component_connection(self) -> '_2205.AbstractShaftToMountableComponentConnection':
        """AbstractShaftToMountableComponentConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2205.AbstractShaftToMountableComponentConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to AbstractShaftToMountableComponentConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_belt_connection(self) -> '_2208.BeltConnection':
        """BeltConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2208.BeltConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to BeltConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_coaxial_connection(self) -> '_2209.CoaxialConnection':
        """CoaxialConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2209.CoaxialConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to CoaxialConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_cvt_belt_connection(self) -> '_2213.CVTBeltConnection':
        """CVTBeltConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2213.CVTBeltConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to CVTBeltConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_inter_mountable_component_connection(self) -> '_2221.InterMountableComponentConnection':
        """InterMountableComponentConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2221.InterMountableComponentConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to InterMountableComponentConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_planetary_connection(self) -> '_2227.PlanetaryConnection':
        """PlanetaryConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2227.PlanetaryConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to PlanetaryConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_rolling_ring_connection(self) -> '_2232.RollingRingConnection':
        """RollingRingConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2232.RollingRingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to RollingRingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_shaft_to_mountable_component_connection(self) -> '_2235.ShaftToMountableComponentConnection':
        """ShaftToMountableComponentConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2235.ShaftToMountableComponentConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to ShaftToMountableComponentConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_agma_gleason_conical_gear_mesh(self) -> '_2239.AGMAGleasonConicalGearMesh':
        """AGMAGleasonConicalGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2239.AGMAGleasonConicalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to AGMAGleasonConicalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_bevel_differential_gear_mesh(self) -> '_2241.BevelDifferentialGearMesh':
        """BevelDifferentialGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2241.BevelDifferentialGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to BevelDifferentialGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_bevel_gear_mesh(self) -> '_2243.BevelGearMesh':
        """BevelGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2243.BevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to BevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_concept_gear_mesh(self) -> '_2245.ConceptGearMesh':
        """ConceptGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2245.ConceptGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to ConceptGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_conical_gear_mesh(self) -> '_2247.ConicalGearMesh':
        """ConicalGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2247.ConicalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to ConicalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_cylindrical_gear_mesh(self) -> '_2249.CylindricalGearMesh':
        """CylindricalGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2249.CylindricalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to CylindricalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_face_gear_mesh(self) -> '_2251.FaceGearMesh':
        """FaceGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2251.FaceGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to FaceGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_gear_mesh(self) -> '_2253.GearMesh':
        """GearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2253.GearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to GearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_hypoid_gear_mesh(self) -> '_2255.HypoidGearMesh':
        """HypoidGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2255.HypoidGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to HypoidGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_klingelnberg_cyclo_palloid_conical_gear_mesh(self) -> '_2258.KlingelnbergCycloPalloidConicalGearMesh':
        """KlingelnbergCycloPalloidConicalGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2258.KlingelnbergCycloPalloidConicalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to KlingelnbergCycloPalloidConicalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self) -> '_2259.KlingelnbergCycloPalloidHypoidGearMesh':
        """KlingelnbergCycloPalloidHypoidGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2259.KlingelnbergCycloPalloidHypoidGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to KlingelnbergCycloPalloidHypoidGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self) -> '_2260.KlingelnbergCycloPalloidSpiralBevelGearMesh':
        """KlingelnbergCycloPalloidSpiralBevelGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2260.KlingelnbergCycloPalloidSpiralBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to KlingelnbergCycloPalloidSpiralBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_spiral_bevel_gear_mesh(self) -> '_2263.SpiralBevelGearMesh':
        """SpiralBevelGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2263.SpiralBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to SpiralBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_straight_bevel_diff_gear_mesh(self) -> '_2265.StraightBevelDiffGearMesh':
        """StraightBevelDiffGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2265.StraightBevelDiffGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to StraightBevelDiffGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_straight_bevel_gear_mesh(self) -> '_2267.StraightBevelGearMesh':
        """StraightBevelGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2267.StraightBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to StraightBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_worm_gear_mesh(self) -> '_2269.WormGearMesh':
        """WormGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2269.WormGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to WormGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_zerol_bevel_gear_mesh(self) -> '_2271.ZerolBevelGearMesh':
        """ZerolBevelGearMesh: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2271.ZerolBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to ZerolBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_cycloidal_disc_central_bearing_connection(self) -> '_2275.CycloidalDiscCentralBearingConnection':
        """CycloidalDiscCentralBearingConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2275.CycloidalDiscCentralBearingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to CycloidalDiscCentralBearingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_cycloidal_disc_planetary_bearing_connection(self) -> '_2278.CycloidalDiscPlanetaryBearingConnection':
        """CycloidalDiscPlanetaryBearingConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2278.CycloidalDiscPlanetaryBearingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to CycloidalDiscPlanetaryBearingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_ring_pins_to_disc_connection(self) -> '_2281.RingPinsToDiscConnection':
        """RingPinsToDiscConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2281.RingPinsToDiscConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to RingPinsToDiscConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_clutch_connection(self) -> '_2282.ClutchConnection':
        """ClutchConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2282.ClutchConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to ClutchConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_concept_coupling_connection(self) -> '_2284.ConceptCouplingConnection':
        """ConceptCouplingConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2284.ConceptCouplingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to ConceptCouplingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_coupling_connection(self) -> '_2286.CouplingConnection':
        """CouplingConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2286.CouplingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to CouplingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_part_to_part_shear_coupling_connection(self) -> '_2288.PartToPartShearCouplingConnection':
        """PartToPartShearCouplingConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2288.PartToPartShearCouplingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to PartToPartShearCouplingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_spring_damper_connection(self) -> '_2290.SpringDamperConnection':
        """SpringDamperConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2290.SpringDamperConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to SpringDamperConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_of_type_torque_converter_connection(self) -> '_2292.TorqueConverterConnection':
        """TorqueConverterConnection: 'Connection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Connection
        if _2292.TorqueConverterConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection to TorqueConverterConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a(self) -> '_2236.Socket':
        """Socket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2236.Socket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to Socket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_bearing_inner_socket(self) -> '_2206.BearingInnerSocket':
        """BearingInnerSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2206.BearingInnerSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to BearingInnerSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_bearing_outer_socket(self) -> '_2207.BearingOuterSocket':
        """BearingOuterSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2207.BearingOuterSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to BearingOuterSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_cvt_pulley_socket(self) -> '_2214.CVTPulleySocket':
        """CVTPulleySocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2214.CVTPulleySocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CVTPulleySocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_cylindrical_socket(self) -> '_2216.CylindricalSocket':
        """CylindricalSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2216.CylindricalSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CylindricalSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_electric_machine_stator_socket(self) -> '_2218.ElectricMachineStatorSocket':
        """ElectricMachineStatorSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2218.ElectricMachineStatorSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ElectricMachineStatorSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_inner_shaft_socket(self) -> '_2219.InnerShaftSocket':
        """InnerShaftSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2219.InnerShaftSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to InnerShaftSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_inner_shaft_socket_base(self) -> '_2220.InnerShaftSocketBase':
        """InnerShaftSocketBase: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2220.InnerShaftSocketBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to InnerShaftSocketBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_mountable_component_inner_socket(self) -> '_2222.MountableComponentInnerSocket':
        """MountableComponentInnerSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2222.MountableComponentInnerSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to MountableComponentInnerSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_mountable_component_outer_socket(self) -> '_2223.MountableComponentOuterSocket':
        """MountableComponentOuterSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2223.MountableComponentOuterSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to MountableComponentOuterSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_mountable_component_socket(self) -> '_2224.MountableComponentSocket':
        """MountableComponentSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2224.MountableComponentSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to MountableComponentSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_outer_shaft_socket(self) -> '_2225.OuterShaftSocket':
        """OuterShaftSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2225.OuterShaftSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to OuterShaftSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_outer_shaft_socket_base(self) -> '_2226.OuterShaftSocketBase':
        """OuterShaftSocketBase: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2226.OuterShaftSocketBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to OuterShaftSocketBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_planetary_socket(self) -> '_2228.PlanetarySocket':
        """PlanetarySocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2228.PlanetarySocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to PlanetarySocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_planetary_socket_base(self) -> '_2229.PlanetarySocketBase':
        """PlanetarySocketBase: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2229.PlanetarySocketBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to PlanetarySocketBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_pulley_socket(self) -> '_2230.PulleySocket':
        """PulleySocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2230.PulleySocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to PulleySocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_rolling_ring_socket(self) -> '_2233.RollingRingSocket':
        """RollingRingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2233.RollingRingSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to RollingRingSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_shaft_socket(self) -> '_2234.ShaftSocket':
        """ShaftSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2234.ShaftSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ShaftSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_agma_gleason_conical_gear_teeth_socket(self) -> '_2240.AGMAGleasonConicalGearTeethSocket':
        """AGMAGleasonConicalGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2240.AGMAGleasonConicalGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to AGMAGleasonConicalGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_bevel_differential_gear_teeth_socket(self) -> '_2242.BevelDifferentialGearTeethSocket':
        """BevelDifferentialGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2242.BevelDifferentialGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to BevelDifferentialGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_bevel_gear_teeth_socket(self) -> '_2244.BevelGearTeethSocket':
        """BevelGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2244.BevelGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to BevelGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_concept_gear_teeth_socket(self) -> '_2246.ConceptGearTeethSocket':
        """ConceptGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2246.ConceptGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ConceptGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_conical_gear_teeth_socket(self) -> '_2248.ConicalGearTeethSocket':
        """ConicalGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2248.ConicalGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ConicalGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_cylindrical_gear_teeth_socket(self) -> '_2250.CylindricalGearTeethSocket':
        """CylindricalGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2250.CylindricalGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CylindricalGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_face_gear_teeth_socket(self) -> '_2252.FaceGearTeethSocket':
        """FaceGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2252.FaceGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to FaceGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_gear_teeth_socket(self) -> '_2254.GearTeethSocket':
        """GearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2254.GearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to GearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_hypoid_gear_teeth_socket(self) -> '_2256.HypoidGearTeethSocket':
        """HypoidGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2256.HypoidGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to HypoidGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_klingelnberg_conical_gear_teeth_socket(self) -> '_2257.KlingelnbergConicalGearTeethSocket':
        """KlingelnbergConicalGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2257.KlingelnbergConicalGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to KlingelnbergConicalGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_klingelnberg_hypoid_gear_teeth_socket(self) -> '_2261.KlingelnbergHypoidGearTeethSocket':
        """KlingelnbergHypoidGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2261.KlingelnbergHypoidGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to KlingelnbergHypoidGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_klingelnberg_spiral_bevel_gear_teeth_socket(self) -> '_2262.KlingelnbergSpiralBevelGearTeethSocket':
        """KlingelnbergSpiralBevelGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2262.KlingelnbergSpiralBevelGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to KlingelnbergSpiralBevelGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_spiral_bevel_gear_teeth_socket(self) -> '_2264.SpiralBevelGearTeethSocket':
        """SpiralBevelGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2264.SpiralBevelGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to SpiralBevelGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_straight_bevel_diff_gear_teeth_socket(self) -> '_2266.StraightBevelDiffGearTeethSocket':
        """StraightBevelDiffGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2266.StraightBevelDiffGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to StraightBevelDiffGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_straight_bevel_gear_teeth_socket(self) -> '_2268.StraightBevelGearTeethSocket':
        """StraightBevelGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2268.StraightBevelGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to StraightBevelGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_worm_gear_teeth_socket(self) -> '_2270.WormGearTeethSocket':
        """WormGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2270.WormGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to WormGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_zerol_bevel_gear_teeth_socket(self) -> '_2272.ZerolBevelGearTeethSocket':
        """ZerolBevelGearTeethSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2272.ZerolBevelGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ZerolBevelGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_cycloidal_disc_axial_left_socket(self) -> '_2273.CycloidalDiscAxialLeftSocket':
        """CycloidalDiscAxialLeftSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2273.CycloidalDiscAxialLeftSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CycloidalDiscAxialLeftSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_cycloidal_disc_axial_right_socket(self) -> '_2274.CycloidalDiscAxialRightSocket':
        """CycloidalDiscAxialRightSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2274.CycloidalDiscAxialRightSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CycloidalDiscAxialRightSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_cycloidal_disc_inner_socket(self) -> '_2276.CycloidalDiscInnerSocket':
        """CycloidalDiscInnerSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2276.CycloidalDiscInnerSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CycloidalDiscInnerSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_cycloidal_disc_outer_socket(self) -> '_2277.CycloidalDiscOuterSocket':
        """CycloidalDiscOuterSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2277.CycloidalDiscOuterSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CycloidalDiscOuterSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_cycloidal_disc_planetary_bearing_socket(self) -> '_2279.CycloidalDiscPlanetaryBearingSocket':
        """CycloidalDiscPlanetaryBearingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2279.CycloidalDiscPlanetaryBearingSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CycloidalDiscPlanetaryBearingSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_ring_pins_socket(self) -> '_2280.RingPinsSocket':
        """RingPinsSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2280.RingPinsSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to RingPinsSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_clutch_socket(self) -> '_2283.ClutchSocket':
        """ClutchSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2283.ClutchSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ClutchSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_concept_coupling_socket(self) -> '_2285.ConceptCouplingSocket':
        """ConceptCouplingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2285.ConceptCouplingSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to ConceptCouplingSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_coupling_socket(self) -> '_2287.CouplingSocket':
        """CouplingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2287.CouplingSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to CouplingSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_part_to_part_shear_coupling_socket(self) -> '_2289.PartToPartShearCouplingSocket':
        """PartToPartShearCouplingSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2289.PartToPartShearCouplingSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to PartToPartShearCouplingSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_spring_damper_socket(self) -> '_2291.SpringDamperSocket':
        """SpringDamperSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2291.SpringDamperSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to SpringDamperSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_torque_converter_pump_socket(self) -> '_2293.TorqueConverterPumpSocket':
        """TorqueConverterPumpSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2293.TorqueConverterPumpSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to TorqueConverterPumpSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_a_of_type_torque_converter_turbine_socket(self) -> '_2294.TorqueConverterTurbineSocket':
        """TorqueConverterTurbineSocket: 'SocketA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketA
        if _2294.TorqueConverterTurbineSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_a to TorqueConverterTurbineSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b(self) -> '_2236.Socket':
        """Socket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2236.Socket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to Socket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_bearing_inner_socket(self) -> '_2206.BearingInnerSocket':
        """BearingInnerSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2206.BearingInnerSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to BearingInnerSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_bearing_outer_socket(self) -> '_2207.BearingOuterSocket':
        """BearingOuterSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2207.BearingOuterSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to BearingOuterSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_cvt_pulley_socket(self) -> '_2214.CVTPulleySocket':
        """CVTPulleySocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2214.CVTPulleySocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CVTPulleySocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_cylindrical_socket(self) -> '_2216.CylindricalSocket':
        """CylindricalSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2216.CylindricalSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CylindricalSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_electric_machine_stator_socket(self) -> '_2218.ElectricMachineStatorSocket':
        """ElectricMachineStatorSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2218.ElectricMachineStatorSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ElectricMachineStatorSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_inner_shaft_socket(self) -> '_2219.InnerShaftSocket':
        """InnerShaftSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2219.InnerShaftSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to InnerShaftSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_inner_shaft_socket_base(self) -> '_2220.InnerShaftSocketBase':
        """InnerShaftSocketBase: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2220.InnerShaftSocketBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to InnerShaftSocketBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_mountable_component_inner_socket(self) -> '_2222.MountableComponentInnerSocket':
        """MountableComponentInnerSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2222.MountableComponentInnerSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to MountableComponentInnerSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_mountable_component_outer_socket(self) -> '_2223.MountableComponentOuterSocket':
        """MountableComponentOuterSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2223.MountableComponentOuterSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to MountableComponentOuterSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_mountable_component_socket(self) -> '_2224.MountableComponentSocket':
        """MountableComponentSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2224.MountableComponentSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to MountableComponentSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_outer_shaft_socket(self) -> '_2225.OuterShaftSocket':
        """OuterShaftSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2225.OuterShaftSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to OuterShaftSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_outer_shaft_socket_base(self) -> '_2226.OuterShaftSocketBase':
        """OuterShaftSocketBase: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2226.OuterShaftSocketBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to OuterShaftSocketBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_planetary_socket(self) -> '_2228.PlanetarySocket':
        """PlanetarySocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2228.PlanetarySocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to PlanetarySocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_planetary_socket_base(self) -> '_2229.PlanetarySocketBase':
        """PlanetarySocketBase: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2229.PlanetarySocketBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to PlanetarySocketBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_pulley_socket(self) -> '_2230.PulleySocket':
        """PulleySocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2230.PulleySocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to PulleySocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_rolling_ring_socket(self) -> '_2233.RollingRingSocket':
        """RollingRingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2233.RollingRingSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to RollingRingSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_shaft_socket(self) -> '_2234.ShaftSocket':
        """ShaftSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2234.ShaftSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ShaftSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_agma_gleason_conical_gear_teeth_socket(self) -> '_2240.AGMAGleasonConicalGearTeethSocket':
        """AGMAGleasonConicalGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2240.AGMAGleasonConicalGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to AGMAGleasonConicalGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_bevel_differential_gear_teeth_socket(self) -> '_2242.BevelDifferentialGearTeethSocket':
        """BevelDifferentialGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2242.BevelDifferentialGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to BevelDifferentialGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_bevel_gear_teeth_socket(self) -> '_2244.BevelGearTeethSocket':
        """BevelGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2244.BevelGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to BevelGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_concept_gear_teeth_socket(self) -> '_2246.ConceptGearTeethSocket':
        """ConceptGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2246.ConceptGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ConceptGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_conical_gear_teeth_socket(self) -> '_2248.ConicalGearTeethSocket':
        """ConicalGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2248.ConicalGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ConicalGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_cylindrical_gear_teeth_socket(self) -> '_2250.CylindricalGearTeethSocket':
        """CylindricalGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2250.CylindricalGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CylindricalGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_face_gear_teeth_socket(self) -> '_2252.FaceGearTeethSocket':
        """FaceGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2252.FaceGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to FaceGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_gear_teeth_socket(self) -> '_2254.GearTeethSocket':
        """GearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2254.GearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to GearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_hypoid_gear_teeth_socket(self) -> '_2256.HypoidGearTeethSocket':
        """HypoidGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2256.HypoidGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to HypoidGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_klingelnberg_conical_gear_teeth_socket(self) -> '_2257.KlingelnbergConicalGearTeethSocket':
        """KlingelnbergConicalGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2257.KlingelnbergConicalGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to KlingelnbergConicalGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_klingelnberg_hypoid_gear_teeth_socket(self) -> '_2261.KlingelnbergHypoidGearTeethSocket':
        """KlingelnbergHypoidGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2261.KlingelnbergHypoidGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to KlingelnbergHypoidGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_klingelnberg_spiral_bevel_gear_teeth_socket(self) -> '_2262.KlingelnbergSpiralBevelGearTeethSocket':
        """KlingelnbergSpiralBevelGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2262.KlingelnbergSpiralBevelGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to KlingelnbergSpiralBevelGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_spiral_bevel_gear_teeth_socket(self) -> '_2264.SpiralBevelGearTeethSocket':
        """SpiralBevelGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2264.SpiralBevelGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to SpiralBevelGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_straight_bevel_diff_gear_teeth_socket(self) -> '_2266.StraightBevelDiffGearTeethSocket':
        """StraightBevelDiffGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2266.StraightBevelDiffGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to StraightBevelDiffGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_straight_bevel_gear_teeth_socket(self) -> '_2268.StraightBevelGearTeethSocket':
        """StraightBevelGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2268.StraightBevelGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to StraightBevelGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_worm_gear_teeth_socket(self) -> '_2270.WormGearTeethSocket':
        """WormGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2270.WormGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to WormGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_zerol_bevel_gear_teeth_socket(self) -> '_2272.ZerolBevelGearTeethSocket':
        """ZerolBevelGearTeethSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2272.ZerolBevelGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ZerolBevelGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_cycloidal_disc_axial_left_socket(self) -> '_2273.CycloidalDiscAxialLeftSocket':
        """CycloidalDiscAxialLeftSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2273.CycloidalDiscAxialLeftSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CycloidalDiscAxialLeftSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_cycloidal_disc_axial_right_socket(self) -> '_2274.CycloidalDiscAxialRightSocket':
        """CycloidalDiscAxialRightSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2274.CycloidalDiscAxialRightSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CycloidalDiscAxialRightSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_cycloidal_disc_inner_socket(self) -> '_2276.CycloidalDiscInnerSocket':
        """CycloidalDiscInnerSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2276.CycloidalDiscInnerSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CycloidalDiscInnerSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_cycloidal_disc_outer_socket(self) -> '_2277.CycloidalDiscOuterSocket':
        """CycloidalDiscOuterSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2277.CycloidalDiscOuterSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CycloidalDiscOuterSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_cycloidal_disc_planetary_bearing_socket(self) -> '_2279.CycloidalDiscPlanetaryBearingSocket':
        """CycloidalDiscPlanetaryBearingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2279.CycloidalDiscPlanetaryBearingSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CycloidalDiscPlanetaryBearingSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_ring_pins_socket(self) -> '_2280.RingPinsSocket':
        """RingPinsSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2280.RingPinsSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to RingPinsSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_clutch_socket(self) -> '_2283.ClutchSocket':
        """ClutchSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2283.ClutchSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ClutchSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_concept_coupling_socket(self) -> '_2285.ConceptCouplingSocket':
        """ConceptCouplingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2285.ConceptCouplingSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to ConceptCouplingSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_coupling_socket(self) -> '_2287.CouplingSocket':
        """CouplingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2287.CouplingSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to CouplingSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_part_to_part_shear_coupling_socket(self) -> '_2289.PartToPartShearCouplingSocket':
        """PartToPartShearCouplingSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2289.PartToPartShearCouplingSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to PartToPartShearCouplingSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_spring_damper_socket(self) -> '_2291.SpringDamperSocket':
        """SpringDamperSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2291.SpringDamperSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to SpringDamperSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_torque_converter_pump_socket(self) -> '_2293.TorqueConverterPumpSocket':
        """TorqueConverterPumpSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2293.TorqueConverterPumpSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to TorqueConverterPumpSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def socket_b_of_type_torque_converter_turbine_socket(self) -> '_2294.TorqueConverterTurbineSocket':
        """TorqueConverterTurbineSocket: 'SocketB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SocketB
        if _2294.TorqueConverterTurbineSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast socket_b to TorqueConverterTurbineSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

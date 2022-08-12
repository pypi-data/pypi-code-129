"""_2404.py

MountableComponent
"""


from typing import Optional

from mastapy._internal import constructor
from mastapy.system_model.part_model import _2376, _2385, _2384
from mastapy.system_model.part_model.shaft_model import _2422
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model.cycloidal import _2508
from mastapy.system_model.connections_and_sockets import (
    _2212, _2205, _2208, _2209,
    _2213, _2221, _2227, _2232,
    _2235, _2216, _2206, _2207,
    _2214, _2219, _2220, _2222,
    _2223, _2224, _2225, _2226,
    _2228, _2229, _2230, _2233,
    _2234
)
from mastapy.system_model.connections_and_sockets.gears import (
    _2239, _2241, _2243, _2245,
    _2247, _2249, _2251, _2253,
    _2255, _2258, _2259, _2260,
    _2263, _2265, _2267, _2269,
    _2271, _2250
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
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'MountableComponent')


__docformat__ = 'restructuredtext en'
__all__ = ('MountableComponent',)


class MountableComponent(_2384.Component):
    """MountableComponent

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MountableComponent.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rotation_about_axis(self) -> 'float':
        """float: 'RotationAboutAxis' is the original name of this property."""

        temp = self.wrapped.RotationAboutAxis
        return temp

    @rotation_about_axis.setter
    def rotation_about_axis(self, value: 'float'):
        self.wrapped.RotationAboutAxis = float(value) if value else 0.0

    @property
    def inner_component(self) -> '_2376.AbstractShaft':
        """AbstractShaft: 'InnerComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerComponent
        if _2376.AbstractShaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_component to AbstractShaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_component_of_type_shaft(self) -> '_2422.Shaft':
        """Shaft: 'InnerComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerComponent
        if _2422.Shaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_component to Shaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_component_of_type_cycloidal_disc(self) -> '_2508.CycloidalDisc':
        """CycloidalDisc: 'InnerComponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerComponent
        if _2508.CycloidalDisc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_component to CycloidalDisc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection(self) -> '_2212.Connection':
        """Connection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2212.Connection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to Connection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_abstract_shaft_to_mountable_component_connection(self) -> '_2205.AbstractShaftToMountableComponentConnection':
        """AbstractShaftToMountableComponentConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2205.AbstractShaftToMountableComponentConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to AbstractShaftToMountableComponentConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_belt_connection(self) -> '_2208.BeltConnection':
        """BeltConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2208.BeltConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to BeltConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_coaxial_connection(self) -> '_2209.CoaxialConnection':
        """CoaxialConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2209.CoaxialConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to CoaxialConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_cvt_belt_connection(self) -> '_2213.CVTBeltConnection':
        """CVTBeltConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2213.CVTBeltConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to CVTBeltConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_inter_mountable_component_connection(self) -> '_2221.InterMountableComponentConnection':
        """InterMountableComponentConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2221.InterMountableComponentConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to InterMountableComponentConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_planetary_connection(self) -> '_2227.PlanetaryConnection':
        """PlanetaryConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2227.PlanetaryConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to PlanetaryConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_rolling_ring_connection(self) -> '_2232.RollingRingConnection':
        """RollingRingConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2232.RollingRingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to RollingRingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_shaft_to_mountable_component_connection(self) -> '_2235.ShaftToMountableComponentConnection':
        """ShaftToMountableComponentConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2235.ShaftToMountableComponentConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to ShaftToMountableComponentConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_agma_gleason_conical_gear_mesh(self) -> '_2239.AGMAGleasonConicalGearMesh':
        """AGMAGleasonConicalGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2239.AGMAGleasonConicalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to AGMAGleasonConicalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_bevel_differential_gear_mesh(self) -> '_2241.BevelDifferentialGearMesh':
        """BevelDifferentialGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2241.BevelDifferentialGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to BevelDifferentialGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_bevel_gear_mesh(self) -> '_2243.BevelGearMesh':
        """BevelGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2243.BevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to BevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_concept_gear_mesh(self) -> '_2245.ConceptGearMesh':
        """ConceptGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2245.ConceptGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to ConceptGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_conical_gear_mesh(self) -> '_2247.ConicalGearMesh':
        """ConicalGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2247.ConicalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to ConicalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_cylindrical_gear_mesh(self) -> '_2249.CylindricalGearMesh':
        """CylindricalGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2249.CylindricalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to CylindricalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_face_gear_mesh(self) -> '_2251.FaceGearMesh':
        """FaceGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2251.FaceGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to FaceGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_gear_mesh(self) -> '_2253.GearMesh':
        """GearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2253.GearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to GearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_hypoid_gear_mesh(self) -> '_2255.HypoidGearMesh':
        """HypoidGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2255.HypoidGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to HypoidGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_klingelnberg_cyclo_palloid_conical_gear_mesh(self) -> '_2258.KlingelnbergCycloPalloidConicalGearMesh':
        """KlingelnbergCycloPalloidConicalGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2258.KlingelnbergCycloPalloidConicalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to KlingelnbergCycloPalloidConicalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self) -> '_2259.KlingelnbergCycloPalloidHypoidGearMesh':
        """KlingelnbergCycloPalloidHypoidGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2259.KlingelnbergCycloPalloidHypoidGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to KlingelnbergCycloPalloidHypoidGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self) -> '_2260.KlingelnbergCycloPalloidSpiralBevelGearMesh':
        """KlingelnbergCycloPalloidSpiralBevelGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2260.KlingelnbergCycloPalloidSpiralBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to KlingelnbergCycloPalloidSpiralBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_spiral_bevel_gear_mesh(self) -> '_2263.SpiralBevelGearMesh':
        """SpiralBevelGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2263.SpiralBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to SpiralBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_straight_bevel_diff_gear_mesh(self) -> '_2265.StraightBevelDiffGearMesh':
        """StraightBevelDiffGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2265.StraightBevelDiffGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to StraightBevelDiffGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_straight_bevel_gear_mesh(self) -> '_2267.StraightBevelGearMesh':
        """StraightBevelGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2267.StraightBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to StraightBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_worm_gear_mesh(self) -> '_2269.WormGearMesh':
        """WormGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2269.WormGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to WormGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_zerol_bevel_gear_mesh(self) -> '_2271.ZerolBevelGearMesh':
        """ZerolBevelGearMesh: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2271.ZerolBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to ZerolBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_cycloidal_disc_central_bearing_connection(self) -> '_2275.CycloidalDiscCentralBearingConnection':
        """CycloidalDiscCentralBearingConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2275.CycloidalDiscCentralBearingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to CycloidalDiscCentralBearingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_cycloidal_disc_planetary_bearing_connection(self) -> '_2278.CycloidalDiscPlanetaryBearingConnection':
        """CycloidalDiscPlanetaryBearingConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2278.CycloidalDiscPlanetaryBearingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to CycloidalDiscPlanetaryBearingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_ring_pins_to_disc_connection(self) -> '_2281.RingPinsToDiscConnection':
        """RingPinsToDiscConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2281.RingPinsToDiscConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to RingPinsToDiscConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_clutch_connection(self) -> '_2282.ClutchConnection':
        """ClutchConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2282.ClutchConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to ClutchConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_concept_coupling_connection(self) -> '_2284.ConceptCouplingConnection':
        """ConceptCouplingConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2284.ConceptCouplingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to ConceptCouplingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_coupling_connection(self) -> '_2286.CouplingConnection':
        """CouplingConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2286.CouplingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to CouplingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_part_to_part_shear_coupling_connection(self) -> '_2288.PartToPartShearCouplingConnection':
        """PartToPartShearCouplingConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2288.PartToPartShearCouplingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to PartToPartShearCouplingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_spring_damper_connection(self) -> '_2290.SpringDamperConnection':
        """SpringDamperConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2290.SpringDamperConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to SpringDamperConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_connection_of_type_torque_converter_connection(self) -> '_2292.TorqueConverterConnection':
        """TorqueConverterConnection: 'InnerConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerConnection
        if _2292.TorqueConverterConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_connection to TorqueConverterConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket(self) -> '_2216.CylindricalSocket':
        """CylindricalSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2216.CylindricalSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to CylindricalSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_bearing_inner_socket(self) -> '_2206.BearingInnerSocket':
        """BearingInnerSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2206.BearingInnerSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to BearingInnerSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_bearing_outer_socket(self) -> '_2207.BearingOuterSocket':
        """BearingOuterSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2207.BearingOuterSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to BearingOuterSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_cvt_pulley_socket(self) -> '_2214.CVTPulleySocket':
        """CVTPulleySocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2214.CVTPulleySocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to CVTPulleySocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_inner_shaft_socket(self) -> '_2219.InnerShaftSocket':
        """InnerShaftSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2219.InnerShaftSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to InnerShaftSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_inner_shaft_socket_base(self) -> '_2220.InnerShaftSocketBase':
        """InnerShaftSocketBase: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2220.InnerShaftSocketBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to InnerShaftSocketBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_mountable_component_inner_socket(self) -> '_2222.MountableComponentInnerSocket':
        """MountableComponentInnerSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2222.MountableComponentInnerSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to MountableComponentInnerSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_mountable_component_outer_socket(self) -> '_2223.MountableComponentOuterSocket':
        """MountableComponentOuterSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2223.MountableComponentOuterSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to MountableComponentOuterSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_mountable_component_socket(self) -> '_2224.MountableComponentSocket':
        """MountableComponentSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2224.MountableComponentSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to MountableComponentSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_outer_shaft_socket(self) -> '_2225.OuterShaftSocket':
        """OuterShaftSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2225.OuterShaftSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to OuterShaftSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_outer_shaft_socket_base(self) -> '_2226.OuterShaftSocketBase':
        """OuterShaftSocketBase: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2226.OuterShaftSocketBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to OuterShaftSocketBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_planetary_socket(self) -> '_2228.PlanetarySocket':
        """PlanetarySocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2228.PlanetarySocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to PlanetarySocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_planetary_socket_base(self) -> '_2229.PlanetarySocketBase':
        """PlanetarySocketBase: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2229.PlanetarySocketBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to PlanetarySocketBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_pulley_socket(self) -> '_2230.PulleySocket':
        """PulleySocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2230.PulleySocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to PulleySocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_rolling_ring_socket(self) -> '_2233.RollingRingSocket':
        """RollingRingSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2233.RollingRingSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to RollingRingSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_shaft_socket(self) -> '_2234.ShaftSocket':
        """ShaftSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2234.ShaftSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to ShaftSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_cylindrical_gear_teeth_socket(self) -> '_2250.CylindricalGearTeethSocket':
        """CylindricalGearTeethSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2250.CylindricalGearTeethSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to CylindricalGearTeethSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_cycloidal_disc_axial_left_socket(self) -> '_2273.CycloidalDiscAxialLeftSocket':
        """CycloidalDiscAxialLeftSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2273.CycloidalDiscAxialLeftSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to CycloidalDiscAxialLeftSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_cycloidal_disc_axial_right_socket(self) -> '_2274.CycloidalDiscAxialRightSocket':
        """CycloidalDiscAxialRightSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2274.CycloidalDiscAxialRightSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to CycloidalDiscAxialRightSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_cycloidal_disc_inner_socket(self) -> '_2276.CycloidalDiscInnerSocket':
        """CycloidalDiscInnerSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2276.CycloidalDiscInnerSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to CycloidalDiscInnerSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_cycloidal_disc_outer_socket(self) -> '_2277.CycloidalDiscOuterSocket':
        """CycloidalDiscOuterSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2277.CycloidalDiscOuterSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to CycloidalDiscOuterSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_cycloidal_disc_planetary_bearing_socket(self) -> '_2279.CycloidalDiscPlanetaryBearingSocket':
        """CycloidalDiscPlanetaryBearingSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2279.CycloidalDiscPlanetaryBearingSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to CycloidalDiscPlanetaryBearingSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_ring_pins_socket(self) -> '_2280.RingPinsSocket':
        """RingPinsSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2280.RingPinsSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to RingPinsSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_clutch_socket(self) -> '_2283.ClutchSocket':
        """ClutchSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2283.ClutchSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to ClutchSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_concept_coupling_socket(self) -> '_2285.ConceptCouplingSocket':
        """ConceptCouplingSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2285.ConceptCouplingSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to ConceptCouplingSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_coupling_socket(self) -> '_2287.CouplingSocket':
        """CouplingSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2287.CouplingSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to CouplingSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_part_to_part_shear_coupling_socket(self) -> '_2289.PartToPartShearCouplingSocket':
        """PartToPartShearCouplingSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2289.PartToPartShearCouplingSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to PartToPartShearCouplingSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_spring_damper_socket(self) -> '_2291.SpringDamperSocket':
        """SpringDamperSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2291.SpringDamperSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to SpringDamperSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_torque_converter_pump_socket(self) -> '_2293.TorqueConverterPumpSocket':
        """TorqueConverterPumpSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2293.TorqueConverterPumpSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to TorqueConverterPumpSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def inner_socket_of_type_torque_converter_turbine_socket(self) -> '_2294.TorqueConverterTurbineSocket':
        """TorqueConverterTurbineSocket: 'InnerSocket' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InnerSocket
        if _2294.TorqueConverterTurbineSocket.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast inner_socket to TorqueConverterTurbineSocket. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def is_mounted(self) -> 'bool':
        """bool: 'IsMounted' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsMounted
        return temp

    def mount_on(self, shaft: '_2376.AbstractShaft', offset: Optional['float'] = float('nan')) -> '_2209.CoaxialConnection':
        """ 'MountOn' is the original name of this method.

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)

        Returns:
            mastapy.system_model.connections_and_sockets.CoaxialConnection
        """

        offset = float(offset)
        method_result = self.wrapped.MountOn(shaft.wrapped if shaft else None, offset if offset else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def try_mount_on(self, shaft: '_2376.AbstractShaft', offset: Optional['float'] = float('nan')) -> '_2385.ComponentsConnectedResult':
        """ 'TryMountOn' is the original name of this method.

        Args:
            shaft (mastapy.system_model.part_model.AbstractShaft)
            offset (float, optional)

        Returns:
            mastapy.system_model.part_model.ComponentsConnectedResult
        """

        offset = float(offset)
        method_result = self.wrapped.TryMountOn(shaft.wrapped if shaft else None, offset if offset else 0.0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

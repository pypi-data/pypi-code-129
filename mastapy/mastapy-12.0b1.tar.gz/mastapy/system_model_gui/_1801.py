"""_1801.py

MASTAGUI
"""


from typing import List, Dict

from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy.system_model import _2143, _2147
from mastapy._math.color import Color
from mastapy.utility.operation_modes import _1748
from mastapy._math.vector_3d import Vector3D
from mastapy.system_model.connections_and_sockets import (
    _2205, _2208, _2209, _2212,
    _2213, _2221, _2227, _2232,
    _2235
)
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.connections_and_sockets.gears import (
    _2239, _2241, _2243, _2245,
    _2247, _2249, _2251, _2253,
    _2255, _2258, _2259, _2260,
    _2263, _2265, _2267, _2269,
    _2271
)
from mastapy.system_model.connections_and_sockets.cycloidal import _2275, _2278, _2281
from mastapy.system_model.connections_and_sockets.couplings import (
    _2282, _2284, _2286, _2288,
    _2290, _2292
)
from mastapy.system_model.part_model import (
    _2374, _2375, _2376, _2377,
    _2380, _2382, _2383, _2384,
    _2387, _2388, _2392, _2393,
    _2394, _2395, _2402, _2403,
    _2404, _2406, _2408, _2409,
    _2411, _2412, _2414, _2416,
    _2417, _2419
)
from mastapy.system_model.part_model.shaft_model import _2422
from mastapy.system_model.part_model.gears import (
    _2452, _2453, _2454, _2455,
    _2456, _2457, _2458, _2459,
    _2460, _2461, _2462, _2463,
    _2464, _2465, _2466, _2467,
    _2468, _2469, _2471, _2473,
    _2474, _2475, _2476, _2477,
    _2478, _2479, _2480, _2481,
    _2482, _2483, _2484, _2485,
    _2486, _2487, _2488, _2489,
    _2490, _2491, _2492, _2493
)
from mastapy.system_model.part_model.cycloidal import _2507, _2508, _2509
from mastapy.system_model.part_model.couplings import (
    _2515, _2517, _2518, _2520,
    _2521, _2522, _2523, _2525,
    _2526, _2527, _2528, _2529,
    _2535, _2536, _2537, _2539,
    _2540, _2541, _2543, _2544,
    _2545, _2546, _2547, _2549
)
from mastapy.geometry.two_d import _302
from mastapy.nodal_analysis.geometry_modeller_link import (
    _154, _155, _161, _162
)
from mastapy.math_utility import _1469, _1452
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_MASTAGUI = python_net_import('SMT.MastaAPI.SystemModelGUI', 'MASTAGUI')


__docformat__ = 'restructuredtext en'
__all__ = ('MASTAGUI',)


class MASTAGUI(_0.APIBase):
    """MASTAGUI

    This is a mastapy class.
    """

    TYPE = _MASTAGUI

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MASTAGUI.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def is_initialised(self) -> 'bool':
        """bool: 'IsInitialised' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsInitialised
        return temp

    @property
    def is_paused(self) -> 'bool':
        """bool: 'IsPaused' is the original name of this property."""

        temp = self.wrapped.IsPaused
        return temp

    @is_paused.setter
    def is_paused(self, value: 'bool'):
        self.wrapped.IsPaused = bool(value) if value else False

    @property
    def is_remoting(self) -> 'bool':
        """bool: 'IsRemoting' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsRemoting
        return temp

    @property
    def active_design(self) -> '_2143.Design':
        """Design: 'ActiveDesign' is the original name of this property."""

        temp = self.wrapped.ActiveDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @active_design.setter
    def active_design(self, value: '_2143.Design'):
        value = value.wrapped if value else None
        self.wrapped.ActiveDesign = value

    @property
    def color_of_new_problem_node_group(self) -> 'Color':
        """Color: 'ColorOfNewProblemNodeGroup' is the original name of this property."""

        temp = self.wrapped.ColorOfNewProblemNodeGroup
        value = conversion.pn_to_mp_color(temp)
        return value

    @color_of_new_problem_node_group.setter
    def color_of_new_problem_node_group(self, value: 'Color'):
        value = value if value else None
        value = conversion.mp_to_pn_color(value)
        self.wrapped.ColorOfNewProblemNodeGroup = value

    @property
    def geometry_modeller_process_id(self) -> 'int':
        """int: 'GeometryModellerProcessID' is the original name of this property."""

        temp = self.wrapped.GeometryModellerProcessID
        return temp

    @geometry_modeller_process_id.setter
    def geometry_modeller_process_id(self, value: 'int'):
        self.wrapped.GeometryModellerProcessID = int(value) if value else 0

    @property
    def is_connected_to_geometry_modeller(self) -> 'bool':
        """bool: 'IsConnectedToGeometryModeller' is the original name of this property."""

        temp = self.wrapped.IsConnectedToGeometryModeller
        return temp

    @is_connected_to_geometry_modeller.setter
    def is_connected_to_geometry_modeller(self, value: 'bool'):
        self.wrapped.IsConnectedToGeometryModeller = bool(value) if value else False

    @property
    def name_of_new_problem_node_group(self) -> 'str':
        """str: 'NameOfNewProblemNodeGroup' is the original name of this property."""

        temp = self.wrapped.NameOfNewProblemNodeGroup
        return temp

    @name_of_new_problem_node_group.setter
    def name_of_new_problem_node_group(self, value: 'str'):
        self.wrapped.NameOfNewProblemNodeGroup = str(value) if value else ''

    @property
    def open_designs(self) -> 'List[_2143.Design]':
        """List[Design]: 'OpenDesigns' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OpenDesigns
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def operation_mode(self) -> '_1748.OperationMode':
        """OperationMode: 'OperationMode' is the original name of this property."""

        temp = self.wrapped.OperationMode
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1748.OperationMode)(value) if value is not None else None

    @operation_mode.setter
    def operation_mode(self, value: '_1748.OperationMode'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.OperationMode = value

    @property
    def positions_of_problem_node_group(self) -> 'List[Vector3D]':
        """List[Vector3D]: 'PositionsOfProblemNodeGroup' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PositionsOfProblemNodeGroup
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def process_id(self) -> 'int':
        """int: 'ProcessId' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProcessId
        return temp

    @property
    def restart_geometry_modeller_flag(self) -> 'bool':
        """bool: 'RestartGeometryModellerFlag' is the original name of this property."""

        temp = self.wrapped.RestartGeometryModellerFlag
        return temp

    @restart_geometry_modeller_flag.setter
    def restart_geometry_modeller_flag(self, value: 'bool'):
        self.wrapped.RestartGeometryModellerFlag = bool(value) if value else False

    @property
    def restart_geometry_modeller_save_file(self) -> 'str':
        """str: 'RestartGeometryModellerSaveFile' is the original name of this property."""

        temp = self.wrapped.RestartGeometryModellerSaveFile
        return temp

    @restart_geometry_modeller_save_file.setter
    def restart_geometry_modeller_save_file(self, value: 'str'):
        self.wrapped.RestartGeometryModellerSaveFile = str(value) if value else ''

    @property
    def selected_design_entity(self) -> '_2147.DesignEntity':
        """DesignEntity: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2147.DesignEntity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to DesignEntity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity.setter
    def selected_design_entity(self, value: '_2147.DesignEntity'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_abstract_shaft_to_mountable_component_connection(self) -> '_2205.AbstractShaftToMountableComponentConnection':
        """AbstractShaftToMountableComponentConnection: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2205.AbstractShaftToMountableComponentConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to AbstractShaftToMountableComponentConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_abstract_shaft_to_mountable_component_connection.setter
    def selected_design_entity_of_type_abstract_shaft_to_mountable_component_connection(self, value: '_2205.AbstractShaftToMountableComponentConnection'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_belt_connection(self) -> '_2208.BeltConnection':
        """BeltConnection: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2208.BeltConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to BeltConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_belt_connection.setter
    def selected_design_entity_of_type_belt_connection(self, value: '_2208.BeltConnection'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_coaxial_connection(self) -> '_2209.CoaxialConnection':
        """CoaxialConnection: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2209.CoaxialConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to CoaxialConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_coaxial_connection.setter
    def selected_design_entity_of_type_coaxial_connection(self, value: '_2209.CoaxialConnection'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_connection(self) -> '_2212.Connection':
        """Connection: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2212.Connection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to Connection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_connection.setter
    def selected_design_entity_of_type_connection(self, value: '_2212.Connection'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_cvt_belt_connection(self) -> '_2213.CVTBeltConnection':
        """CVTBeltConnection: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2213.CVTBeltConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to CVTBeltConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_cvt_belt_connection.setter
    def selected_design_entity_of_type_cvt_belt_connection(self, value: '_2213.CVTBeltConnection'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_inter_mountable_component_connection(self) -> '_2221.InterMountableComponentConnection':
        """InterMountableComponentConnection: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2221.InterMountableComponentConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to InterMountableComponentConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_inter_mountable_component_connection.setter
    def selected_design_entity_of_type_inter_mountable_component_connection(self, value: '_2221.InterMountableComponentConnection'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_planetary_connection(self) -> '_2227.PlanetaryConnection':
        """PlanetaryConnection: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2227.PlanetaryConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to PlanetaryConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_planetary_connection.setter
    def selected_design_entity_of_type_planetary_connection(self, value: '_2227.PlanetaryConnection'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_rolling_ring_connection(self) -> '_2232.RollingRingConnection':
        """RollingRingConnection: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2232.RollingRingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to RollingRingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_rolling_ring_connection.setter
    def selected_design_entity_of_type_rolling_ring_connection(self, value: '_2232.RollingRingConnection'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_shaft_to_mountable_component_connection(self) -> '_2235.ShaftToMountableComponentConnection':
        """ShaftToMountableComponentConnection: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2235.ShaftToMountableComponentConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to ShaftToMountableComponentConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_shaft_to_mountable_component_connection.setter
    def selected_design_entity_of_type_shaft_to_mountable_component_connection(self, value: '_2235.ShaftToMountableComponentConnection'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_agma_gleason_conical_gear_mesh(self) -> '_2239.AGMAGleasonConicalGearMesh':
        """AGMAGleasonConicalGearMesh: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2239.AGMAGleasonConicalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to AGMAGleasonConicalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_agma_gleason_conical_gear_mesh.setter
    def selected_design_entity_of_type_agma_gleason_conical_gear_mesh(self, value: '_2239.AGMAGleasonConicalGearMesh'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_bevel_differential_gear_mesh(self) -> '_2241.BevelDifferentialGearMesh':
        """BevelDifferentialGearMesh: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2241.BevelDifferentialGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to BevelDifferentialGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_bevel_differential_gear_mesh.setter
    def selected_design_entity_of_type_bevel_differential_gear_mesh(self, value: '_2241.BevelDifferentialGearMesh'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_bevel_gear_mesh(self) -> '_2243.BevelGearMesh':
        """BevelGearMesh: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2243.BevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to BevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_bevel_gear_mesh.setter
    def selected_design_entity_of_type_bevel_gear_mesh(self, value: '_2243.BevelGearMesh'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_concept_gear_mesh(self) -> '_2245.ConceptGearMesh':
        """ConceptGearMesh: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2245.ConceptGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to ConceptGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_concept_gear_mesh.setter
    def selected_design_entity_of_type_concept_gear_mesh(self, value: '_2245.ConceptGearMesh'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_conical_gear_mesh(self) -> '_2247.ConicalGearMesh':
        """ConicalGearMesh: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2247.ConicalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to ConicalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_conical_gear_mesh.setter
    def selected_design_entity_of_type_conical_gear_mesh(self, value: '_2247.ConicalGearMesh'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_cylindrical_gear_mesh(self) -> '_2249.CylindricalGearMesh':
        """CylindricalGearMesh: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2249.CylindricalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to CylindricalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_cylindrical_gear_mesh.setter
    def selected_design_entity_of_type_cylindrical_gear_mesh(self, value: '_2249.CylindricalGearMesh'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_face_gear_mesh(self) -> '_2251.FaceGearMesh':
        """FaceGearMesh: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2251.FaceGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to FaceGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_face_gear_mesh.setter
    def selected_design_entity_of_type_face_gear_mesh(self, value: '_2251.FaceGearMesh'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_gear_mesh(self) -> '_2253.GearMesh':
        """GearMesh: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2253.GearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to GearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_gear_mesh.setter
    def selected_design_entity_of_type_gear_mesh(self, value: '_2253.GearMesh'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_hypoid_gear_mesh(self) -> '_2255.HypoidGearMesh':
        """HypoidGearMesh: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2255.HypoidGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to HypoidGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_hypoid_gear_mesh.setter
    def selected_design_entity_of_type_hypoid_gear_mesh(self, value: '_2255.HypoidGearMesh'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_klingelnberg_cyclo_palloid_conical_gear_mesh(self) -> '_2258.KlingelnbergCycloPalloidConicalGearMesh':
        """KlingelnbergCycloPalloidConicalGearMesh: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2258.KlingelnbergCycloPalloidConicalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to KlingelnbergCycloPalloidConicalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_klingelnberg_cyclo_palloid_conical_gear_mesh.setter
    def selected_design_entity_of_type_klingelnberg_cyclo_palloid_conical_gear_mesh(self, value: '_2258.KlingelnbergCycloPalloidConicalGearMesh'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self) -> '_2259.KlingelnbergCycloPalloidHypoidGearMesh':
        """KlingelnbergCycloPalloidHypoidGearMesh: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2259.KlingelnbergCycloPalloidHypoidGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to KlingelnbergCycloPalloidHypoidGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh.setter
    def selected_design_entity_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self, value: '_2259.KlingelnbergCycloPalloidHypoidGearMesh'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self) -> '_2260.KlingelnbergCycloPalloidSpiralBevelGearMesh':
        """KlingelnbergCycloPalloidSpiralBevelGearMesh: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2260.KlingelnbergCycloPalloidSpiralBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to KlingelnbergCycloPalloidSpiralBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh.setter
    def selected_design_entity_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self, value: '_2260.KlingelnbergCycloPalloidSpiralBevelGearMesh'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_spiral_bevel_gear_mesh(self) -> '_2263.SpiralBevelGearMesh':
        """SpiralBevelGearMesh: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2263.SpiralBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to SpiralBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_spiral_bevel_gear_mesh.setter
    def selected_design_entity_of_type_spiral_bevel_gear_mesh(self, value: '_2263.SpiralBevelGearMesh'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_straight_bevel_diff_gear_mesh(self) -> '_2265.StraightBevelDiffGearMesh':
        """StraightBevelDiffGearMesh: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2265.StraightBevelDiffGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to StraightBevelDiffGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_straight_bevel_diff_gear_mesh.setter
    def selected_design_entity_of_type_straight_bevel_diff_gear_mesh(self, value: '_2265.StraightBevelDiffGearMesh'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_straight_bevel_gear_mesh(self) -> '_2267.StraightBevelGearMesh':
        """StraightBevelGearMesh: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2267.StraightBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to StraightBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_straight_bevel_gear_mesh.setter
    def selected_design_entity_of_type_straight_bevel_gear_mesh(self, value: '_2267.StraightBevelGearMesh'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_worm_gear_mesh(self) -> '_2269.WormGearMesh':
        """WormGearMesh: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2269.WormGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to WormGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_worm_gear_mesh.setter
    def selected_design_entity_of_type_worm_gear_mesh(self, value: '_2269.WormGearMesh'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_zerol_bevel_gear_mesh(self) -> '_2271.ZerolBevelGearMesh':
        """ZerolBevelGearMesh: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2271.ZerolBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to ZerolBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_zerol_bevel_gear_mesh.setter
    def selected_design_entity_of_type_zerol_bevel_gear_mesh(self, value: '_2271.ZerolBevelGearMesh'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_cycloidal_disc_central_bearing_connection(self) -> '_2275.CycloidalDiscCentralBearingConnection':
        """CycloidalDiscCentralBearingConnection: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2275.CycloidalDiscCentralBearingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to CycloidalDiscCentralBearingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_cycloidal_disc_central_bearing_connection.setter
    def selected_design_entity_of_type_cycloidal_disc_central_bearing_connection(self, value: '_2275.CycloidalDiscCentralBearingConnection'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_cycloidal_disc_planetary_bearing_connection(self) -> '_2278.CycloidalDiscPlanetaryBearingConnection':
        """CycloidalDiscPlanetaryBearingConnection: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2278.CycloidalDiscPlanetaryBearingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to CycloidalDiscPlanetaryBearingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_cycloidal_disc_planetary_bearing_connection.setter
    def selected_design_entity_of_type_cycloidal_disc_planetary_bearing_connection(self, value: '_2278.CycloidalDiscPlanetaryBearingConnection'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_ring_pins_to_disc_connection(self) -> '_2281.RingPinsToDiscConnection':
        """RingPinsToDiscConnection: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2281.RingPinsToDiscConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to RingPinsToDiscConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_ring_pins_to_disc_connection.setter
    def selected_design_entity_of_type_ring_pins_to_disc_connection(self, value: '_2281.RingPinsToDiscConnection'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_clutch_connection(self) -> '_2282.ClutchConnection':
        """ClutchConnection: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2282.ClutchConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to ClutchConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_clutch_connection.setter
    def selected_design_entity_of_type_clutch_connection(self, value: '_2282.ClutchConnection'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_concept_coupling_connection(self) -> '_2284.ConceptCouplingConnection':
        """ConceptCouplingConnection: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2284.ConceptCouplingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to ConceptCouplingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_concept_coupling_connection.setter
    def selected_design_entity_of_type_concept_coupling_connection(self, value: '_2284.ConceptCouplingConnection'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_coupling_connection(self) -> '_2286.CouplingConnection':
        """CouplingConnection: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2286.CouplingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to CouplingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_coupling_connection.setter
    def selected_design_entity_of_type_coupling_connection(self, value: '_2286.CouplingConnection'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_part_to_part_shear_coupling_connection(self) -> '_2288.PartToPartShearCouplingConnection':
        """PartToPartShearCouplingConnection: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2288.PartToPartShearCouplingConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to PartToPartShearCouplingConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_part_to_part_shear_coupling_connection.setter
    def selected_design_entity_of_type_part_to_part_shear_coupling_connection(self, value: '_2288.PartToPartShearCouplingConnection'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_spring_damper_connection(self) -> '_2290.SpringDamperConnection':
        """SpringDamperConnection: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2290.SpringDamperConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to SpringDamperConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_spring_damper_connection.setter
    def selected_design_entity_of_type_spring_damper_connection(self, value: '_2290.SpringDamperConnection'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_torque_converter_connection(self) -> '_2292.TorqueConverterConnection':
        """TorqueConverterConnection: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2292.TorqueConverterConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to TorqueConverterConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_torque_converter_connection.setter
    def selected_design_entity_of_type_torque_converter_connection(self, value: '_2292.TorqueConverterConnection'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_assembly(self) -> '_2374.Assembly':
        """Assembly: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2374.Assembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to Assembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_assembly.setter
    def selected_design_entity_of_type_assembly(self, value: '_2374.Assembly'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_abstract_assembly(self) -> '_2375.AbstractAssembly':
        """AbstractAssembly: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2375.AbstractAssembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to AbstractAssembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_abstract_assembly.setter
    def selected_design_entity_of_type_abstract_assembly(self, value: '_2375.AbstractAssembly'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_abstract_shaft(self) -> '_2376.AbstractShaft':
        """AbstractShaft: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2376.AbstractShaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to AbstractShaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_abstract_shaft.setter
    def selected_design_entity_of_type_abstract_shaft(self, value: '_2376.AbstractShaft'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_abstract_shaft_or_housing(self) -> '_2377.AbstractShaftOrHousing':
        """AbstractShaftOrHousing: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2377.AbstractShaftOrHousing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to AbstractShaftOrHousing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_abstract_shaft_or_housing.setter
    def selected_design_entity_of_type_abstract_shaft_or_housing(self, value: '_2377.AbstractShaftOrHousing'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_bearing(self) -> '_2380.Bearing':
        """Bearing: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2380.Bearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to Bearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_bearing.setter
    def selected_design_entity_of_type_bearing(self, value: '_2380.Bearing'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_bolt(self) -> '_2382.Bolt':
        """Bolt: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2382.Bolt.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to Bolt. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_bolt.setter
    def selected_design_entity_of_type_bolt(self, value: '_2382.Bolt'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_bolted_joint(self) -> '_2383.BoltedJoint':
        """BoltedJoint: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2383.BoltedJoint.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to BoltedJoint. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_bolted_joint.setter
    def selected_design_entity_of_type_bolted_joint(self, value: '_2383.BoltedJoint'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_component(self) -> '_2384.Component':
        """Component: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2384.Component.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to Component. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_component.setter
    def selected_design_entity_of_type_component(self, value: '_2384.Component'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_connector(self) -> '_2387.Connector':
        """Connector: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2387.Connector.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to Connector. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_connector.setter
    def selected_design_entity_of_type_connector(self, value: '_2387.Connector'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_datum(self) -> '_2388.Datum':
        """Datum: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2388.Datum.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to Datum. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_datum.setter
    def selected_design_entity_of_type_datum(self, value: '_2388.Datum'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_external_cad_model(self) -> '_2392.ExternalCADModel':
        """ExternalCADModel: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2392.ExternalCADModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to ExternalCADModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_external_cad_model.setter
    def selected_design_entity_of_type_external_cad_model(self, value: '_2392.ExternalCADModel'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_fe_part(self) -> '_2393.FEPart':
        """FEPart: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2393.FEPart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to FEPart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_fe_part.setter
    def selected_design_entity_of_type_fe_part(self, value: '_2393.FEPart'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_flexible_pin_assembly(self) -> '_2394.FlexiblePinAssembly':
        """FlexiblePinAssembly: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2394.FlexiblePinAssembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to FlexiblePinAssembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_flexible_pin_assembly.setter
    def selected_design_entity_of_type_flexible_pin_assembly(self, value: '_2394.FlexiblePinAssembly'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_guide_dxf_model(self) -> '_2395.GuideDxfModel':
        """GuideDxfModel: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2395.GuideDxfModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to GuideDxfModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_guide_dxf_model.setter
    def selected_design_entity_of_type_guide_dxf_model(self, value: '_2395.GuideDxfModel'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_mass_disc(self) -> '_2402.MassDisc':
        """MassDisc: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2402.MassDisc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to MassDisc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_mass_disc.setter
    def selected_design_entity_of_type_mass_disc(self, value: '_2402.MassDisc'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_measurement_component(self) -> '_2403.MeasurementComponent':
        """MeasurementComponent: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2403.MeasurementComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to MeasurementComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_measurement_component.setter
    def selected_design_entity_of_type_measurement_component(self, value: '_2403.MeasurementComponent'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_mountable_component(self) -> '_2404.MountableComponent':
        """MountableComponent: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2404.MountableComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to MountableComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_mountable_component.setter
    def selected_design_entity_of_type_mountable_component(self, value: '_2404.MountableComponent'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_oil_seal(self) -> '_2406.OilSeal':
        """OilSeal: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2406.OilSeal.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to OilSeal. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_oil_seal.setter
    def selected_design_entity_of_type_oil_seal(self, value: '_2406.OilSeal'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_part(self) -> '_2408.Part':
        """Part: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2408.Part.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to Part. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_part.setter
    def selected_design_entity_of_type_part(self, value: '_2408.Part'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_planet_carrier(self) -> '_2409.PlanetCarrier':
        """PlanetCarrier: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2409.PlanetCarrier.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to PlanetCarrier. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_planet_carrier.setter
    def selected_design_entity_of_type_planet_carrier(self, value: '_2409.PlanetCarrier'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_point_load(self) -> '_2411.PointLoad':
        """PointLoad: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2411.PointLoad.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to PointLoad. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_point_load.setter
    def selected_design_entity_of_type_point_load(self, value: '_2411.PointLoad'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_power_load(self) -> '_2412.PowerLoad':
        """PowerLoad: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2412.PowerLoad.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to PowerLoad. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_power_load.setter
    def selected_design_entity_of_type_power_load(self, value: '_2412.PowerLoad'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_root_assembly(self) -> '_2414.RootAssembly':
        """RootAssembly: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2414.RootAssembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to RootAssembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_root_assembly.setter
    def selected_design_entity_of_type_root_assembly(self, value: '_2414.RootAssembly'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_specialised_assembly(self) -> '_2416.SpecialisedAssembly':
        """SpecialisedAssembly: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2416.SpecialisedAssembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to SpecialisedAssembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_specialised_assembly.setter
    def selected_design_entity_of_type_specialised_assembly(self, value: '_2416.SpecialisedAssembly'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_unbalanced_mass(self) -> '_2417.UnbalancedMass':
        """UnbalancedMass: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2417.UnbalancedMass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to UnbalancedMass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_unbalanced_mass.setter
    def selected_design_entity_of_type_unbalanced_mass(self, value: '_2417.UnbalancedMass'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_virtual_component(self) -> '_2419.VirtualComponent':
        """VirtualComponent: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2419.VirtualComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to VirtualComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_virtual_component.setter
    def selected_design_entity_of_type_virtual_component(self, value: '_2419.VirtualComponent'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_shaft(self) -> '_2422.Shaft':
        """Shaft: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2422.Shaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to Shaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_shaft.setter
    def selected_design_entity_of_type_shaft(self, value: '_2422.Shaft'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_agma_gleason_conical_gear(self) -> '_2452.AGMAGleasonConicalGear':
        """AGMAGleasonConicalGear: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2452.AGMAGleasonConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to AGMAGleasonConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_agma_gleason_conical_gear.setter
    def selected_design_entity_of_type_agma_gleason_conical_gear(self, value: '_2452.AGMAGleasonConicalGear'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_agma_gleason_conical_gear_set(self) -> '_2453.AGMAGleasonConicalGearSet':
        """AGMAGleasonConicalGearSet: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2453.AGMAGleasonConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to AGMAGleasonConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_agma_gleason_conical_gear_set.setter
    def selected_design_entity_of_type_agma_gleason_conical_gear_set(self, value: '_2453.AGMAGleasonConicalGearSet'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_bevel_differential_gear(self) -> '_2454.BevelDifferentialGear':
        """BevelDifferentialGear: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2454.BevelDifferentialGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to BevelDifferentialGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_bevel_differential_gear.setter
    def selected_design_entity_of_type_bevel_differential_gear(self, value: '_2454.BevelDifferentialGear'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_bevel_differential_gear_set(self) -> '_2455.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2455.BevelDifferentialGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to BevelDifferentialGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_bevel_differential_gear_set.setter
    def selected_design_entity_of_type_bevel_differential_gear_set(self, value: '_2455.BevelDifferentialGearSet'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_bevel_differential_planet_gear(self) -> '_2456.BevelDifferentialPlanetGear':
        """BevelDifferentialPlanetGear: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2456.BevelDifferentialPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to BevelDifferentialPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_bevel_differential_planet_gear.setter
    def selected_design_entity_of_type_bevel_differential_planet_gear(self, value: '_2456.BevelDifferentialPlanetGear'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_bevel_differential_sun_gear(self) -> '_2457.BevelDifferentialSunGear':
        """BevelDifferentialSunGear: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2457.BevelDifferentialSunGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to BevelDifferentialSunGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_bevel_differential_sun_gear.setter
    def selected_design_entity_of_type_bevel_differential_sun_gear(self, value: '_2457.BevelDifferentialSunGear'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_bevel_gear(self) -> '_2458.BevelGear':
        """BevelGear: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2458.BevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to BevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_bevel_gear.setter
    def selected_design_entity_of_type_bevel_gear(self, value: '_2458.BevelGear'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_bevel_gear_set(self) -> '_2459.BevelGearSet':
        """BevelGearSet: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2459.BevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to BevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_bevel_gear_set.setter
    def selected_design_entity_of_type_bevel_gear_set(self, value: '_2459.BevelGearSet'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_concept_gear(self) -> '_2460.ConceptGear':
        """ConceptGear: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2460.ConceptGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to ConceptGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_concept_gear.setter
    def selected_design_entity_of_type_concept_gear(self, value: '_2460.ConceptGear'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_concept_gear_set(self) -> '_2461.ConceptGearSet':
        """ConceptGearSet: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2461.ConceptGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to ConceptGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_concept_gear_set.setter
    def selected_design_entity_of_type_concept_gear_set(self, value: '_2461.ConceptGearSet'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_conical_gear(self) -> '_2462.ConicalGear':
        """ConicalGear: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2462.ConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to ConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_conical_gear.setter
    def selected_design_entity_of_type_conical_gear(self, value: '_2462.ConicalGear'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_conical_gear_set(self) -> '_2463.ConicalGearSet':
        """ConicalGearSet: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2463.ConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to ConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_conical_gear_set.setter
    def selected_design_entity_of_type_conical_gear_set(self, value: '_2463.ConicalGearSet'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_cylindrical_gear(self) -> '_2464.CylindricalGear':
        """CylindricalGear: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2464.CylindricalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to CylindricalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_cylindrical_gear.setter
    def selected_design_entity_of_type_cylindrical_gear(self, value: '_2464.CylindricalGear'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_cylindrical_gear_set(self) -> '_2465.CylindricalGearSet':
        """CylindricalGearSet: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2465.CylindricalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to CylindricalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_cylindrical_gear_set.setter
    def selected_design_entity_of_type_cylindrical_gear_set(self, value: '_2465.CylindricalGearSet'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_cylindrical_planet_gear(self) -> '_2466.CylindricalPlanetGear':
        """CylindricalPlanetGear: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2466.CylindricalPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to CylindricalPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_cylindrical_planet_gear.setter
    def selected_design_entity_of_type_cylindrical_planet_gear(self, value: '_2466.CylindricalPlanetGear'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_face_gear(self) -> '_2467.FaceGear':
        """FaceGear: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2467.FaceGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to FaceGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_face_gear.setter
    def selected_design_entity_of_type_face_gear(self, value: '_2467.FaceGear'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_face_gear_set(self) -> '_2468.FaceGearSet':
        """FaceGearSet: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2468.FaceGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to FaceGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_face_gear_set.setter
    def selected_design_entity_of_type_face_gear_set(self, value: '_2468.FaceGearSet'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_gear(self) -> '_2469.Gear':
        """Gear: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2469.Gear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to Gear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_gear.setter
    def selected_design_entity_of_type_gear(self, value: '_2469.Gear'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_gear_set(self) -> '_2471.GearSet':
        """GearSet: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2471.GearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to GearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_gear_set.setter
    def selected_design_entity_of_type_gear_set(self, value: '_2471.GearSet'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_hypoid_gear(self) -> '_2473.HypoidGear':
        """HypoidGear: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2473.HypoidGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to HypoidGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_hypoid_gear.setter
    def selected_design_entity_of_type_hypoid_gear(self, value: '_2473.HypoidGear'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_hypoid_gear_set(self) -> '_2474.HypoidGearSet':
        """HypoidGearSet: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2474.HypoidGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to HypoidGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_hypoid_gear_set.setter
    def selected_design_entity_of_type_hypoid_gear_set(self, value: '_2474.HypoidGearSet'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> '_2475.KlingelnbergCycloPalloidConicalGear':
        """KlingelnbergCycloPalloidConicalGear: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2475.KlingelnbergCycloPalloidConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to KlingelnbergCycloPalloidConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_klingelnberg_cyclo_palloid_conical_gear.setter
    def selected_design_entity_of_type_klingelnberg_cyclo_palloid_conical_gear(self, value: '_2475.KlingelnbergCycloPalloidConicalGear'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_klingelnberg_cyclo_palloid_conical_gear_set(self) -> '_2476.KlingelnbergCycloPalloidConicalGearSet':
        """KlingelnbergCycloPalloidConicalGearSet: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2476.KlingelnbergCycloPalloidConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to KlingelnbergCycloPalloidConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_klingelnberg_cyclo_palloid_conical_gear_set.setter
    def selected_design_entity_of_type_klingelnberg_cyclo_palloid_conical_gear_set(self, value: '_2476.KlingelnbergCycloPalloidConicalGearSet'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> '_2477.KlingelnbergCycloPalloidHypoidGear':
        """KlingelnbergCycloPalloidHypoidGear: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2477.KlingelnbergCycloPalloidHypoidGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to KlingelnbergCycloPalloidHypoidGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_klingelnberg_cyclo_palloid_hypoid_gear.setter
    def selected_design_entity_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self, value: '_2477.KlingelnbergCycloPalloidHypoidGear'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self) -> '_2478.KlingelnbergCycloPalloidHypoidGearSet':
        """KlingelnbergCycloPalloidHypoidGearSet: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2478.KlingelnbergCycloPalloidHypoidGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to KlingelnbergCycloPalloidHypoidGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set.setter
    def selected_design_entity_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self, value: '_2478.KlingelnbergCycloPalloidHypoidGearSet'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> '_2479.KlingelnbergCycloPalloidSpiralBevelGear':
        """KlingelnbergCycloPalloidSpiralBevelGear: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2479.KlingelnbergCycloPalloidSpiralBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to KlingelnbergCycloPalloidSpiralBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear.setter
    def selected_design_entity_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self, value: '_2479.KlingelnbergCycloPalloidSpiralBevelGear'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> '_2480.KlingelnbergCycloPalloidSpiralBevelGearSet':
        """KlingelnbergCycloPalloidSpiralBevelGearSet: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2480.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to KlingelnbergCycloPalloidSpiralBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set.setter
    def selected_design_entity_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self, value: '_2480.KlingelnbergCycloPalloidSpiralBevelGearSet'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_planetary_gear_set(self) -> '_2481.PlanetaryGearSet':
        """PlanetaryGearSet: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2481.PlanetaryGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to PlanetaryGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_planetary_gear_set.setter
    def selected_design_entity_of_type_planetary_gear_set(self, value: '_2481.PlanetaryGearSet'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_spiral_bevel_gear(self) -> '_2482.SpiralBevelGear':
        """SpiralBevelGear: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2482.SpiralBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to SpiralBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_spiral_bevel_gear.setter
    def selected_design_entity_of_type_spiral_bevel_gear(self, value: '_2482.SpiralBevelGear'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_spiral_bevel_gear_set(self) -> '_2483.SpiralBevelGearSet':
        """SpiralBevelGearSet: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2483.SpiralBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to SpiralBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_spiral_bevel_gear_set.setter
    def selected_design_entity_of_type_spiral_bevel_gear_set(self, value: '_2483.SpiralBevelGearSet'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_straight_bevel_diff_gear(self) -> '_2484.StraightBevelDiffGear':
        """StraightBevelDiffGear: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2484.StraightBevelDiffGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to StraightBevelDiffGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_straight_bevel_diff_gear.setter
    def selected_design_entity_of_type_straight_bevel_diff_gear(self, value: '_2484.StraightBevelDiffGear'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_straight_bevel_diff_gear_set(self) -> '_2485.StraightBevelDiffGearSet':
        """StraightBevelDiffGearSet: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2485.StraightBevelDiffGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to StraightBevelDiffGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_straight_bevel_diff_gear_set.setter
    def selected_design_entity_of_type_straight_bevel_diff_gear_set(self, value: '_2485.StraightBevelDiffGearSet'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_straight_bevel_gear(self) -> '_2486.StraightBevelGear':
        """StraightBevelGear: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2486.StraightBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to StraightBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_straight_bevel_gear.setter
    def selected_design_entity_of_type_straight_bevel_gear(self, value: '_2486.StraightBevelGear'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_straight_bevel_gear_set(self) -> '_2487.StraightBevelGearSet':
        """StraightBevelGearSet: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2487.StraightBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to StraightBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_straight_bevel_gear_set.setter
    def selected_design_entity_of_type_straight_bevel_gear_set(self, value: '_2487.StraightBevelGearSet'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_straight_bevel_planet_gear(self) -> '_2488.StraightBevelPlanetGear':
        """StraightBevelPlanetGear: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2488.StraightBevelPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to StraightBevelPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_straight_bevel_planet_gear.setter
    def selected_design_entity_of_type_straight_bevel_planet_gear(self, value: '_2488.StraightBevelPlanetGear'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_straight_bevel_sun_gear(self) -> '_2489.StraightBevelSunGear':
        """StraightBevelSunGear: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2489.StraightBevelSunGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to StraightBevelSunGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_straight_bevel_sun_gear.setter
    def selected_design_entity_of_type_straight_bevel_sun_gear(self, value: '_2489.StraightBevelSunGear'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_worm_gear(self) -> '_2490.WormGear':
        """WormGear: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2490.WormGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to WormGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_worm_gear.setter
    def selected_design_entity_of_type_worm_gear(self, value: '_2490.WormGear'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_worm_gear_set(self) -> '_2491.WormGearSet':
        """WormGearSet: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2491.WormGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to WormGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_worm_gear_set.setter
    def selected_design_entity_of_type_worm_gear_set(self, value: '_2491.WormGearSet'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_zerol_bevel_gear(self) -> '_2492.ZerolBevelGear':
        """ZerolBevelGear: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2492.ZerolBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to ZerolBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_zerol_bevel_gear.setter
    def selected_design_entity_of_type_zerol_bevel_gear(self, value: '_2492.ZerolBevelGear'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_zerol_bevel_gear_set(self) -> '_2493.ZerolBevelGearSet':
        """ZerolBevelGearSet: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2493.ZerolBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to ZerolBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_zerol_bevel_gear_set.setter
    def selected_design_entity_of_type_zerol_bevel_gear_set(self, value: '_2493.ZerolBevelGearSet'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_cycloidal_assembly(self) -> '_2507.CycloidalAssembly':
        """CycloidalAssembly: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2507.CycloidalAssembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to CycloidalAssembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_cycloidal_assembly.setter
    def selected_design_entity_of_type_cycloidal_assembly(self, value: '_2507.CycloidalAssembly'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_cycloidal_disc(self) -> '_2508.CycloidalDisc':
        """CycloidalDisc: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2508.CycloidalDisc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to CycloidalDisc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_cycloidal_disc.setter
    def selected_design_entity_of_type_cycloidal_disc(self, value: '_2508.CycloidalDisc'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_ring_pins(self) -> '_2509.RingPins':
        """RingPins: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2509.RingPins.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to RingPins. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_ring_pins.setter
    def selected_design_entity_of_type_ring_pins(self, value: '_2509.RingPins'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_belt_drive(self) -> '_2515.BeltDrive':
        """BeltDrive: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2515.BeltDrive.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to BeltDrive. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_belt_drive.setter
    def selected_design_entity_of_type_belt_drive(self, value: '_2515.BeltDrive'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_clutch(self) -> '_2517.Clutch':
        """Clutch: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2517.Clutch.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to Clutch. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_clutch.setter
    def selected_design_entity_of_type_clutch(self, value: '_2517.Clutch'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_clutch_half(self) -> '_2518.ClutchHalf':
        """ClutchHalf: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2518.ClutchHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to ClutchHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_clutch_half.setter
    def selected_design_entity_of_type_clutch_half(self, value: '_2518.ClutchHalf'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_concept_coupling(self) -> '_2520.ConceptCoupling':
        """ConceptCoupling: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2520.ConceptCoupling.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to ConceptCoupling. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_concept_coupling.setter
    def selected_design_entity_of_type_concept_coupling(self, value: '_2520.ConceptCoupling'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_concept_coupling_half(self) -> '_2521.ConceptCouplingHalf':
        """ConceptCouplingHalf: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2521.ConceptCouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to ConceptCouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_concept_coupling_half.setter
    def selected_design_entity_of_type_concept_coupling_half(self, value: '_2521.ConceptCouplingHalf'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_coupling(self) -> '_2522.Coupling':
        """Coupling: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2522.Coupling.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to Coupling. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_coupling.setter
    def selected_design_entity_of_type_coupling(self, value: '_2522.Coupling'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_coupling_half(self) -> '_2523.CouplingHalf':
        """CouplingHalf: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2523.CouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to CouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_coupling_half.setter
    def selected_design_entity_of_type_coupling_half(self, value: '_2523.CouplingHalf'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_cvt(self) -> '_2525.CVT':
        """CVT: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2525.CVT.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to CVT. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_cvt.setter
    def selected_design_entity_of_type_cvt(self, value: '_2525.CVT'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_cvt_pulley(self) -> '_2526.CVTPulley':
        """CVTPulley: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2526.CVTPulley.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to CVTPulley. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_cvt_pulley.setter
    def selected_design_entity_of_type_cvt_pulley(self, value: '_2526.CVTPulley'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_part_to_part_shear_coupling(self) -> '_2527.PartToPartShearCoupling':
        """PartToPartShearCoupling: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2527.PartToPartShearCoupling.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to PartToPartShearCoupling. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_part_to_part_shear_coupling.setter
    def selected_design_entity_of_type_part_to_part_shear_coupling(self, value: '_2527.PartToPartShearCoupling'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_part_to_part_shear_coupling_half(self) -> '_2528.PartToPartShearCouplingHalf':
        """PartToPartShearCouplingHalf: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2528.PartToPartShearCouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to PartToPartShearCouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_part_to_part_shear_coupling_half.setter
    def selected_design_entity_of_type_part_to_part_shear_coupling_half(self, value: '_2528.PartToPartShearCouplingHalf'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_pulley(self) -> '_2529.Pulley':
        """Pulley: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2529.Pulley.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to Pulley. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_pulley.setter
    def selected_design_entity_of_type_pulley(self, value: '_2529.Pulley'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_rolling_ring(self) -> '_2535.RollingRing':
        """RollingRing: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2535.RollingRing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to RollingRing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_rolling_ring.setter
    def selected_design_entity_of_type_rolling_ring(self, value: '_2535.RollingRing'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_rolling_ring_assembly(self) -> '_2536.RollingRingAssembly':
        """RollingRingAssembly: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2536.RollingRingAssembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to RollingRingAssembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_rolling_ring_assembly.setter
    def selected_design_entity_of_type_rolling_ring_assembly(self, value: '_2536.RollingRingAssembly'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_shaft_hub_connection(self) -> '_2537.ShaftHubConnection':
        """ShaftHubConnection: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2537.ShaftHubConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to ShaftHubConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_shaft_hub_connection.setter
    def selected_design_entity_of_type_shaft_hub_connection(self, value: '_2537.ShaftHubConnection'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_spring_damper(self) -> '_2539.SpringDamper':
        """SpringDamper: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2539.SpringDamper.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to SpringDamper. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_spring_damper.setter
    def selected_design_entity_of_type_spring_damper(self, value: '_2539.SpringDamper'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_spring_damper_half(self) -> '_2540.SpringDamperHalf':
        """SpringDamperHalf: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2540.SpringDamperHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to SpringDamperHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_spring_damper_half.setter
    def selected_design_entity_of_type_spring_damper_half(self, value: '_2540.SpringDamperHalf'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_synchroniser(self) -> '_2541.Synchroniser':
        """Synchroniser: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2541.Synchroniser.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to Synchroniser. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_synchroniser.setter
    def selected_design_entity_of_type_synchroniser(self, value: '_2541.Synchroniser'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_synchroniser_half(self) -> '_2543.SynchroniserHalf':
        """SynchroniserHalf: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2543.SynchroniserHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to SynchroniserHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_synchroniser_half.setter
    def selected_design_entity_of_type_synchroniser_half(self, value: '_2543.SynchroniserHalf'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_synchroniser_part(self) -> '_2544.SynchroniserPart':
        """SynchroniserPart: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2544.SynchroniserPart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to SynchroniserPart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_synchroniser_part.setter
    def selected_design_entity_of_type_synchroniser_part(self, value: '_2544.SynchroniserPart'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_synchroniser_sleeve(self) -> '_2545.SynchroniserSleeve':
        """SynchroniserSleeve: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2545.SynchroniserSleeve.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to SynchroniserSleeve. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_synchroniser_sleeve.setter
    def selected_design_entity_of_type_synchroniser_sleeve(self, value: '_2545.SynchroniserSleeve'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_torque_converter(self) -> '_2546.TorqueConverter':
        """TorqueConverter: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2546.TorqueConverter.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to TorqueConverter. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_torque_converter.setter
    def selected_design_entity_of_type_torque_converter(self, value: '_2546.TorqueConverter'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_torque_converter_pump(self) -> '_2547.TorqueConverterPump':
        """TorqueConverterPump: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2547.TorqueConverterPump.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to TorqueConverterPump. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_torque_converter_pump.setter
    def selected_design_entity_of_type_torque_converter_pump(self, value: '_2547.TorqueConverterPump'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def selected_design_entity_of_type_torque_converter_turbine(self) -> '_2549.TorqueConverterTurbine':
        """TorqueConverterTurbine: 'SelectedDesignEntity' is the original name of this property."""

        temp = self.wrapped.SelectedDesignEntity
        if _2549.TorqueConverterTurbine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_design_entity to TorqueConverterTurbine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @selected_design_entity_of_type_torque_converter_turbine.setter
    def selected_design_entity_of_type_torque_converter_turbine(self, value: '_2549.TorqueConverterTurbine'):
        value = value.wrapped if value else None
        self.wrapped.SelectedDesignEntity = value

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames
        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    @staticmethod
    def get_mastagui(process_id: 'int') -> 'MASTAGUI':
        """ 'GetMASTAGUI' is the original name of this method.

        Args:
            process_id (int)

        Returns:
            mastapy.system_model_gui.MASTAGUI
        """

        process_id = int(process_id)
        method_result = MASTAGUI.TYPE.GetMASTAGUI(process_id if process_id else 0)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def pause(self):
        """ 'Pause' is the original name of this method."""

        self.wrapped.Pause()

    def resume(self):
        """ 'Resume' is the original name of this method."""

        self.wrapped.Resume()

    def start_remoting(self):
        """ 'StartRemoting' is the original name of this method."""

        self.wrapped.StartRemoting()

    def stop_remoting(self):
        """ 'StopRemoting' is the original name of this method."""

        self.wrapped.StopRemoting()

    def aborted(self):
        """ 'Aborted' is the original name of this method."""

        self.wrapped.Aborted()

    def add_electric_machine_from_cad_face_group(self, cad_face_group: '_302.CADFaceGroup', geometry_modeller_design_information: '_154.GeometryModellerDesignInformation', dimensions: 'Dict[str, _155.GeometryModellerDimension]'):
        """ 'AddElectricMachineFromCADFaceGroup' is the original name of this method.

        Args:
            cad_face_group (mastapy.geometry.two_d.CADFaceGroup)
            geometry_modeller_design_information (mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerDesignInformation)
            dimensions (Dict[str, mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerDimension])
        """

        self.wrapped.AddElectricMachineFromCADFaceGroup(cad_face_group.wrapped if cad_face_group else None, geometry_modeller_design_information.wrapped if geometry_modeller_design_information else None, dimensions)

    def add_fe_substructure_from_data(self, vertices_and_facets: '_1469.FacetedBody', geometry_modeller_design_information: '_154.GeometryModellerDesignInformation', dimensions: 'Dict[str, _155.GeometryModellerDimension]', body_moniker: 'str'):
        """ 'AddFESubstructureFromData' is the original name of this method.

        Args:
            vertices_and_facets (mastapy.math_utility.FacetedBody)
            geometry_modeller_design_information (mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerDesignInformation)
            dimensions (Dict[str, mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerDimension])
            body_moniker (str)
        """

        body_moniker = str(body_moniker)
        self.wrapped.AddFESubstructureFromData(vertices_and_facets.wrapped if vertices_and_facets else None, geometry_modeller_design_information.wrapped if geometry_modeller_design_information else None, dimensions, body_moniker if body_moniker else '')

    def add_fe_substructure_from_file(self, length_scale: 'float', stl_file_name: 'str', dimensions: 'Dict[str, _155.GeometryModellerDimension]'):
        """ 'AddFESubstructureFromFile' is the original name of this method.

        Args:
            length_scale (float)
            stl_file_name (str)
            dimensions (Dict[str, mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerDimension])
        """

        length_scale = float(length_scale)
        stl_file_name = str(stl_file_name)
        self.wrapped.AddFESubstructureFromFile(length_scale if length_scale else 0.0, stl_file_name if stl_file_name else '', dimensions)

    def add_line_from_geometry_modeller(self, circles_on_axis: '_1452.CirclesOnAxis'):
        """ 'AddLineFromGeometryModeller' is the original name of this method.

        Args:
            circles_on_axis (mastapy.math_utility.CirclesOnAxis)
        """

        self.wrapped.AddLineFromGeometryModeller(circles_on_axis.wrapped if circles_on_axis else None)

    def are_new_input_available(self) -> '_161.MeshRequest':
        """ 'AreNewInputAvailable' is the original name of this method.

        Returns:
            mastapy.nodal_analysis.geometry_modeller_link.MeshRequest
        """

        method_result = self.wrapped.AreNewInputAvailable()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def circle_pairs_from_geometry_modeller(self, preselection_circles: '_1452.CirclesOnAxis', selected_circles: 'List[_1452.CirclesOnAxis]'):
        """ 'CirclePairsFromGeometryModeller' is the original name of this method.

        Args:
            preselection_circles (mastapy.math_utility.CirclesOnAxis)
            selected_circles (List[mastapy.math_utility.CirclesOnAxis])
        """

        selected_circles = conversion.mp_to_pn_objects_in_list(selected_circles)
        self.wrapped.CirclePairsFromGeometryModeller(preselection_circles.wrapped if preselection_circles else None, selected_circles)

    def create_geometry_modeller_design_information(self, file_name: 'str', main_part_moniker: 'str', tab_name: 'str') -> '_154.GeometryModellerDesignInformation':
        """ 'CreateGeometryModellerDesignInformation' is the original name of this method.

        Args:
            file_name (str)
            main_part_moniker (str)
            tab_name (str)

        Returns:
            mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerDesignInformation
        """

        file_name = str(file_name)
        main_part_moniker = str(main_part_moniker)
        tab_name = str(tab_name)
        method_result = self.wrapped.CreateGeometryModellerDesignInformation(file_name if file_name else '', main_part_moniker if main_part_moniker else '', tab_name if tab_name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def create_geometry_modeller_dimension(self) -> '_155.GeometryModellerDimension':
        """ 'CreateGeometryModellerDimension' is the original name of this method.

        Returns:
            mastapy.nodal_analysis.geometry_modeller_link.GeometryModellerDimension
        """

        method_result = self.wrapped.CreateGeometryModellerDimension()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def create_mesh_request_result(self) -> '_162.MeshRequestResult':
        """ 'CreateMeshRequestResult' is the original name of this method.

        Returns:
            mastapy.nodal_analysis.geometry_modeller_link.MeshRequestResult
        """

        method_result = self.wrapped.CreateMeshRequestResult()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def create_new_cad_face_group(self) -> '_302.CADFaceGroup':
        """ 'CreateNewCADFaceGroup' is the original name of this method.

        Returns:
            mastapy.geometry.two_d.CADFaceGroup
        """

        method_result = self.wrapped.CreateNewCADFaceGroup()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def create_new_circles_on_axis(self) -> '_1452.CirclesOnAxis':
        """ 'CreateNewCirclesOnAxis' is the original name of this method.

        Returns:
            mastapy.math_utility.CirclesOnAxis
        """

        method_result = self.wrapped.CreateNewCirclesOnAxis()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def create_new_faceted_body(self) -> '_1469.FacetedBody':
        """ 'CreateNewFacetedBody' is the original name of this method.

        Returns:
            mastapy.math_utility.FacetedBody
        """

        method_result = self.wrapped.CreateNewFacetedBody()
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def flag_message_received(self):
        """ 'FlagMessageReceived' is the original name of this method."""

        self.wrapped.FlagMessageReceived()

    def geometry_modeller_document_loaded(self):
        """ 'GeometryModellerDocumentLoaded' is the original name of this method."""

        self.wrapped.GeometryModellerDocumentLoaded()

    def move_selected_component(self, origin: 'Vector3D', axis: 'Vector3D'):
        """ 'MoveSelectedComponent' is the original name of this method.

        Args:
            origin (Vector3D)
            axis (Vector3D)
        """

        origin = conversion.mp_to_pn_vector3d(origin)
        axis = conversion.mp_to_pn_vector3d(axis)
        self.wrapped.MoveSelectedComponent(origin, axis)

    def open_design_in_new_tab(self, design: '_2143.Design'):
        """ 'OpenDesignInNewTab' is the original name of this method.

        Args:
            design (mastapy.system_model.Design)
        """

        self.wrapped.OpenDesignInNewTab(design.wrapped if design else None)

    def run_command(self, command: 'str'):
        """ 'RunCommand' is the original name of this method.

        Args:
            command (str)
        """

        command = str(command)
        self.wrapped.RunCommand(command if command else '')

    def select_tab(self, tab_text: 'str'):
        """ 'SelectTab' is the original name of this method.

        Args:
            tab_text (str)
        """

        tab_text = str(tab_text)
        self.wrapped.SelectTab(tab_text if tab_text else '')

    def set_error(self, error: 'str'):
        """ 'SetError' is the original name of this method.

        Args:
            error (str)
        """

        error = str(error)
        self.wrapped.SetError(error if error else '')

    def set_mesh_request_result(self, mesh_request_result: '_162.MeshRequestResult'):
        """ 'SetMeshRequestResult' is the original name of this method.

        Args:
            mesh_request_result (mastapy.nodal_analysis.geometry_modeller_link.MeshRequestResult)
        """

        self.wrapped.SetMeshRequestResult(mesh_request_result.wrapped if mesh_request_result else None)

    def show_boxes(self, small_box: 'List[Vector3D]', big_box: 'List[Vector3D]'):
        """ 'ShowBoxes' is the original name of this method.

        Args:
            small_box (List[Vector3D])
            big_box (List[Vector3D])
        """

        small_box = conversion.mp_to_pn_objects_in_list(small_box)
        big_box = conversion.mp_to_pn_objects_in_list(big_box)
        self.wrapped.ShowBoxes(small_box, big_box)

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

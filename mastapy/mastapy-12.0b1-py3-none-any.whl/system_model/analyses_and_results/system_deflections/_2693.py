"""_2693.py

GearMeshSystemDeflection
"""


from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.nodal_analysis import _69
from mastapy.system_model.connections_and_sockets.gears import (
    _2253, _2239, _2241, _2243,
    _2245, _2247, _2249, _2251,
    _2255, _2258, _2259, _2260,
    _2263, _2265, _2267, _2269,
    _2271
)
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.system_deflections import (
    _2695, _2630, _2637, _2638,
    _2639, _2642, _2656, _2660,
    _2679, _2680, _2681, _2684,
    _2690, _2699, _2704, _2707,
    _2710, _2743, _2749, _2752,
    _2753, _2754, _2772, _2775,
    _2715, _2701
)
from mastapy.math_utility.measured_vectors import _1523
from mastapy._math.vector_3d import Vector3D
from mastapy.gears.rating import _351
from mastapy.gears.rating.zerol_bevel import _360
from mastapy.gears.rating.worm import _364
from mastapy.gears.rating.straight_bevel import _386
from mastapy.gears.rating.straight_bevel_diff import _389
from mastapy.gears.rating.spiral_bevel import _393
from mastapy.gears.rating.klingelnberg_spiral_bevel import _396
from mastapy.gears.rating.klingelnberg_hypoid import _399
from mastapy.gears.rating.klingelnberg_conical import _402
from mastapy.gears.rating.hypoid import _429
from mastapy.gears.rating.face import _438
from mastapy.gears.rating.cylindrical import _449
from mastapy.gears.rating.conical import _529
from mastapy.gears.rating.concept import _540
from mastapy.gears.rating.bevel import _544
from mastapy.gears.rating.agma_gleason_conical import _555
from mastapy.system_model.analyses_and_results.power_flows import (
    _4023, _3968, _3975, _3980,
    _3993, _3996, _4012, _4018,
    _4027, _4031, _4034, _4037,
    _4066, _4072, _4075, _4091,
    _4094
)
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'GearMeshSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshSystemDeflection',)


class GearMeshSystemDeflection(_2701.InterMountableComponentConnectionSystemDeflection):
    """GearMeshSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearMeshSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def calculated_mesh_stiffness_along_face_width(self) -> 'float':
        """float: 'CalculatedMeshStiffnessAlongFaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedMeshStiffnessAlongFaceWidth
        return temp

    @property
    def flank_sign(self) -> 'float':
        """float: 'FlankSign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlankSign
        return temp

    @property
    def gear_a_torque_left_flank(self) -> 'float':
        """float: 'GearATorqueLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearATorqueLeftFlank
        return temp

    @property
    def gear_a_torque_right_flank(self) -> 'float':
        """float: 'GearATorqueRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearATorqueRightFlank
        return temp

    @property
    def gear_b_torque_left_flank(self) -> 'float':
        """float: 'GearBTorqueLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBTorqueLeftFlank
        return temp

    @property
    def gear_b_torque_right_flank(self) -> 'float':
        """float: 'GearBTorqueRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBTorqueRightFlank
        return temp

    @property
    def gear_mesh_contact_status(self) -> '_69.GearMeshContactStatus':
        """GearMeshContactStatus: 'GearMeshContactStatus' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshContactStatus
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_69.GearMeshContactStatus)(value) if value is not None else None

    @property
    def is_in_contact(self) -> 'bool':
        """bool: 'IsInContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsInContact
        return temp

    @property
    def load_in_loa_from_stiffness_model(self) -> 'float':
        """float: 'LoadInLOAFromStiffnessModel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadInLOAFromStiffnessModel
        return temp

    @property
    def maximum_possible_mesh_stiffness_along_face_width(self) -> 'float':
        """float: 'MaximumPossibleMeshStiffnessAlongFaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumPossibleMeshStiffnessAlongFaceWidth
        return temp

    @property
    def mesh_power(self) -> 'float':
        """float: 'MeshPower' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshPower
        return temp

    @property
    def mesh_power_gear_a_left_flank(self) -> 'float':
        """float: 'MeshPowerGearALeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshPowerGearALeftFlank
        return temp

    @property
    def mesh_power_gear_a_right_flank(self) -> 'float':
        """float: 'MeshPowerGearARightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshPowerGearARightFlank
        return temp

    @property
    def mesh_power_gear_b_left_flank(self) -> 'float':
        """float: 'MeshPowerGearBLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshPowerGearBLeftFlank
        return temp

    @property
    def mesh_power_gear_b_right_flank(self) -> 'float':
        """float: 'MeshPowerGearBRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshPowerGearBRightFlank
        return temp

    @property
    def minimum_separation_left_flank(self) -> 'float':
        """float: 'MinimumSeparationLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumSeparationLeftFlank
        return temp

    @property
    def minimum_separation_right_flank(self) -> 'float':
        """float: 'MinimumSeparationRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumSeparationRightFlank
        return temp

    @property
    def moment_about_centre_from_ltca(self) -> 'float':
        """float: 'MomentAboutCentreFromLTCA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MomentAboutCentreFromLTCA
        return temp

    @property
    def moment_about_centre_from_stiffness_model(self) -> 'float':
        """float: 'MomentAboutCentreFromStiffnessModel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MomentAboutCentreFromStiffnessModel
        return temp

    @property
    def node_pair_backlash_on_left_side(self) -> 'List[float]':
        """List[float]: 'NodePairBacklashOnLeftSide' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairBacklashOnLeftSide
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def node_pair_backlash_on_right_side(self) -> 'List[float]':
        """List[float]: 'NodePairBacklashOnRightSide' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairBacklashOnRightSide
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def node_pair_contact_status(self) -> 'List[str]':
        """List[str]: 'NodePairContactStatus' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairContactStatus
        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    @property
    def node_pair_deflections(self) -> 'List[float]':
        """List[float]: 'NodePairDeflections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairDeflections
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def node_pair_load_in_loa(self) -> 'List[float]':
        """List[float]: 'NodePairLoadInLOA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairLoadInLOA
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def node_pair_load_in_loa_left_flank(self) -> 'List[float]':
        """List[float]: 'NodePairLoadInLOALeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairLoadInLOALeftFlank
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def node_pair_load_in_loa_right_flank(self) -> 'List[float]':
        """List[float]: 'NodePairLoadInLOARightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairLoadInLOARightFlank
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def node_pair_mesh_stiffness(self) -> 'List[float]':
        """List[float]: 'NodePairMeshStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairMeshStiffness
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def node_pair_mesh_stiffness_z_theta(self) -> 'List[float]':
        """List[float]: 'NodePairMeshStiffnessZTheta' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairMeshStiffnessZTheta
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def node_pair_mesh_stiffness_theta_z(self) -> 'List[float]':
        """List[float]: 'NodePairMeshStiffnessThetaZ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairMeshStiffnessThetaZ
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def node_pair_mesh_stiffness_theta_theta(self) -> 'List[float]':
        """List[float]: 'NodePairMeshStiffnessThetaTheta' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairMeshStiffnessThetaTheta
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def node_pair_separations(self) -> 'List[float]':
        """List[float]: 'NodePairSeparations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairSeparations
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def node_pair_separations_left_flank(self) -> 'List[float]':
        """List[float]: 'NodePairSeparationsLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairSeparationsLeftFlank
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def node_pair_separations_right_flank(self) -> 'List[float]':
        """List[float]: 'NodePairSeparationsRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairSeparationsRightFlank
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def node_pair_separations_inactive_flank(self) -> 'List[float]':
        """List[float]: 'NodePairSeparationsInactiveFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairSeparationsInactiveFlank
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def number_of_teeth_in_contact(self) -> 'int':
        """int: 'NumberOfTeethInContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfTeethInContact
        return temp

    @property
    def stiffness_kzz(self) -> 'float':
        """float: 'StiffnessKzz' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessKzz
        return temp

    @property
    def total_contact_length(self) -> 'float':
        """float: 'TotalContactLength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalContactLength
        return temp

    @property
    def connection_design(self) -> '_2253.GearMesh':
        """GearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        if _2253.GearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to GearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_agma_gleason_conical_gear_mesh(self) -> '_2239.AGMAGleasonConicalGearMesh':
        """AGMAGleasonConicalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        if _2239.AGMAGleasonConicalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to AGMAGleasonConicalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_bevel_differential_gear_mesh(self) -> '_2241.BevelDifferentialGearMesh':
        """BevelDifferentialGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        if _2241.BevelDifferentialGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to BevelDifferentialGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_bevel_gear_mesh(self) -> '_2243.BevelGearMesh':
        """BevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        if _2243.BevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to BevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_concept_gear_mesh(self) -> '_2245.ConceptGearMesh':
        """ConceptGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        if _2245.ConceptGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to ConceptGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_conical_gear_mesh(self) -> '_2247.ConicalGearMesh':
        """ConicalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        if _2247.ConicalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to ConicalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_cylindrical_gear_mesh(self) -> '_2249.CylindricalGearMesh':
        """CylindricalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        if _2249.CylindricalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to CylindricalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_face_gear_mesh(self) -> '_2251.FaceGearMesh':
        """FaceGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        if _2251.FaceGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to FaceGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_hypoid_gear_mesh(self) -> '_2255.HypoidGearMesh':
        """HypoidGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        if _2255.HypoidGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to HypoidGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_klingelnberg_cyclo_palloid_conical_gear_mesh(self) -> '_2258.KlingelnbergCycloPalloidConicalGearMesh':
        """KlingelnbergCycloPalloidConicalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        if _2258.KlingelnbergCycloPalloidConicalGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to KlingelnbergCycloPalloidConicalGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh(self) -> '_2259.KlingelnbergCycloPalloidHypoidGearMesh':
        """KlingelnbergCycloPalloidHypoidGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        if _2259.KlingelnbergCycloPalloidHypoidGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to KlingelnbergCycloPalloidHypoidGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh(self) -> '_2260.KlingelnbergCycloPalloidSpiralBevelGearMesh':
        """KlingelnbergCycloPalloidSpiralBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        if _2260.KlingelnbergCycloPalloidSpiralBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to KlingelnbergCycloPalloidSpiralBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_spiral_bevel_gear_mesh(self) -> '_2263.SpiralBevelGearMesh':
        """SpiralBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        if _2263.SpiralBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to SpiralBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_straight_bevel_diff_gear_mesh(self) -> '_2265.StraightBevelDiffGearMesh':
        """StraightBevelDiffGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        if _2265.StraightBevelDiffGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to StraightBevelDiffGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_straight_bevel_gear_mesh(self) -> '_2267.StraightBevelGearMesh':
        """StraightBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        if _2267.StraightBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to StraightBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_worm_gear_mesh(self) -> '_2269.WormGearMesh':
        """WormGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        if _2269.WormGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to WormGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design_of_type_zerol_bevel_gear_mesh(self) -> '_2271.ZerolBevelGearMesh':
        """ZerolBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        if _2271.ZerolBevelGearMesh.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to ZerolBevelGearMesh. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a(self) -> '_2695.GearSystemDeflection':
        """GearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2695.GearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to GearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_agma_gleason_conical_gear_system_deflection(self) -> '_2630.AGMAGleasonConicalGearSystemDeflection':
        """AGMAGleasonConicalGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2630.AGMAGleasonConicalGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to AGMAGleasonConicalGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_bevel_differential_gear_system_deflection(self) -> '_2637.BevelDifferentialGearSystemDeflection':
        """BevelDifferentialGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2637.BevelDifferentialGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to BevelDifferentialGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_bevel_differential_planet_gear_system_deflection(self) -> '_2638.BevelDifferentialPlanetGearSystemDeflection':
        """BevelDifferentialPlanetGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2638.BevelDifferentialPlanetGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to BevelDifferentialPlanetGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_bevel_differential_sun_gear_system_deflection(self) -> '_2639.BevelDifferentialSunGearSystemDeflection':
        """BevelDifferentialSunGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2639.BevelDifferentialSunGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to BevelDifferentialSunGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_bevel_gear_system_deflection(self) -> '_2642.BevelGearSystemDeflection':
        """BevelGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2642.BevelGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to BevelGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_concept_gear_system_deflection(self) -> '_2656.ConceptGearSystemDeflection':
        """ConceptGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2656.ConceptGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConceptGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_conical_gear_system_deflection(self) -> '_2660.ConicalGearSystemDeflection':
        """ConicalGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2660.ConicalGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConicalGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_system_deflection(self) -> '_2679.CylindricalGearSystemDeflection':
        """CylindricalGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2679.CylindricalGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_system_deflection_timestep(self) -> '_2680.CylindricalGearSystemDeflectionTimestep':
        """CylindricalGearSystemDeflectionTimestep: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2680.CylindricalGearSystemDeflectionTimestep.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearSystemDeflectionTimestep. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_system_deflection_with_ltca_results(self) -> '_2681.CylindricalGearSystemDeflectionWithLTCAResults':
        """CylindricalGearSystemDeflectionWithLTCAResults: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2681.CylindricalGearSystemDeflectionWithLTCAResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearSystemDeflectionWithLTCAResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_planet_gear_system_deflection(self) -> '_2684.CylindricalPlanetGearSystemDeflection':
        """CylindricalPlanetGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2684.CylindricalPlanetGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalPlanetGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_face_gear_system_deflection(self) -> '_2690.FaceGearSystemDeflection':
        """FaceGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2690.FaceGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to FaceGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_hypoid_gear_system_deflection(self) -> '_2699.HypoidGearSystemDeflection':
        """HypoidGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2699.HypoidGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to HypoidGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_klingelnberg_cyclo_palloid_conical_gear_system_deflection(self) -> '_2704.KlingelnbergCycloPalloidConicalGearSystemDeflection':
        """KlingelnbergCycloPalloidConicalGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2704.KlingelnbergCycloPalloidConicalGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to KlingelnbergCycloPalloidConicalGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(self) -> '_2707.KlingelnbergCycloPalloidHypoidGearSystemDeflection':
        """KlingelnbergCycloPalloidHypoidGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2707.KlingelnbergCycloPalloidHypoidGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to KlingelnbergCycloPalloidHypoidGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(self) -> '_2710.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection':
        """KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2710.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_spiral_bevel_gear_system_deflection(self) -> '_2743.SpiralBevelGearSystemDeflection':
        """SpiralBevelGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2743.SpiralBevelGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to SpiralBevelGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_straight_bevel_diff_gear_system_deflection(self) -> '_2749.StraightBevelDiffGearSystemDeflection':
        """StraightBevelDiffGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2749.StraightBevelDiffGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to StraightBevelDiffGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_straight_bevel_gear_system_deflection(self) -> '_2752.StraightBevelGearSystemDeflection':
        """StraightBevelGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2752.StraightBevelGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to StraightBevelGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_straight_bevel_planet_gear_system_deflection(self) -> '_2753.StraightBevelPlanetGearSystemDeflection':
        """StraightBevelPlanetGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2753.StraightBevelPlanetGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to StraightBevelPlanetGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_straight_bevel_sun_gear_system_deflection(self) -> '_2754.StraightBevelSunGearSystemDeflection':
        """StraightBevelSunGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2754.StraightBevelSunGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to StraightBevelSunGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_worm_gear_system_deflection(self) -> '_2772.WormGearSystemDeflection':
        """WormGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2772.WormGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to WormGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_zerol_bevel_gear_system_deflection(self) -> '_2775.ZerolBevelGearSystemDeflection':
        """ZerolBevelGearSystemDeflection: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _2775.ZerolBevelGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ZerolBevelGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_total_mesh_force_in_wcs(self) -> '_1523.VectorWithLinearAndAngularComponents':
        """VectorWithLinearAndAngularComponents: 'GearATotalMeshForceInWCS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearATotalMeshForceInWCS
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b(self) -> '_2695.GearSystemDeflection':
        """GearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2695.GearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to GearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_agma_gleason_conical_gear_system_deflection(self) -> '_2630.AGMAGleasonConicalGearSystemDeflection':
        """AGMAGleasonConicalGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2630.AGMAGleasonConicalGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to AGMAGleasonConicalGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_bevel_differential_gear_system_deflection(self) -> '_2637.BevelDifferentialGearSystemDeflection':
        """BevelDifferentialGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2637.BevelDifferentialGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to BevelDifferentialGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_bevel_differential_planet_gear_system_deflection(self) -> '_2638.BevelDifferentialPlanetGearSystemDeflection':
        """BevelDifferentialPlanetGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2638.BevelDifferentialPlanetGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to BevelDifferentialPlanetGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_bevel_differential_sun_gear_system_deflection(self) -> '_2639.BevelDifferentialSunGearSystemDeflection':
        """BevelDifferentialSunGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2639.BevelDifferentialSunGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to BevelDifferentialSunGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_bevel_gear_system_deflection(self) -> '_2642.BevelGearSystemDeflection':
        """BevelGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2642.BevelGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to BevelGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_concept_gear_system_deflection(self) -> '_2656.ConceptGearSystemDeflection':
        """ConceptGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2656.ConceptGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConceptGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_conical_gear_system_deflection(self) -> '_2660.ConicalGearSystemDeflection':
        """ConicalGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2660.ConicalGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConicalGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_system_deflection(self) -> '_2679.CylindricalGearSystemDeflection':
        """CylindricalGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2679.CylindricalGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_system_deflection_timestep(self) -> '_2680.CylindricalGearSystemDeflectionTimestep':
        """CylindricalGearSystemDeflectionTimestep: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2680.CylindricalGearSystemDeflectionTimestep.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearSystemDeflectionTimestep. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_system_deflection_with_ltca_results(self) -> '_2681.CylindricalGearSystemDeflectionWithLTCAResults':
        """CylindricalGearSystemDeflectionWithLTCAResults: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2681.CylindricalGearSystemDeflectionWithLTCAResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearSystemDeflectionWithLTCAResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_planet_gear_system_deflection(self) -> '_2684.CylindricalPlanetGearSystemDeflection':
        """CylindricalPlanetGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2684.CylindricalPlanetGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalPlanetGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_face_gear_system_deflection(self) -> '_2690.FaceGearSystemDeflection':
        """FaceGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2690.FaceGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to FaceGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_hypoid_gear_system_deflection(self) -> '_2699.HypoidGearSystemDeflection':
        """HypoidGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2699.HypoidGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to HypoidGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_klingelnberg_cyclo_palloid_conical_gear_system_deflection(self) -> '_2704.KlingelnbergCycloPalloidConicalGearSystemDeflection':
        """KlingelnbergCycloPalloidConicalGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2704.KlingelnbergCycloPalloidConicalGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to KlingelnbergCycloPalloidConicalGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(self) -> '_2707.KlingelnbergCycloPalloidHypoidGearSystemDeflection':
        """KlingelnbergCycloPalloidHypoidGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2707.KlingelnbergCycloPalloidHypoidGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to KlingelnbergCycloPalloidHypoidGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(self) -> '_2710.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection':
        """KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2710.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_spiral_bevel_gear_system_deflection(self) -> '_2743.SpiralBevelGearSystemDeflection':
        """SpiralBevelGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2743.SpiralBevelGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to SpiralBevelGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_straight_bevel_diff_gear_system_deflection(self) -> '_2749.StraightBevelDiffGearSystemDeflection':
        """StraightBevelDiffGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2749.StraightBevelDiffGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to StraightBevelDiffGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_straight_bevel_gear_system_deflection(self) -> '_2752.StraightBevelGearSystemDeflection':
        """StraightBevelGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2752.StraightBevelGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to StraightBevelGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_straight_bevel_planet_gear_system_deflection(self) -> '_2753.StraightBevelPlanetGearSystemDeflection':
        """StraightBevelPlanetGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2753.StraightBevelPlanetGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to StraightBevelPlanetGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_straight_bevel_sun_gear_system_deflection(self) -> '_2754.StraightBevelSunGearSystemDeflection':
        """StraightBevelSunGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2754.StraightBevelSunGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to StraightBevelSunGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_worm_gear_system_deflection(self) -> '_2772.WormGearSystemDeflection':
        """WormGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2772.WormGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to WormGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_zerol_bevel_gear_system_deflection(self) -> '_2775.ZerolBevelGearSystemDeflection':
        """ZerolBevelGearSystemDeflection: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _2775.ZerolBevelGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ZerolBevelGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_total_mesh_force_in_wcs(self) -> '_1523.VectorWithLinearAndAngularComponents':
        """VectorWithLinearAndAngularComponents: 'GearBTotalMeshForceInWCS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBTotalMeshForceInWCS
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mean_contact_point_in_world_coordinate_system(self) -> 'Vector3D':
        """Vector3D: 'MeanContactPointInWorldCoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanContactPointInWorldCoordinateSystem
        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def rating(self) -> '_351.GearMeshRating':
        """GearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _351.GearMeshRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to GearMeshRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_zerol_bevel_gear_mesh_rating(self) -> '_360.ZerolBevelGearMeshRating':
        """ZerolBevelGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _360.ZerolBevelGearMeshRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to ZerolBevelGearMeshRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_worm_gear_mesh_rating(self) -> '_364.WormGearMeshRating':
        """WormGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _364.WormGearMeshRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to WormGearMeshRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_straight_bevel_gear_mesh_rating(self) -> '_386.StraightBevelGearMeshRating':
        """StraightBevelGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _386.StraightBevelGearMeshRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to StraightBevelGearMeshRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_straight_bevel_diff_gear_mesh_rating(self) -> '_389.StraightBevelDiffGearMeshRating':
        """StraightBevelDiffGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _389.StraightBevelDiffGearMeshRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to StraightBevelDiffGearMeshRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_spiral_bevel_gear_mesh_rating(self) -> '_393.SpiralBevelGearMeshRating':
        """SpiralBevelGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _393.SpiralBevelGearMeshRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to SpiralBevelGearMeshRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_rating(self) -> '_396.KlingelnbergCycloPalloidSpiralBevelGearMeshRating':
        """KlingelnbergCycloPalloidSpiralBevelGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _396.KlingelnbergCycloPalloidSpiralBevelGearMeshRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to KlingelnbergCycloPalloidSpiralBevelGearMeshRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh_rating(self) -> '_399.KlingelnbergCycloPalloidHypoidGearMeshRating':
        """KlingelnbergCycloPalloidHypoidGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _399.KlingelnbergCycloPalloidHypoidGearMeshRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to KlingelnbergCycloPalloidHypoidGearMeshRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_klingelnberg_cyclo_palloid_conical_gear_mesh_rating(self) -> '_402.KlingelnbergCycloPalloidConicalGearMeshRating':
        """KlingelnbergCycloPalloidConicalGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _402.KlingelnbergCycloPalloidConicalGearMeshRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to KlingelnbergCycloPalloidConicalGearMeshRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_hypoid_gear_mesh_rating(self) -> '_429.HypoidGearMeshRating':
        """HypoidGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _429.HypoidGearMeshRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to HypoidGearMeshRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_face_gear_mesh_rating(self) -> '_438.FaceGearMeshRating':
        """FaceGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _438.FaceGearMeshRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to FaceGearMeshRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_cylindrical_gear_mesh_rating(self) -> '_449.CylindricalGearMeshRating':
        """CylindricalGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _449.CylindricalGearMeshRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to CylindricalGearMeshRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_conical_gear_mesh_rating(self) -> '_529.ConicalGearMeshRating':
        """ConicalGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _529.ConicalGearMeshRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to ConicalGearMeshRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_concept_gear_mesh_rating(self) -> '_540.ConceptGearMeshRating':
        """ConceptGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _540.ConceptGearMeshRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to ConceptGearMeshRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_bevel_gear_mesh_rating(self) -> '_544.BevelGearMeshRating':
        """BevelGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _544.BevelGearMeshRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to BevelGearMeshRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_agma_gleason_conical_gear_mesh_rating(self) -> '_555.AGMAGleasonConicalGearMeshRating':
        """AGMAGleasonConicalGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _555.AGMAGleasonConicalGearMeshRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to AGMAGleasonConicalGearMeshRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_separations(self) -> 'List[_2715.MeshSeparationsAtFaceWidth]':
        """List[MeshSeparationsAtFaceWidth]: 'MeshSeparations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshSeparations
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def power_flow_results(self) -> '_4023.GearMeshPowerFlow':
        """GearMeshPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        if _4023.GearMeshPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to GearMeshPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_agma_gleason_conical_gear_mesh_power_flow(self) -> '_3968.AGMAGleasonConicalGearMeshPowerFlow':
        """AGMAGleasonConicalGearMeshPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        if _3968.AGMAGleasonConicalGearMeshPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to AGMAGleasonConicalGearMeshPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_bevel_differential_gear_mesh_power_flow(self) -> '_3975.BevelDifferentialGearMeshPowerFlow':
        """BevelDifferentialGearMeshPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        if _3975.BevelDifferentialGearMeshPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to BevelDifferentialGearMeshPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_bevel_gear_mesh_power_flow(self) -> '_3980.BevelGearMeshPowerFlow':
        """BevelGearMeshPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        if _3980.BevelGearMeshPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to BevelGearMeshPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_concept_gear_mesh_power_flow(self) -> '_3993.ConceptGearMeshPowerFlow':
        """ConceptGearMeshPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        if _3993.ConceptGearMeshPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to ConceptGearMeshPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_conical_gear_mesh_power_flow(self) -> '_3996.ConicalGearMeshPowerFlow':
        """ConicalGearMeshPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        if _3996.ConicalGearMeshPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to ConicalGearMeshPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_cylindrical_gear_mesh_power_flow(self) -> '_4012.CylindricalGearMeshPowerFlow':
        """CylindricalGearMeshPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        if _4012.CylindricalGearMeshPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to CylindricalGearMeshPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_face_gear_mesh_power_flow(self) -> '_4018.FaceGearMeshPowerFlow':
        """FaceGearMeshPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        if _4018.FaceGearMeshPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to FaceGearMeshPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_hypoid_gear_mesh_power_flow(self) -> '_4027.HypoidGearMeshPowerFlow':
        """HypoidGearMeshPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        if _4027.HypoidGearMeshPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to HypoidGearMeshPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_klingelnberg_cyclo_palloid_conical_gear_mesh_power_flow(self) -> '_4031.KlingelnbergCycloPalloidConicalGearMeshPowerFlow':
        """KlingelnbergCycloPalloidConicalGearMeshPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        if _4031.KlingelnbergCycloPalloidConicalGearMeshPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to KlingelnbergCycloPalloidConicalGearMeshPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh_power_flow(self) -> '_4034.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow':
        """KlingelnbergCycloPalloidHypoidGearMeshPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        if _4034.KlingelnbergCycloPalloidHypoidGearMeshPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to KlingelnbergCycloPalloidHypoidGearMeshPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_power_flow(self) -> '_4037.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow':
        """KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        if _4037.KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to KlingelnbergCycloPalloidSpiralBevelGearMeshPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_spiral_bevel_gear_mesh_power_flow(self) -> '_4066.SpiralBevelGearMeshPowerFlow':
        """SpiralBevelGearMeshPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        if _4066.SpiralBevelGearMeshPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to SpiralBevelGearMeshPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_straight_bevel_diff_gear_mesh_power_flow(self) -> '_4072.StraightBevelDiffGearMeshPowerFlow':
        """StraightBevelDiffGearMeshPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        if _4072.StraightBevelDiffGearMeshPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to StraightBevelDiffGearMeshPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_straight_bevel_gear_mesh_power_flow(self) -> '_4075.StraightBevelGearMeshPowerFlow':
        """StraightBevelGearMeshPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        if _4075.StraightBevelGearMeshPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to StraightBevelGearMeshPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_worm_gear_mesh_power_flow(self) -> '_4091.WormGearMeshPowerFlow':
        """WormGearMeshPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        if _4091.WormGearMeshPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to WormGearMeshPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_zerol_bevel_gear_mesh_power_flow(self) -> '_4094.ZerolBevelGearMeshPowerFlow':
        """ZerolBevelGearMeshPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        if _4094.ZerolBevelGearMeshPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to ZerolBevelGearMeshPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

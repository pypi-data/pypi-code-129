"""_4156.py

GearMeshCompoundPowerFlow
"""


from typing import List

from mastapy.gears.rating import _356
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.worm import _368
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.face import _437
from mastapy.gears.rating.cylindrical import _457
from mastapy.gears.rating.conical import _534
from mastapy.gears.rating.concept import _539
from mastapy.system_model.analyses_and_results.power_flows import _4023
from mastapy.system_model.analyses_and_results.power_flows.compound import _4162
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'GearMeshCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshCompoundPowerFlow',)


class GearMeshCompoundPowerFlow(_4162.InterMountableComponentConnectionCompoundPowerFlow):
    """GearMeshCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearMeshCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_mesh_duty_cycle_rating(self) -> '_356.MeshDutyCycleRating':
        """MeshDutyCycleRating: 'GearMeshDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshDutyCycleRating
        if _356.MeshDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh_duty_cycle_rating to MeshDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_mesh_duty_cycle_rating_of_type_worm_mesh_duty_cycle_rating(self) -> '_368.WormMeshDutyCycleRating':
        """WormMeshDutyCycleRating: 'GearMeshDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshDutyCycleRating
        if _368.WormMeshDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh_duty_cycle_rating to WormMeshDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_mesh_duty_cycle_rating_of_type_face_gear_mesh_duty_cycle_rating(self) -> '_437.FaceGearMeshDutyCycleRating':
        """FaceGearMeshDutyCycleRating: 'GearMeshDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshDutyCycleRating
        if _437.FaceGearMeshDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh_duty_cycle_rating to FaceGearMeshDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_mesh_duty_cycle_rating_of_type_cylindrical_mesh_duty_cycle_rating(self) -> '_457.CylindricalMeshDutyCycleRating':
        """CylindricalMeshDutyCycleRating: 'GearMeshDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshDutyCycleRating
        if _457.CylindricalMeshDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh_duty_cycle_rating to CylindricalMeshDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_mesh_duty_cycle_rating_of_type_conical_mesh_duty_cycle_rating(self) -> '_534.ConicalMeshDutyCycleRating':
        """ConicalMeshDutyCycleRating: 'GearMeshDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshDutyCycleRating
        if _534.ConicalMeshDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh_duty_cycle_rating to ConicalMeshDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_mesh_duty_cycle_rating_of_type_concept_gear_mesh_duty_cycle_rating(self) -> '_539.ConceptGearMeshDutyCycleRating':
        """ConceptGearMeshDutyCycleRating: 'GearMeshDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshDutyCycleRating
        if _539.ConceptGearMeshDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_mesh_duty_cycle_rating to ConceptGearMeshDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases(self) -> 'List[_4023.GearMeshPowerFlow]':
        """List[GearMeshPowerFlow]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4023.GearMeshPowerFlow]':
        """List[GearMeshPowerFlow]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

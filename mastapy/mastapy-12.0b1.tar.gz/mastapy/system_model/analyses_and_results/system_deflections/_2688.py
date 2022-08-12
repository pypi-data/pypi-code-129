"""_2688.py

FaceGearMeshSystemDeflection
"""


from mastapy._internal import constructor
from mastapy.gears.rating.face import _438
from mastapy.system_model.connections_and_sockets.gears import _2251
from mastapy.system_model.analyses_and_results.static_loads import _6799
from mastapy.gears.gear_designs.conical import _1148
from mastapy.system_model.analyses_and_results.power_flows import _4018
from mastapy.system_model.analyses_and_results.system_deflections import _2693
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'FaceGearMeshSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMeshSystemDeflection',)


class FaceGearMeshSystemDeflection(_2693.GearMeshSystemDeflection):
    """FaceGearMeshSystemDeflection

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearMeshSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angular_misalignment_in_surface_of_action(self) -> 'float':
        """float: 'AngularMisalignmentInSurfaceOfAction' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngularMisalignmentInSurfaceOfAction
        return temp

    @property
    def linear_misalignment_in_surface_of_action(self) -> 'float':
        """float: 'LinearMisalignmentInSurfaceOfAction' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LinearMisalignmentInSurfaceOfAction
        return temp

    @property
    def pinion_angular_misalignment_in_surface_of_action(self) -> 'float':
        """float: 'PinionAngularMisalignmentInSurfaceOfAction' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionAngularMisalignmentInSurfaceOfAction
        return temp

    @property
    def wheel_angular_misalignment_in_surface_of_action(self) -> 'float':
        """float: 'WheelAngularMisalignmentInSurfaceOfAction' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelAngularMisalignmentInSurfaceOfAction
        return temp

    @property
    def rating(self) -> '_438.FaceGearMeshRating':
        """FaceGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_438.FaceGearMeshRating':
        """FaceGearMeshRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2251.FaceGearMesh':
        """FaceGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6799.FaceGearMeshLoadCase':
        """FaceGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def misalignments_pinion(self) -> '_1148.ConicalMeshMisalignments':
        """ConicalMeshMisalignments: 'MisalignmentsPinion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MisalignmentsPinion
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def misalignments_total(self) -> '_1148.ConicalMeshMisalignments':
        """ConicalMeshMisalignments: 'MisalignmentsTotal' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MisalignmentsTotal
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def misalignments_wheel(self) -> '_1148.ConicalMeshMisalignments':
        """ConicalMeshMisalignments: 'MisalignmentsWheel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MisalignmentsWheel
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4018.FaceGearMeshPowerFlow':
        """FaceGearMeshPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

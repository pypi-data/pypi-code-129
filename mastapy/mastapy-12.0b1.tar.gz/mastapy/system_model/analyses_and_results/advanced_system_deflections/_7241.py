"""_7241.py

FaceGearMeshAdvancedSystemDeflection
"""


from typing import List

from mastapy.gears.rating.face import _438
from mastapy._internal import constructor, conversion
from mastapy.system_model.connections_and_sockets.gears import _2251
from mastapy.system_model.analyses_and_results.static_loads import _6799
from mastapy.system_model.analyses_and_results.system_deflections import _2688
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7246
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'FaceGearMeshAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMeshAdvancedSystemDeflection',)


class FaceGearMeshAdvancedSystemDeflection(_7246.GearMeshAdvancedSystemDeflection):
    """FaceGearMeshAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearMeshAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def connection_system_deflection_results(self) -> 'List[_2688.FaceGearMeshSystemDeflection]':
        """List[FaceGearMeshSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionSystemDeflectionResults
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

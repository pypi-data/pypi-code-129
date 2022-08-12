"""_7316.py

ZerolBevelGearMeshAdvancedSystemDeflection
"""


from typing import List

from mastapy.gears.rating.zerol_bevel import _360
from mastapy._internal import constructor, conversion
from mastapy.system_model.connections_and_sockets.gears import _2271
from mastapy.system_model.analyses_and_results.static_loads import _6900
from mastapy.system_model.analyses_and_results.system_deflections import _2773
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7202
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'ZerolBevelGearMeshAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearMeshAdvancedSystemDeflection',)


class ZerolBevelGearMeshAdvancedSystemDeflection(_7202.BevelGearMeshAdvancedSystemDeflection):
    """ZerolBevelGearMeshAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearMeshAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_detailed_analysis(self) -> '_360.ZerolBevelGearMeshRating':
        """ZerolBevelGearMeshRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2271.ZerolBevelGearMesh':
        """ZerolBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6900.ZerolBevelGearMeshLoadCase':
        """ZerolBevelGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_system_deflection_results(self) -> 'List[_2773.ZerolBevelGearMeshSystemDeflection]':
        """List[ZerolBevelGearMeshSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionSystemDeflectionResults
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

"""_7313.py

WormGearMeshAdvancedSystemDeflection
"""


from typing import List

from mastapy.gears.rating.worm import _364
from mastapy._internal import constructor, conversion
from mastapy.system_model.connections_and_sockets.gears import _2269
from mastapy.system_model.analyses_and_results.static_loads import _6897
from mastapy.system_model.analyses_and_results.system_deflections import _2770
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7246
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'WormGearMeshAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearMeshAdvancedSystemDeflection',)


class WormGearMeshAdvancedSystemDeflection(_7246.GearMeshAdvancedSystemDeflection):
    """WormGearMeshAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearMeshAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_detailed_analysis(self) -> '_364.WormGearMeshRating':
        """WormGearMeshRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2269.WormGearMesh':
        """WormGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6897.WormGearMeshLoadCase':
        """WormGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_system_deflection_results(self) -> 'List[_2770.WormGearMeshSystemDeflection]':
        """List[WormGearMeshSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionSystemDeflectionResults
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

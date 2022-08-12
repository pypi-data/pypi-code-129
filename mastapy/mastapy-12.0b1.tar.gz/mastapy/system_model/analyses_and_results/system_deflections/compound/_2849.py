"""_2849.py

HypoidGearMeshCompoundSystemDeflection
"""


from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2255
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2697
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2790
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'HypoidGearMeshCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearMeshCompoundSystemDeflection',)


class HypoidGearMeshCompoundSystemDeflection(_2790.AGMAGleasonConicalGearMeshCompoundSystemDeflection):
    """HypoidGearMeshCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearMeshCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2255.HypoidGearMesh':
        """HypoidGearMesh: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2255.HypoidGearMesh':
        """HypoidGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_2697.HypoidGearMeshSystemDeflection]':
        """List[HypoidGearMeshSystemDeflection]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_2697.HypoidGearMeshSystemDeflection]':
        """List[HypoidGearMeshSystemDeflection]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

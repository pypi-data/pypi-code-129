"""_2850.py

HypoidGearSetCompoundSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model.gears import _2474
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2698
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2848, _2849, _2791
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'HypoidGearSetCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('HypoidGearSetCompoundSystemDeflection',)


class HypoidGearSetCompoundSystemDeflection(_2791.AGMAGleasonConicalGearSetCompoundSystemDeflection):
    """HypoidGearSetCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HypoidGearSetCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2474.HypoidGearSet':
        """HypoidGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2474.HypoidGearSet':
        """HypoidGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_2698.HypoidGearSetSystemDeflection]':
        """List[HypoidGearSetSystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_gears_compound_system_deflection(self) -> 'List[_2848.HypoidGearCompoundSystemDeflection]':
        """List[HypoidGearCompoundSystemDeflection]: 'HypoidGearsCompoundSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearsCompoundSystemDeflection
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_meshes_compound_system_deflection(self) -> 'List[_2849.HypoidGearMeshCompoundSystemDeflection]':
        """List[HypoidGearMeshCompoundSystemDeflection]: 'HypoidMeshesCompoundSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidMeshesCompoundSystemDeflection
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_2698.HypoidGearSetSystemDeflection]':
        """List[HypoidGearSetSystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

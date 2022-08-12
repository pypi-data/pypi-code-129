"""_2806.py

ClutchCompoundSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2517
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2647
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2822
from mastapy._internal.python_net import python_net_import

_CLUTCH_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'ClutchCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchCompoundSystemDeflection',)


class ClutchCompoundSystemDeflection(_2822.CouplingCompoundSystemDeflection):
    """ClutchCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CLUTCH_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2517.Clutch':
        """Clutch: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2517.Clutch':
        """Clutch: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_2647.ClutchSystemDeflection]':
        """List[ClutchSystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_2647.ClutchSystemDeflection]':
        """List[ClutchSystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

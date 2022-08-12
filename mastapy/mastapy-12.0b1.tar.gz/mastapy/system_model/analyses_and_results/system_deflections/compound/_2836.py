"""_2836.py

DatumCompoundSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model import _2388
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2685
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2810
from mastapy._internal.python_net import python_net_import

_DATUM_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'DatumCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('DatumCompoundSystemDeflection',)


class DatumCompoundSystemDeflection(_2810.ComponentCompoundSystemDeflection):
    """DatumCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _DATUM_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DatumCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2388.Datum':
        """Datum: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_2685.DatumSystemDeflection]':
        """List[DatumSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_2685.DatumSystemDeflection]':
        """List[DatumSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

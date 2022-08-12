"""_2821.py

ConnectorCompoundSystemDeflection
"""


from typing import List

from mastapy.system_model.analyses_and_results.system_deflections import _2662
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2863
from mastapy._internal.python_net import python_net_import

_CONNECTOR_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'ConnectorCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectorCompoundSystemDeflection',)


class ConnectorCompoundSystemDeflection(_2863.MountableComponentCompoundSystemDeflection):
    """ConnectorCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConnectorCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self) -> 'List[_2662.ConnectorSystemDeflection]':
        """List[ConnectorSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_2662.ConnectorSystemDeflection]':
        """List[ConnectorSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

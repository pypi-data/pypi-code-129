"""_6345.py

ClutchConnectionCompoundDynamicAnalysis
"""


from typing import List

from mastapy.system_model.connections_and_sockets.couplings import _2282
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6214
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6361
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound', 'ClutchConnectionCompoundDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchConnectionCompoundDynamicAnalysis',)


class ClutchConnectionCompoundDynamicAnalysis(_6361.CouplingConnectionCompoundDynamicAnalysis):
    """ClutchConnectionCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchConnectionCompoundDynamicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2282.ClutchConnection':
        """ClutchConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2282.ClutchConnection':
        """ClutchConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_analysis_cases_ready(self) -> 'List[_6214.ClutchConnectionDynamicAnalysis]':
        """List[ClutchConnectionDynamicAnalysis]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_6214.ClutchConnectionDynamicAnalysis]':
        """List[ClutchConnectionDynamicAnalysis]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

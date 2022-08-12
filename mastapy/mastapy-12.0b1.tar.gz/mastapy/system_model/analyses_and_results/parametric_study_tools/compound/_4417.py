"""_4417.py

CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool
"""


from typing import List

from mastapy.system_model.analyses_and_results.parametric_study_tools import _4270
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4397
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool',)


class CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool(_4397.CoaxialConnectionCompoundParametricStudyTool):
    """CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CycloidalDiscCentralBearingConnectionCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(self) -> 'List[_4270.CycloidalDiscCentralBearingConnectionParametricStudyTool]':
        """List[CycloidalDiscCentralBearingConnectionParametricStudyTool]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases(self) -> 'List[_4270.CycloidalDiscCentralBearingConnectionParametricStudyTool]':
        """List[CycloidalDiscCentralBearingConnectionParametricStudyTool]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

"""_6090.py

ConnectionCompoundHarmonicAnalysisOfSingleExcitation
"""


from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5960
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7451
from mastapy._internal.python_net import python_net_import

_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'ConnectionCompoundHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectionCompoundHarmonicAnalysisOfSingleExcitation',)


class ConnectionCompoundHarmonicAnalysisOfSingleExcitation(_7451.ConnectionCompoundAnalysis):
    """ConnectionCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConnectionCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(self) -> 'List[_5960.ConnectionHarmonicAnalysisOfSingleExcitation]':
        """List[ConnectionHarmonicAnalysisOfSingleExcitation]: 'ConnectionAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def connection_analysis_cases_ready(self) -> 'List[_5960.ConnectionHarmonicAnalysisOfSingleExcitation]':
        """List[ConnectionHarmonicAnalysisOfSingleExcitation]: 'ConnectionAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

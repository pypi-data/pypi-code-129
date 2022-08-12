"""_7455.py

DesignEntityCompoundAnalysis
"""


from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results import _2590
from mastapy._internal.python_net import python_net_import

_DESIGN_ENTITY_COMPOUND_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases', 'DesignEntityCompoundAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('DesignEntityCompoundAnalysis',)


class DesignEntityCompoundAnalysis(_2590.DesignEntityAnalysis):
    """DesignEntityCompoundAnalysis

    This is a mastapy class.
    """

    TYPE = _DESIGN_ENTITY_COMPOUND_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DesignEntityCompoundAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis_time(self) -> 'float':
        """float: 'AnalysisTime' is the original name of this property."""

        temp = self.wrapped.AnalysisTime
        return temp

    @analysis_time.setter
    def analysis_time(self, value: 'float'):
        self.wrapped.AnalysisTime = float(value) if value else 0.0

    @property
    def real_name_in_context_name(self) -> 'str':
        """str: 'RealNameInContextName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RealNameInContextName
        return temp

"""_7447.py

AnalysisCase
"""


from mastapy._internal import constructor
from mastapy.utility import _1538
from mastapy.system_model import _2147
from mastapy.system_model.analyses_and_results import _2590, _2589
from mastapy._internal.python_net import python_net_import

_ANALYSIS_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases', 'AnalysisCase')


__docformat__ = 'restructuredtext en'
__all__ = ('AnalysisCase',)


class AnalysisCase(_2589.Context):
    """AnalysisCase

    This is a mastapy class.
    """

    TYPE = _ANALYSIS_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AnalysisCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def analysis_setup_time(self) -> 'float':
        """float: 'AnalysisSetupTime' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AnalysisSetupTime
        return temp

    @property
    def load_case_name(self) -> 'str':
        """str: 'LoadCaseName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadCaseName
        return temp

    @property
    def analysis_run_information(self) -> '_1538.AnalysisRunInformation':
        """AnalysisRunInformation: 'AnalysisRunInformation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AnalysisRunInformation
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def results_ready(self) -> 'bool':
        """bool: 'ResultsReady' is the original name of this property."""

        temp = self.wrapped.ResultsReady
        return temp

    @results_ready.setter
    def results_ready(self, value: 'bool'):
        self.wrapped.ResultsReady = bool(value) if value else False

    def results_for(self, design_entity: '_2147.DesignEntity') -> '_2590.DesignEntityAnalysis':
        """ 'ResultsFor' is the original name of this method.

        Args:
            design_entity (mastapy.system_model.DesignEntity)

        Returns:
            mastapy.system_model.analyses_and_results.DesignEntityAnalysis
        """

        method_result = self.wrapped.ResultsFor(design_entity.wrapped if design_entity else None)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def perform_analysis(self):
        """ 'PerformAnalysis' is the original name of this method."""

        self.wrapped.PerformAnalysis()

"""_2581.py

StabilityAnalysis
"""


from mastapy.system_model.analyses_and_results.stability_analyses import _3804
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7462
from mastapy._internal.python_net import python_net_import

_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'StabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StabilityAnalysis',)


class StabilityAnalysis(_7462.StaticLoadAnalysisCase):
    """StabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def stability_analysis_options(self) -> '_3804.StabilityAnalysisOptions':
        """StabilityAnalysisOptions: 'StabilityAnalysisOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StabilityAnalysisOptions
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

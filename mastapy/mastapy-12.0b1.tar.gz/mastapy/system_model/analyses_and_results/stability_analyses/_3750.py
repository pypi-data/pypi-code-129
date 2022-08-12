"""_3750.py

ExternalCADModelStabilityAnalysis
"""


from mastapy.system_model.part_model import _2392
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6797
from mastapy.system_model.analyses_and_results.stability_analyses import _3722
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'ExternalCADModelStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ExternalCADModelStabilityAnalysis',)


class ExternalCADModelStabilityAnalysis(_3722.ComponentStabilityAnalysis):
    """ExternalCADModelStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ExternalCADModelStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2392.ExternalCADModel':
        """ExternalCADModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6797.ExternalCADModelLoadCase':
        """ExternalCADModelLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

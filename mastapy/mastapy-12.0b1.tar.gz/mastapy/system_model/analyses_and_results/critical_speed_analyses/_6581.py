"""_6581.py

UnbalancedMassCriticalSpeedAnalysis
"""


from mastapy.system_model.part_model import _2417
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6894
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6582
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'UnbalancedMassCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('UnbalancedMassCriticalSpeedAnalysis',)


class UnbalancedMassCriticalSpeedAnalysis(_6582.VirtualComponentCriticalSpeedAnalysis):
    """UnbalancedMassCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'UnbalancedMassCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2417.UnbalancedMass':
        """UnbalancedMass: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6894.UnbalancedMassLoadCase':
        """UnbalancedMassLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

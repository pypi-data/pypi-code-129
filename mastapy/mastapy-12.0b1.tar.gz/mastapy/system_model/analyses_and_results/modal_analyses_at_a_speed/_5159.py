"""_5159.py

SynchroniserSleeveModalAnalysisAtASpeed
"""


from mastapy.system_model.part_model.couplings import _2545
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6884
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5158
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'SynchroniserSleeveModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserSleeveModalAnalysisAtASpeed',)


class SynchroniserSleeveModalAnalysisAtASpeed(_5158.SynchroniserPartModalAnalysisAtASpeed):
    """SynchroniserSleeveModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SynchroniserSleeveModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2545.SynchroniserSleeve':
        """SynchroniserSleeve: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6884.SynchroniserSleeveLoadCase':
        """SynchroniserSleeveLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

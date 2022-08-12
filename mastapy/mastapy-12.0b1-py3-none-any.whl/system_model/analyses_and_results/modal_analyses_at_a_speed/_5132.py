"""_5132.py

RingPinsModalAnalysisAtASpeed
"""


from mastapy.system_model.part_model.cycloidal import _2509
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6857
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5120
from mastapy._internal.python_net import python_net_import

_RING_PINS_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'RingPinsModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('RingPinsModalAnalysisAtASpeed',)


class RingPinsModalAnalysisAtASpeed(_5120.MountableComponentModalAnalysisAtASpeed):
    """RingPinsModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _RING_PINS_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RingPinsModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2509.RingPins':
        """RingPins: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6857.RingPinsLoadCase':
        """RingPinsLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

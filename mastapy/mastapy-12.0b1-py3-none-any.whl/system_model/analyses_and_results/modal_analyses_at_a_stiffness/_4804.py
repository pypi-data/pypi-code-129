"""_4804.py

BoltModalAnalysisAtAStiffness
"""


from mastapy.system_model.part_model import _2382
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6746
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4809
from mastapy._internal.python_net import python_net_import

_BOLT_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'BoltModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltModalAnalysisAtAStiffness',)


class BoltModalAnalysisAtAStiffness(_4809.ComponentModalAnalysisAtAStiffness):
    """BoltModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _BOLT_MODAL_ANALYSIS_AT_A_STIFFNESS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BoltModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2382.Bolt':
        """Bolt: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6746.BoltLoadCase':
        """BoltLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

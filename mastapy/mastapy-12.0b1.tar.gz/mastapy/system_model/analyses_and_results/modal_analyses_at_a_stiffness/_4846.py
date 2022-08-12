"""_4846.py

GuideDxfModelModalAnalysisAtAStiffness
"""


from mastapy.system_model.part_model import _2395
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6810
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import _4809
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness', 'GuideDxfModelModalAnalysisAtAStiffness')


__docformat__ = 'restructuredtext en'
__all__ = ('GuideDxfModelModalAnalysisAtAStiffness',)


class GuideDxfModelModalAnalysisAtAStiffness(_4809.ComponentModalAnalysisAtAStiffness):
    """GuideDxfModelModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_MODAL_ANALYSIS_AT_A_STIFFNESS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GuideDxfModelModalAnalysisAtAStiffness.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2395.GuideDxfModel':
        """GuideDxfModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6810.GuideDxfModelLoadCase':
        """GuideDxfModelLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

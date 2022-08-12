"""_5157.py

SynchroniserModalAnalysisAtASpeed
"""


from mastapy.system_model.part_model.couplings import _2541
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6882
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5141
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'SynchroniserModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserModalAnalysisAtASpeed',)


class SynchroniserModalAnalysisAtASpeed(_5141.SpecialisedAssemblyModalAnalysisAtASpeed):
    """SynchroniserModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SynchroniserModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2541.Synchroniser':
        """Synchroniser: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6882.SynchroniserLoadCase':
        """SynchroniserLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

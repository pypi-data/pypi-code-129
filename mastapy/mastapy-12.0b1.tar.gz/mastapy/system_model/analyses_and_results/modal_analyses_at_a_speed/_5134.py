"""_5134.py

RollingRingAssemblyModalAnalysisAtASpeed
"""


from mastapy.system_model.part_model.couplings import _2536
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6859
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5141
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'RollingRingAssemblyModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingAssemblyModalAnalysisAtASpeed',)


class RollingRingAssemblyModalAnalysisAtASpeed(_5141.SpecialisedAssemblyModalAnalysisAtASpeed):
    """RollingRingAssemblyModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RollingRingAssemblyModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2536.RollingRingAssembly':
        """RollingRingAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6859.RollingRingAssemblyLoadCase':
        """RollingRingAssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

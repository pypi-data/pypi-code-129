"""_5118.py

MassDiscModalAnalysisAtASpeed
"""


from typing import List

from mastapy.system_model.part_model import _2402
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6835
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5165
from mastapy._internal.python_net import python_net_import

_MASS_DISC_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'MassDiscModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('MassDiscModalAnalysisAtASpeed',)


class MassDiscModalAnalysisAtASpeed(_5165.VirtualComponentModalAnalysisAtASpeed):
    """MassDiscModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _MASS_DISC_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MassDiscModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2402.MassDisc':
        """MassDisc: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6835.MassDiscLoadCase':
        """MassDiscLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[MassDiscModalAnalysisAtASpeed]':
        """List[MassDiscModalAnalysisAtASpeed]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

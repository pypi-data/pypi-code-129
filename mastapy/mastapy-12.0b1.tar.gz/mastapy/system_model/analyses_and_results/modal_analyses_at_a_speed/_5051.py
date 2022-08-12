"""_5051.py

BearingModalAnalysisAtASpeed
"""


from typing import List

from mastapy.system_model.part_model import _2380
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6734
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5079
from mastapy._internal.python_net import python_net_import

_BEARING_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'BearingModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingModalAnalysisAtASpeed',)


class BearingModalAnalysisAtASpeed(_5079.ConnectorModalAnalysisAtASpeed):
    """BearingModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _BEARING_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BearingModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2380.Bearing':
        """Bearing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6734.BearingLoadCase':
        """BearingLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[BearingModalAnalysisAtASpeed]':
        """List[BearingModalAnalysisAtASpeed]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

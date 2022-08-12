"""_5099.py

FEPartModalAnalysisAtASpeed
"""


from typing import List

from mastapy.system_model.part_model import _2393
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6801
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5045
from mastapy._internal.python_net import python_net_import

_FE_PART_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'FEPartModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('FEPartModalAnalysisAtASpeed',)


class FEPartModalAnalysisAtASpeed(_5045.AbstractShaftOrHousingModalAnalysisAtASpeed):
    """FEPartModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _FE_PART_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FEPartModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2393.FEPart':
        """FEPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6801.FEPartLoadCase':
        """FEPartLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[FEPartModalAnalysisAtASpeed]':
        """List[FEPartModalAnalysisAtASpeed]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

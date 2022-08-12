"""_6555.py

ShaftCriticalSpeedAnalysis
"""


from typing import List

from mastapy.system_model.part_model.shaft_model import _2422
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6864
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6459
from mastapy._internal.python_net import python_net_import

_SHAFT_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'ShaftCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftCriticalSpeedAnalysis',)


class ShaftCriticalSpeedAnalysis(_6459.AbstractShaftCriticalSpeedAnalysis):
    """ShaftCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShaftCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2422.Shaft':
        """Shaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6864.ShaftLoadCase':
        """ShaftLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[ShaftCriticalSpeedAnalysis]':
        """List[ShaftCriticalSpeedAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

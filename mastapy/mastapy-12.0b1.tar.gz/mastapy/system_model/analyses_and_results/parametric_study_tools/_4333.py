"""_4333.py

RingPinsParametricStudyTool
"""


from typing import List

from mastapy.system_model.part_model.cycloidal import _2509
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6857
from mastapy.system_model.analyses_and_results.system_deflections import _2728
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4311
from mastapy._internal.python_net import python_net_import

_RING_PINS_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'RingPinsParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('RingPinsParametricStudyTool',)


class RingPinsParametricStudyTool(_4311.MountableComponentParametricStudyTool):
    """RingPinsParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _RING_PINS_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RingPinsParametricStudyTool.TYPE'):
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

    @property
    def component_system_deflection_results(self) -> 'List[_2728.RingPinsSystemDeflection]':
        """List[RingPinsSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentSystemDeflectionResults
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

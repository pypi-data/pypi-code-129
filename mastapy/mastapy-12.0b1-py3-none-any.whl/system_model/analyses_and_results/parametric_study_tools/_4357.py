"""_4357.py

SynchroniserHalfParametricStudyTool
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2543
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6881
from mastapy.system_model.analyses_and_results.system_deflections import _2755
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4359
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'SynchroniserHalfParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserHalfParametricStudyTool',)


class SynchroniserHalfParametricStudyTool(_4359.SynchroniserPartParametricStudyTool):
    """SynchroniserHalfParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SynchroniserHalfParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2543.SynchroniserHalf':
        """SynchroniserHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6881.SynchroniserHalfLoadCase':
        """SynchroniserHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_system_deflection_results(self) -> 'List[_2755.SynchroniserHalfSystemDeflection]':
        """List[SynchroniserHalfSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentSystemDeflectionResults
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

"""_4234.py

BearingParametricStudyTool
"""


from typing import List

from mastapy.system_model.part_model import _2380
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6734
from mastapy.bearings.bearing_results import _1896
from mastapy.system_model.analyses_and_results.system_deflections import _2632
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4262
from mastapy._internal.python_net import python_net_import

_BEARING_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'BearingParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingParametricStudyTool',)


class BearingParametricStudyTool(_4262.ConnectorParametricStudyTool):
    """BearingParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BEARING_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BearingParametricStudyTool.TYPE'):
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
    def bearing_duty_cycle_results(self) -> 'List[_1896.LoadedBearingDutyCycle]':
        """List[LoadedBearingDutyCycle]: 'BearingDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDutyCycleResults
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_system_deflection_results(self) -> 'List[_2632.BearingSystemDeflection]':
        """List[BearingSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentSystemDeflectionResults
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[BearingParametricStudyTool]':
        """List[BearingParametricStudyTool]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

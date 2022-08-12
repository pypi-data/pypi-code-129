"""_4285.py

ExternalCADModelParametricStudyTool
"""


from typing import List

from mastapy.system_model.part_model import _2392
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6797
from mastapy.system_model.analyses_and_results.system_deflections import _2686
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4251
from mastapy._internal.python_net import python_net_import

_EXTERNAL_CAD_MODEL_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'ExternalCADModelParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('ExternalCADModelParametricStudyTool',)


class ExternalCADModelParametricStudyTool(_4251.ComponentParametricStudyTool):
    """ExternalCADModelParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _EXTERNAL_CAD_MODEL_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ExternalCADModelParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2392.ExternalCADModel':
        """ExternalCADModel: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6797.ExternalCADModelLoadCase':
        """ExternalCADModelLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_system_deflection_results(self) -> 'List[_2686.ExternalCADModelSystemDeflection]':
        """List[ExternalCADModelSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentSystemDeflectionResults
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

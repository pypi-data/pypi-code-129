"""_4346.py

SpringDamperConnectionParametricStudyTool
"""


from typing import List

from mastapy.system_model.connections_and_sockets.couplings import _2290
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6870
from mastapy.system_model.analyses_and_results.system_deflections import _2744
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4263
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'SpringDamperConnectionParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperConnectionParametricStudyTool',)


class SpringDamperConnectionParametricStudyTool(_4263.CouplingConnectionParametricStudyTool):
    """SpringDamperConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperConnectionParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2290.SpringDamperConnection':
        """SpringDamperConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6870.SpringDamperConnectionLoadCase':
        """SpringDamperConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_system_deflection_results(self) -> 'List[_2744.SpringDamperConnectionSystemDeflection]':
        """List[SpringDamperConnectionSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionSystemDeflectionResults
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

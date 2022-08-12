"""_4245.py

BoltedJointParametricStudyTool
"""


from typing import List

from mastapy.system_model.part_model import _2383
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6745
from mastapy.system_model.analyses_and_results.system_deflections import _2643
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4342
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'BoltedJointParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltedJointParametricStudyTool',)


class BoltedJointParametricStudyTool(_4342.SpecialisedAssemblyParametricStudyTool):
    """BoltedJointParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BoltedJointParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2383.BoltedJoint':
        """BoltedJoint: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6745.BoltedJointLoadCase':
        """BoltedJointLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2643.BoltedJointSystemDeflection]':
        """List[BoltedJointSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblySystemDeflectionResults
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

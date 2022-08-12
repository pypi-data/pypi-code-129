"""_4288.py

FaceGearSetParametricStudyTool
"""


from typing import List

from mastapy.system_model.part_model.gears import _2468
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6800
from mastapy.system_model.analyses_and_results.system_deflections import _2689
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4287, _4286, _4293
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'FaceGearSetParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetParametricStudyTool',)


class FaceGearSetParametricStudyTool(_4293.GearSetParametricStudyTool):
    """FaceGearSetParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearSetParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2468.FaceGearSet':
        """FaceGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6800.FaceGearSetLoadCase':
        """FaceGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2689.FaceGearSetSystemDeflection]':
        """List[FaceGearSetSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblySystemDeflectionResults
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_gears_parametric_study_tool(self) -> 'List[_4287.FaceGearParametricStudyTool]':
        """List[FaceGearParametricStudyTool]: 'FaceGearsParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearsParametricStudyTool
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_meshes_parametric_study_tool(self) -> 'List[_4286.FaceGearMeshParametricStudyTool]':
        """List[FaceGearMeshParametricStudyTool]: 'FaceMeshesParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceMeshesParametricStudyTool
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

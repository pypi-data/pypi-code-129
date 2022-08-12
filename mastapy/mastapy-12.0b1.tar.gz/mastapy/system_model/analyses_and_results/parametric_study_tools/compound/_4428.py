"""_4428.py

FaceGearSetCompoundParametricStudyTool
"""


from typing import List

from mastapy.system_model.part_model.gears import _2468
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4288
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4426, _4427, _4433
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'FaceGearSetCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetCompoundParametricStudyTool',)


class FaceGearSetCompoundParametricStudyTool(_4433.GearSetCompoundParametricStudyTool):
    """FaceGearSetCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearSetCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2468.FaceGearSet':
        """FaceGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def assembly_analysis_cases_ready(self) -> 'List[_4288.FaceGearSetParametricStudyTool]':
        """List[FaceGearSetParametricStudyTool]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_gears_compound_parametric_study_tool(self) -> 'List[_4426.FaceGearCompoundParametricStudyTool]':
        """List[FaceGearCompoundParametricStudyTool]: 'FaceGearsCompoundParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearsCompoundParametricStudyTool
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_meshes_compound_parametric_study_tool(self) -> 'List[_4427.FaceGearMeshCompoundParametricStudyTool]':
        """List[FaceGearMeshCompoundParametricStudyTool]: 'FaceMeshesCompoundParametricStudyTool' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceMeshesCompoundParametricStudyTool
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4288.FaceGearSetParametricStudyTool]':
        """List[FaceGearSetParametricStudyTool]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

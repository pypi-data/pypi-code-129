"""_6249.py

FaceGearSetDynamicAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2468
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6800
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6247, _6248, _6254
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'FaceGearSetDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetDynamicAnalysis',)


class FaceGearSetDynamicAnalysis(_6254.GearSetDynamicAnalysis):
    """FaceGearSetDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearSetDynamicAnalysis.TYPE'):
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
    def face_gears_dynamic_analysis(self) -> 'List[_6247.FaceGearDynamicAnalysis]':
        """List[FaceGearDynamicAnalysis]: 'FaceGearsDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearsDynamicAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_meshes_dynamic_analysis(self) -> 'List[_6248.FaceGearMeshDynamicAnalysis]':
        """List[FaceGearMeshDynamicAnalysis]: 'FaceMeshesDynamicAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceMeshesDynamicAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

"""_3752.py

FaceGearSetStabilityAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2468
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6800
from mastapy.system_model.analyses_and_results.stability_analyses import _3753, _3751, _3757
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'FaceGearSetStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetStabilityAnalysis',)


class FaceGearSetStabilityAnalysis(_3757.GearSetStabilityAnalysis):
    """FaceGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearSetStabilityAnalysis.TYPE'):
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
    def face_gears_stability_analysis(self) -> 'List[_3753.FaceGearStabilityAnalysis]':
        """List[FaceGearStabilityAnalysis]: 'FaceGearsStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearsStabilityAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_meshes_stability_analysis(self) -> 'List[_3751.FaceGearMeshStabilityAnalysis]':
        """List[FaceGearMeshStabilityAnalysis]: 'FaceMeshesStabilityAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceMeshesStabilityAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

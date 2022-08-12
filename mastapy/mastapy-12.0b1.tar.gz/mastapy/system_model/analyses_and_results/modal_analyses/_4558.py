"""_4558.py

FaceGearMeshModalAnalysis
"""


from mastapy.system_model.connections_and_sockets.gears import _2251
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6799
from mastapy.system_model.analyses_and_results.system_deflections import _2688
from mastapy.system_model.analyses_and_results.modal_analyses import _4564
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'FaceGearMeshModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMeshModalAnalysis',)


class FaceGearMeshModalAnalysis(_4564.GearMeshModalAnalysis):
    """FaceGearMeshModalAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearMeshModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2251.FaceGearMesh':
        """FaceGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6799.FaceGearMeshLoadCase':
        """FaceGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2688.FaceGearMeshSystemDeflection':
        """FaceGearMeshSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

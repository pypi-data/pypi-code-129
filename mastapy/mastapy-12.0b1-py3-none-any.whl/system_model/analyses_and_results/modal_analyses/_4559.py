"""_4559.py

FaceGearModalAnalysis
"""


from mastapy.system_model.part_model.gears import _2467
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6798
from mastapy.system_model.analyses_and_results.system_deflections import _2690
from mastapy.system_model.analyses_and_results.modal_analyses import _4565
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'FaceGearModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearModalAnalysis',)


class FaceGearModalAnalysis(_4565.GearModalAnalysis):
    """FaceGearModalAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2467.FaceGear':
        """FaceGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6798.FaceGearLoadCase':
        """FaceGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2690.FaceGearSystemDeflection':
        """FaceGearSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

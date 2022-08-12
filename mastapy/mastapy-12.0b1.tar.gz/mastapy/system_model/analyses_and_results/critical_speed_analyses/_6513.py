"""_6513.py

FaceGearCriticalSpeedAnalysis
"""


from mastapy.system_model.part_model.gears import _2467
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6798
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6518
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'FaceGearCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearCriticalSpeedAnalysis',)


class FaceGearCriticalSpeedAnalysis(_6518.GearCriticalSpeedAnalysis):
    """FaceGearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearCriticalSpeedAnalysis.TYPE'):
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

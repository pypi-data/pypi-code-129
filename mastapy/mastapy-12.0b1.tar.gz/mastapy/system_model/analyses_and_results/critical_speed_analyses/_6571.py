"""_6571.py

StraightBevelPlanetGearCriticalSpeedAnalysis
"""


from mastapy.system_model.part_model.gears import _2488
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6565
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses', 'StraightBevelPlanetGearCriticalSpeedAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelPlanetGearCriticalSpeedAnalysis',)


class StraightBevelPlanetGearCriticalSpeedAnalysis(_6565.StraightBevelDiffGearCriticalSpeedAnalysis):
    """StraightBevelPlanetGearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_CRITICAL_SPEED_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelPlanetGearCriticalSpeedAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2488.StraightBevelPlanetGear':
        """StraightBevelPlanetGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

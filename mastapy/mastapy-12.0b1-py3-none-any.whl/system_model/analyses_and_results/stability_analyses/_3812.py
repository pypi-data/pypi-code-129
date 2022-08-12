"""_3812.py

StraightBevelSunGearStabilityAnalysis
"""


from mastapy.system_model.part_model.gears import _2489
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3807
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_SUN_GEAR_STABILITY_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses', 'StraightBevelSunGearStabilityAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelSunGearStabilityAnalysis',)


class StraightBevelSunGearStabilityAnalysis(_3807.StraightBevelDiffGearStabilityAnalysis):
    """StraightBevelSunGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_SUN_GEAR_STABILITY_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelSunGearStabilityAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2489.StraightBevelSunGear':
        """StraightBevelSunGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

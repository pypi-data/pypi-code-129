"""_4092.py

WormGearPowerFlow
"""


from mastapy.system_model.part_model.gears import _2490
from mastapy._internal import constructor
from mastapy.gears.rating.worm import _365
from mastapy.system_model.analyses_and_results.static_loads import _6896
from mastapy.system_model.analyses_and_results.power_flows import _4024
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'WormGearPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearPowerFlow',)


class WormGearPowerFlow(_4024.GearPowerFlow):
    """WormGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2490.WormGear':
        """WormGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_365.WormGearRating':
        """WormGearRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6896.WormGearLoadCase':
        """WormGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

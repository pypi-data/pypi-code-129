"""_2743.py

SpiralBevelGearSystemDeflection
"""


from mastapy.system_model.part_model.gears import _2482
from mastapy._internal import constructor
from mastapy.gears.rating.spiral_bevel import _394
from mastapy.system_model.analyses_and_results.static_loads import _6867
from mastapy.system_model.analyses_and_results.power_flows import _4067
from mastapy.system_model.analyses_and_results.system_deflections import _2642
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'SpiralBevelGearSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('SpiralBevelGearSystemDeflection',)


class SpiralBevelGearSystemDeflection(_2642.BevelGearSystemDeflection):
    """SpiralBevelGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpiralBevelGearSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2482.SpiralBevelGear':
        """SpiralBevelGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_394.SpiralBevelGearRating':
        """SpiralBevelGearRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6867.SpiralBevelGearLoadCase':
        """SpiralBevelGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4067.SpiralBevelGearPowerFlow':
        """SpiralBevelGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

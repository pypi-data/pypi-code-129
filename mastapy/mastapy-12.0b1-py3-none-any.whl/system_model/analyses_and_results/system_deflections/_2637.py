"""_2637.py

BevelDifferentialGearSystemDeflection
"""


from mastapy.system_model.part_model.gears import _2454, _2456, _2457
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.bevel import _545
from mastapy.gears.rating.zerol_bevel import _361
from mastapy.gears.rating.straight_bevel import _387
from mastapy.gears.rating.spiral_bevel import _394
from mastapy.system_model.analyses_and_results.static_loads import _6737, _6740, _6741
from mastapy.system_model.analyses_and_results.power_flows import _3976, _3978, _3979
from mastapy.system_model.analyses_and_results.system_deflections import _2642
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'BevelDifferentialGearSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSystemDeflection',)


class BevelDifferentialGearSystemDeflection(_2642.BevelGearSystemDeflection):
    """BevelDifferentialGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2454.BevelDifferentialGear':
        """BevelDifferentialGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        if _2454.BevelDifferentialGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelDifferentialGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_545.BevelGearRating':
        """BevelGearRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _545.BevelGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to BevelGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_zerol_bevel_gear_rating(self) -> '_361.ZerolBevelGearRating':
        """ZerolBevelGearRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _361.ZerolBevelGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to ZerolBevelGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_straight_bevel_gear_rating(self) -> '_387.StraightBevelGearRating':
        """StraightBevelGearRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _387.StraightBevelGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to StraightBevelGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_spiral_bevel_gear_rating(self) -> '_394.SpiralBevelGearRating':
        """SpiralBevelGearRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _394.SpiralBevelGearRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to SpiralBevelGearRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6737.BevelDifferentialGearLoadCase':
        """BevelDifferentialGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        if _6737.BevelDifferentialGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_load_case to BevelDifferentialGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_3976.BevelDifferentialGearPowerFlow':
        """BevelDifferentialGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        if _3976.BevelDifferentialGearPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to BevelDifferentialGearPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

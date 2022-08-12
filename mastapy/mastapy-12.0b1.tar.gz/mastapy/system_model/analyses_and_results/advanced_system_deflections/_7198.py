"""_7198.py

BevelDifferentialGearSetAdvancedSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model.gears import _2455
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6739
from mastapy.gears.rating.bevel import _546
from mastapy.gears.rating.zerol_bevel import _362
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.straight_bevel import _388
from mastapy.gears.rating.spiral_bevel import _395
from mastapy.system_model.analyses_and_results.system_deflections import _2636
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7196, _7197, _7203
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'BevelDifferentialGearSetAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSetAdvancedSystemDeflection',)


class BevelDifferentialGearSetAdvancedSystemDeflection(_7203.BevelGearSetAdvancedSystemDeflection):
    """BevelDifferentialGearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSetAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2455.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6739.BevelDifferentialGearSetLoadCase':
        """BevelDifferentialGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_546.BevelGearSetRating':
        """BevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _546.BevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to BevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_zerol_bevel_gear_set_rating(self) -> '_362.ZerolBevelGearSetRating':
        """ZerolBevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _362.ZerolBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to ZerolBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_straight_bevel_gear_set_rating(self) -> '_388.StraightBevelGearSetRating':
        """StraightBevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _388.StraightBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to StraightBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating_of_type_spiral_bevel_gear_set_rating(self) -> '_395.SpiralBevelGearSetRating':
        """SpiralBevelGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        if _395.SpiralBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast rating to SpiralBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_546.BevelGearSetRating':
        """BevelGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _546.BevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to BevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_zerol_bevel_gear_set_rating(self) -> '_362.ZerolBevelGearSetRating':
        """ZerolBevelGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _362.ZerolBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to ZerolBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_straight_bevel_gear_set_rating(self) -> '_388.StraightBevelGearSetRating':
        """StraightBevelGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _388.StraightBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to StraightBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_spiral_bevel_gear_set_rating(self) -> '_395.SpiralBevelGearSetRating':
        """SpiralBevelGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _395.SpiralBevelGearSetRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to SpiralBevelGearSetRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2636.BevelDifferentialGearSetSystemDeflection]':
        """List[BevelDifferentialGearSetSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblySystemDeflectionResults
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_gears_advanced_system_deflection(self) -> 'List[_7196.BevelDifferentialGearAdvancedSystemDeflection]':
        """List[BevelDifferentialGearAdvancedSystemDeflection]: 'BevelDifferentialGearsAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialGearsAdvancedSystemDeflection
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_meshes_advanced_system_deflection(self) -> 'List[_7197.BevelDifferentialGearMeshAdvancedSystemDeflection]':
        """List[BevelDifferentialGearMeshAdvancedSystemDeflection]: 'BevelDifferentialMeshesAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialMeshesAdvancedSystemDeflection
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

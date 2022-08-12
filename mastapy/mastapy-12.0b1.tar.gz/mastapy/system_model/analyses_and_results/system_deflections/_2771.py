"""_2771.py

WormGearSetSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model.gears import _2491
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6898
from mastapy.gears.rating.worm import _367
from mastapy.system_model.analyses_and_results.power_flows import _4093
from mastapy.system_model.analyses_and_results.system_deflections import _2772, _2770, _2694
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_SET_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'WormGearSetSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGearSetSystemDeflection',)


class WormGearSetSystemDeflection(_2694.GearSetSystemDeflection):
    """WormGearSetSystemDeflection

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_SET_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGearSetSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2491.WormGearSet':
        """WormGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6898.WormGearSetLoadCase':
        """WormGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_367.WormGearSetRating':
        """WormGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_367.WormGearSetRating':
        """WormGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4093.WormGearSetPowerFlow':
        """WormGearSetPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def worm_gears_system_deflection(self) -> 'List[_2772.WormGearSystemDeflection]':
        """List[WormGearSystemDeflection]: 'WormGearsSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearsSystemDeflection
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_meshes_system_deflection(self) -> 'List[_2770.WormGearMeshSystemDeflection]':
        """List[WormGearMeshSystemDeflection]: 'WormMeshesSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormMeshesSystemDeflection
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

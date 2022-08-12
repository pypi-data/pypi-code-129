"""_7283.py

ShaftAdvancedSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model.shaft_model import _2422
from mastapy._internal import constructor, conversion
from mastapy.shafts import _19
from mastapy.system_model.analyses_and_results.static_loads import _6864
from mastapy.system_model.analyses_and_results.system_deflections import _2738
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7183
from mastapy._internal.python_net import python_net_import

_SHAFT_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'ShaftAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftAdvancedSystemDeflection',)


class ShaftAdvancedSystemDeflection(_7183.AbstractShaftAdvancedSystemDeflection):
    """ShaftAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SHAFT_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShaftAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2422.Shaft':
        """Shaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_19.ShaftDamageResults':
        """ShaftDamageResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6864.ShaftLoadCase':
        """ShaftLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_system_deflection_results(self) -> 'List[_2738.ShaftSystemDeflection]':
        """List[ShaftSystemDeflection]: 'ComponentSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentSystemDeflectionResults
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[ShaftAdvancedSystemDeflection]':
        """List[ShaftAdvancedSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

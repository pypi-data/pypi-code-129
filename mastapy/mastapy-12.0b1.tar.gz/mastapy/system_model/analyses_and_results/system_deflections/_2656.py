"""_2656.py

ConceptGearSystemDeflection
"""


from mastapy.system_model.part_model.gears import _2460
from mastapy._internal import constructor
from mastapy.gears.rating.concept import _541
from mastapy.system_model.analyses_and_results.static_loads import _6755
from mastapy.system_model.analyses_and_results.power_flows import _3994
from mastapy.system_model.analyses_and_results.system_deflections import _2695
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'ConceptGearSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptGearSystemDeflection',)


class ConceptGearSystemDeflection(_2695.GearSystemDeflection):
    """ConceptGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptGearSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2460.ConceptGear':
        """ConceptGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_541.ConceptGearRating':
        """ConceptGearRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6755.ConceptGearLoadCase':
        """ConceptGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_3994.ConceptGearPowerFlow':
        """ConceptGearPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

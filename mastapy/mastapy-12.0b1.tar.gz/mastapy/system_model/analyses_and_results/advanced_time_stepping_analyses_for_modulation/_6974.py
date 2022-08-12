"""_6974.py

DatumAdvancedTimeSteppingAnalysisForModulation
"""


from mastapy.system_model.part_model import _2388
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6783
from mastapy.system_model.analyses_and_results.system_deflections import _2685
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6948
from mastapy._internal.python_net import python_net_import

_DATUM_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'DatumAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('DatumAdvancedTimeSteppingAnalysisForModulation',)


class DatumAdvancedTimeSteppingAnalysisForModulation(_6948.ComponentAdvancedTimeSteppingAnalysisForModulation):
    """DatumAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _DATUM_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DatumAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2388.Datum':
        """Datum: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6783.DatumLoadCase':
        """DatumLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2685.DatumSystemDeflection':
        """DatumSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

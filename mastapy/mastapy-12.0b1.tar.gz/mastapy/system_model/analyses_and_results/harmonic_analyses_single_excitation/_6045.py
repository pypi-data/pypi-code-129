"""_6045.py

TorqueConverterPumpHarmonicAnalysisOfSingleExcitation
"""


from mastapy.system_model.part_model.couplings import _2547
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6888
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5963
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_PUMP_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'TorqueConverterPumpHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterPumpHarmonicAnalysisOfSingleExcitation',)


class TorqueConverterPumpHarmonicAnalysisOfSingleExcitation(_5963.CouplingHalfHarmonicAnalysisOfSingleExcitation):
    """TorqueConverterPumpHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_PUMP_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterPumpHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2547.TorqueConverterPump':
        """TorqueConverterPump: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6888.TorqueConverterPumpLoadCase':
        """TorqueConverterPumpLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

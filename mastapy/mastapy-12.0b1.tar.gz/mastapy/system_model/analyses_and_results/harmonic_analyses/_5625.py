"""_5625.py

ClutchHalfHarmonicAnalysis
"""


from mastapy.system_model.part_model.couplings import _2518
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6748
from mastapy.system_model.analyses_and_results.system_deflections import _2646
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5642
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'ClutchHalfHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchHalfHarmonicAnalysis',)


class ClutchHalfHarmonicAnalysis(_5642.CouplingHalfHarmonicAnalysis):
    """ClutchHalfHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchHalfHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2518.ClutchHalf':
        """ClutchHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6748.ClutchHalfLoadCase':
        """ClutchHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2646.ClutchHalfSystemDeflection':
        """ClutchHalfSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

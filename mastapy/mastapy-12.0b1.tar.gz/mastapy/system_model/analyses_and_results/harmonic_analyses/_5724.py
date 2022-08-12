"""_5724.py

ShaftHarmonicAnalysis
"""


from typing import List

from mastapy.system_model.part_model.shaft_model import _2422
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6864
from mastapy.system_model.analyses_and_results.modal_analyses import _4606
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5688, _5604
from mastapy.system_model.analyses_and_results.system_deflections import _2738
from mastapy._internal.python_net import python_net_import

_SHAFT_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'ShaftHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftHarmonicAnalysis',)


class ShaftHarmonicAnalysis(_5604.AbstractShaftHarmonicAnalysis):
    """ShaftHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShaftHarmonicAnalysis.TYPE'):
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
    def component_load_case(self) -> '_6864.ShaftLoadCase':
        """ShaftLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def coupled_modal_analysis(self) -> '_4606.ShaftModalAnalysis':
        """ShaftModalAnalysis: 'CoupledModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoupledModalAnalysis
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def export(self) -> '_5688.HarmonicAnalysisShaftExportOptions':
        """HarmonicAnalysisShaftExportOptions: 'Export' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Export
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2738.ShaftSystemDeflection':
        """ShaftSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[ShaftHarmonicAnalysis]':
        """List[ShaftHarmonicAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

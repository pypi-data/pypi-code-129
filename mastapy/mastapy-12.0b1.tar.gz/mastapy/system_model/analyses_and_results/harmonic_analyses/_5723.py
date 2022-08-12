"""_5723.py

RootAssemblyHarmonicAnalysis
"""


from mastapy.system_model.part_model import _2414
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import (
    _5687, _2571, _2572, _5610
)
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5793
from mastapy.system_model.analyses_and_results.system_deflections import _2734
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'RootAssemblyHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyHarmonicAnalysis',)


class RootAssemblyHarmonicAnalysis(_5610.AssemblyHarmonicAnalysis):
    """RootAssemblyHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RootAssemblyHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2414.RootAssembly':
        """RootAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def export(self) -> '_5687.HarmonicAnalysisRootAssemblyExportOptions':
        """HarmonicAnalysisRootAssemblyExportOptions: 'Export' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Export
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def harmonic_analysis_inputs(self) -> '_2571.HarmonicAnalysis':
        """HarmonicAnalysis: 'HarmonicAnalysisInputs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HarmonicAnalysisInputs
        if _2571.HarmonicAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast harmonic_analysis_inputs to HarmonicAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def results(self) -> '_5793.RootAssemblyHarmonicAnalysisResultsPropertyAccessor':
        """RootAssemblyHarmonicAnalysisResultsPropertyAccessor: 'Results' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Results
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2734.RootAssemblySystemDeflection':
        """RootAssemblySystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

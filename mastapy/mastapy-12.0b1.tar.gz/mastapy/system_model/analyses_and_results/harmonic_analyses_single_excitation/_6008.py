"""_6008.py

PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation
"""


from mastapy.system_model.part_model.couplings import _2527
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6845
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _5964
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation',)


class PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation(_5964.CouplingHarmonicAnalysisOfSingleExcitation):
    """PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2527.PartToPartShearCoupling':
        """PartToPartShearCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6845.PartToPartShearCouplingLoadCase':
        """PartToPartShearCouplingLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

"""_5944.py

BoltedJointHarmonicAnalysisOfSingleExcitation
"""


from mastapy.system_model.part_model import _2383
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6745
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6024
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation', 'BoltedJointHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltedJointHarmonicAnalysisOfSingleExcitation',)


class BoltedJointHarmonicAnalysisOfSingleExcitation(_6024.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation):
    """BoltedJointHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BoltedJointHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2383.BoltedJoint':
        """BoltedJoint: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6745.BoltedJointLoadCase':
        """BoltedJointLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

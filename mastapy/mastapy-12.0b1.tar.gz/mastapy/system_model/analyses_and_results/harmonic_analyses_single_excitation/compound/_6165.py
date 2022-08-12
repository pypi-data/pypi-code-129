"""_6165.py

StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
"""


from typing import List

from mastapy.system_model.part_model.gears import _2487
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import _6036
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import _6163, _6164, _6073
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound', 'StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation')


__docformat__ = 'restructuredtext en'
__all__ = ('StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation',)


class StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation(_6073.BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation):
    """StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2487.StraightBevelGearSet':
        """StraightBevelGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2487.StraightBevelGearSet':
        """StraightBevelGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6036.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation]':
        """List[StraightBevelGearSetHarmonicAnalysisOfSingleExcitation]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_gears_compound_harmonic_analysis_of_single_excitation(self) -> 'List[_6163.StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation]':
        """List[StraightBevelGearCompoundHarmonicAnalysisOfSingleExcitation]: 'StraightBevelGearsCompoundHarmonicAnalysisOfSingleExcitation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearsCompoundHarmonicAnalysisOfSingleExcitation
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_meshes_compound_harmonic_analysis_of_single_excitation(self) -> 'List[_6164.StraightBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]':
        """List[StraightBevelGearMeshCompoundHarmonicAnalysisOfSingleExcitation]: 'StraightBevelMeshesCompoundHarmonicAnalysisOfSingleExcitation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelMeshesCompoundHarmonicAnalysisOfSingleExcitation
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_6036.StraightBevelGearSetHarmonicAnalysisOfSingleExcitation]':
        """List[StraightBevelGearSetHarmonicAnalysisOfSingleExcitation]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

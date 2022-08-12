"""_4433.py

GearSetCompoundParametricStudyTool
"""


from typing import List

from mastapy.gears.rating import _353
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.worm import _366
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.face import _440
from mastapy.gears.rating.cylindrical import _454
from mastapy.gears.rating.conical import _531
from mastapy.gears.rating.concept import _542
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4293
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4471
from mastapy._internal.python_net import python_net_import

_GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'GearSetCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetCompoundParametricStudyTool',)


class GearSetCompoundParametricStudyTool(_4471.SpecialisedAssemblyCompoundParametricStudyTool):
    """GearSetCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_COMPOUND_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearSetCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_set_duty_cycle_results(self) -> '_353.GearSetDutyCycleRating':
        """GearSetDutyCycleRating: 'GearSetDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDutyCycleResults
        if _353.GearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_duty_cycle_results to GearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_duty_cycle_results_of_type_worm_gear_set_duty_cycle_rating(self) -> '_366.WormGearSetDutyCycleRating':
        """WormGearSetDutyCycleRating: 'GearSetDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDutyCycleResults
        if _366.WormGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_duty_cycle_results to WormGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_duty_cycle_results_of_type_face_gear_set_duty_cycle_rating(self) -> '_440.FaceGearSetDutyCycleRating':
        """FaceGearSetDutyCycleRating: 'GearSetDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDutyCycleResults
        if _440.FaceGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_duty_cycle_results to FaceGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_duty_cycle_results_of_type_cylindrical_gear_set_duty_cycle_rating(self) -> '_454.CylindricalGearSetDutyCycleRating':
        """CylindricalGearSetDutyCycleRating: 'GearSetDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDutyCycleResults
        if _454.CylindricalGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_duty_cycle_results to CylindricalGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_duty_cycle_results_of_type_conical_gear_set_duty_cycle_rating(self) -> '_531.ConicalGearSetDutyCycleRating':
        """ConicalGearSetDutyCycleRating: 'GearSetDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDutyCycleResults
        if _531.ConicalGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_duty_cycle_results to ConicalGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_set_duty_cycle_results_of_type_concept_gear_set_duty_cycle_rating(self) -> '_542.ConceptGearSetDutyCycleRating':
        """ConceptGearSetDutyCycleRating: 'GearSetDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearSetDutyCycleResults
        if _542.ConceptGearSetDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_set_duty_cycle_results to ConceptGearSetDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases(self) -> 'List[_4293.GearSetParametricStudyTool]':
        """List[GearSetParametricStudyTool]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4293.GearSetParametricStudyTool]':
        """List[GearSetParametricStudyTool]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

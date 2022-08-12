"""_4431.py

GearCompoundParametricStudyTool
"""


from typing import List

from mastapy.gears.rating import _349
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.worm import _363
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.face import _436
from mastapy.gears.rating.cylindrical import _446
from mastapy.gears.rating.conical import _528
from mastapy.gears.rating.concept import _538
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4292
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4450
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'GearCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('GearCompoundParametricStudyTool',)


class GearCompoundParametricStudyTool(_4450.MountableComponentCompoundParametricStudyTool):
    """GearCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_duty_cycle_results(self) -> '_349.GearDutyCycleRating':
        """GearDutyCycleRating: 'GearDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleResults
        if _349.GearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_duty_cycle_results to GearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_duty_cycle_results_of_type_worm_gear_duty_cycle_rating(self) -> '_363.WormGearDutyCycleRating':
        """WormGearDutyCycleRating: 'GearDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleResults
        if _363.WormGearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_duty_cycle_results to WormGearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_duty_cycle_results_of_type_face_gear_duty_cycle_rating(self) -> '_436.FaceGearDutyCycleRating':
        """FaceGearDutyCycleRating: 'GearDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleResults
        if _436.FaceGearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_duty_cycle_results to FaceGearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_duty_cycle_results_of_type_cylindrical_gear_duty_cycle_rating(self) -> '_446.CylindricalGearDutyCycleRating':
        """CylindricalGearDutyCycleRating: 'GearDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleResults
        if _446.CylindricalGearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_duty_cycle_results to CylindricalGearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_duty_cycle_results_of_type_conical_gear_duty_cycle_rating(self) -> '_528.ConicalGearDutyCycleRating':
        """ConicalGearDutyCycleRating: 'GearDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleResults
        if _528.ConicalGearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_duty_cycle_results to ConicalGearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_duty_cycle_results_of_type_concept_gear_duty_cycle_rating(self) -> '_538.ConceptGearDutyCycleRating':
        """ConceptGearDutyCycleRating: 'GearDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleResults
        if _538.ConceptGearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_duty_cycle_results to ConceptGearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases(self) -> 'List[_4292.GearParametricStudyTool]':
        """List[GearParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_4292.GearParametricStudyTool]':
        """List[GearParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

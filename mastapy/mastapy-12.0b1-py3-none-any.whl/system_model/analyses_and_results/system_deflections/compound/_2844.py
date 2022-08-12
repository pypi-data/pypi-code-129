"""_2844.py

GearCompoundSystemDeflection
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
from mastapy.system_model.analyses_and_results.system_deflections import _2695
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2863
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'GearCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('GearCompoundSystemDeflection',)


class GearCompoundSystemDeflection(_2863.MountableComponentCompoundSystemDeflection):
    """GearCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duty_cycle_rating(self) -> '_349.GearDutyCycleRating':
        """GearDutyCycleRating: 'DutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DutyCycleRating
        if _349.GearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast duty_cycle_rating to GearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def duty_cycle_rating_of_type_worm_gear_duty_cycle_rating(self) -> '_363.WormGearDutyCycleRating':
        """WormGearDutyCycleRating: 'DutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DutyCycleRating
        if _363.WormGearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast duty_cycle_rating to WormGearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def duty_cycle_rating_of_type_face_gear_duty_cycle_rating(self) -> '_436.FaceGearDutyCycleRating':
        """FaceGearDutyCycleRating: 'DutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DutyCycleRating
        if _436.FaceGearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast duty_cycle_rating to FaceGearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def duty_cycle_rating_of_type_cylindrical_gear_duty_cycle_rating(self) -> '_446.CylindricalGearDutyCycleRating':
        """CylindricalGearDutyCycleRating: 'DutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DutyCycleRating
        if _446.CylindricalGearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast duty_cycle_rating to CylindricalGearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def duty_cycle_rating_of_type_conical_gear_duty_cycle_rating(self) -> '_528.ConicalGearDutyCycleRating':
        """ConicalGearDutyCycleRating: 'DutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DutyCycleRating
        if _528.ConicalGearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast duty_cycle_rating to ConicalGearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def duty_cycle_rating_of_type_concept_gear_duty_cycle_rating(self) -> '_538.ConceptGearDutyCycleRating':
        """ConceptGearDutyCycleRating: 'DutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DutyCycleRating
        if _538.ConceptGearDutyCycleRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast duty_cycle_rating to ConceptGearDutyCycleRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases(self) -> 'List[_2695.GearSystemDeflection]':
        """List[GearSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases_ready(self) -> 'List[_2695.GearSystemDeflection]':
        """List[GearSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

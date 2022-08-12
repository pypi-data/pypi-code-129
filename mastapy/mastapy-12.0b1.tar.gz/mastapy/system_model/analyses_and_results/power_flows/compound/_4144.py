"""_4144.py

CylindricalGearCompoundPowerFlow
"""


from typing import List

from mastapy.system_model.part_model.gears import _2464, _2466
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.cylindrical import _446
from mastapy.system_model.analyses_and_results.power_flows import _4013
from mastapy.system_model.analyses_and_results.power_flows.compound import _4155
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'CylindricalGearCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearCompoundPowerFlow',)


class CylindricalGearCompoundPowerFlow(_4155.GearCompoundPowerFlow):
    """CylindricalGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2464.CylindricalGear':
        """CylindricalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        if _2464.CylindricalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CylindricalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_duty_cycle_rating(self) -> '_446.CylindricalGearDutyCycleRating':
        """CylindricalGearDutyCycleRating: 'GearDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDutyCycleRating
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_duty_cycle_rating(self) -> '_446.CylindricalGearDutyCycleRating':
        """CylindricalGearDutyCycleRating: 'CylindricalGearDutyCycleRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearDutyCycleRating
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_4013.CylindricalGearPowerFlow]':
        """List[CylindricalGearPowerFlow]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4013.CylindricalGearPowerFlow]':
        """List[CylindricalGearPowerFlow]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

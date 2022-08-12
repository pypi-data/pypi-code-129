"""_4191.py

RootAssemblyCompoundPowerFlow
"""


from typing import List

from mastapy.system_model.analyses_and_results.load_case_groups import (
    _5584, _5582, _5587, _5588,
    _5591
)
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.power_flows import _4061
from mastapy.system_model.analyses_and_results.power_flows.compound import _4104
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound', 'RootAssemblyCompoundPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyCompoundPowerFlow',)


class RootAssemblyCompoundPowerFlow(_4104.AssemblyCompoundPowerFlow):
    """RootAssemblyCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RootAssemblyCompoundPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def compound_static_load(self) -> '_5584.AbstractStaticLoadCaseGroup':
        """AbstractStaticLoadCaseGroup: 'CompoundStaticLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundStaticLoad
        if _5584.AbstractStaticLoadCaseGroup.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast compound_static_load to AbstractStaticLoadCaseGroup. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_static_load_of_type_abstract_design_state_load_case_group(self) -> '_5582.AbstractDesignStateLoadCaseGroup':
        """AbstractDesignStateLoadCaseGroup: 'CompoundStaticLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundStaticLoad
        if _5582.AbstractDesignStateLoadCaseGroup.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast compound_static_load to AbstractDesignStateLoadCaseGroup. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_static_load_of_type_design_state(self) -> '_5587.DesignState':
        """DesignState: 'CompoundStaticLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundStaticLoad
        if _5587.DesignState.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast compound_static_load to DesignState. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_static_load_of_type_duty_cycle(self) -> '_5588.DutyCycle':
        """DutyCycle: 'CompoundStaticLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundStaticLoad
        if _5588.DutyCycle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast compound_static_load to DutyCycle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def compound_static_load_of_type_sub_group_in_single_design_state(self) -> '_5591.SubGroupInSingleDesignState':
        """SubGroupInSingleDesignState: 'CompoundStaticLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundStaticLoad
        if _5591.SubGroupInSingleDesignState.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast compound_static_load to SubGroupInSingleDesignState. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_4061.RootAssemblyPowerFlow]':
        """List[RootAssemblyPowerFlow]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_4061.RootAssemblyPowerFlow]':
        """List[RootAssemblyPowerFlow]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def set_face_widths_for_specified_safety_factors(self):
        """ 'SetFaceWidthsForSpecifiedSafetyFactors' is the original name of this method."""

        self.wrapped.SetFaceWidthsForSpecifiedSafetyFactors()

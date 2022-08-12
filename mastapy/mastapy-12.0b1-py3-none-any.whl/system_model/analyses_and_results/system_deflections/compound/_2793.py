"""_2793.py

BearingCompoundSystemDeflection
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model import _2380
from mastapy.bearings.bearing_results import _1896, _1904, _1907
from mastapy._internal.cast_exception import CastException
from mastapy.bearings.bearing_results.rolling import (
    _1936, _1943, _1951, _1967,
    _1990
)
from mastapy.system_model.analyses_and_results.system_deflections import _2632
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2821
from mastapy._internal.python_net import python_net_import

_BEARING_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'BearingCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingCompoundSystemDeflection',)


class BearingCompoundSystemDeflection(_2821.ConnectorCompoundSystemDeflection):
    """BearingCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEARING_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BearingCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_element_stress_for_iso2812007_dynamic_equivalent_load(self) -> 'float':
        """float: 'MaximumElementStressForISO2812007DynamicEquivalentLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumElementStressForISO2812007DynamicEquivalentLoad
        return temp

    @property
    def maximum_element_stress_for_isots162812008_dynamic_equivalent_load(self) -> 'float':
        """float: 'MaximumElementStressForISOTS162812008DynamicEquivalentLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumElementStressForISOTS162812008DynamicEquivalentLoad
        return temp

    @property
    def component_design(self) -> '_2380.Bearing':
        """Bearing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_1896.LoadedBearingDutyCycle':
        """LoadedBearingDutyCycle: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1896.LoadedBearingDutyCycle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to LoadedBearingDutyCycle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_2632.BearingSystemDeflection]':
        """List[BearingSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[BearingCompoundSystemDeflection]':
        """List[BearingCompoundSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_2632.BearingSystemDeflection]':
        """List[BearingSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

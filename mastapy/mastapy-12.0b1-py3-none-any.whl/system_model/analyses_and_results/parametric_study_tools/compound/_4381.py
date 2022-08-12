"""_4381.py

BearingCompoundParametricStudyTool
"""


from typing import List

from mastapy.bearings.bearing_results import _1896, _1904, _1907
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.bearings.bearing_results.rolling import (
    _1936, _1943, _1951, _1967,
    _1990
)
from mastapy.system_model.part_model import _2380
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4234
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import _4409
from mastapy._internal.python_net import python_net_import

_BEARING_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound', 'BearingCompoundParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingCompoundParametricStudyTool',)


class BearingCompoundParametricStudyTool(_4409.ConnectorCompoundParametricStudyTool):
    """BearingCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _BEARING_COMPOUND_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BearingCompoundParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bearing_duty_cycle_results(self) -> '_1896.LoadedBearingDutyCycle':
        """LoadedBearingDutyCycle: 'BearingDutyCycleResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDutyCycleResults
        if _1896.LoadedBearingDutyCycle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_duty_cycle_results to LoadedBearingDutyCycle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def component_analysis_cases_ready(self) -> 'List[_4234.BearingParametricStudyTool]':
        """List[BearingParametricStudyTool]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[BearingCompoundParametricStudyTool]':
        """List[BearingCompoundParametricStudyTool]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_4234.BearingParametricStudyTool]':
        """List[BearingParametricStudyTool]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

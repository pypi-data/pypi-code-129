"""_5595.py

TimeSeriesLoadCaseGroup
"""


from typing import List

from mastapy.system_model.analyses_and_results.static_loads import _6720, _6732
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results import _2614, _2558
from mastapy.system_model.analyses_and_results.load_case_groups import _5583
from mastapy._internal.python_net import python_net_import

_TIME_SERIES_LOAD_CASE_GROUP = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.LoadCaseGroups', 'TimeSeriesLoadCaseGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('TimeSeriesLoadCaseGroup',)


class TimeSeriesLoadCaseGroup(_5583.AbstractLoadCaseGroup):
    """TimeSeriesLoadCaseGroup

    This is a mastapy class.
    """

    TYPE = _TIME_SERIES_LOAD_CASE_GROUP

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TimeSeriesLoadCaseGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def load_cases(self) -> 'List[_6720.TimeSeriesLoadCase]':
        """List[TimeSeriesLoadCase]: 'LoadCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def compound_multibody_dynamics_analysis(self) -> '_2614.CompoundMultibodyDynamicsAnalysis':
        """CompoundMultibodyDynamicsAnalysis: 'CompoundMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CompoundMultibodyDynamicsAnalysis
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def delete(self):
        """ 'Delete' is the original name of this method."""

        self.wrapped.Delete()

    def analysis_of(self, analysis_type: '_6732.AnalysisType') -> '_2558.CompoundAnalysis':
        """ 'AnalysisOf' is the original name of this method.

        Args:
            analysis_type (mastapy.system_model.analyses_and_results.static_loads.AnalysisType)

        Returns:
            mastapy.system_model.analyses_and_results.CompoundAnalysis
        """

        analysis_type = conversion.mp_to_pn_enum(analysis_type)
        method_result = self.wrapped.AnalysisOf(analysis_type)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

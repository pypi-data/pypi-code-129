"""_6720.py

TimeSeriesLoadCase
"""


from typing import Optional

from mastapy.system_model.analyses_and_results import _2578, _2559
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5386
from mastapy.system_model.analyses_and_results.load_case_groups import _5595
from mastapy.system_model.analyses_and_results.static_loads import _6732, _6718
from mastapy._internal.python_net import python_net_import

_TIME_SERIES_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'TimeSeriesLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('TimeSeriesLoadCase',)


class TimeSeriesLoadCase(_6718.LoadCase):
    """TimeSeriesLoadCase

    This is a mastapy class.
    """

    TYPE = _TIME_SERIES_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TimeSeriesLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def multibody_dynamics_analysis(self) -> '_2578.MultibodyDynamicsAnalysis':
        """MultibodyDynamicsAnalysis: 'MultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MultibodyDynamicsAnalysis
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def duration_for_rating(self) -> 'float':
        """float: 'DurationForRating' is the original name of this property."""

        temp = self.wrapped.DurationForRating
        return temp

    @duration_for_rating.setter
    def duration_for_rating(self, value: 'float'):
        self.wrapped.DurationForRating = float(value) if value else 0.0

    @property
    def driva_analysis_options(self) -> '_5386.MBDAnalysisOptions':
        """MBDAnalysisOptions: 'DRIVAAnalysisOptions' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DRIVAAnalysisOptions
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def time_series_load_case_group(self) -> '_5595.TimeSeriesLoadCaseGroup':
        """TimeSeriesLoadCaseGroup: 'TimeSeriesLoadCaseGroup' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TimeSeriesLoadCaseGroup
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def analysis_of(self, analysis_type: '_6732.AnalysisType') -> '_2559.SingleAnalysis':
        """ 'AnalysisOf' is the original name of this method.

        Args:
            analysis_type (mastapy.system_model.analyses_and_results.static_loads.AnalysisType)

        Returns:
            mastapy.system_model.analyses_and_results.SingleAnalysis
        """

        analysis_type = conversion.mp_to_pn_enum(analysis_type)
        method_result = self.wrapped.AnalysisOf(analysis_type)
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

    def duplicate(self, new_load_case_group: '_5595.TimeSeriesLoadCaseGroup', name: Optional['str'] = 'None') -> 'TimeSeriesLoadCase':
        """ 'Duplicate' is the original name of this method.

        Args:
            new_load_case_group (mastapy.system_model.analyses_and_results.load_case_groups.TimeSeriesLoadCaseGroup)
            name (str, optional)

        Returns:
            mastapy.system_model.analyses_and_results.static_loads.TimeSeriesLoadCase
        """

        name = str(name)
        method_result = self.wrapped.Duplicate(new_load_case_group.wrapped if new_load_case_group else None, name if name else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

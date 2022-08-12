"""_5790.py

ResultsForResponseOfAComponentOrSurfaceInAHarmonic
"""


from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5792, _5772
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_RESULTS_FOR_RESPONSE_OF_A_COMPONENT_OR_SURFACE_IN_A_HARMONIC = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults', 'ResultsForResponseOfAComponentOrSurfaceInAHarmonic')


__docformat__ = 'restructuredtext en'
__all__ = ('ResultsForResponseOfAComponentOrSurfaceInAHarmonic',)


class ResultsForResponseOfAComponentOrSurfaceInAHarmonic(_0.APIBase):
    """ResultsForResponseOfAComponentOrSurfaceInAHarmonic

    This is a mastapy class.
    """

    TYPE = _RESULTS_FOR_RESPONSE_OF_A_COMPONENT_OR_SURFACE_IN_A_HARMONIC

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ResultsForResponseOfAComponentOrSurfaceInAHarmonic.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def magnitude(self) -> '_5792.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic':
        """ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic: 'Magnitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Magnitude
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def result_at_reference_speed(self) -> '_5772.DatapointForResponseOfAComponentOrSurfaceAtAFrequencyInAHarmonic':
        """DatapointForResponseOfAComponentOrSurfaceAtAFrequencyInAHarmonic: 'ResultAtReferenceSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResultAtReferenceSpeed
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def data_points(self) -> 'List[_5772.DatapointForResponseOfAComponentOrSurfaceAtAFrequencyInAHarmonic]':
        """List[DatapointForResponseOfAComponentOrSurfaceAtAFrequencyInAHarmonic]: 'DataPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DataPoints
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

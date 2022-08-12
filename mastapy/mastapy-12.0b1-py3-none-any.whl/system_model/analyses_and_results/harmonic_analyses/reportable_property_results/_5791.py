"""_5791.py

ResultsForResponseOfANodeOnAHarmonic
"""


from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import _5792, _5773
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_RESULTS_FOR_RESPONSE_OF_A_NODE_ON_A_HARMONIC = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults', 'ResultsForResponseOfANodeOnAHarmonic')


__docformat__ = 'restructuredtext en'
__all__ = ('ResultsForResponseOfANodeOnAHarmonic',)


class ResultsForResponseOfANodeOnAHarmonic(_0.APIBase):
    """ResultsForResponseOfANodeOnAHarmonic

    This is a mastapy class.
    """

    TYPE = _RESULTS_FOR_RESPONSE_OF_A_NODE_ON_A_HARMONIC

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ResultsForResponseOfANodeOnAHarmonic.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angular_magnitude(self) -> '_5792.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic':
        """ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic: 'AngularMagnitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AngularMagnitude
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def linear_magnitude(self) -> '_5792.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic':
        """ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic: 'LinearMagnitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LinearMagnitude
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def radial_angular_magnitude(self) -> '_5792.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic':
        """ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic: 'RadialAngularMagnitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadialAngularMagnitude
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def radial_magnitude(self) -> '_5792.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic':
        """ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic: 'RadialMagnitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadialMagnitude
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def result_at_reference_speed(self) -> '_5773.DatapointForResponseOfANodeAtAFrequencyOnAHarmonic':
        """DatapointForResponseOfANodeAtAFrequencyOnAHarmonic: 'ResultAtReferenceSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResultAtReferenceSpeed
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def theta_x(self) -> '_5792.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic':
        """ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic: 'ThetaX' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ThetaX
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def theta_y(self) -> '_5792.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic':
        """ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic: 'ThetaY' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ThetaY
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def theta_z(self) -> '_5792.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic':
        """ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic: 'ThetaZ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ThetaZ
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def x(self) -> '_5792.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic':
        """ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic: 'X' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.X
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def y(self) -> '_5792.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic':
        """ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic: 'Y' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Y
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def z(self) -> '_5792.ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic':
        """ResultsForSingleDegreeOfFreedomOfResponseOfNodeInHarmonic: 'Z' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Z
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def data_points(self) -> 'List[_5773.DatapointForResponseOfANodeAtAFrequencyOnAHarmonic]':
        """List[DatapointForResponseOfANodeAtAFrequencyOnAHarmonic]: 'DataPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DataPoints
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

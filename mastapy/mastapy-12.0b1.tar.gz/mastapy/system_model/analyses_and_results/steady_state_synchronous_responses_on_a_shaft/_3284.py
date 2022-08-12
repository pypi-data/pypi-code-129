"""_3284.py

SteadyStateSynchronousResponseOnAShaft
"""


from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3025
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7462
from mastapy._internal.python_net import python_net_import

_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft', 'SteadyStateSynchronousResponseOnAShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('SteadyStateSynchronousResponseOnAShaft',)


class SteadyStateSynchronousResponseOnAShaft(_7462.StaticLoadAnalysisCase):
    """SteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SteadyStateSynchronousResponseOnAShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def options(self) -> '_3025.SteadyStateSynchronousResponseOptions':
        """SteadyStateSynchronousResponseOptions: 'Options' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Options
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

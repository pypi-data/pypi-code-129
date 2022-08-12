"""_2996.py

OilSealSteadyStateSynchronousResponse
"""


from mastapy.system_model.part_model import _2406
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6840
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _2953
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'OilSealSteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('OilSealSteadyStateSynchronousResponse',)


class OilSealSteadyStateSynchronousResponse(_2953.ConnectorSteadyStateSynchronousResponse):
    """OilSealSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'OilSealSteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2406.OilSeal':
        """OilSeal: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6840.OilSealLoadCase':
        """OilSealLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

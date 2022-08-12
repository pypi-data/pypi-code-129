"""_2960.py

CycloidalAssemblySteadyStateSynchronousResponse
"""


from mastapy.system_model.part_model.cycloidal import _2507
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6771
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3016
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'CycloidalAssemblySteadyStateSynchronousResponse')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalAssemblySteadyStateSynchronousResponse',)


class CycloidalAssemblySteadyStateSynchronousResponse(_3016.SpecialisedAssemblySteadyStateSynchronousResponse):
    """CycloidalAssemblySteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_ASSEMBLY_STEADY_STATE_SYNCHRONOUS_RESPONSE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CycloidalAssemblySteadyStateSynchronousResponse.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2507.CycloidalAssembly':
        """CycloidalAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6771.CycloidalAssemblyLoadCase':
        """CycloidalAssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

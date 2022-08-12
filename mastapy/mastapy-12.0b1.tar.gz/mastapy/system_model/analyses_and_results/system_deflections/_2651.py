"""_2651.py

ConceptCouplingConnectionSystemDeflection
"""


from mastapy.system_model.connections_and_sockets.couplings import _2284
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6752
from mastapy.system_model.analyses_and_results.power_flows import _3990
from mastapy.system_model.analyses_and_results.system_deflections import _2663
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'ConceptCouplingConnectionSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ConceptCouplingConnectionSystemDeflection',)


class ConceptCouplingConnectionSystemDeflection(_2663.CouplingConnectionSystemDeflection):
    """ConceptCouplingConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConceptCouplingConnectionSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2284.ConceptCouplingConnection':
        """ConceptCouplingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6752.ConceptCouplingConnectionLoadCase':
        """ConceptCouplingConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_3990.ConceptCouplingConnectionPowerFlow':
        """ConceptCouplingConnectionPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

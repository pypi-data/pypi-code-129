"""_2633.py

BeltConnectionSystemDeflection
"""


from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets import _2208, _2213
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6735, _6768
from mastapy.system_model.analyses_and_results.power_flows import _3973, _4004
from mastapy.system_model.analyses_and_results.system_deflections import _2701
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'BeltConnectionSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BeltConnectionSystemDeflection',)


class BeltConnectionSystemDeflection(_2701.InterMountableComponentConnectionSystemDeflection):
    """BeltConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BeltConnectionSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def extension(self) -> 'float':
        """float: 'Extension' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Extension
        return temp

    @property
    def extension_including_pre_tension(self) -> 'float':
        """float: 'ExtensionIncludingPreTension' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExtensionIncludingPreTension
        return temp

    @property
    def force_in_loa(self) -> 'float':
        """float: 'ForceInLOA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceInLOA
        return temp

    @property
    def connection_design(self) -> '_2208.BeltConnection':
        """BeltConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        if _2208.BeltConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to BeltConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6735.BeltConnectionLoadCase':
        """BeltConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase
        if _6735.BeltConnectionLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_load_case to BeltConnectionLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_3973.BeltConnectionPowerFlow':
        """BeltConnectionPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        if _3973.BeltConnectionPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to BeltConnectionPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

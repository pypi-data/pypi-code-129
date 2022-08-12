"""_2666.py

CVTBeltConnectionSystemDeflection
"""


from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets import _2213
from mastapy.system_model.analyses_and_results.power_flows import _4004
from mastapy.system_model.analyses_and_results.system_deflections import _2633
from mastapy._internal.python_net import python_net_import

_CVT_BELT_CONNECTION_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'CVTBeltConnectionSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CVTBeltConnectionSystemDeflection',)


class CVTBeltConnectionSystemDeflection(_2633.BeltConnectionSystemDeflection):
    """CVTBeltConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CVT_BELT_CONNECTION_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CVTBeltConnectionSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def belt_clamping_force_safety_factor(self) -> 'float':
        """float: 'BeltClampingForceSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BeltClampingForceSafetyFactor
        return temp

    @property
    def minimum_required_clamping_force(self) -> 'float':
        """float: 'MinimumRequiredClampingForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumRequiredClampingForce
        return temp

    @property
    def pump_efficiency(self) -> 'float':
        """float: 'PumpEfficiency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PumpEfficiency
        return temp

    @property
    def total_efficiency(self) -> 'float':
        """float: 'TotalEfficiency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalEfficiency
        return temp

    @property
    def variator_efficiency(self) -> 'float':
        """float: 'VariatorEfficiency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VariatorEfficiency
        return temp

    @property
    def connection_design(self) -> '_2213.CVTBeltConnection':
        """CVTBeltConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4004.CVTBeltConnectionPowerFlow':
        """CVTBeltConnectionPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

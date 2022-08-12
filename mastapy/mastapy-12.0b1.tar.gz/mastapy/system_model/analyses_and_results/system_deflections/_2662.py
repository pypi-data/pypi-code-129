"""_2662.py

ConnectorSystemDeflection
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy._math.vector_3d import Vector3D
from mastapy.system_model.part_model import _2387, _2380, _2406
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.part_model.couplings import _2537
from mastapy.math_utility.measured_vectors import _1523
from mastapy.system_model.analyses_and_results.system_deflections import _2691, _2716
from mastapy.system_model.fe import _2324
from mastapy.system_model.analyses_and_results.power_flows import (
    _4000, _3972, _4043, _4062
)
from mastapy._internal.python_net import python_net_import

_CONNECTOR_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'ConnectorSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectorSystemDeflection',)


class ConnectorSystemDeflection(_2716.MountableComponentSystemDeflection):
    """ConnectorSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConnectorSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def convergence_delta_energy(self) -> 'float':
        """float: 'ConvergenceDeltaEnergy' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConvergenceDeltaEnergy
        return temp

    @property
    def linear_force_on_inner(self) -> 'Vector3D':
        """Vector3D: 'LinearForceOnInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LinearForceOnInner
        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def moment_on_inner(self) -> 'Vector3D':
        """Vector3D: 'MomentOnInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MomentOnInner
        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def component_design(self) -> '_2387.Connector':
        """Connector: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        if _2387.Connector.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Connector. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_bearing(self) -> '_2380.Bearing':
        """Bearing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        if _2380.Bearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Bearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_oil_seal(self) -> '_2406.OilSeal':
        """OilSeal: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        if _2406.OilSeal.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to OilSeal. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design_of_type_shaft_hub_connection(self) -> '_2537.ShaftHubConnection':
        """ShaftHubConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        if _2537.ShaftHubConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to ShaftHubConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def force_on_outer_support_in_lcs(self) -> '_1523.VectorWithLinearAndAngularComponents':
        """VectorWithLinearAndAngularComponents: 'ForceOnOuterSupportInLCS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceOnOuterSupportInLCS
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def force_on_outer_support_in_wcs(self) -> '_1523.VectorWithLinearAndAngularComponents':
        """VectorWithLinearAndAngularComponents: 'ForceOnOuterSupportInWCS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceOnOuterSupportInWCS
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_fe_part(self) -> '_2691.FEPartSystemDeflection':
        """FEPartSystemDeflection: 'OuterFEPart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterFEPart
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def outer_fe_substructure_nodes(self) -> 'List[_2324.FESubstructureNode]':
        """List[FESubstructureNode]: 'OuterFESubstructureNodes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OuterFESubstructureNodes
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def power_flow_results(self) -> '_4000.ConnectorPowerFlow':
        """ConnectorPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        if _4000.ConnectorPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to ConnectorPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_bearing_power_flow(self) -> '_3972.BearingPowerFlow':
        """BearingPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        if _3972.BearingPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to BearingPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_oil_seal_power_flow(self) -> '_4043.OilSealPowerFlow':
        """OilSealPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        if _4043.OilSealPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to OilSealPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results_of_type_shaft_hub_connection_power_flow(self) -> '_4062.ShaftHubConnectionPowerFlow':
        """ShaftHubConnectionPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        if _4062.ShaftHubConnectionPowerFlow.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_results to ShaftHubConnectionPowerFlow. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

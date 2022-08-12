"""_2359.py

FELinkWithSelection
"""


from mastapy.system_model.fe.links import (
    _2357, _2358, _2360, _2361,
    _2362, _2363, _2364, _2365,
    _2366, _2367, _2368, _2369,
    _2370, _2371
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_FE_LINK_WITH_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.FE.Links', 'FELinkWithSelection')


__docformat__ = 'restructuredtext en'
__all__ = ('FELinkWithSelection',)


class FELinkWithSelection(_0.APIBase):
    """FELinkWithSelection

    This is a mastapy class.
    """

    TYPE = _FE_LINK_WITH_SELECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FELinkWithSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def link(self) -> '_2357.FELink':
        """FELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link
        if _2357.FELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to FELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def link_of_type_electric_machine_stator_fe_link(self) -> '_2358.ElectricMachineStatorFELink':
        """ElectricMachineStatorFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link
        if _2358.ElectricMachineStatorFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to ElectricMachineStatorFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def link_of_type_gear_mesh_fe_link(self) -> '_2360.GearMeshFELink':
        """GearMeshFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link
        if _2360.GearMeshFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to GearMeshFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def link_of_type_gear_with_duplicated_meshes_fe_link(self) -> '_2361.GearWithDuplicatedMeshesFELink':
        """GearWithDuplicatedMeshesFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link
        if _2361.GearWithDuplicatedMeshesFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to GearWithDuplicatedMeshesFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def link_of_type_multi_angle_connection_fe_link(self) -> '_2362.MultiAngleConnectionFELink':
        """MultiAngleConnectionFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link
        if _2362.MultiAngleConnectionFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to MultiAngleConnectionFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def link_of_type_multi_node_connector_fe_link(self) -> '_2363.MultiNodeConnectorFELink':
        """MultiNodeConnectorFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link
        if _2363.MultiNodeConnectorFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to MultiNodeConnectorFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def link_of_type_multi_node_fe_link(self) -> '_2364.MultiNodeFELink':
        """MultiNodeFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link
        if _2364.MultiNodeFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to MultiNodeFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def link_of_type_planetary_connector_multi_node_fe_link(self) -> '_2365.PlanetaryConnectorMultiNodeFELink':
        """PlanetaryConnectorMultiNodeFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link
        if _2365.PlanetaryConnectorMultiNodeFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to PlanetaryConnectorMultiNodeFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def link_of_type_planet_based_fe_link(self) -> '_2366.PlanetBasedFELink':
        """PlanetBasedFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link
        if _2366.PlanetBasedFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to PlanetBasedFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def link_of_type_planet_carrier_fe_link(self) -> '_2367.PlanetCarrierFELink':
        """PlanetCarrierFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link
        if _2367.PlanetCarrierFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to PlanetCarrierFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def link_of_type_point_load_fe_link(self) -> '_2368.PointLoadFELink':
        """PointLoadFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link
        if _2368.PointLoadFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to PointLoadFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def link_of_type_rolling_ring_connection_fe_link(self) -> '_2369.RollingRingConnectionFELink':
        """RollingRingConnectionFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link
        if _2369.RollingRingConnectionFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to RollingRingConnectionFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def link_of_type_shaft_hub_connection_fe_link(self) -> '_2370.ShaftHubConnectionFELink':
        """ShaftHubConnectionFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link
        if _2370.ShaftHubConnectionFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to ShaftHubConnectionFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def link_of_type_single_node_fe_link(self) -> '_2371.SingleNodeFELink':
        """SingleNodeFELink: 'Link' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Link
        if _2371.SingleNodeFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast link to SingleNodeFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    def add_selected_nodes(self):
        """ 'AddSelectedNodes' is the original name of this method."""

        self.wrapped.AddSelectedNodes()

    def delete_all_nodes(self):
        """ 'DeleteAllNodes' is the original name of this method."""

        self.wrapped.DeleteAllNodes()

    def select_component(self):
        """ 'SelectComponent' is the original name of this method."""

        self.wrapped.SelectComponent()

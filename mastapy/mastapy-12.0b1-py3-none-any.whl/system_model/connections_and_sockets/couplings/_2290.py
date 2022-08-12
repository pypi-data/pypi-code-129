"""_2290.py

SpringDamperConnection
"""


from mastapy.system_model import _2145
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.nodal_analysis import _72
from mastapy.system_model.connections_and_sockets.couplings import _2286
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings', 'SpringDamperConnection')


__docformat__ = 'restructuredtext en'
__all__ = ('SpringDamperConnection',)


class SpringDamperConnection(_2286.CouplingConnection):
    """SpringDamperConnection

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpringDamperConnection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def damping_option(self) -> '_2145.ComponentDampingOption':
        """ComponentDampingOption: 'DampingOption' is the original name of this property."""

        temp = self.wrapped.DampingOption
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_2145.ComponentDampingOption)(value) if value is not None else None

    @damping_option.setter
    def damping_option(self, value: '_2145.ComponentDampingOption'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.DampingOption = value

    @property
    def damping(self) -> '_72.LinearDampingConnectionProperties':
        """LinearDampingConnectionProperties: 'Damping' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Damping
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

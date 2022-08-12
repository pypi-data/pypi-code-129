"""_6860.py

RollingRingConnectionLoadCase
"""


from typing import List

from mastapy.system_model.connections_and_sockets import _2232
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6825
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'RollingRingConnectionLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingConnectionLoadCase',)


class RollingRingConnectionLoadCase(_6825.InterMountableComponentConnectionLoadCase):
    """RollingRingConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_CONNECTION_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RollingRingConnectionLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2232.RollingRingConnection':
        """RollingRingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[RollingRingConnectionLoadCase]':
        """List[RollingRingConnectionLoadCase]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

"""_5404.py

RollingRingConnectionMultibodyDynamicsAnalysis
"""


from typing import List

from mastapy._math.vector_3d import Vector3D
from mastapy._internal import constructor, conversion
from mastapy.system_model.connections_and_sockets import _2232
from mastapy.system_model.analyses_and_results.static_loads import _6860
from mastapy.system_model.analyses_and_results.mbd_analyses import _5374
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'RollingRingConnectionMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRingConnectionMultibodyDynamicsAnalysis',)


class RollingRingConnectionMultibodyDynamicsAnalysis(_5374.InterMountableComponentConnectionMultibodyDynamicsAnalysis):
    """RollingRingConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RollingRingConnectionMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def force_on_ring_a(self) -> 'Vector3D':
        """Vector3D: 'ForceOnRingA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceOnRingA
        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def normal_force(self) -> 'float':
        """float: 'NormalForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalForce
        return temp

    @property
    def separation(self) -> 'float':
        """float: 'Separation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Separation
        return temp

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
    def connection_load_case(self) -> '_6860.RollingRingConnectionLoadCase':
        """RollingRingConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[RollingRingConnectionMultibodyDynamicsAnalysis]':
        """List[RollingRingConnectionMultibodyDynamicsAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

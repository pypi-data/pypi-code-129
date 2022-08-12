"""_2247.py

ConicalGearMesh
"""


from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2253
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH = python_net_import('SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears', 'ConicalGearMesh')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalGearMesh',)


class ConicalGearMesh(_2253.GearMesh):
    """ConicalGearMesh

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalGearMesh.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def crowning(self) -> 'float':
        """float: 'Crowning' is the original name of this property."""

        temp = self.wrapped.Crowning
        return temp

    @crowning.setter
    def crowning(self, value: 'float'):
        self.wrapped.Crowning = float(value) if value else 0.0

    @property
    def pinion_drop_angle(self) -> 'float':
        """float: 'PinionDropAngle' is the original name of this property."""

        temp = self.wrapped.PinionDropAngle
        return temp

    @pinion_drop_angle.setter
    def pinion_drop_angle(self, value: 'float'):
        self.wrapped.PinionDropAngle = float(value) if value else 0.0

    @property
    def wheel_drop_angle(self) -> 'float':
        """float: 'WheelDropAngle' is the original name of this property."""

        temp = self.wrapped.WheelDropAngle
        return temp

    @wheel_drop_angle.setter
    def wheel_drop_angle(self, value: 'float'):
        self.wrapped.WheelDropAngle = float(value) if value else 0.0

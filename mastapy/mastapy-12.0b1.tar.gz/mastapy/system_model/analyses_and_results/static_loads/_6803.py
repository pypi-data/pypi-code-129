"""_6803.py

ForceAndTorqueScalingFactor
"""


from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_FORCE_AND_TORQUE_SCALING_FACTOR = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ForceAndTorqueScalingFactor')


__docformat__ = 'restructuredtext en'
__all__ = ('ForceAndTorqueScalingFactor',)


class ForceAndTorqueScalingFactor(_0.APIBase):
    """ForceAndTorqueScalingFactor

    This is a mastapy class.
    """

    TYPE = _FORCE_AND_TORQUE_SCALING_FACTOR

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ForceAndTorqueScalingFactor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def force_scaling_factor(self) -> 'float':
        """float: 'ForceScalingFactor' is the original name of this property."""

        temp = self.wrapped.ForceScalingFactor
        return temp

    @force_scaling_factor.setter
    def force_scaling_factor(self, value: 'float'):
        self.wrapped.ForceScalingFactor = float(value) if value else 0.0

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name
        return temp

    @property
    def speed(self) -> 'float':
        """float: 'Speed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Speed
        return temp

    @property
    def torque_scaling_factor(self) -> 'float':
        """float: 'TorqueScalingFactor' is the original name of this property."""

        temp = self.wrapped.TorqueScalingFactor
        return temp

    @torque_scaling_factor.setter
    def torque_scaling_factor(self, value: 'float'):
        self.wrapped.TorqueScalingFactor = float(value) if value else 0.0

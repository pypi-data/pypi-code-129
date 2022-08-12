"""_2391.py

EngineSpeed
"""


from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ENGINE_SPEED = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'EngineSpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('EngineSpeed',)


class EngineSpeed(_0.APIBase):
    """EngineSpeed

    This is a mastapy class.
    """

    TYPE = _ENGINE_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'EngineSpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def can_do_efficiency(self) -> 'bool':
        """bool: 'CanDoEfficiency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CanDoEfficiency
        return temp

    @property
    def number_of_part_loads(self) -> 'int':
        """int: 'NumberOfPartLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfPartLoads
        return temp

    @property
    def number_of_part_torques(self) -> 'int':
        """int: 'NumberOfPartTorques' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfPartTorques
        return temp

    @property
    def part_loads_dummy(self) -> 'str':
        """str: 'PartLoadsDummy' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PartLoadsDummy
        return temp

    @property
    def torque(self) -> 'float':
        """float: 'Torque' is the original name of this property."""

        temp = self.wrapped.Torque
        return temp

    @torque.setter
    def torque(self, value: 'float'):
        self.wrapped.Torque = float(value) if value else 0.0

"""_2382.py

Bolt
"""


from mastapy.system_model.part_model import _2383, _2384
from mastapy._internal import constructor
from mastapy.bolts import _1441
from mastapy._internal.python_net import python_net_import

_BOLT = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'Bolt')


__docformat__ = 'restructuredtext en'
__all__ = ('Bolt',)


class Bolt(_2384.Component):
    """Bolt

    This is a mastapy class.
    """

    TYPE = _BOLT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'Bolt.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bolted_joint(self) -> '_2383.BoltedJoint':
        """BoltedJoint: 'BoltedJoint' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoltedJoint
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def loaded_bolt(self) -> '_1441.LoadedBolt':
        """LoadedBolt: 'LoadedBolt' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadedBolt
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

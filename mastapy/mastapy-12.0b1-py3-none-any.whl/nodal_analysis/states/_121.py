"""_121.py

EntityVectorState
"""


from mastapy._internal import constructor
from mastapy.math_utility import (
    _1484, _1467, _1482, _1494
)
from mastapy._internal.cast_exception import CastException
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ENTITY_VECTOR_STATE = python_net_import('SMT.MastaAPI.NodalAnalysis.States', 'EntityVectorState')


__docformat__ = 'restructuredtext en'
__all__ = ('EntityVectorState',)


class EntityVectorState(_0.APIBase):
    """EntityVectorState

    This is a mastapy class.
    """

    TYPE = _ENTITY_VECTOR_STATE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'EntityVectorState.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def degrees_of_freedom_per_entity(self) -> 'int':
        """int: 'DegreesOfFreedomPerEntity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DegreesOfFreedomPerEntity
        return temp

    @property
    def number_of_entities(self) -> 'int':
        """int: 'NumberOfEntities' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfEntities
        return temp

    @property
    def vector(self) -> '_1484.RealVector':
        """RealVector: 'Vector' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Vector
        if _1484.RealVector.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast vector to RealVector. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

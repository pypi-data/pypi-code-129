"""_270.py

SafetyFactorGroup
"""


from typing import List

from mastapy.materials import _271
from mastapy._internal import constructor, conversion
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_SAFETY_FACTOR_GROUP = python_net_import('SMT.MastaAPI.Materials', 'SafetyFactorGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('SafetyFactorGroup',)


class SafetyFactorGroup(_0.APIBase):
    """SafetyFactorGroup

    This is a mastapy class.
    """

    TYPE = _SAFETY_FACTOR_GROUP

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SafetyFactorGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def items(self) -> 'List[_271.SafetyFactorItem]':
        """List[SafetyFactorItem]: 'Items' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Items
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

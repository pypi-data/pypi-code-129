"""_2535.py

RollingRing
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears import _324
from mastapy.system_model.part_model.couplings import _2523
from mastapy._internal.python_net import python_net_import

_ROLLING_RING = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Couplings', 'RollingRing')


__docformat__ = 'restructuredtext en'
__all__ = ('RollingRing',)


class RollingRing(_2523.CouplingHalf):
    """RollingRing

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RollingRing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_diameter(self) -> 'float':
        """float: 'AverageDiameter' is the original name of this property."""

        temp = self.wrapped.AverageDiameter
        return temp

    @average_diameter.setter
    def average_diameter(self, value: 'float'):
        self.wrapped.AverageDiameter = float(value) if value else 0.0

    @property
    def is_internal(self) -> 'bool':
        """bool: 'IsInternal' is the original name of this property."""

        temp = self.wrapped.IsInternal
        return temp

    @is_internal.setter
    def is_internal(self, value: 'bool'):
        self.wrapped.IsInternal = bool(value) if value else False

    @property
    def largest_end(self) -> '_324.Hand':
        """Hand: 'LargestEnd' is the original name of this property."""

        temp = self.wrapped.LargestEnd
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_324.Hand)(value) if value is not None else None

    @largest_end.setter
    def largest_end(self, value: '_324.Hand'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.LargestEnd = value

    @property
    def width(self) -> 'float':
        """float: 'Width' is the original name of this property."""

        temp = self.wrapped.Width
        return temp

    @width.setter
    def width(self, value: 'float'):
        self.wrapped.Width = float(value) if value else 0.0

"""_2432.py

AbstractShaftFromCAD
"""


from mastapy._internal import constructor
from mastapy.system_model.part_model.import_from_cad import _2434
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_FROM_CAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD', 'AbstractShaftFromCAD')


__docformat__ = 'restructuredtext en'
__all__ = ('AbstractShaftFromCAD',)


class AbstractShaftFromCAD(_2434.ComponentFromCAD):
    """AbstractShaftFromCAD

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_FROM_CAD

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AbstractShaftFromCAD.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def inner_diameter(self) -> 'float':
        """float: 'InnerDiameter' is the original name of this property."""

        temp = self.wrapped.InnerDiameter
        return temp

    @inner_diameter.setter
    def inner_diameter(self, value: 'float'):
        self.wrapped.InnerDiameter = float(value) if value else 0.0

    @property
    def length(self) -> 'float':
        """float: 'Length' is the original name of this property."""

        temp = self.wrapped.Length
        return temp

    @length.setter
    def length(self, value: 'float'):
        self.wrapped.Length = float(value) if value else 0.0

    @property
    def offset(self) -> 'float':
        """float: 'Offset' is the original name of this property."""

        temp = self.wrapped.Offset
        return temp

    @offset.setter
    def offset(self, value: 'float'):
        self.wrapped.Offset = float(value) if value else 0.0

    @property
    def outer_diameter(self) -> 'float':
        """float: 'OuterDiameter' is the original name of this property."""

        temp = self.wrapped.OuterDiameter
        return temp

    @outer_diameter.setter
    def outer_diameter(self, value: 'float'):
        self.wrapped.OuterDiameter = float(value) if value else 0.0

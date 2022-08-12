"""_1857.py

InterferenceDetail
"""


from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.materials import _260, _236
from mastapy.shafts import _24
from mastapy._internal.cast_exception import CastException
from mastapy.gears.materials import (
    _573, _575, _577, _581,
    _584, _587, _591, _593
)
from mastapy.electric_machines import _1260, _1277, _1287
from mastapy.detailed_rigid_connectors.splines import _1377
from mastapy.cycloidal import _1416, _1422
from mastapy.bolts import _1425, _1429
from mastapy.bearings.tolerances import _1850
from mastapy._internal.python_net import python_net_import

_INTERFERENCE_DETAIL = python_net_import('SMT.MastaAPI.Bearings.Tolerances', 'InterferenceDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('InterferenceDetail',)


class InterferenceDetail(_1850.BearingConnectionComponent):
    """InterferenceDetail

    This is a mastapy class.
    """

    TYPE = _INTERFERENCE_DETAIL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'InterferenceDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def diameter_tolerance_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'DiameterToleranceFactor' is the original name of this property."""

        temp = self.wrapped.DiameterToleranceFactor
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @diameter_tolerance_factor.setter
    def diameter_tolerance_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.DiameterToleranceFactor = value

    @property
    def temperature(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'Temperature' is the original name of this property."""

        temp = self.wrapped.Temperature
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @temperature.setter
    def temperature(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.Temperature = value

    @property
    def material(self) -> '_260.Material':
        """Material: 'Material' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Material
        if _260.Material.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast material to Material. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

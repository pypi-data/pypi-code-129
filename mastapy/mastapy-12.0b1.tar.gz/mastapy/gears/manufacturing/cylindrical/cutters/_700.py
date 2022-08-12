"""_700.py

CylindricalGearPlungeShaver
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.manufacturing.cylindrical import _603
from mastapy.gears.manufacturing.cylindrical.cutters import _705
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_PLUNGE_SHAVER = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters', 'CylindricalGearPlungeShaver')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearPlungeShaver',)


class CylindricalGearPlungeShaver(_705.CylindricalGearShaver):
    """CylindricalGearPlungeShaver

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_PLUNGE_SHAVER

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearPlungeShaver.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_width(self) -> 'float':
        """float: 'FaceWidth' is the original name of this property."""

        temp = self.wrapped.FaceWidth
        return temp

    @face_width.setter
    def face_width(self, value: 'float'):
        self.wrapped.FaceWidth = float(value) if value else 0.0

    @property
    def has_tolerances(self) -> 'bool':
        """bool: 'HasTolerances' is the original name of this property."""

        temp = self.wrapped.HasTolerances
        return temp

    @has_tolerances.setter
    def has_tolerances(self, value: 'bool'):
        self.wrapped.HasTolerances = bool(value) if value else False

    @property
    def left_flank_micro_geometry(self) -> '_603.CylindricalGearSpecifiedMicroGeometry':
        """CylindricalGearSpecifiedMicroGeometry: 'LeftFlankMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlankMicroGeometry
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def right_flank_micro_geometry(self) -> '_603.CylindricalGearSpecifiedMicroGeometry':
        """CylindricalGearSpecifiedMicroGeometry: 'RightFlankMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlankMicroGeometry
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def micro_geometry(self) -> 'List[_603.CylindricalGearSpecifiedMicroGeometry]':
        """List[CylindricalGearSpecifiedMicroGeometry]: 'MicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicroGeometry
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

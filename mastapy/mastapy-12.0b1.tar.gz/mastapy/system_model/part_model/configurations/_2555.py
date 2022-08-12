"""_2555.py

BearingDetailSelection
"""


from typing import List

from mastapy.bearings.bearing_results import _1908
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.system_model.part_model import _2381, _2380
from mastapy.system_model.part_model.configurations import _2557
from mastapy.bearings.bearing_designs import _2073
from mastapy._internal.python_net import python_net_import

_BEARING_DETAIL_SELECTION = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Configurations', 'BearingDetailSelection')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingDetailSelection',)


class BearingDetailSelection(_2557.PartDetailSelection['_2380.Bearing', '_2073.BearingDesign']):
    """BearingDetailSelection

    This is a mastapy class.
    """

    TYPE = _BEARING_DETAIL_SELECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BearingDetailSelection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def orientation(self) -> '_1908.Orientations':
        """Orientations: 'Orientation' is the original name of this property."""

        temp = self.wrapped.Orientation
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1908.Orientations)(value) if value is not None else None

    @orientation.setter
    def orientation(self, value: '_1908.Orientations'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.Orientation = value

    @property
    def mounting(self) -> 'List[_2381.BearingRaceMountingOptions]':
        """List[BearingRaceMountingOptions]: 'Mounting' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mounting
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

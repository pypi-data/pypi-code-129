"""_625.py

MicroGeometryInputsProfile
"""


from mastapy._internal import constructor
from mastapy.math_utility import _1448
from mastapy.math_utility.measured_ranges import _1524
from mastapy._internal.cast_exception import CastException
from mastapy.gears.manufacturing.cylindrical import _623, _627
from mastapy._internal.python_net import python_net_import

_MICRO_GEOMETRY_INPUTS_PROFILE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'MicroGeometryInputsProfile')


__docformat__ = 'restructuredtext en'
__all__ = ('MicroGeometryInputsProfile',)


class MicroGeometryInputsProfile(_623.MicroGeometryInputs['_627.ProfileModificationSegment']):
    """MicroGeometryInputsProfile

    This is a mastapy class.
    """

    TYPE = _MICRO_GEOMETRY_INPUTS_PROFILE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MicroGeometryInputsProfile.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_profile_segments(self) -> 'int':
        """int: 'NumberOfProfileSegments' is the original name of this property."""

        temp = self.wrapped.NumberOfProfileSegments
        return temp

    @number_of_profile_segments.setter
    def number_of_profile_segments(self, value: 'int'):
        self.wrapped.NumberOfProfileSegments = int(value) if value else 0

    @property
    def profile_micro_geometry_range(self) -> '_1448.Range':
        """Range: 'ProfileMicroGeometryRange' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileMicroGeometryRange
        if _1448.Range.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast profile_micro_geometry_range to Range. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def z_plane(self) -> 'float':
        """float: 'ZPlane' is the original name of this property."""

        temp = self.wrapped.ZPlane
        return temp

    @z_plane.setter
    def z_plane(self, value: 'float'):
        self.wrapped.ZPlane = float(value) if value else 0.0

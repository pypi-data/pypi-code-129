"""_1869.py

SupportDetail
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.bearings.tolerances import _1870, _1865, _1857
from mastapy._internal.python_net import python_net_import

_SUPPORT_DETAIL = python_net_import('SMT.MastaAPI.Bearings.Tolerances', 'SupportDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('SupportDetail',)


class SupportDetail(_1857.InterferenceDetail):
    """SupportDetail

    This is a mastapy class.
    """

    TYPE = _SUPPORT_DETAIL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SupportDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def angle_of_radial_error(self) -> 'float':
        """float: 'AngleOfRadialError' is the original name of this property."""

        temp = self.wrapped.AngleOfRadialError
        return temp

    @angle_of_radial_error.setter
    def angle_of_radial_error(self, value: 'float'):
        self.wrapped.AngleOfRadialError = float(value) if value else 0.0

    @property
    def material_source(self) -> '_1870.SupportMaterialSource':
        """SupportMaterialSource: 'MaterialSource' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaterialSource
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1870.SupportMaterialSource)(value) if value is not None else None

    @property
    def radial_error_magnitude(self) -> 'float':
        """float: 'RadialErrorMagnitude' is the original name of this property."""

        temp = self.wrapped.RadialErrorMagnitude
        return temp

    @radial_error_magnitude.setter
    def radial_error_magnitude(self, value: 'float'):
        self.wrapped.RadialErrorMagnitude = float(value) if value else 0.0

    @property
    def radial_specification_method(self) -> '_1865.RadialSpecificationMethod':
        """RadialSpecificationMethod: 'RadialSpecificationMethod' is the original name of this property."""

        temp = self.wrapped.RadialSpecificationMethod
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1865.RadialSpecificationMethod)(value) if value is not None else None

    @radial_specification_method.setter
    def radial_specification_method(self, value: '_1865.RadialSpecificationMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.RadialSpecificationMethod = value

    @property
    def theta_x(self) -> 'float':
        """float: 'ThetaX' is the original name of this property."""

        temp = self.wrapped.ThetaX
        return temp

    @theta_x.setter
    def theta_x(self, value: 'float'):
        self.wrapped.ThetaX = float(value) if value else 0.0

    @property
    def theta_y(self) -> 'float':
        """float: 'ThetaY' is the original name of this property."""

        temp = self.wrapped.ThetaY
        return temp

    @theta_y.setter
    def theta_y(self, value: 'float'):
        self.wrapped.ThetaY = float(value) if value else 0.0

    @property
    def x(self) -> 'float':
        """float: 'X' is the original name of this property."""

        temp = self.wrapped.X
        return temp

    @x.setter
    def x(self, value: 'float'):
        self.wrapped.X = float(value) if value else 0.0

    @property
    def y(self) -> 'float':
        """float: 'Y' is the original name of this property."""

        temp = self.wrapped.Y
        return temp

    @y.setter
    def y(self, value: 'float'):
        self.wrapped.Y = float(value) if value else 0.0

    @property
    def z(self) -> 'float':
        """float: 'Z' is the original name of this property."""

        temp = self.wrapped.Z
        return temp

    @z.setter
    def z(self, value: 'float'):
        self.wrapped.Z = float(value) if value else 0.0

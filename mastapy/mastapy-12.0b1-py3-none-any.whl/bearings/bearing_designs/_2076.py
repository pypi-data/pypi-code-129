"""_2076.py

LinearBearing
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.bearings import _1831
from mastapy.bearings.bearing_designs import _2073
from mastapy._internal.python_net import python_net_import

_LINEAR_BEARING = python_net_import('SMT.MastaAPI.Bearings.BearingDesigns', 'LinearBearing')


__docformat__ = 'restructuredtext en'
__all__ = ('LinearBearing',)


class LinearBearing(_2073.BearingDesign):
    """LinearBearing

    This is a mastapy class.
    """

    TYPE = _LINEAR_BEARING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'LinearBearing.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_stiffness(self) -> 'float':
        """float: 'AxialStiffness' is the original name of this property."""

        temp = self.wrapped.AxialStiffness
        return temp

    @axial_stiffness.setter
    def axial_stiffness(self, value: 'float'):
        self.wrapped.AxialStiffness = float(value) if value else 0.0

    @property
    def bore(self) -> 'float':
        """float: 'Bore' is the original name of this property."""

        temp = self.wrapped.Bore
        return temp

    @bore.setter
    def bore(self, value: 'float'):
        self.wrapped.Bore = float(value) if value else 0.0

    @property
    def outer_diameter(self) -> 'float':
        """float: 'OuterDiameter' is the original name of this property."""

        temp = self.wrapped.OuterDiameter
        return temp

    @outer_diameter.setter
    def outer_diameter(self, value: 'float'):
        self.wrapped.OuterDiameter = float(value) if value else 0.0

    @property
    def radial_stiffness(self) -> 'float':
        """float: 'RadialStiffness' is the original name of this property."""

        temp = self.wrapped.RadialStiffness
        return temp

    @radial_stiffness.setter
    def radial_stiffness(self, value: 'float'):
        self.wrapped.RadialStiffness = float(value) if value else 0.0

    @property
    def stiffness_options(self) -> '_1831.BearingStiffnessMatrixOption':
        """BearingStiffnessMatrixOption: 'StiffnessOptions' is the original name of this property."""

        temp = self.wrapped.StiffnessOptions
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1831.BearingStiffnessMatrixOption)(value) if value is not None else None

    @stiffness_options.setter
    def stiffness_options(self, value: '_1831.BearingStiffnessMatrixOption'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.StiffnessOptions = value

    @property
    def tilt_stiffness(self) -> 'float':
        """float: 'TiltStiffness' is the original name of this property."""

        temp = self.wrapped.TiltStiffness
        return temp

    @tilt_stiffness.setter
    def tilt_stiffness(self, value: 'float'):
        self.wrapped.TiltStiffness = float(value) if value else 0.0

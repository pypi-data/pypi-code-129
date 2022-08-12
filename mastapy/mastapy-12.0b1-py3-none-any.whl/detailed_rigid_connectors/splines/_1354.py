"""_1354.py

DIN5480SplineJointDesign
"""


from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.detailed_rigid_connectors.splines import _1381
from mastapy._internal.python_net import python_net_import

_DIN5480_SPLINE_JOINT_DESIGN = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Splines', 'DIN5480SplineJointDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('DIN5480SplineJointDesign',)


class DIN5480SplineJointDesign(_1381.StandardSplineJointDesign):
    """DIN5480SplineJointDesign

    This is a mastapy class.
    """

    TYPE = _DIN5480_SPLINE_JOINT_DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DIN5480SplineJointDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def addendum_modification_factor(self) -> 'overridable.Overridable_float':
        """overridable.Overridable_float: 'AddendumModificationFactor' is the original name of this property."""

        temp = self.wrapped.AddendumModificationFactor
        return constructor.new_from_mastapy_type(overridable.Overridable_float)(temp) if temp is not None else None

    @addendum_modification_factor.setter
    def addendum_modification_factor(self, value: 'overridable.Overridable_float.implicit_type()'):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else 0.0, is_overridden)
        self.wrapped.AddendumModificationFactor = value

    @property
    def base_diameter(self) -> 'float':
        """float: 'BaseDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BaseDiameter
        return temp

    @property
    def minimum_form_clearance(self) -> 'float':
        """float: 'MinimumFormClearance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumFormClearance
        return temp

    @property
    def nominal_space_width(self) -> 'float':
        """float: 'NominalSpaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalSpaceWidth
        return temp

    @property
    def nominal_tooth_thickness(self) -> 'float':
        """float: 'NominalToothThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalToothThickness
        return temp

    @property
    def pitch_diameter(self) -> 'float':
        """float: 'PitchDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PitchDiameter
        return temp

    @property
    def reference_diameter(self) -> 'float':
        """float: 'ReferenceDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReferenceDiameter
        return temp

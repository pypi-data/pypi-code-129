"""_1369.py

SAESplineJointDesign
"""


from mastapy.detailed_rigid_connectors.splines import _1356, _1381
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.python_net import python_net_import

_SAE_SPLINE_JOINT_DESIGN = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Splines', 'SAESplineJointDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('SAESplineJointDesign',)


class SAESplineJointDesign(_1381.StandardSplineJointDesign):
    """SAESplineJointDesign

    This is a mastapy class.
    """

    TYPE = _SAE_SPLINE_JOINT_DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SAESplineJointDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fit_type(self) -> '_1356.FitTypes':
        """FitTypes: 'FitType' is the original name of this property."""

        temp = self.wrapped.FitType
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1356.FitTypes)(value) if value is not None else None

    @fit_type.setter
    def fit_type(self, value: '_1356.FitTypes'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.FitType = value

    @property
    def form_clearance(self) -> 'float':
        """float: 'FormClearance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FormClearance
        return temp

    @property
    def maximum_effective_clearance(self) -> 'float':
        """float: 'MaximumEffectiveClearance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumEffectiveClearance
        return temp

    @property
    def maximum_tip_chamfer(self) -> 'float':
        """float: 'MaximumTipChamfer' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumTipChamfer
        return temp

    @property
    def minimum_effective_clearance(self) -> 'float':
        """float: 'MinimumEffectiveClearance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumEffectiveClearance
        return temp

    @property
    def minimum_tip_chamfer(self) -> 'float':
        """float: 'MinimumTipChamfer' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumTipChamfer
        return temp

    @property
    def number_of_teeth(self) -> 'int':
        """int: 'NumberOfTeeth' is the original name of this property."""

        temp = self.wrapped.NumberOfTeeth
        return temp

    @number_of_teeth.setter
    def number_of_teeth(self, value: 'int'):
        self.wrapped.NumberOfTeeth = int(value) if value else 0

    @property
    def use_internal_half_minimum_minor_diameter_for_external_half_form_diameter_calculation(self) -> 'bool':
        """bool: 'UseInternalHalfMinimumMinorDiameterForExternalHalfFormDiameterCalculation' is the original name of this property."""

        temp = self.wrapped.UseInternalHalfMinimumMinorDiameterForExternalHalfFormDiameterCalculation
        return temp

    @use_internal_half_minimum_minor_diameter_for_external_half_form_diameter_calculation.setter
    def use_internal_half_minimum_minor_diameter_for_external_half_form_diameter_calculation(self, value: 'bool'):
        self.wrapped.UseInternalHalfMinimumMinorDiameterForExternalHalfFormDiameterCalculation = bool(value) if value else False

    @property
    def use_saeb921b_1996(self) -> 'bool':
        """bool: 'UseSAEB921b1996' is the original name of this property."""

        temp = self.wrapped.UseSAEB921b1996
        return temp

    @use_saeb921b_1996.setter
    def use_saeb921b_1996(self, value: 'bool'):
        self.wrapped.UseSAEB921b1996 = bool(value) if value else False

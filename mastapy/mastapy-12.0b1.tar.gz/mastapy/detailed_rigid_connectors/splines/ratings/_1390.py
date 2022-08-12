"""_1390.py

SAESplineHalfRating
"""


from mastapy._internal import constructor
from mastapy.detailed_rigid_connectors.splines.ratings import _1392
from mastapy._internal.python_net import python_net_import

_SAE_SPLINE_HALF_RATING = python_net_import('SMT.MastaAPI.DetailedRigidConnectors.Splines.Ratings', 'SAESplineHalfRating')


__docformat__ = 'restructuredtext en'
__all__ = ('SAESplineHalfRating',)


class SAESplineHalfRating(_1392.SplineHalfRating):
    """SAESplineHalfRating

    This is a mastapy class.
    """

    TYPE = _SAE_SPLINE_HALF_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SAESplineHalfRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_compressive_stress(self) -> 'float':
        """float: 'AllowableCompressiveStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableCompressiveStress
        return temp

    @property
    def allowable_shear_stress(self) -> 'float':
        """float: 'AllowableShearStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableShearStress
        return temp

    @property
    def equivalent_stress(self) -> 'float':
        """float: 'EquivalentStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EquivalentStress
        return temp

    @property
    def fatigue_damage_for_compressive_stress(self) -> 'float':
        """float: 'FatigueDamageForCompressiveStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FatigueDamageForCompressiveStress
        return temp

    @property
    def fatigue_damage_for_equivalent_root_stress(self) -> 'float':
        """float: 'FatigueDamageForEquivalentRootStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FatigueDamageForEquivalentRootStress
        return temp

    @property
    def fatigue_damage_for_tooth_shearing_stress(self) -> 'float':
        """float: 'FatigueDamageForToothShearingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FatigueDamageForToothShearingStress
        return temp

    @property
    def maximum_allowable_compressive_stress(self) -> 'float':
        """float: 'MaximumAllowableCompressiveStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumAllowableCompressiveStress
        return temp

    @property
    def maximum_allowable_shear_stress(self) -> 'float':
        """float: 'MaximumAllowableShearStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumAllowableShearStress
        return temp

    @property
    def maximum_allowable_tensile_stress(self) -> 'float':
        """float: 'MaximumAllowableTensileStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumAllowableTensileStress
        return temp

    @property
    def root_bending_stress(self) -> 'float':
        """float: 'RootBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RootBendingStress
        return temp

    @property
    def safety_factor_for_compressive_stress(self) -> 'float':
        """float: 'SafetyFactorForCompressiveStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorForCompressiveStress
        return temp

    @property
    def safety_factor_for_equivalent_root_stress(self) -> 'float':
        """float: 'SafetyFactorForEquivalentRootStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorForEquivalentRootStress
        return temp

    @property
    def safety_factor_for_tooth_shearing_stress(self) -> 'float':
        """float: 'SafetyFactorForToothShearingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SafetyFactorForToothShearingStress
        return temp

    @property
    def stress_concentration_factor(self) -> 'float':
        """float: 'StressConcentrationFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StressConcentrationFactor
        return temp

    @property
    def torsional_shear_stress(self) -> 'float':
        """float: 'TorsionalShearStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorsionalShearStress
        return temp

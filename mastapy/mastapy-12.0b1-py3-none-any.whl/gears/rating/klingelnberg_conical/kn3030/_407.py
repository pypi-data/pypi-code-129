"""_407.py

KlingelnbergCycloPalloidConicalGearSingleFlankRating
"""


from mastapy._internal import constructor
from mastapy.gears.rating import _355
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.KlingelnbergConical.KN3030', 'KlingelnbergCycloPalloidConicalGearSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGearSingleFlankRating',)


class KlingelnbergCycloPalloidConicalGearSingleFlankRating(_355.GearSingleFlankRating):
    """KlingelnbergCycloPalloidConicalGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SINGLE_FLANK_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGearSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allowable_bending_stress_number(self) -> 'float':
        """float: 'AllowableBendingStressNumber' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableBendingStressNumber
        return temp

    @property
    def allowable_contact_stress_number(self) -> 'float':
        """float: 'AllowableContactStressNumber' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllowableContactStressNumber
        return temp

    @property
    def bending_stress(self) -> 'float':
        """float: 'BendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BendingStress
        return temp

    @property
    def bending_stress_limit(self) -> 'float':
        """float: 'BendingStressLimit' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BendingStressLimit
        return temp

    @property
    def bending_stress_safety_factor(self) -> 'float':
        """float: 'BendingStressSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BendingStressSafetyFactor
        return temp

    @property
    def flank_roughness(self) -> 'float':
        """float: 'FlankRoughness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlankRoughness
        return temp

    @property
    def mean_pitch_diameter(self) -> 'float':
        """float: 'MeanPitchDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanPitchDiameter
        return temp

    @property
    def rated_tangential_force(self) -> 'float':
        """float: 'RatedTangentialForce' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatedTangentialForce
        return temp

    @property
    def rated_torque(self) -> 'float':
        """float: 'RatedTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatedTorque
        return temp

    @property
    def relative_sensitivity_factor(self) -> 'float':
        """float: 'RelativeSensitivityFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeSensitivityFactor
        return temp

    @property
    def relative_surface_factor(self) -> 'float':
        """float: 'RelativeSurfaceFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeSurfaceFactor
        return temp

    @property
    def size_factor(self) -> 'float':
        """float: 'SizeFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SizeFactor
        return temp

    @property
    def stress_correction_factor(self) -> 'float':
        """float: 'StressCorrectionFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StressCorrectionFactor
        return temp

    @property
    def tangential_speed(self) -> 'float':
        """float: 'TangentialSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TangentialSpeed
        return temp

    @property
    def tooth_form_factor(self) -> 'float':
        """float: 'ToothFormFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothFormFactor
        return temp

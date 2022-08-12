"""_549.py

GleasonSpiralBevelGearSingleFlankRating
"""


from mastapy._internal import constructor
from mastapy.gears.rating.bevel.standards import _551
from mastapy._internal.python_net import python_net_import

_GLEASON_SPIRAL_BEVEL_GEAR_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Bevel.Standards', 'GleasonSpiralBevelGearSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('GleasonSpiralBevelGearSingleFlankRating',)


class GleasonSpiralBevelGearSingleFlankRating(_551.SpiralBevelGearSingleFlankRating):
    """GleasonSpiralBevelGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _GLEASON_SPIRAL_BEVEL_GEAR_SINGLE_FLANK_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GleasonSpiralBevelGearSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending_safety_factor_for_fatigue(self) -> 'float':
        """float: 'BendingSafetyFactorForFatigue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BendingSafetyFactorForFatigue
        return temp

    @property
    def calculated_bending_stress(self) -> 'float':
        """float: 'CalculatedBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedBendingStress
        return temp

    @property
    def calculated_contact_stress(self) -> 'float':
        """float: 'CalculatedContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedContactStress
        return temp

    @property
    def calculated_scoring_index(self) -> 'float':
        """float: 'CalculatedScoringIndex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedScoringIndex
        return temp

    @property
    def contact_safety_factor_for_fatigue(self) -> 'float':
        """float: 'ContactSafetyFactorForFatigue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactSafetyFactorForFatigue
        return temp

    @property
    def gear_blank_temperature(self) -> 'float':
        """float: 'GearBlankTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBlankTemperature
        return temp

    @property
    def hardness_ratio_factor(self) -> 'float':
        """float: 'HardnessRatioFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HardnessRatioFactor
        return temp

    @property
    def working_bending_stress(self) -> 'float':
        """float: 'WorkingBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorkingBendingStress
        return temp

    @property
    def working_contact_stress(self) -> 'float':
        """float: 'WorkingContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorkingContactStress
        return temp

    @property
    def working_scoring_index(self) -> 'float':
        """float: 'WorkingScoringIndex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorkingScoringIndex
        return temp

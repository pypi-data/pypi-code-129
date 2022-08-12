"""_433.py

GleasonHypoidGearSingleFlankRating
"""


from mastapy._internal import constructor
from mastapy.gears.rating.conical import _533
from mastapy._internal.python_net import python_net_import

_GLEASON_HYPOID_GEAR_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Hypoid.Standards', 'GleasonHypoidGearSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('GleasonHypoidGearSingleFlankRating',)


class GleasonHypoidGearSingleFlankRating(_533.ConicalGearSingleFlankRating):
    """GleasonHypoidGearSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _GLEASON_HYPOID_GEAR_SINGLE_FLANK_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GleasonHypoidGearSingleFlankRating.TYPE'):
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
    def contact_safety_factor_for_fatigue(self) -> 'float':
        """float: 'ContactSafetyFactorForFatigue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactSafetyFactorForFatigue
        return temp

    @property
    def geometry_factor_j(self) -> 'float':
        """float: 'GeometryFactorJ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GeometryFactorJ
        return temp

    @property
    def life_factor_bending(self) -> 'float':
        """float: 'LifeFactorBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LifeFactorBending
        return temp

    @property
    def life_factor_contact(self) -> 'float':
        """float: 'LifeFactorContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LifeFactorContact
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

"""_350.py

GearFlankRating
"""


from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_GEAR_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating', 'GearFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('GearFlankRating',)


class GearFlankRating(_0.APIBase):
    """GearFlankRating

    This is a mastapy class.
    """

    TYPE = _GEAR_FLANK_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearFlankRating.TYPE'):
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
    def bending_safety_factor_for_static(self) -> 'float':
        """float: 'BendingSafetyFactorForStatic' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BendingSafetyFactorForStatic
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
    def contact_safety_factor_for_static(self) -> 'float':
        """float: 'ContactSafetyFactorForStatic' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactSafetyFactorForStatic
        return temp

    @property
    def cycles(self) -> 'float':
        """float: 'Cycles' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Cycles
        return temp

    @property
    def damage_bending(self) -> 'float':
        """float: 'DamageBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DamageBending
        return temp

    @property
    def damage_contact(self) -> 'float':
        """float: 'DamageContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DamageContact
        return temp

    @property
    def maximum_bending_stress(self) -> 'float':
        """float: 'MaximumBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumBendingStress
        return temp

    @property
    def maximum_contact_stress(self) -> 'float':
        """float: 'MaximumContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumContactStress
        return temp

    @property
    def maximum_static_bending_stress(self) -> 'float':
        """float: 'MaximumStaticBendingStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumStaticBendingStress
        return temp

    @property
    def maximum_static_contact_stress(self) -> 'float':
        """float: 'MaximumStaticContactStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumStaticContactStress
        return temp

    @property
    def reliability_bending(self) -> 'float':
        """float: 'ReliabilityBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReliabilityBending
        return temp

    @property
    def reliability_contact(self) -> 'float':
        """float: 'ReliabilityContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReliabilityContact
        return temp

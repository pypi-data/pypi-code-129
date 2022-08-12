"""_352.py

GearRating
"""


from mastapy.materials import (
    _271, _241, _244, _245
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating import _347, _345
from mastapy._internal.python_net import python_net_import

_GEAR_RATING = python_net_import('SMT.MastaAPI.Gears.Rating', 'GearRating')


__docformat__ = 'restructuredtext en'
__all__ = ('GearRating',)


class GearRating(_345.AbstractGearRating):
    """GearRating

    This is a mastapy class.
    """

    TYPE = _GEAR_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending_safety_factor_results(self) -> '_271.SafetyFactorItem':
        """SafetyFactorItem: 'BendingSafetyFactorResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BendingSafetyFactorResults
        if _271.SafetyFactorItem.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bending_safety_factor_results to SafetyFactorItem. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def contact_safety_factor_results(self) -> '_271.SafetyFactorItem':
        """SafetyFactorItem: 'ContactSafetyFactorResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactSafetyFactorResults
        if _271.SafetyFactorItem.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast contact_safety_factor_results to SafetyFactorItem. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def static_safety_factor(self) -> '_347.BendingAndContactReportingObject':
        """BendingAndContactReportingObject: 'StaticSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StaticSafetyFactor
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

"""_1116.py

ProfileReliefWithDeviation
"""


from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical import _1016
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1118
from mastapy._internal.python_net import python_net_import

_PROFILE_RELIEF_WITH_DEVIATION = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical.MicroGeometry', 'ProfileReliefWithDeviation')


__docformat__ = 'restructuredtext en'
__all__ = ('ProfileReliefWithDeviation',)


class ProfileReliefWithDeviation(_1118.ReliefWithDeviation):
    """ProfileReliefWithDeviation

    This is a mastapy class.
    """

    TYPE = _PROFILE_RELIEF_WITH_DEVIATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ProfileReliefWithDeviation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def profile_relief(self) -> 'float':
        """float: 'ProfileRelief' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileRelief
        return temp

    @property
    def roll_distance(self) -> 'float':
        """float: 'RollDistance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollDistance
        return temp

    @property
    def position_on_profile(self) -> '_1016.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'PositionOnProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PositionOnProfile
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

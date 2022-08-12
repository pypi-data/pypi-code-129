"""_610.py

CylindricalManufacturedGearSetDutyCycle
"""


from mastapy.gears.manufacturing.cylindrical import _615
from mastapy._internal import constructor
from mastapy.gears.rating.cylindrical import _454
from mastapy.gears.analysis import _1216
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MANUFACTURED_GEAR_SET_DUTY_CYCLE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical', 'CylindricalManufacturedGearSetDutyCycle')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalManufacturedGearSetDutyCycle',)


class CylindricalManufacturedGearSetDutyCycle(_1216.GearSetImplementationAnalysisDutyCycle):
    """CylindricalManufacturedGearSetDutyCycle

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MANUFACTURED_GEAR_SET_DUTY_CYCLE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalManufacturedGearSetDutyCycle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def manufacturing_configuration(self) -> '_615.CylindricalSetManufacturingConfig':
        """CylindricalSetManufacturingConfig: 'ManufacturingConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ManufacturingConfiguration
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_454.CylindricalGearSetDutyCycleRating':
        """CylindricalGearSetDutyCycleRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

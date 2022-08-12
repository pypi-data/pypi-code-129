"""_715.py

CylindricalGearHobShape
"""


from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutters import _699
from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _720
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_HOB_SHAPE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters.Tangibles', 'CylindricalGearHobShape')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearHobShape',)


class CylindricalGearHobShape(_720.RackShape):
    """CylindricalGearHobShape

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_HOB_SHAPE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearHobShape.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def edge_height(self) -> 'float':
        """float: 'EdgeHeight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EdgeHeight
        return temp

    @property
    def maximum_blade_control_distance(self) -> 'float':
        """float: 'MaximumBladeControlDistance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumBladeControlDistance
        return temp

    @property
    def maximum_tip_control_distance_for_zero_protuberance(self) -> 'float':
        """float: 'MaximumTipControlDistanceForZeroProtuberance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumTipControlDistanceForZeroProtuberance
        return temp

    @property
    def protuberance_length(self) -> 'float':
        """float: 'ProtuberanceLength' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProtuberanceLength
        return temp

    @property
    def protuberance_pressure_angle(self) -> 'float':
        """float: 'ProtuberancePressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProtuberancePressureAngle
        return temp

    @property
    def design(self) -> '_699.CylindricalGearHobDesign':
        """CylindricalGearHobDesign: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

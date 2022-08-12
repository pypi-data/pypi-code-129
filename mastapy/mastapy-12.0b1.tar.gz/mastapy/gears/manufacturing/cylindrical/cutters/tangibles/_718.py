"""_718.py

CylindricalGearWormGrinderShape
"""


from mastapy.gears.manufacturing.cylindrical.cutters import _698
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _720
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_WORM_GRINDER_SHAPE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters.Tangibles', 'CylindricalGearWormGrinderShape')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearWormGrinderShape',)


class CylindricalGearWormGrinderShape(_720.RackShape):
    """CylindricalGearWormGrinderShape

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_WORM_GRINDER_SHAPE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearWormGrinderShape.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design(self) -> '_698.CylindricalGearGrindingWorm':
        """CylindricalGearGrindingWorm: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

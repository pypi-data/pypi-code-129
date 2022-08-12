"""_381.py

VirtualCylindricalGearISO10300MethodB1
"""


from mastapy._internal import constructor
from mastapy.gears.rating.virtual_cylindrical_gears import _379
from mastapy._internal.python_net import python_net_import

_VIRTUAL_CYLINDRICAL_GEAR_ISO10300_METHOD_B1 = python_net_import('SMT.MastaAPI.Gears.Rating.VirtualCylindricalGears', 'VirtualCylindricalGearISO10300MethodB1')


__docformat__ = 'restructuredtext en'
__all__ = ('VirtualCylindricalGearISO10300MethodB1',)


class VirtualCylindricalGearISO10300MethodB1(_379.VirtualCylindricalGear):
    """VirtualCylindricalGearISO10300MethodB1

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_CYLINDRICAL_GEAR_ISO10300_METHOD_B1

    __hash__ = None

    def __init__(self, instance_to_wrap: 'VirtualCylindricalGearISO10300MethodB1.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def base_diameter_of_virtual_cylindrical_gear_in_normal_section(self) -> 'float':
        """float: 'BaseDiameterOfVirtualCylindricalGearInNormalSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BaseDiameterOfVirtualCylindricalGearInNormalSection
        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name
        return temp

    @property
    def reference_diameter_in_normal_section(self) -> 'float':
        """float: 'ReferenceDiameterInNormalSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReferenceDiameterInNormalSection
        return temp

    @property
    def root_diameter_of_virtual_cylindrical_gear(self) -> 'float':
        """float: 'RootDiameterOfVirtualCylindricalGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RootDiameterOfVirtualCylindricalGear
        return temp

    @property
    def tip_diameter_of_virtual_cylindrical_gear_in_normal_section(self) -> 'float':
        """float: 'TipDiameterOfVirtualCylindricalGearInNormalSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TipDiameterOfVirtualCylindricalGearInNormalSection
        return temp

    @property
    def transverse_module(self) -> 'float':
        """float: 'TransverseModule' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseModule
        return temp

    @property
    def virtual_number_of_teeth_transverse(self) -> 'float':
        """float: 'VirtualNumberOfTeethTransverse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VirtualNumberOfTeethTransverse
        return temp

    @property
    def virtual_spur_gear_number_of_teeth(self) -> 'float':
        """float: 'VirtualSpurGearNumberOfTeeth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VirtualSpurGearNumberOfTeeth
        return temp

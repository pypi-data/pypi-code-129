"""_1276.py

Stator
"""


from mastapy._internal import constructor
from mastapy.electric_machines import _1282, _1229
from mastapy._internal.python_net import python_net_import

_STATOR = python_net_import('SMT.MastaAPI.ElectricMachines', 'Stator')


__docformat__ = 'restructuredtext en'
__all__ = ('Stator',)


class Stator(_1229.AbstractStator):
    """Stator

    This is a mastapy class.
    """

    TYPE = _STATOR

    __hash__ = None

    def __init__(self, instance_to_wrap: 'Stator.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def back_iron_inner_radius(self) -> 'float':
        """float: 'BackIronInnerRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BackIronInnerRadius
        return temp

    @property
    def back_iron_mid_radius(self) -> 'float':
        """float: 'BackIronMidRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BackIronMidRadius
        return temp

    @property
    def mid_tooth_radius(self) -> 'float':
        """float: 'MidToothRadius' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MidToothRadius
        return temp

    @property
    def radius_at_mid_coil_height(self) -> 'float':
        """float: 'RadiusAtMidCoilHeight' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadiusAtMidCoilHeight
        return temp

    @property
    def tooth_and_slot(self) -> '_1282.ToothAndSlot':
        """ToothAndSlot: 'ToothAndSlot' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothAndSlot
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

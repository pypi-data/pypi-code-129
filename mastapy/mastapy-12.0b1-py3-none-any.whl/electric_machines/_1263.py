"""_1263.py

NonCADElectricMachineDetail
"""


from mastapy.electric_machines import _1276, _1245
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import

_NON_CAD_ELECTRIC_MACHINE_DETAIL = python_net_import('SMT.MastaAPI.ElectricMachines', 'NonCADElectricMachineDetail')


__docformat__ = 'restructuredtext en'
__all__ = ('NonCADElectricMachineDetail',)


class NonCADElectricMachineDetail(_1245.ElectricMachineDetail):
    """NonCADElectricMachineDetail

    This is a mastapy class.
    """

    TYPE = _NON_CAD_ELECTRIC_MACHINE_DETAIL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'NonCADElectricMachineDetail.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def stator(self) -> '_1276.Stator':
        """Stator: 'Stator' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Stator
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

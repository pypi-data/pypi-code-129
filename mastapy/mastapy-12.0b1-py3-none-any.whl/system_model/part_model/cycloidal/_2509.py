"""_2509.py

RingPins
"""


from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import
from mastapy.cycloidal import _1421, _1422
from mastapy.system_model.part_model import _2404

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_RING_PINS = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Cycloidal', 'RingPins')


__docformat__ = 'restructuredtext en'
__all__ = ('RingPins',)


class RingPins(_2404.MountableComponent):
    """RingPins

    This is a mastapy class.
    """

    TYPE = _RING_PINS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RingPins.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def length(self) -> 'float':
        """float: 'Length' is the original name of this property."""

        temp = self.wrapped.Length
        return temp

    @length.setter
    def length(self, value: 'float'):
        self.wrapped.Length = float(value) if value else 0.0

    @property
    def ring_pins_material_database(self) -> 'str':
        """str: 'RingPinsMaterialDatabase' is the original name of this property."""

        temp = self.wrapped.RingPinsMaterialDatabase.SelectedItemName
        return temp

    @ring_pins_material_database.setter
    def ring_pins_material_database(self, value: 'str'):
        self.wrapped.RingPinsMaterialDatabase.SetSelectedItem(str(value) if value else '')

    @property
    def ring_pins_design(self) -> '_1421.RingPinsDesign':
        """RingPinsDesign: 'RingPinsDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingPinsDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ring_pins_material(self) -> '_1422.RingPinsMaterial':
        """RingPinsMaterial: 'RingPinsMaterial' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingPinsMaterial
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

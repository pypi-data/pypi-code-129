"""_2436.py

ConnectorFromCAD
"""


from mastapy.system_model.part_model.import_from_cad import _2442, _2443
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy._internal.python_net import python_net_import

_CONNECTOR_FROM_CAD = python_net_import('SMT.MastaAPI.SystemModel.PartModel.ImportFromCAD', 'ConnectorFromCAD')


__docformat__ = 'restructuredtext en'
__all__ = ('ConnectorFromCAD',)


class ConnectorFromCAD(_2443.MountableComponentFromCAD):
    """ConnectorFromCAD

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_FROM_CAD

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConnectorFromCAD.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mounting(self) -> '_2442.HousedOrMounted':
        """HousedOrMounted: 'Mounting' is the original name of this property."""

        temp = self.wrapped.Mounting
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_2442.HousedOrMounted)(value) if value is not None else None

    @mounting.setter
    def mounting(self, value: '_2442.HousedOrMounted'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.Mounting = value

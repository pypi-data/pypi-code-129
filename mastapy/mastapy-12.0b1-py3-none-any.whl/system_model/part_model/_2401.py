"""_2401.py

LoadSharingSettings
"""


from mastapy.system_model.part_model import _2400, _2378
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_LOAD_SHARING_SETTINGS = python_net_import('SMT.MastaAPI.SystemModel.PartModel', 'LoadSharingSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadSharingSettings',)


class LoadSharingSettings(_0.APIBase):
    """LoadSharingSettings

    This is a mastapy class.
    """

    TYPE = _LOAD_SHARING_SETTINGS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'LoadSharingSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetary_load_sharing(self) -> '_2400.LoadSharingModes':
        """LoadSharingModes: 'PlanetaryLoadSharing' is the original name of this property."""

        temp = self.wrapped.PlanetaryLoadSharing
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_2400.LoadSharingModes)(value) if value is not None else None

    @planetary_load_sharing.setter
    def planetary_load_sharing(self, value: '_2400.LoadSharingModes'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.PlanetaryLoadSharing = value

    @property
    def planetary_load_sharing_agma_application_level(self) -> '_2378.AGMALoadSharingTableApplicationLevel':
        """AGMALoadSharingTableApplicationLevel: 'PlanetaryLoadSharingAGMAApplicationLevel' is the original name of this property."""

        temp = self.wrapped.PlanetaryLoadSharingAGMAApplicationLevel
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_2378.AGMALoadSharingTableApplicationLevel)(value) if value is not None else None

    @planetary_load_sharing_agma_application_level.setter
    def planetary_load_sharing_agma_application_level(self, value: '_2378.AGMALoadSharingTableApplicationLevel'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.PlanetaryLoadSharingAGMAApplicationLevel = value

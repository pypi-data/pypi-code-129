"""_263.py

MaterialsSettingsDatabase
"""


from mastapy.utility.databases import _1784
from mastapy.materials import _264
from mastapy._internal.python_net import python_net_import

_MATERIALS_SETTINGS_DATABASE = python_net_import('SMT.MastaAPI.Materials', 'MaterialsSettingsDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('MaterialsSettingsDatabase',)


class MaterialsSettingsDatabase(_1784.NamedDatabase['_264.MaterialsSettingsItem']):
    """MaterialsSettingsDatabase

    This is a mastapy class.
    """

    TYPE = _MATERIALS_SETTINGS_DATABASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MaterialsSettingsDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

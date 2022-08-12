"""_1829.py

BearingSettingsDatabase
"""


from mastapy.utility.databases import _1784
from mastapy.bearings import _1830
from mastapy._internal.python_net import python_net_import

_BEARING_SETTINGS_DATABASE = python_net_import('SMT.MastaAPI.Bearings', 'BearingSettingsDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingSettingsDatabase',)


class BearingSettingsDatabase(_1784.NamedDatabase['_1830.BearingSettingsItem']):
    """BearingSettingsDatabase

    This is a mastapy class.
    """

    TYPE = _BEARING_SETTINGS_DATABASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BearingSettingsDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

"""_1012.py

CylindricalGearMicroGeometrySettingsDatabase
"""


from mastapy.utility.databases import _1784
from mastapy.gears.gear_designs.cylindrical import _1013
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MICRO_GEOMETRY_SETTINGS_DATABASE = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalGearMicroGeometrySettingsDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMicroGeometrySettingsDatabase',)


class CylindricalGearMicroGeometrySettingsDatabase(_1784.NamedDatabase['_1013.CylindricalGearMicroGeometrySettingsItem']):
    """CylindricalGearMicroGeometrySettingsDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MICRO_GEOMETRY_SETTINGS_DATABASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearMicroGeometrySettingsDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

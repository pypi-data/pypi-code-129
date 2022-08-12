"""_460.py

CylindricalPlasticGearRatingSettingsDatabase
"""


from mastapy.utility.databases import _1784
from mastapy.gears.rating.cylindrical import _461
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLASTIC_GEAR_RATING_SETTINGS_DATABASE = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'CylindricalPlasticGearRatingSettingsDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalPlasticGearRatingSettingsDatabase',)


class CylindricalPlasticGearRatingSettingsDatabase(_1784.NamedDatabase['_461.CylindricalPlasticGearRatingSettingsItem']):
    """CylindricalPlasticGearRatingSettingsDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLASTIC_GEAR_RATING_SETTINGS_DATABASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalPlasticGearRatingSettingsDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

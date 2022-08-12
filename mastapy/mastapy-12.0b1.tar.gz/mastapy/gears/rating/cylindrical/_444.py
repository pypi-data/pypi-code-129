"""_444.py

CylindricalGearDesignAndRatingSettingsDatabase
"""


from mastapy.utility.databases import _1784
from mastapy.gears.rating.cylindrical import _445
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_DESIGN_AND_RATING_SETTINGS_DATABASE = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical', 'CylindricalGearDesignAndRatingSettingsDatabase')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearDesignAndRatingSettingsDatabase',)


class CylindricalGearDesignAndRatingSettingsDatabase(_1784.NamedDatabase['_445.CylindricalGearDesignAndRatingSettingsItem']):
    """CylindricalGearDesignAndRatingSettingsDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_DESIGN_AND_RATING_SETTINGS_DATABASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearDesignAndRatingSettingsDatabase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

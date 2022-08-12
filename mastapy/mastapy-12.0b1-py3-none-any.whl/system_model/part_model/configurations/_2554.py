"""_2554.py

BearingDetailConfiguration
"""


from mastapy.system_model.part_model.configurations import _2556, _2555
from mastapy.system_model.part_model import _2380
from mastapy.bearings.bearing_designs import _2073
from mastapy._internal.python_net import python_net_import

_BEARING_DETAIL_CONFIGURATION = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Configurations', 'BearingDetailConfiguration')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingDetailConfiguration',)


class BearingDetailConfiguration(_2556.PartDetailConfiguration['_2555.BearingDetailSelection', '_2380.Bearing', '_2073.BearingDesign']):
    """BearingDetailConfiguration

    This is a mastapy class.
    """

    TYPE = _BEARING_DETAIL_CONFIGURATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BearingDetailConfiguration.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

"""_1848.py

SKFSettings
"""


from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling.skf_module import _2039
from mastapy.utility import _1554
from mastapy._internal.python_net import python_net_import

_SKF_SETTINGS = python_net_import('SMT.MastaAPI.Bearings', 'SKFSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('SKFSettings',)


class SKFSettings(_1554.PerMachineSettings):
    """SKFSettings

    This is a mastapy class.
    """

    TYPE = _SKF_SETTINGS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SKFSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def enable_skf_module(self) -> 'bool':
        """bool: 'EnableSKFModule' is the original name of this property."""

        temp = self.wrapped.EnableSKFModule
        return temp

    @enable_skf_module.setter
    def enable_skf_module(self, value: 'bool'):
        self.wrapped.EnableSKFModule = bool(value) if value else False

    @property
    def log_file_path(self) -> 'str':
        """str: 'LogFilePath' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LogFilePath
        return temp

    @property
    def log_http_requests(self) -> 'bool':
        """bool: 'LogHTTPRequests' is the original name of this property."""

        temp = self.wrapped.LogHTTPRequests
        return temp

    @log_http_requests.setter
    def log_http_requests(self, value: 'bool'):
        self.wrapped.LogHTTPRequests = bool(value) if value else False

    @property
    def skf_authentication(self) -> '_2039.SKFAuthentication':
        """SKFAuthentication: 'SKFAuthentication' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SKFAuthentication
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

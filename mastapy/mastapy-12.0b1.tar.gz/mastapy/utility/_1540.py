"""_1540.py

EnvironmentSummary
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.utility import _1553, _1539
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_ENVIRONMENT_SUMMARY = python_net_import('SMT.MastaAPI.Utility', 'EnvironmentSummary')


__docformat__ = 'restructuredtext en'
__all__ = ('EnvironmentSummary',)


class EnvironmentSummary(_0.APIBase):
    """EnvironmentSummary

    This is a mastapy class.
    """

    TYPE = _ENVIRONMENT_SUMMARY

    __hash__ = None

    def __init__(self, instance_to_wrap: 'EnvironmentSummary.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def build_date(self) -> 'str':
        """str: 'BuildDate' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BuildDate
        return temp

    @property
    def build_date_and_age(self) -> 'str':
        """str: 'BuildDateAndAge' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BuildDateAndAge
        return temp

    @property
    def core_feature_code_in_use(self) -> 'str':
        """str: 'CoreFeatureCodeInUse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoreFeatureCodeInUse
        return temp

    @property
    def core_feature_expiry(self) -> 'str':
        """str: 'CoreFeatureExpiry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoreFeatureExpiry
        return temp

    @property
    def current_net_version(self) -> 'str':
        """str: 'CurrentNETVersion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentNETVersion
        return temp

    @property
    def current_culture_system_locale(self) -> 'str':
        """str: 'CurrentCultureSystemLocale' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentCultureSystemLocale
        return temp

    @property
    def current_ui_culture_system_locale(self) -> 'str':
        """str: 'CurrentUICultureSystemLocale' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentUICultureSystemLocale
        return temp

    @property
    def date_time_iso8601(self) -> 'str':
        """str: 'DateTimeISO8601' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DateTimeISO8601
        return temp

    @property
    def date_time_local_format(self) -> 'str':
        """str: 'DateTimeLocalFormat' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DateTimeLocalFormat
        return temp

    @property
    def dispatcher_information(self) -> 'str':
        """str: 'DispatcherInformation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DispatcherInformation
        return temp

    @property
    def entry_assembly(self) -> 'str':
        """str: 'EntryAssembly' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EntryAssembly
        return temp

    @property
    def executable_directory(self) -> 'str':
        """str: 'ExecutableDirectory' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExecutableDirectory
        return temp

    @property
    def executable_directory_is_network_path(self) -> 'bool':
        """bool: 'ExecutableDirectoryIsNetworkPath' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ExecutableDirectoryIsNetworkPath
        return temp

    @property
    def installed_video_controllers(self) -> 'str':
        """str: 'InstalledVideoControllers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.InstalledVideoControllers
        return temp

    @property
    def is_64_bit_operating_system(self) -> 'bool':
        """bool: 'Is64BitOperatingSystem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Is64BitOperatingSystem
        return temp

    @property
    def licence_key(self) -> 'str':
        """str: 'LicenceKey' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LicenceKey
        return temp

    @property
    def masta_version(self) -> 'str':
        """str: 'MASTAVersion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MASTAVersion
        return temp

    @property
    def machine_name(self) -> 'str':
        """str: 'MachineName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MachineName
        return temp

    @property
    def open_gl_renderer(self) -> 'str':
        """str: 'OpenGLRenderer' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OpenGLRenderer
        return temp

    @property
    def open_gl_vendor(self) -> 'str':
        """str: 'OpenGLVendor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OpenGLVendor
        return temp

    @property
    def open_gl_version(self) -> 'str':
        """str: 'OpenGLVersion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OpenGLVersion
        return temp

    @property
    def operating_system(self) -> 'str':
        """str: 'OperatingSystem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OperatingSystem
        return temp

    @property
    def prerequisites(self) -> 'str':
        """str: 'Prerequisites' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Prerequisites
        return temp

    @property
    def process_render_mode(self) -> 'str':
        """str: 'ProcessRenderMode' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProcessRenderMode
        return temp

    @property
    def processor(self) -> 'str':
        """str: 'Processor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Processor
        return temp

    @property
    def ram(self) -> 'str':
        """str: 'RAM' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RAM
        return temp

    @property
    def remote_desktop_information(self) -> 'str':
        """str: 'RemoteDesktopInformation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RemoteDesktopInformation
        return temp

    @property
    def start_date_time_and_age(self) -> 'str':
        """str: 'StartDateTimeAndAge' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StartDateTimeAndAge
        return temp

    @property
    def user_name(self) -> 'str':
        """str: 'UserName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UserName
        return temp

    @property
    def video_controller_in_use(self) -> 'str':
        """str: 'VideoControllerInUse' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VideoControllerInUse
        return temp

    @property
    def current_culture(self) -> '_1553.NumberFormatInfoSummary':
        """NumberFormatInfoSummary: 'CurrentCulture' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CurrentCulture
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def dispatchers(self) -> 'List[_1539.DispatcherHelper]':
        """List[DispatcherHelper]: 'Dispatchers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Dispatchers
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames
        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def __copy__(self):
        """ 'Copy' is the original name of this method."""

        self.wrapped.Copy()

    def __deepcopy__(self, memo):
        """ 'Copy' is the original name of this method."""

        self.wrapped.Copy()

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result

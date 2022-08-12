"""_1268.py

Phase
"""


from typing import List

from mastapy.utility_gui.charts import (
    _1815, _1805, _1810, _1812
)
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.math_utility import _1471
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_PHASE = python_net_import('SMT.MastaAPI.ElectricMachines', 'Phase')


__docformat__ = 'restructuredtext en'
__all__ = ('Phase',)


class Phase(_0.APIBase):
    """Phase

    This is a mastapy class.
    """

    TYPE = _PHASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'Phase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mmf(self) -> '_1815.TwoDChartDefinition':
        """TwoDChartDefinition: 'MMF' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MMF
        if _1815.TwoDChartDefinition.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mmf to TwoDChartDefinition. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def phase_index(self) -> 'int':
        """int: 'PhaseIndex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseIndex
        return temp

    @property
    def mmf_fourier_series_electrical(self) -> '_1471.FourierSeries':
        """FourierSeries: 'MMFFourierSeriesElectrical' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MMFFourierSeriesElectrical
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mmf_fourier_series_mechanical(self) -> '_1471.FourierSeries':
        """FourierSeries: 'MMFFourierSeriesMechanical' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MMFFourierSeriesMechanical
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def winding_factor_harmonics_electrical(self) -> '_1471.FourierSeries':
        """FourierSeries: 'WindingFactorHarmonicsElectrical' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WindingFactorHarmonicsElectrical
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def winding_factor_harmonics_mechanical(self) -> '_1471.FourierSeries':
        """FourierSeries: 'WindingFactorHarmonicsMechanical' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WindingFactorHarmonicsMechanical
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames
        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

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

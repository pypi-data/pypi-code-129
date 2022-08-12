"""_5611.py

BearingHarmonicAnalysis
"""


from typing import List

from mastapy.system_model.part_model import _2380
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6734
from mastapy.bearings.bearing_results.rolling import _2015
from mastapy.system_model.analyses_and_results.system_deflections import _2632
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5640
from mastapy._internal.python_net import python_net_import

_BEARING_HARMONIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses', 'BearingHarmonicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingHarmonicAnalysis',)


class BearingHarmonicAnalysis(_5640.ConnectorHarmonicAnalysis):
    """BearingHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEARING_HARMONIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BearingHarmonicAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2380.Bearing':
        """Bearing: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6734.BearingLoadCase':
        """BearingLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rolling_bearing_speed_results(self) -> '_2015.RollingBearingSpeedResults':
        """RollingBearingSpeedResults: 'RollingBearingSpeedResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollingBearingSpeedResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2632.BearingSystemDeflection':
        """BearingSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[BearingHarmonicAnalysis]':
        """List[BearingHarmonicAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

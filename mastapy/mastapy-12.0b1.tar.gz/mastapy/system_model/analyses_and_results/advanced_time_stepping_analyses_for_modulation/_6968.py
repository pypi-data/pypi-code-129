"""_6968.py

CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation
"""


from mastapy.system_model.connections_and_sockets.cycloidal import _2275
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2670
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6947
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation', 'CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation',)


class CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation(_6947.CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation):
    """CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2275.CycloidalDiscCentralBearingConnection':
        """CycloidalDiscCentralBearingConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2670.CycloidalDiscCentralBearingConnectionSystemDeflection':
        """CycloidalDiscCentralBearingConnectionSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

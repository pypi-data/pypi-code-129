"""_1336.py

SpeedTorqueCurveAnalysis
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.electric_machines.load_cases_and_analyses import _1337, _1316
from mastapy.electric_machines.results import _1307
from mastapy._internal.python_net import python_net_import

_SPEED_TORQUE_CURVE_ANALYSIS = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'SpeedTorqueCurveAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SpeedTorqueCurveAnalysis',)


class SpeedTorqueCurveAnalysis(_1316.ElectricMachineAnalysis):
    """SpeedTorqueCurveAnalysis

    This is a mastapy class.
    """

    TYPE = _SPEED_TORQUE_CURVE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SpeedTorqueCurveAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def base_speed(self) -> 'float':
        """float: 'BaseSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BaseSpeed
        return temp

    @property
    def maximum_speed(self) -> 'float':
        """float: 'MaximumSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumSpeed
        return temp

    @property
    def maximum_torque_at_rated_inverter_current(self) -> 'float':
        """float: 'MaximumTorqueAtRatedInverterCurrent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumTorqueAtRatedInverterCurrent
        return temp

    @property
    def permanent_magnet_flux_linkage_at_reference_temperature(self) -> 'float':
        """float: 'PermanentMagnetFluxLinkageAtReferenceTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PermanentMagnetFluxLinkageAtReferenceTemperature
        return temp

    @property
    def load_case(self) -> '_1337.SpeedTorqueCurveLoadCase':
        """SpeedTorqueCurveLoadCase: 'LoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def results_points(self) -> 'List[_1307.MaximumTorqueResultsPoints]':
        """List[MaximumTorqueResultsPoints]: 'ResultsPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResultsPoints
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

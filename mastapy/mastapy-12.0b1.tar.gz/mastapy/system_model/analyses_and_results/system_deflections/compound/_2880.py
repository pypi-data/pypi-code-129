"""_2880.py

RootAssemblyCompoundSystemDeflection
"""


from typing import List

from mastapy.system_model.analyses_and_results.system_deflections.compound import _2837, _2792
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4191
from mastapy.system_model.analyses_and_results.system_deflections import _2734
from mastapy.system_model.fe import _2346
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1089
from mastapy.utility_gui.charts import _1815
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'RootAssemblyCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyCompoundSystemDeflection',)


class RootAssemblyCompoundSystemDeflection(_2792.AssemblyCompoundSystemDeflection):
    """RootAssemblyCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RootAssemblyCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duty_cycle_efficiency_results(self) -> '_2837.DutyCycleEfficiencyResults':
        """DutyCycleEfficiencyResults: 'DutyCycleEfficiencyResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DutyCycleEfficiencyResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def root_assembly_compound_power_flow(self) -> '_4191.RootAssemblyCompoundPowerFlow':
        """RootAssemblyCompoundPowerFlow: 'RootAssemblyCompoundPowerFlow' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RootAssemblyCompoundPowerFlow
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_2734.RootAssemblySystemDeflection]':
        """List[RootAssemblySystemDeflection]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bearing_race_f_es(self) -> 'List[_2346.RaceBearingFESystemDeflection]':
        """List[RaceBearingFESystemDeflection]: 'BearingRaceFEs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingRaceFEs
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_2734.RootAssemblySystemDeflection]':
        """List[RootAssemblySystemDeflection]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def peak_to_peak_transmission_error_chart(self, mesh_duty_cycles: 'List[_1089.CylindricalGearMeshMicroGeometryDutyCycle]', header: 'str', x_axis_title: 'str', y_axis_title: 'str') -> '_1815.TwoDChartDefinition':
        """ 'PeakToPeakTransmissionErrorChart' is the original name of this method.

        Args:
            mesh_duty_cycles (List[mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearMeshMicroGeometryDutyCycle])
            header (str)
            x_axis_title (str)
            y_axis_title (str)

        Returns:
            mastapy.utility_gui.charts.TwoDChartDefinition
        """

        mesh_duty_cycles = conversion.mp_to_pn_objects_in_list(mesh_duty_cycles)
        header = str(header)
        x_axis_title = str(x_axis_title)
        y_axis_title = str(y_axis_title)
        method_result = self.wrapped.PeakToPeakTransmissionErrorChart(mesh_duty_cycles, header if header else '', x_axis_title if x_axis_title else '', y_axis_title if y_axis_title else '')
        type_ = method_result.GetType()
        return constructor.new(type_.Namespace, type_.Name)(method_result) if method_result is not None else None

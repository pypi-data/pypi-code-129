"""_2907.py

TorqueConverterTurbineCompoundSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2549
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2765
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2824
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'TorqueConverterTurbineCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterTurbineCompoundSystemDeflection',)


class TorqueConverterTurbineCompoundSystemDeflection(_2824.CouplingHalfCompoundSystemDeflection):
    """TorqueConverterTurbineCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterTurbineCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2549.TorqueConverterTurbine':
        """TorqueConverterTurbine: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_2765.TorqueConverterTurbineSystemDeflection]':
        """List[TorqueConverterTurbineSystemDeflection]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_2765.TorqueConverterTurbineSystemDeflection]':
        """List[TorqueConverterTurbineSystemDeflection]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

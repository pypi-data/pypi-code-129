"""_2669.py

CycloidalAssemblySystemDeflection
"""


from typing import List

from mastapy.system_model.part_model.cycloidal import _2507
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6771
from mastapy.system_model.analyses_and_results.power_flows import _4007
from mastapy.system_model.analyses_and_results.system_deflections import _2729, _2740
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_ASSEMBLY_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'CycloidalAssemblySystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CycloidalAssemblySystemDeflection',)


class CycloidalAssemblySystemDeflection(_2740.SpecialisedAssemblySystemDeflection):
    """CycloidalAssemblySystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_ASSEMBLY_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CycloidalAssemblySystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2507.CycloidalAssembly':
        """CycloidalAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6771.CycloidalAssemblyLoadCase':
        """CycloidalAssemblyLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4007.CycloidalAssemblyPowerFlow':
        """CycloidalAssemblyPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ring_pins_to_disc_connections(self) -> 'List[_2729.RingPinsToDiscConnectionSystemDeflection]':
        """List[RingPinsToDiscConnectionSystemDeflection]: 'RingPinsToDiscConnections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingPinsToDiscConnections
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

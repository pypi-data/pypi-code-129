"""_2758.py

SynchroniserSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2541
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6882
from mastapy.system_model.analyses_and_results.power_flows import _4082
from mastapy.system_model.analyses_and_results.system_deflections import _2755, _2740
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'SynchroniserSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserSystemDeflection',)


class SynchroniserSystemDeflection(_2740.SpecialisedAssemblySystemDeflection):
    """SynchroniserSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SynchroniserSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2541.Synchroniser':
        """Synchroniser: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6882.SynchroniserLoadCase':
        """SynchroniserLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4082.SynchroniserPowerFlow':
        """SynchroniserPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cones(self) -> 'List[_2755.SynchroniserHalfSystemDeflection]':
        """List[SynchroniserHalfSystemDeflection]: 'Cones' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Cones
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

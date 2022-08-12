"""_3987.py

ClutchPowerFlow
"""


from mastapy.system_model.part_model.couplings import _2517
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6749
from mastapy.system_model.analyses_and_results.power_flows import _3985, _4003
from mastapy._internal.python_net import python_net_import

_CLUTCH_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'ClutchPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchPowerFlow',)


class ClutchPowerFlow(_4003.CouplingPowerFlow):
    """ClutchPowerFlow

    This is a mastapy class.
    """

    TYPE = _CLUTCH_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2517.Clutch':
        """Clutch: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6749.ClutchLoadCase':
        """ClutchLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def clutch_connection(self) -> '_3985.ClutchConnectionPowerFlow':
        """ClutchConnectionPowerFlow: 'ClutchConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ClutchConnection
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

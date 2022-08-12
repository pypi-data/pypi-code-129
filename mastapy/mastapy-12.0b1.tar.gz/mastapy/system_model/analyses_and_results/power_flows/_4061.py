"""_4061.py

RootAssemblyPowerFlow
"""


from mastapy.system_model.part_model import _2414
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4052, _3971
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'RootAssemblyPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyPowerFlow',)


class RootAssemblyPowerFlow(_3971.AssemblyPowerFlow):
    """RootAssemblyPowerFlow

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RootAssemblyPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2414.RootAssembly':
        """RootAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_inputs(self) -> '_4052.PowerFlow':
        """PowerFlow: 'PowerFlowInputs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowInputs
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

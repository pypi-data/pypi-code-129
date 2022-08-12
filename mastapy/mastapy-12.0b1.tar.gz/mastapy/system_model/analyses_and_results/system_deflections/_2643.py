"""_2643.py

BoltedJointSystemDeflection
"""


from mastapy.system_model.part_model import _2383
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6745
from mastapy.system_model.analyses_and_results.power_flows import _3983
from mastapy.system_model.analyses_and_results.system_deflections import _2740
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'BoltedJointSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('BoltedJointSystemDeflection',)


class BoltedJointSystemDeflection(_2740.SpecialisedAssemblySystemDeflection):
    """BoltedJointSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BoltedJointSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2383.BoltedJoint':
        """BoltedJoint: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6745.BoltedJointLoadCase':
        """BoltedJointLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_3983.BoltedJointPowerFlow':
        """BoltedJointPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

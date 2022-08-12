"""_2722.py

PartToPartShearCouplingSystemDeflection
"""


from mastapy.system_model.part_model.couplings import _2527
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6845
from mastapy.system_model.analyses_and_results.system_deflections import _2720, _2665
from mastapy.system_model.analyses_and_results.power_flows import _4047
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'PartToPartShearCouplingSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('PartToPartShearCouplingSystemDeflection',)


class PartToPartShearCouplingSystemDeflection(_2665.CouplingSystemDeflection):
    """PartToPartShearCouplingSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PartToPartShearCouplingSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2527.PartToPartShearCoupling':
        """PartToPartShearCoupling: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6845.PartToPartShearCouplingLoadCase':
        """PartToPartShearCouplingLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def part_to_part_shear_coupling_connection(self) -> '_2720.PartToPartShearCouplingConnectionSystemDeflection':
        """PartToPartShearCouplingConnectionSystemDeflection: 'PartToPartShearCouplingConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PartToPartShearCouplingConnection
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4047.PartToPartShearCouplingPowerFlow':
        """PartToPartShearCouplingPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

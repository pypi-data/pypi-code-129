"""_2714.py

MeasurementComponentSystemDeflection
"""


from mastapy.system_model.part_model import _2403
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6836
from mastapy.system_model.analyses_and_results.power_flows import _4041
from mastapy.system_model.analyses_and_results.system_deflections import _2769
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'MeasurementComponentSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('MeasurementComponentSystemDeflection',)


class MeasurementComponentSystemDeflection(_2769.VirtualComponentSystemDeflection):
    """MeasurementComponentSystemDeflection

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MeasurementComponentSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2403.MeasurementComponent':
        """MeasurementComponent: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6836.MeasurementComponentLoadCase':
        """MeasurementComponentLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4041.MeasurementComponentPowerFlow':
        """MeasurementComponentPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

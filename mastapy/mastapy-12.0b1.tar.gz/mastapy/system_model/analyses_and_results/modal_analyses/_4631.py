"""_4631.py

TorqueConverterTurbineModalAnalysis
"""


from mastapy.system_model.part_model.couplings import _2549
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6889
from mastapy.system_model.analyses_and_results.system_deflections import _2765
from mastapy.system_model.analyses_and_results.modal_analyses import _4541
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'TorqueConverterTurbineModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('TorqueConverterTurbineModalAnalysis',)


class TorqueConverterTurbineModalAnalysis(_4541.CouplingHalfModalAnalysis):
    """TorqueConverterTurbineModalAnalysis

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'TorqueConverterTurbineModalAnalysis.TYPE'):
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
    def component_load_case(self) -> '_6889.TorqueConverterTurbineLoadCase':
        """TorqueConverterTurbineLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2765.TorqueConverterTurbineSystemDeflection':
        """TorqueConverterTurbineSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

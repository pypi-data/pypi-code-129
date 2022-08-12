"""_6215.py

ClutchDynamicAnalysis
"""


from mastapy.system_model.part_model.couplings import _2517
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6749
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6231
from mastapy._internal.python_net import python_net_import

_CLUTCH_DYNAMIC_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses', 'ClutchDynamicAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchDynamicAnalysis',)


class ClutchDynamicAnalysis(_6231.CouplingDynamicAnalysis):
    """ClutchDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_DYNAMIC_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchDynamicAnalysis.TYPE'):
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

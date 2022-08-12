"""_2755.py

SynchroniserHalfSystemDeflection
"""


from mastapy.system_model.analyses_and_results.system_deflections import _2645, _2756
from mastapy._internal import constructor
from mastapy.system_model.part_model.couplings import _2543
from mastapy.system_model.analyses_and_results.static_loads import _6881
from mastapy.system_model.analyses_and_results.power_flows import _4080
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'SynchroniserHalfSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserHalfSystemDeflection',)


class SynchroniserHalfSystemDeflection(_2756.SynchroniserPartSystemDeflection):
    """SynchroniserHalfSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SynchroniserHalfSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def clutch_connection(self) -> '_2645.ClutchConnectionSystemDeflection':
        """ClutchConnectionSystemDeflection: 'ClutchConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ClutchConnection
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design(self) -> '_2543.SynchroniserHalf':
        """SynchroniserHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6881.SynchroniserHalfLoadCase':
        """SynchroniserHalfLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4080.SynchroniserHalfPowerFlow':
        """SynchroniserHalfPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

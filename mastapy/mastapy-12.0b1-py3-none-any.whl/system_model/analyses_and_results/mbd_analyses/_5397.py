"""_5397.py

PlanetCarrierMultibodyDynamicsAnalysis
"""


from mastapy.system_model.part_model import _2409
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6849
from mastapy.system_model.analyses_and_results.mbd_analyses import _5389
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'PlanetCarrierMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('PlanetCarrierMultibodyDynamicsAnalysis',)


class PlanetCarrierMultibodyDynamicsAnalysis(_5389.MountableComponentMultibodyDynamicsAnalysis):
    """PlanetCarrierMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PlanetCarrierMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2409.PlanetCarrier':
        """PlanetCarrier: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6849.PlanetCarrierLoadCase':
        """PlanetCarrierLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

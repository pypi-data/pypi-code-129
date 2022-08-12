"""_5431.py

SynchroniserSleeveMultibodyDynamicsAnalysis
"""


from mastapy.system_model.part_model.couplings import _2545
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6884
from mastapy.system_model.analyses_and_results.mbd_analyses import _5430
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'SynchroniserSleeveMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('SynchroniserSleeveMultibodyDynamicsAnalysis',)


class SynchroniserSleeveMultibodyDynamicsAnalysis(_5430.SynchroniserPartMultibodyDynamicsAnalysis):
    """SynchroniserSleeveMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SynchroniserSleeveMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2545.SynchroniserSleeve':
        """SynchroniserSleeve: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6884.SynchroniserSleeveLoadCase':
        """SynchroniserSleeveLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

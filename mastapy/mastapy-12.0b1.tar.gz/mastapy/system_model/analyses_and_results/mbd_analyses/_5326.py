"""_5326.py

ClutchMultibodyDynamicsAnalysis
"""


from mastapy.system_model.part_model.couplings import _2517
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6749
from mastapy.system_model.analyses_and_results.mbd_analyses import _5324, _5343
from mastapy._internal.python_net import python_net_import

_CLUTCH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'ClutchMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchMultibodyDynamicsAnalysis',)


class ClutchMultibodyDynamicsAnalysis(_5343.CouplingMultibodyDynamicsAnalysis):
    """ClutchMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchMultibodyDynamicsAnalysis.TYPE'):
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
    def clutch_connection(self) -> '_5324.ClutchConnectionMultibodyDynamicsAnalysis':
        """ClutchConnectionMultibodyDynamicsAnalysis: 'ClutchConnection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ClutchConnection
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

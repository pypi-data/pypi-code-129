"""_5476.py

ClutchHalfCompoundMultibodyDynamicsAnalysis
"""


from typing import List

from mastapy.system_model.part_model.couplings import _2518
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5325
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5492
from mastapy._internal.python_net import python_net_import

_CLUTCH_HALF_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'ClutchHalfCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchHalfCompoundMultibodyDynamicsAnalysis',)


class ClutchHalfCompoundMultibodyDynamicsAnalysis(_5492.CouplingHalfCompoundMultibodyDynamicsAnalysis):
    """ClutchHalfCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CLUTCH_HALF_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchHalfCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2518.ClutchHalf':
        """ClutchHalf: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5325.ClutchHalfMultibodyDynamicsAnalysis]':
        """List[ClutchHalfMultibodyDynamicsAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5325.ClutchHalfMultibodyDynamicsAnalysis]':
        """List[ClutchHalfMultibodyDynamicsAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

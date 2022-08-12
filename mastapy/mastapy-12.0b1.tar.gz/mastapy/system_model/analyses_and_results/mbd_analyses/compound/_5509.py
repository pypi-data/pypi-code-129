"""_5509.py

FEPartCompoundMultibodyDynamicsAnalysis
"""


from typing import List

from mastapy.system_model.part_model import _2393
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5360
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5455
from mastapy._internal.python_net import python_net_import

_FE_PART_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'FEPartCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('FEPartCompoundMultibodyDynamicsAnalysis',)


class FEPartCompoundMultibodyDynamicsAnalysis(_5455.AbstractShaftOrHousingCompoundMultibodyDynamicsAnalysis):
    """FEPartCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _FE_PART_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FEPartCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2393.FEPart':
        """FEPart: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5360.FEPartMultibodyDynamicsAnalysis]':
        """List[FEPartMultibodyDynamicsAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[FEPartCompoundMultibodyDynamicsAnalysis]':
        """List[FEPartCompoundMultibodyDynamicsAnalysis]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5360.FEPartMultibodyDynamicsAnalysis]':
        """List[FEPartMultibodyDynamicsAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

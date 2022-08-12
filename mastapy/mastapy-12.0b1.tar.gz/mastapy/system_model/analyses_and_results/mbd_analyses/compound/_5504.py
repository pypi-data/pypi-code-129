"""_5504.py

DatumCompoundMultibodyDynamicsAnalysis
"""


from typing import List

from mastapy.system_model.part_model import _2388
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses import _5355
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5478
from mastapy._internal.python_net import python_net_import

_DATUM_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound', 'DatumCompoundMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('DatumCompoundMultibodyDynamicsAnalysis',)


class DatumCompoundMultibodyDynamicsAnalysis(_5478.ComponentCompoundMultibodyDynamicsAnalysis):
    """DatumCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _DATUM_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DatumCompoundMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2388.Datum':
        """Datum: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_analysis_cases_ready(self) -> 'List[_5355.DatumMultibodyDynamicsAnalysis]':
        """List[DatumMultibodyDynamicsAnalysis]: 'ComponentAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def component_analysis_cases(self) -> 'List[_5355.DatumMultibodyDynamicsAnalysis]':
        """List[DatumMultibodyDynamicsAnalysis]: 'ComponentAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

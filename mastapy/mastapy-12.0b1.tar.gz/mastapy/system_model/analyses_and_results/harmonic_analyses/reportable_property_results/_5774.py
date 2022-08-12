"""_5774.py

FEPartHarmonicAnalysisResultsPropertyAccessor
"""


from typing import List

from mastapy.system_model.analyses_and_results.harmonic_analyses.reportable_property_results import (
    _5784, _5775, _5789, _5782
)
from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import

_FE_PART_HARMONIC_ANALYSIS_RESULTS_PROPERTY_ACCESSOR = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.ReportablePropertyResults', 'FEPartHarmonicAnalysisResultsPropertyAccessor')


__docformat__ = 'restructuredtext en'
__all__ = ('FEPartHarmonicAnalysisResultsPropertyAccessor',)


class FEPartHarmonicAnalysisResultsPropertyAccessor(_5782.HarmonicAnalysisResultsPropertyAccessor):
    """FEPartHarmonicAnalysisResultsPropertyAccessor

    This is a mastapy class.
    """

    TYPE = _FE_PART_HARMONIC_ANALYSIS_RESULTS_PROPERTY_ACCESSOR

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FEPartHarmonicAnalysisResultsPropertyAccessor.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def combined_orders(self) -> '_5784.ResultsForMultipleOrdersForFESurface':
        """ResultsForMultipleOrdersForFESurface: 'CombinedOrders' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CombinedOrders
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def excitations(self) -> 'List[_5775.FEPartSingleWhineAnalysisResultsPropertyAccessor]':
        """List[FEPartSingleWhineAnalysisResultsPropertyAccessor]: 'Excitations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Excitations
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def orders_for_combined_excitations(self) -> 'List[_5789.ResultsForOrderIncludingSurfaces]':
        """List[ResultsForOrderIncludingSurfaces]: 'OrdersForCombinedExcitations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OrdersForCombinedExcitations
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def orders_for_combined_excitations_from_same_parts(self) -> 'List[_5789.ResultsForOrderIncludingSurfaces]':
        """List[ResultsForOrderIncludingSurfaces]: 'OrdersForCombinedExcitationsFromSameParts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OrdersForCombinedExcitationsFromSameParts
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

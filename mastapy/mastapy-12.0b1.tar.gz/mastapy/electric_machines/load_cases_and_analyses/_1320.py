"""_1320.py

ElectricMachineFEAnalysis
"""


from mastapy.electric_machines.results import _1291, _1303
from mastapy._internal import constructor
from mastapy.nodal_analysis.elmer import _168
from mastapy._internal.cast_exception import CastException
from mastapy.electric_machines.load_cases_and_analyses import _1332
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_FE_ANALYSIS = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'ElectricMachineFEAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ElectricMachineFEAnalysis',)


class ElectricMachineFEAnalysis(_1332.SingleOperatingPointAnalysis):
    """ElectricMachineFEAnalysis

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_FE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ElectricMachineFEAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def dynamic_force_results(self) -> '_1291.DynamicForceResults':
        """DynamicForceResults: 'DynamicForceResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DynamicForceResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def viewable(self) -> '_168.ElmerResultsViewable':
        """ElmerResultsViewable: 'Viewable' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Viewable
        if _168.ElmerResultsViewable.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast viewable to ElmerResultsViewable. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def viewable_of_type_electric_machine_results_viewable(self) -> '_1303.ElectricMachineResultsViewable':
        """ElectricMachineResultsViewable: 'Viewable' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Viewable
        if _1303.ElectricMachineResultsViewable.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast viewable to ElectricMachineResultsViewable. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

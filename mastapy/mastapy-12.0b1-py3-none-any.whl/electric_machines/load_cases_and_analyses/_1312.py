"""_1312.py

DynamicForceAnalysis
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.electric_machines.load_cases_and_analyses import _1313, _1320, _1316
from mastapy.electric_machines.results import _1291
from mastapy._internal.python_net import python_net_import

_DYNAMIC_FORCE_ANALYSIS = python_net_import('SMT.MastaAPI.ElectricMachines.LoadCasesAndAnalyses', 'DynamicForceAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicForceAnalysis',)


class DynamicForceAnalysis(_1316.ElectricMachineAnalysis):
    """DynamicForceAnalysis

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_FORCE_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DynamicForceAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_steps_per_operating_point(self) -> 'int':
        """int: 'NumberOfStepsPerOperatingPoint' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfStepsPerOperatingPoint
        return temp

    @property
    def load_case(self) -> '_1313.DynamicForceLoadCase':
        """DynamicForceLoadCase: 'LoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def results(self) -> '_1291.DynamicForceResults':
        """DynamicForceResults: 'Results' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Results
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def single_operating_point_analyses(self) -> 'List[_1320.ElectricMachineFEAnalysis]':
        """List[ElectricMachineFEAnalysis]: 'SingleOperatingPointAnalyses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SingleOperatingPointAnalyses
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

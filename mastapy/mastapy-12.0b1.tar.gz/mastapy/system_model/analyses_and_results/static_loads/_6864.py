"""_6864.py

ShaftLoadCase
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.shaft_model import _2422
from mastapy.system_model.analyses_and_results.static_loads import _6722
from mastapy._internal.python_net import python_net_import

_SHAFT_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'ShaftLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftLoadCase',)


class ShaftLoadCase(_6722.AbstractShaftLoadCase):
    """ShaftLoadCase

    This is a mastapy class.
    """

    TYPE = _SHAFT_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShaftLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def diameter_scaling_factor(self) -> 'float':
        """float: 'DiameterScalingFactor' is the original name of this property."""

        temp = self.wrapped.DiameterScalingFactor
        return temp

    @diameter_scaling_factor.setter
    def diameter_scaling_factor(self, value: 'float'):
        self.wrapped.DiameterScalingFactor = float(value) if value else 0.0

    @property
    def component_design(self) -> '_2422.Shaft':
        """Shaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[ShaftLoadCase]':
        """List[ShaftLoadCase]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

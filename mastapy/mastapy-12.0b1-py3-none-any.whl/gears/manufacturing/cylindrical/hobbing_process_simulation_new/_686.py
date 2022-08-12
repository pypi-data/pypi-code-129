"""_686.py

WormGrindingProcessMarkOnShaft
"""


from mastapy._internal import constructor
from mastapy.utility_gui.charts import _1813
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _684
from mastapy._internal.python_net import python_net_import

_WORM_GRINDING_PROCESS_MARK_ON_SHAFT = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'WormGrindingProcessMarkOnShaft')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGrindingProcessMarkOnShaft',)


class WormGrindingProcessMarkOnShaft(_684.WormGrindingProcessCalculation):
    """WormGrindingProcessMarkOnShaft

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDING_PROCESS_MARK_ON_SHAFT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGrindingProcessMarkOnShaft.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_profile_bands(self) -> 'int':
        """int: 'NumberOfProfileBands' is the original name of this property."""

        temp = self.wrapped.NumberOfProfileBands
        return temp

    @number_of_profile_bands.setter
    def number_of_profile_bands(self, value: 'int'):
        self.wrapped.NumberOfProfileBands = int(value) if value else 0

    @property
    def number_of_transverse_plane(self) -> 'int':
        """int: 'NumberOfTransversePlane' is the original name of this property."""

        temp = self.wrapped.NumberOfTransversePlane
        return temp

    @number_of_transverse_plane.setter
    def number_of_transverse_plane(self, value: 'int'):
        self.wrapped.NumberOfTransversePlane = int(value) if value else 0

    @property
    def shaft_diameter(self) -> 'float':
        """float: 'ShaftDiameter' is the original name of this property."""

        temp = self.wrapped.ShaftDiameter
        return temp

    @shaft_diameter.setter
    def shaft_diameter(self, value: 'float'):
        self.wrapped.ShaftDiameter = float(value) if value else 0.0

    @property
    def shaft_mark_chart(self) -> '_1813.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'ShaftMarkChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftMarkChart
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

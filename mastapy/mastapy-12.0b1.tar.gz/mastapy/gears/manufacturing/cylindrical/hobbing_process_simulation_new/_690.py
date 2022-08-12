"""_690.py

WormGrindingProcessSimulationNew
"""


from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
    _682, _685, _683, _686,
    _687, _688, _692, _676,
    _689
)
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import

_WORM_GRINDING_PROCESS_SIMULATION_NEW = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'WormGrindingProcessSimulationNew')


__docformat__ = 'restructuredtext en'
__all__ = ('WormGrindingProcessSimulationNew',)


class WormGrindingProcessSimulationNew(_676.ProcessSimulationNew['_689.WormGrindingProcessSimulationInput']):
    """WormGrindingProcessSimulationNew

    This is a mastapy class.
    """

    TYPE = _WORM_GRINDING_PROCESS_SIMULATION_NEW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'WormGrindingProcessSimulationNew.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def worm_grinding_cutter_calculation(self) -> '_682.WormGrindingCutterCalculation':
        """WormGrindingCutterCalculation: 'WormGrindingCutterCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGrindingCutterCalculation
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def worm_grinding_process_gear_shape_calculation(self) -> '_685.WormGrindingProcessGearShape':
        """WormGrindingProcessGearShape: 'WormGrindingProcessGearShapeCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGrindingProcessGearShapeCalculation
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def worm_grinding_process_lead_calculation(self) -> '_683.WormGrindingLeadCalculation':
        """WormGrindingLeadCalculation: 'WormGrindingProcessLeadCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGrindingProcessLeadCalculation
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def worm_grinding_process_mark_on_shaft_calculation(self) -> '_686.WormGrindingProcessMarkOnShaft':
        """WormGrindingProcessMarkOnShaft: 'WormGrindingProcessMarkOnShaftCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGrindingProcessMarkOnShaftCalculation
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def worm_grinding_process_pitch_calculation(self) -> '_687.WormGrindingProcessPitchCalculation':
        """WormGrindingProcessPitchCalculation: 'WormGrindingProcessPitchCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGrindingProcessPitchCalculation
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def worm_grinding_process_profile_calculation(self) -> '_688.WormGrindingProcessProfileCalculation':
        """WormGrindingProcessProfileCalculation: 'WormGrindingProcessProfileCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGrindingProcessProfileCalculation
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def worm_grinding_process_total_modification_calculation(self) -> '_692.WormGrindingProcessTotalModificationCalculation':
        """WormGrindingProcessTotalModificationCalculation: 'WormGrindingProcessTotalModificationCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGrindingProcessTotalModificationCalculation
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

"""_663.py

HobbingProcessSimulationNew
"""


from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import (
    _657, _658, _659, _660,
    _661, _665, _676, _662
)
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import

_HOBBING_PROCESS_SIMULATION_NEW = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.HobbingProcessSimulationNew', 'HobbingProcessSimulationNew')


__docformat__ = 'restructuredtext en'
__all__ = ('HobbingProcessSimulationNew',)


class HobbingProcessSimulationNew(_676.ProcessSimulationNew['_662.HobbingProcessSimulationInput']):
    """HobbingProcessSimulationNew

    This is a mastapy class.
    """

    TYPE = _HOBBING_PROCESS_SIMULATION_NEW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HobbingProcessSimulationNew.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hobbing_process_gear_shape_calculation(self) -> '_657.HobbingProcessGearShape':
        """HobbingProcessGearShape: 'HobbingProcessGearShapeCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HobbingProcessGearShapeCalculation
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hobbing_process_lead_calculation(self) -> '_658.HobbingProcessLeadCalculation':
        """HobbingProcessLeadCalculation: 'HobbingProcessLeadCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HobbingProcessLeadCalculation
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hobbing_process_mark_on_shaft_calculation(self) -> '_659.HobbingProcessMarkOnShaft':
        """HobbingProcessMarkOnShaft: 'HobbingProcessMarkOnShaftCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HobbingProcessMarkOnShaftCalculation
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hobbing_process_pitch_calculation(self) -> '_660.HobbingProcessPitchCalculation':
        """HobbingProcessPitchCalculation: 'HobbingProcessPitchCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HobbingProcessPitchCalculation
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hobbing_process_profile_calculation(self) -> '_661.HobbingProcessProfileCalculation':
        """HobbingProcessProfileCalculation: 'HobbingProcessProfileCalculation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HobbingProcessProfileCalculation
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def hobbing_process_total_modification(self) -> '_665.HobbingProcessTotalModificationCalculation':
        """HobbingProcessTotalModificationCalculation: 'HobbingProcessTotalModification' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HobbingProcessTotalModification
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

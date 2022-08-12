"""_729.py

GearCutterSimulation
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.manufacturing.cylindrical.cutter_simulation import (
    _721, _728, _730, _733,
    _735, _736, _737, _738,
    _726, _734, _724, _725
)
from mastapy._internal.cast_exception import CastException
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_GEAR_CUTTER_SIMULATION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.CutterSimulation', 'GearCutterSimulation')


__docformat__ = 'restructuredtext en'
__all__ = ('GearCutterSimulation',)


class GearCutterSimulation(_0.APIBase):
    """GearCutterSimulation

    This is a mastapy class.
    """

    TYPE = _GEAR_CUTTER_SIMULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearCutterSimulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def highest_finished_form_diameter(self) -> 'float':
        """float: 'HighestFinishedFormDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HighestFinishedFormDiameter
        return temp

    @property
    def least_sap_to_form_radius_clearance(self) -> 'float':
        """float: 'LeastSAPToFormRadiusClearance' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeastSAPToFormRadiusClearance
        return temp

    @property
    def lowest_finished_tip_form_diameter(self) -> 'float':
        """float: 'LowestFinishedTipFormDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LowestFinishedTipFormDiameter
        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name
        return temp

    @property
    def average_thickness(self) -> '_721.CutterSimulationCalc':
        """CutterSimulationCalc: 'AverageThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageThickness
        if _721.CutterSimulationCalc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast average_thickness to CutterSimulationCalc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def average_thickness_of_type_form_wheel_grinding_simulation_calculator(self) -> '_728.FormWheelGrindingSimulationCalculator':
        """FormWheelGrindingSimulationCalculator: 'AverageThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageThickness
        if _728.FormWheelGrindingSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast average_thickness to FormWheelGrindingSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def average_thickness_of_type_hob_simulation_calculator(self) -> '_730.HobSimulationCalculator':
        """HobSimulationCalculator: 'AverageThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageThickness
        if _730.HobSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast average_thickness to HobSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def average_thickness_of_type_rack_simulation_calculator(self) -> '_733.RackSimulationCalculator':
        """RackSimulationCalculator: 'AverageThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageThickness
        if _733.RackSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast average_thickness to RackSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def average_thickness_of_type_shaper_simulation_calculator(self) -> '_735.ShaperSimulationCalculator':
        """ShaperSimulationCalculator: 'AverageThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageThickness
        if _735.ShaperSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast average_thickness to ShaperSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def average_thickness_of_type_shaving_simulation_calculator(self) -> '_736.ShavingSimulationCalculator':
        """ShavingSimulationCalculator: 'AverageThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageThickness
        if _736.ShavingSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast average_thickness to ShavingSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def average_thickness_of_type_virtual_simulation_calculator(self) -> '_737.VirtualSimulationCalculator':
        """VirtualSimulationCalculator: 'AverageThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageThickness
        if _737.VirtualSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast average_thickness to VirtualSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def average_thickness_of_type_worm_grinder_simulation_calculator(self) -> '_738.WormGrinderSimulationCalculator':
        """WormGrinderSimulationCalculator: 'AverageThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageThickness
        if _738.WormGrinderSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast average_thickness to WormGrinderSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def average_thickness_virtual(self) -> '_737.VirtualSimulationCalculator':
        """VirtualSimulationCalculator: 'AverageThicknessVirtual' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageThicknessVirtual
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def maximum_thickness(self) -> '_721.CutterSimulationCalc':
        """CutterSimulationCalc: 'MaximumThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumThickness
        if _721.CutterSimulationCalc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast maximum_thickness to CutterSimulationCalc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def maximum_thickness_of_type_form_wheel_grinding_simulation_calculator(self) -> '_728.FormWheelGrindingSimulationCalculator':
        """FormWheelGrindingSimulationCalculator: 'MaximumThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumThickness
        if _728.FormWheelGrindingSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast maximum_thickness to FormWheelGrindingSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def maximum_thickness_of_type_hob_simulation_calculator(self) -> '_730.HobSimulationCalculator':
        """HobSimulationCalculator: 'MaximumThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumThickness
        if _730.HobSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast maximum_thickness to HobSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def maximum_thickness_of_type_rack_simulation_calculator(self) -> '_733.RackSimulationCalculator':
        """RackSimulationCalculator: 'MaximumThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumThickness
        if _733.RackSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast maximum_thickness to RackSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def maximum_thickness_of_type_shaper_simulation_calculator(self) -> '_735.ShaperSimulationCalculator':
        """ShaperSimulationCalculator: 'MaximumThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumThickness
        if _735.ShaperSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast maximum_thickness to ShaperSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def maximum_thickness_of_type_shaving_simulation_calculator(self) -> '_736.ShavingSimulationCalculator':
        """ShavingSimulationCalculator: 'MaximumThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumThickness
        if _736.ShavingSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast maximum_thickness to ShavingSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def maximum_thickness_of_type_virtual_simulation_calculator(self) -> '_737.VirtualSimulationCalculator':
        """VirtualSimulationCalculator: 'MaximumThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumThickness
        if _737.VirtualSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast maximum_thickness to VirtualSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def maximum_thickness_of_type_worm_grinder_simulation_calculator(self) -> '_738.WormGrinderSimulationCalculator':
        """WormGrinderSimulationCalculator: 'MaximumThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumThickness
        if _738.WormGrinderSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast maximum_thickness to WormGrinderSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def maximum_thickness_virtual(self) -> '_737.VirtualSimulationCalculator':
        """VirtualSimulationCalculator: 'MaximumThicknessVirtual' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumThicknessVirtual
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def minimum_thickness(self) -> '_721.CutterSimulationCalc':
        """CutterSimulationCalc: 'MinimumThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumThickness
        if _721.CutterSimulationCalc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast minimum_thickness to CutterSimulationCalc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def minimum_thickness_of_type_form_wheel_grinding_simulation_calculator(self) -> '_728.FormWheelGrindingSimulationCalculator':
        """FormWheelGrindingSimulationCalculator: 'MinimumThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumThickness
        if _728.FormWheelGrindingSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast minimum_thickness to FormWheelGrindingSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def minimum_thickness_of_type_hob_simulation_calculator(self) -> '_730.HobSimulationCalculator':
        """HobSimulationCalculator: 'MinimumThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumThickness
        if _730.HobSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast minimum_thickness to HobSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def minimum_thickness_of_type_rack_simulation_calculator(self) -> '_733.RackSimulationCalculator':
        """RackSimulationCalculator: 'MinimumThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumThickness
        if _733.RackSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast minimum_thickness to RackSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def minimum_thickness_of_type_shaper_simulation_calculator(self) -> '_735.ShaperSimulationCalculator':
        """ShaperSimulationCalculator: 'MinimumThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumThickness
        if _735.ShaperSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast minimum_thickness to ShaperSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def minimum_thickness_of_type_shaving_simulation_calculator(self) -> '_736.ShavingSimulationCalculator':
        """ShavingSimulationCalculator: 'MinimumThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumThickness
        if _736.ShavingSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast minimum_thickness to ShavingSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def minimum_thickness_of_type_virtual_simulation_calculator(self) -> '_737.VirtualSimulationCalculator':
        """VirtualSimulationCalculator: 'MinimumThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumThickness
        if _737.VirtualSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast minimum_thickness to VirtualSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def minimum_thickness_of_type_worm_grinder_simulation_calculator(self) -> '_738.WormGrinderSimulationCalculator':
        """WormGrinderSimulationCalculator: 'MinimumThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumThickness
        if _738.WormGrinderSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast minimum_thickness to WormGrinderSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def minimum_thickness_virtual(self) -> '_737.VirtualSimulationCalculator':
        """VirtualSimulationCalculator: 'MinimumThicknessVirtual' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumThicknessVirtual
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cutter_simulation(self) -> 'GearCutterSimulation':
        """GearCutterSimulation: 'CutterSimulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CutterSimulation
        if GearCutterSimulation.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast cutter_simulation to GearCutterSimulation. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cutter_simulation_of_type_finish_cutter_simulation(self) -> '_726.FinishCutterSimulation':
        """FinishCutterSimulation: 'CutterSimulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CutterSimulation
        if _726.FinishCutterSimulation.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast cutter_simulation to FinishCutterSimulation. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cutter_simulation_of_type_rough_cutter_simulation(self) -> '_734.RoughCutterSimulation':
        """RoughCutterSimulation: 'CutterSimulation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CutterSimulation
        if _734.RoughCutterSimulation.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast cutter_simulation to RoughCutterSimulation. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def smallest_active_profile(self) -> '_721.CutterSimulationCalc':
        """CutterSimulationCalc: 'SmallestActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmallestActiveProfile
        if _721.CutterSimulationCalc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast smallest_active_profile to CutterSimulationCalc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def smallest_active_profile_of_type_form_wheel_grinding_simulation_calculator(self) -> '_728.FormWheelGrindingSimulationCalculator':
        """FormWheelGrindingSimulationCalculator: 'SmallestActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmallestActiveProfile
        if _728.FormWheelGrindingSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast smallest_active_profile to FormWheelGrindingSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def smallest_active_profile_of_type_hob_simulation_calculator(self) -> '_730.HobSimulationCalculator':
        """HobSimulationCalculator: 'SmallestActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmallestActiveProfile
        if _730.HobSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast smallest_active_profile to HobSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def smallest_active_profile_of_type_rack_simulation_calculator(self) -> '_733.RackSimulationCalculator':
        """RackSimulationCalculator: 'SmallestActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmallestActiveProfile
        if _733.RackSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast smallest_active_profile to RackSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def smallest_active_profile_of_type_shaper_simulation_calculator(self) -> '_735.ShaperSimulationCalculator':
        """ShaperSimulationCalculator: 'SmallestActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmallestActiveProfile
        if _735.ShaperSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast smallest_active_profile to ShaperSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def smallest_active_profile_of_type_shaving_simulation_calculator(self) -> '_736.ShavingSimulationCalculator':
        """ShavingSimulationCalculator: 'SmallestActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmallestActiveProfile
        if _736.ShavingSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast smallest_active_profile to ShavingSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def smallest_active_profile_of_type_virtual_simulation_calculator(self) -> '_737.VirtualSimulationCalculator':
        """VirtualSimulationCalculator: 'SmallestActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmallestActiveProfile
        if _737.VirtualSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast smallest_active_profile to VirtualSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def smallest_active_profile_of_type_worm_grinder_simulation_calculator(self) -> '_738.WormGrinderSimulationCalculator':
        """WormGrinderSimulationCalculator: 'SmallestActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SmallestActiveProfile
        if _738.WormGrinderSimulationCalculator.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast smallest_active_profile to WormGrinderSimulationCalculator. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_mesh_cutter_simulations(self) -> 'List[_724.CylindricalManufacturedRealGearInMesh]':
        """List[CylindricalManufacturedRealGearInMesh]: 'GearMeshCutterSimulations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshCutterSimulations
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def gear_mesh_cutter_simulations_virtual(self) -> 'List[_725.CylindricalManufacturedVirtualGearInMesh]':
        """List[CylindricalManufacturedVirtualGearInMesh]: 'GearMeshCutterSimulationsVirtual' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMeshCutterSimulationsVirtual
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def thickness_calculators(self) -> 'List[_721.CutterSimulationCalc]':
        """List[CutterSimulationCalc]: 'ThicknessCalculators' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ThicknessCalculators
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def virtual_thickness_calculators(self) -> 'List[_737.VirtualSimulationCalculator]':
        """List[VirtualSimulationCalculator]: 'VirtualThicknessCalculators' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.VirtualThicknessCalculators
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames
        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result

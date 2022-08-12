"""_2204.py

Databases
"""


from mastapy.materials import _237, _240, _259
from mastapy._internal import constructor
from mastapy.gears.materials import (
    _576, _578, _579, _580,
    _583, _590, _597
)
from mastapy.bolts import _1428, _1430, _1435
from mastapy.system_model.optimization import _2171, _2180
from mastapy.gears.manufacturing.cylindrical.cutters import (
    _695, _701, _706, _707
)
from mastapy.gears.manufacturing.cylindrical import _605, _616
from mastapy.electric_machines import _1261, _1278, _1288
from mastapy.gears.manufacturing.bevel import _790
from mastapy.gears.gear_set_pareto_optimiser import (
    _910, _911, _914, _915,
    _920, _921, _923, _924,
    _925, _926
)
from mastapy.bearings import _1842
from mastapy.shafts import _25
from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2503
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_DATABASES = python_net_import('SMT.MastaAPI.SystemModel.DatabaseAccess', 'Databases')


__docformat__ = 'restructuredtext en'
__all__ = ('Databases',)


class Databases(_0.APIBase):
    """Databases

    This is a mastapy class.
    """

    TYPE = _DATABASES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'Databases.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bearing_material_database(self) -> '_237.BearingMaterialDatabase':
        """BearingMaterialDatabase: 'BearingMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingMaterialDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_gear_iso_material_database(self) -> '_576.BevelGearIsoMaterialDatabase':
        """BevelGearIsoMaterialDatabase: 'BevelGearIsoMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearIsoMaterialDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_gear_material_database(self) -> '_578.BevelGearMaterialDatabase':
        """BevelGearMaterialDatabase: 'BevelGearMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelGearMaterialDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bolt_geometry_database(self) -> '_1428.BoltGeometryDatabase':
        """BoltGeometryDatabase: 'BoltGeometryDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoltGeometryDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bolt_material_database(self) -> '_1430.BoltMaterialDatabase':
        """BoltMaterialDatabase: 'BoltMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoltMaterialDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def clamped_section_material_database(self) -> '_1435.ClampedSectionMaterialDatabase':
        """ClampedSectionMaterialDatabase: 'ClampedSectionMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ClampedSectionMaterialDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_material_database(self) -> '_240.ComponentMaterialDatabase':
        """ComponentMaterialDatabase: 'ComponentMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentMaterialDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gear_optimization_strategy_database(self) -> '_2171.ConicalGearOptimizationStrategyDatabase':
        """ConicalGearOptimizationStrategyDatabase: 'ConicalGearOptimizationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearOptimizationStrategyDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_formed_wheel_grinder_database(self) -> '_695.CylindricalFormedWheelGrinderDatabase':
        """CylindricalFormedWheelGrinderDatabase: 'CylindricalFormedWheelGrinderDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalFormedWheelGrinderDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_agma_material_database(self) -> '_579.CylindricalGearAGMAMaterialDatabase':
        """CylindricalGearAGMAMaterialDatabase: 'CylindricalGearAGMAMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearAGMAMaterialDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_iso_material_database(self) -> '_580.CylindricalGearISOMaterialDatabase':
        """CylindricalGearISOMaterialDatabase: 'CylindricalGearISOMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearISOMaterialDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_plastic_material_database(self) -> '_583.CylindricalGearPlasticMaterialDatabase':
        """CylindricalGearPlasticMaterialDatabase: 'CylindricalGearPlasticMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearPlasticMaterialDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_plunge_shaver_database(self) -> '_701.CylindricalGearPlungeShaverDatabase':
        """CylindricalGearPlungeShaverDatabase: 'CylindricalGearPlungeShaverDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearPlungeShaverDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_shaver_database(self) -> '_706.CylindricalGearShaverDatabase':
        """CylindricalGearShaverDatabase: 'CylindricalGearShaverDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearShaverDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_hob_database(self) -> '_605.CylindricalHobDatabase':
        """CylindricalHobDatabase: 'CylindricalHobDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalHobDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_shaper_database(self) -> '_616.CylindricalShaperDatabase':
        """CylindricalShaperDatabase: 'CylindricalShaperDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalShaperDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_worm_grinder_database(self) -> '_707.CylindricalWormGrinderDatabase':
        """CylindricalWormGrinderDatabase: 'CylindricalWormGrinderDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalWormGrinderDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def klingelnberg_conical_gear_material_database(self) -> '_590.KlingelnbergConicalGearMaterialDatabase':
        """KlingelnbergConicalGearMaterialDatabase: 'KlingelnbergConicalGearMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergConicalGearMaterialDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def lubrication_detail_database(self) -> '_259.LubricationDetailDatabase':
        """LubricationDetailDatabase: 'LubricationDetailDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LubricationDetailDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def magnet_material_database(self) -> '_1261.MagnetMaterialDatabase':
        """MagnetMaterialDatabase: 'MagnetMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MagnetMaterialDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def manufacturing_machine_database(self) -> '_790.ManufacturingMachineDatabase':
        """ManufacturingMachineDatabase: 'ManufacturingMachineDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ManufacturingMachineDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def micro_geometry_gear_set_design_space_search_strategy_database(self) -> '_910.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase':
        """MicroGeometryGearSetDesignSpaceSearchStrategyDatabase: 'MicroGeometryGearSetDesignSpaceSearchStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def micro_geometry_gear_set_duty_cycle_design_space_search_strategy_database(self) -> '_911.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase':
        """MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase: 'MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def optimization_strategy_database(self) -> '_2180.OptimizationStrategyDatabase':
        """OptimizationStrategyDatabase: 'OptimizationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OptimizationStrategyDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_cylindrical_gear_set_duty_cycle_optimisation_strategy_database(self) -> '_914.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase':
        """ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase: 'ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_cylindrical_gear_set_optimisation_strategy_database(self) -> '_915.ParetoCylindricalGearSetOptimisationStrategyDatabase':
        """ParetoCylindricalGearSetOptimisationStrategyDatabase: 'ParetoCylindricalGearSetOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoCylindricalGearSetOptimisationStrategyDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_hypoid_gear_set_duty_cycle_optimisation_strategy_database(self) -> '_920.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase':
        """ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase: 'ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_hypoid_gear_set_optimisation_strategy_database(self) -> '_921.ParetoHypoidGearSetOptimisationStrategyDatabase':
        """ParetoHypoidGearSetOptimisationStrategyDatabase: 'ParetoHypoidGearSetOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoHypoidGearSetOptimisationStrategyDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_spiral_bevel_gear_set_duty_cycle_optimisation_strategy_database(self) -> '_923.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase':
        """ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase: 'ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_spiral_bevel_gear_set_optimisation_strategy_database(self) -> '_924.ParetoSpiralBevelGearSetOptimisationStrategyDatabase':
        """ParetoSpiralBevelGearSetOptimisationStrategyDatabase: 'ParetoSpiralBevelGearSetOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoSpiralBevelGearSetOptimisationStrategyDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_straight_bevel_gear_set_duty_cycle_optimisation_strategy_database(self) -> '_925.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase':
        """ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase: 'ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_straight_bevel_gear_set_optimisation_strategy_database(self) -> '_926.ParetoStraightBevelGearSetOptimisationStrategyDatabase':
        """ParetoStraightBevelGearSetOptimisationStrategyDatabase: 'ParetoStraightBevelGearSetOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoStraightBevelGearSetOptimisationStrategyDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def raw_material_database(self) -> '_597.RawMaterialDatabase':
        """RawMaterialDatabase: 'RawMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RawMaterialDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rolling_bearing_database(self) -> '_1842.RollingBearingDatabase':
        """RollingBearingDatabase: 'RollingBearingDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollingBearingDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shaft_material_database(self) -> '_25.ShaftMaterialDatabase':
        """ShaftMaterialDatabase: 'ShaftMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftMaterialDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stator_and_rotor_material_database(self) -> '_1278.StatorRotorMaterialDatabase':
        """StatorRotorMaterialDatabase: 'StatorAndRotorMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StatorAndRotorMaterialDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def supercharger_rotor_set_database(self) -> '_2503.SuperchargerRotorSetDatabase':
        """SuperchargerRotorSetDatabase: 'SuperchargerRotorSetDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SuperchargerRotorSetDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def winding_material_database(self) -> '_1288.WindingMaterialDatabase':
        """WindingMaterialDatabase: 'WindingMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WindingMaterialDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

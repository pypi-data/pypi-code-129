"""_2144.py

MastaSettings
"""


from mastapy.bearings.bearing_results.rolling import _1923
from mastapy._internal import constructor
from mastapy.bearings import (
    _1828, _1829, _1842, _1848
)
from mastapy.bolts import _1428, _1430, _1435
from mastapy.cycloidal import _1417, _1423
from mastapy.electric_machines import _1261, _1278, _1288
from mastapy.gears import _307, _308, _334
from mastapy.gears.gear_designs import (
    _931, _933, _936, _942
)
from mastapy.gears.gear_designs.cylindrical import (
    _1002, _1006, _1007, _1012,
    _1023
)
from mastapy.gears.gear_set_pareto_optimiser import (
    _910, _911, _914, _915,
    _917, _918, _920, _921,
    _923, _924, _925, _926
)
from mastapy.gears.ltca.cylindrical import _845
from mastapy.gears.manufacturing.bevel import _790
from mastapy.gears.manufacturing.cylindrical.cutters import (
    _695, _701, _706, _707
)
from mastapy.gears.manufacturing.cylindrical import _605, _616
from mastapy.gears.materials import (
    _576, _578, _579, _580,
    _583, _586, _589, _590,
    _597
)
from mastapy.gears.rating.cylindrical import (
    _443, _444, _459, _460
)
from mastapy.materials import (
    _237, _240, _259, _262,
    _263
)
from mastapy.nodal_analysis import _48, _49, _68
from mastapy.nodal_analysis.geometry_modeller_link import _159
from mastapy.shafts import _25, _38, _39
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6498
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5683
from mastapy.system_model.analyses_and_results.mbd_analyses import _5385
from mastapy.system_model.analyses_and_results.modal_analyses import _4584
from mastapy.system_model.analyses_and_results.power_flows import _4053, _4011
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.stability_analyses import _3803
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import _3024
from mastapy.system_model.analyses_and_results.system_deflections import _2760
from mastapy.system_model.drawing import _2191
from mastapy.system_model.optimization import _2171, _2180
from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2503
from mastapy.system_model.part_model import _2410
from mastapy.utility.cad_export import _1788
from mastapy.utility.databases import _1783
from mastapy.utility import _1556, _1557
from mastapy.utility.scripting import _1698
from mastapy.utility.units_and_measurements import _1566
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_MASTA_SETTINGS = python_net_import('SMT.MastaAPI.SystemModel', 'MastaSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('MastaSettings',)


class MastaSettings(_0.APIBase):
    """MastaSettings

    This is a mastapy class.
    """

    TYPE = _MASTA_SETTINGS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MastaSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def iso14179_settings_database(self) -> '_1923.ISO14179SettingsDatabase':
        """ISO14179SettingsDatabase: 'ISO14179SettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISO14179SettingsDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_settings(self) -> '_1828.BearingSettings':
        """BearingSettings: 'BearingSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingSettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_settings_database(self) -> '_1829.BearingSettingsDatabase':
        """BearingSettingsDatabase: 'BearingSettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingSettingsDatabase
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
    def skf_settings(self) -> '_1848.SKFSettings':
        """SKFSettings: 'SKFSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SKFSettings
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
    def cycloidal_disc_material_database(self) -> '_1417.CycloidalDiscMaterialDatabase':
        """CycloidalDiscMaterialDatabase: 'CycloidalDiscMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CycloidalDiscMaterialDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def ring_pins_material_database(self) -> '_1423.RingPinsMaterialDatabase':
        """RingPinsMaterialDatabase: 'RingPinsMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingPinsMaterialDatabase
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
    def stator_rotor_material_database(self) -> '_1278.StatorRotorMaterialDatabase':
        """StatorRotorMaterialDatabase: 'StatorRotorMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StatorRotorMaterialDatabase
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

    @property
    def bevel_hypoid_gear_design_settings(self) -> '_307.BevelHypoidGearDesignSettings':
        """BevelHypoidGearDesignSettings: 'BevelHypoidGearDesignSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelHypoidGearDesignSettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_hypoid_gear_rating_settings(self) -> '_308.BevelHypoidGearRatingSettings':
        """BevelHypoidGearRatingSettings: 'BevelHypoidGearRatingSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelHypoidGearRatingSettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_hypoid_gear_design_settings_database(self) -> '_931.BevelHypoidGearDesignSettingsDatabase':
        """BevelHypoidGearDesignSettingsDatabase: 'BevelHypoidGearDesignSettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelHypoidGearDesignSettingsDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_hypoid_gear_rating_settings_database(self) -> '_933.BevelHypoidGearRatingSettingsDatabase':
        """BevelHypoidGearRatingSettingsDatabase: 'BevelHypoidGearRatingSettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelHypoidGearRatingSettingsDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_defaults(self) -> '_1002.CylindricalGearDefaults':
        """CylindricalGearDefaults: 'CylindricalGearDefaults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearDefaults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_design_constraints_database(self) -> '_1006.CylindricalGearDesignConstraintsDatabase':
        """CylindricalGearDesignConstraintsDatabase: 'CylindricalGearDesignConstraintsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearDesignConstraintsDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_design_constraint_settings(self) -> '_1007.CylindricalGearDesignConstraintSettings':
        """CylindricalGearDesignConstraintSettings: 'CylindricalGearDesignConstraintSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearDesignConstraintSettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_micro_geometry_settings_database(self) -> '_1012.CylindricalGearMicroGeometrySettingsDatabase':
        """CylindricalGearMicroGeometrySettingsDatabase: 'CylindricalGearMicroGeometrySettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearMicroGeometrySettingsDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_set_micro_geometry_settings(self) -> '_1023.CylindricalGearSetMicroGeometrySettings':
        """CylindricalGearSetMicroGeometrySettings: 'CylindricalGearSetMicroGeometrySettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSetMicroGeometrySettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def design_constraint_collection_database(self) -> '_936.DesignConstraintCollectionDatabase':
        """DesignConstraintCollectionDatabase: 'DesignConstraintCollectionDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DesignConstraintCollectionDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_design_constraints_collection(self) -> '_942.SelectedDesignConstraintsCollection':
        """SelectedDesignConstraintsCollection: 'SelectedDesignConstraintsCollection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SelectedDesignConstraintsCollection
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
    def pareto_face_gear_set_duty_cycle_optimisation_strategy_database(self) -> '_917.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase':
        """ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase: 'ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pareto_face_gear_set_optimisation_strategy_database(self) -> '_918.ParetoFaceGearSetOptimisationStrategyDatabase':
        """ParetoFaceGearSetOptimisationStrategyDatabase: 'ParetoFaceGearSetOptimisationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParetoFaceGearSetOptimisationStrategyDatabase
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
    def cylindrical_gear_fe_settings(self) -> '_845.CylindricalGearFESettings':
        """CylindricalGearFESettings: 'CylindricalGearFESettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearFESettings
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
    def cylindrical_formed_wheel_grinder_database(self) -> '_695.CylindricalFormedWheelGrinderDatabase':
        """CylindricalFormedWheelGrinderDatabase: 'CylindricalFormedWheelGrinderDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalFormedWheelGrinderDatabase
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
    def cylindrical_worm_grinder_database(self) -> '_707.CylindricalWormGrinderDatabase':
        """CylindricalWormGrinderDatabase: 'CylindricalWormGrinderDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalWormGrinderDatabase
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
    def gear_material_expert_system_factor_settings(self) -> '_586.GearMaterialExpertSystemFactorSettings':
        """GearMaterialExpertSystemFactorSettings: 'GearMaterialExpertSystemFactorSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearMaterialExpertSystemFactorSettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def isotr1417912001_coefficient_of_friction_constants_database(self) -> '_589.ISOTR1417912001CoefficientOfFrictionConstantsDatabase':
        """ISOTR1417912001CoefficientOfFrictionConstantsDatabase: 'ISOTR1417912001CoefficientOfFrictionConstantsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISOTR1417912001CoefficientOfFrictionConstantsDatabase
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
    def raw_material_database(self) -> '_597.RawMaterialDatabase':
        """RawMaterialDatabase: 'RawMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RawMaterialDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pocketing_power_loss_coefficients_database(self) -> '_334.PocketingPowerLossCoefficientsDatabase':
        """PocketingPowerLossCoefficientsDatabase: 'PocketingPowerLossCoefficientsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PocketingPowerLossCoefficientsDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_design_and_rating_settings(self) -> '_443.CylindricalGearDesignAndRatingSettings':
        """CylindricalGearDesignAndRatingSettings: 'CylindricalGearDesignAndRatingSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearDesignAndRatingSettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_design_and_rating_settings_database(self) -> '_444.CylindricalGearDesignAndRatingSettingsDatabase':
        """CylindricalGearDesignAndRatingSettingsDatabase: 'CylindricalGearDesignAndRatingSettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearDesignAndRatingSettingsDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_plastic_gear_rating_settings(self) -> '_459.CylindricalPlasticGearRatingSettings':
        """CylindricalPlasticGearRatingSettings: 'CylindricalPlasticGearRatingSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalPlasticGearRatingSettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_plastic_gear_rating_settings_database(self) -> '_460.CylindricalPlasticGearRatingSettingsDatabase':
        """CylindricalPlasticGearRatingSettingsDatabase: 'CylindricalPlasticGearRatingSettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalPlasticGearRatingSettingsDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

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
    def component_material_database(self) -> '_240.ComponentMaterialDatabase':
        """ComponentMaterialDatabase: 'ComponentMaterialDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentMaterialDatabase
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
    def materials_settings(self) -> '_262.MaterialsSettings':
        """MaterialsSettings: 'MaterialsSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaterialsSettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def materials_settings_database(self) -> '_263.MaterialsSettingsDatabase':
        """MaterialsSettingsDatabase: 'MaterialsSettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaterialsSettingsDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def analysis_settings(self) -> '_48.AnalysisSettings':
        """AnalysisSettings: 'AnalysisSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AnalysisSettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def analysis_settings_database(self) -> '_49.AnalysisSettingsDatabase':
        """AnalysisSettingsDatabase: 'AnalysisSettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AnalysisSettingsDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def fe_user_settings(self) -> '_68.FEUserSettings':
        """FEUserSettings: 'FEUserSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FEUserSettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def geometry_modeller_settings(self) -> '_159.GeometryModellerSettings':
        """GeometryModellerSettings: 'GeometryModellerSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GeometryModellerSettings
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
    def shaft_settings(self) -> '_38.ShaftSettings':
        """ShaftSettings: 'ShaftSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftSettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shaft_settings_database(self) -> '_39.ShaftSettingsDatabase':
        """ShaftSettingsDatabase: 'ShaftSettingsDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftSettingsDatabase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def critical_speed_analysis_draw_style(self) -> '_6498.CriticalSpeedAnalysisDrawStyle':
        """CriticalSpeedAnalysisDrawStyle: 'CriticalSpeedAnalysisDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CriticalSpeedAnalysisDrawStyle
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def harmonic_analysis_draw_style(self) -> '_5683.HarmonicAnalysisDrawStyle':
        """HarmonicAnalysisDrawStyle: 'HarmonicAnalysisDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HarmonicAnalysisDrawStyle
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mbd_analysis_draw_style(self) -> '_5385.MBDAnalysisDrawStyle':
        """MBDAnalysisDrawStyle: 'MBDAnalysisDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MBDAnalysisDrawStyle
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def modal_analysis_draw_style(self) -> '_4584.ModalAnalysisDrawStyle':
        """ModalAnalysisDrawStyle: 'ModalAnalysisDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModalAnalysisDrawStyle
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_draw_style(self) -> '_4053.PowerFlowDrawStyle':
        """PowerFlowDrawStyle: 'PowerFlowDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowDrawStyle
        if _4053.PowerFlowDrawStyle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast power_flow_draw_style to PowerFlowDrawStyle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stability_analysis_draw_style(self) -> '_3803.StabilityAnalysisDrawStyle':
        """StabilityAnalysisDrawStyle: 'StabilityAnalysisDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StabilityAnalysisDrawStyle
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def steady_state_synchronous_response_draw_style(self) -> '_3024.SteadyStateSynchronousResponseDrawStyle':
        """SteadyStateSynchronousResponseDrawStyle: 'SteadyStateSynchronousResponseDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SteadyStateSynchronousResponseDrawStyle
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_draw_style(self) -> '_2760.SystemDeflectionDrawStyle':
        """SystemDeflectionDrawStyle: 'SystemDeflectionDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionDrawStyle
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def model_view_options_draw_style(self) -> '_2191.ModelViewOptionsDrawStyle':
        """ModelViewOptionsDrawStyle: 'ModelViewOptionsDrawStyle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ModelViewOptionsDrawStyle
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
    def optimization_strategy_database(self) -> '_2180.OptimizationStrategyDatabase':
        """OptimizationStrategyDatabase: 'OptimizationStrategyDatabase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OptimizationStrategyDatabase
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
    def planet_carrier_settings(self) -> '_2410.PlanetCarrierSettings':
        """PlanetCarrierSettings: 'PlanetCarrierSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetCarrierSettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cad_export_settings(self) -> '_1788.CADExportSettings':
        """CADExportSettings: 'CADExportSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CADExportSettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def database_settings(self) -> '_1783.DatabaseSettings':
        """DatabaseSettings: 'DatabaseSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DatabaseSettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def program_settings(self) -> '_1556.ProgramSettings':
        """ProgramSettings: 'ProgramSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProgramSettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pushbullet_settings(self) -> '_1557.PushbulletSettings':
        """PushbulletSettings: 'PushbulletSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PushbulletSettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def scripting_setup(self) -> '_1698.ScriptingSetup':
        """ScriptingSetup: 'ScriptingSetup' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ScriptingSetup
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def measurement_settings(self) -> '_1566.MeasurementSettings':
        """MeasurementSettings: 'MeasurementSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeasurementSettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

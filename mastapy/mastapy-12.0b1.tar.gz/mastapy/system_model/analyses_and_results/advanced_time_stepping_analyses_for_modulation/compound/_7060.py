"""_7060.py

AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
"""


from typing import List

from mastapy.system_model.part_model import _2374, _2414
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import _6929
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7061, _7063, _7066, _7073,
    _7072, _7094, _7074, _7079,
    _7084, _7096, _7098, _7102,
    _7109, _7108, _7110, _7117,
    _7124, _7127, _7128, _7129,
    _7131, _7133, _7138, _7139,
    _7140, _7142, _7144, _7149,
    _7148, _7154, _7155, _7160,
    _7163, _7166, _7170, _7174,
    _7178, _7181, _7053
)
from mastapy._internal.python_net import python_net_import

_ASSEMBLY_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound', 'AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation')


__docformat__ = 'restructuredtext en'
__all__ = ('AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation',)


class AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation(_7053.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation):
    """AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _ASSEMBLY_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2374.Assembly':
        """Assembly: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        if _2374.Assembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to Assembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2374.Assembly':
        """Assembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        if _2374.Assembly.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to Assembly. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_6929.AssemblyAdvancedTimeSteppingAnalysisForModulation]':
        """List[AssemblyAdvancedTimeSteppingAnalysisForModulation]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bearings(self) -> 'List[_7061.BearingCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[BearingCompoundAdvancedTimeSteppingAnalysisForModulation]: 'Bearings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bearings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def belt_drives(self) -> 'List[_7063.BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[BeltDriveCompoundAdvancedTimeSteppingAnalysisForModulation]: 'BeltDrives' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BeltDrives
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_gear_sets(self) -> 'List[_7066.BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[BevelDifferentialGearSetCompoundAdvancedTimeSteppingAnalysisForModulation]: 'BevelDifferentialGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialGearSets
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bolted_joints(self) -> 'List[_7073.BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[BoltedJointCompoundAdvancedTimeSteppingAnalysisForModulation]: 'BoltedJoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BoltedJoints
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bolts(self) -> 'List[_7072.BoltCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[BoltCompoundAdvancedTimeSteppingAnalysisForModulation]: 'Bolts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Bolts
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cv_ts(self) -> 'List[_7094.CVTCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[CVTCompoundAdvancedTimeSteppingAnalysisForModulation]: 'CVTs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CVTs
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def clutches(self) -> 'List[_7074.ClutchCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[ClutchCompoundAdvancedTimeSteppingAnalysisForModulation]: 'Clutches' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Clutches
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_couplings(self) -> 'List[_7079.ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[ConceptCouplingCompoundAdvancedTimeSteppingAnalysisForModulation]: 'ConceptCouplings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptCouplings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def concept_gear_sets(self) -> 'List[_7084.ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[ConceptGearSetCompoundAdvancedTimeSteppingAnalysisForModulation]: 'ConceptGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConceptGearSets
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cycloidal_assemblies(self) -> 'List[_7096.CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[CycloidalAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation]: 'CycloidalAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CycloidalAssemblies
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cycloidal_discs(self) -> 'List[_7098.CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[CycloidalDiscCompoundAdvancedTimeSteppingAnalysisForModulation]: 'CycloidalDiscs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CycloidalDiscs
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_gear_sets(self) -> 'List[_7102.CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[CylindricalGearSetCompoundAdvancedTimeSteppingAnalysisForModulation]: 'CylindricalGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSets
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def fe_parts(self) -> 'List[_7109.FEPartCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[FEPartCompoundAdvancedTimeSteppingAnalysisForModulation]: 'FEParts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FEParts
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_gear_sets(self) -> 'List[_7108.FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[FaceGearSetCompoundAdvancedTimeSteppingAnalysisForModulation]: 'FaceGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearSets
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def flexible_pin_assemblies(self) -> 'List[_7110.FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[FlexiblePinAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation]: 'FlexiblePinAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlexiblePinAssemblies
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def hypoid_gear_sets(self) -> 'List[_7117.HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[HypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation]: 'HypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HypoidGearSets
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_sets(self) -> 'List[_7124.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedTimeSteppingAnalysisForModulation]: 'KlingelnbergCycloPalloidHypoidGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearSets
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_sets(self) -> 'List[_7127.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation]: 'KlingelnbergCycloPalloidSpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearSets
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def mass_discs(self) -> 'List[_7128.MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation]: 'MassDiscs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MassDiscs
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def measurement_components(self) -> 'List[_7129.MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation]: 'MeasurementComponents' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeasurementComponents
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def oil_seals(self) -> 'List[_7131.OilSealCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[OilSealCompoundAdvancedTimeSteppingAnalysisForModulation]: 'OilSeals' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.OilSeals
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def part_to_part_shear_couplings(self) -> 'List[_7133.PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[PartToPartShearCouplingCompoundAdvancedTimeSteppingAnalysisForModulation]: 'PartToPartShearCouplings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PartToPartShearCouplings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planet_carriers(self) -> 'List[_7138.PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation]: 'PlanetCarriers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlanetCarriers
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def point_loads(self) -> 'List[_7139.PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation]: 'PointLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PointLoads
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def power_loads(self) -> 'List[_7140.PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation]: 'PowerLoads' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerLoads
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def ring_pins(self) -> 'List[_7142.RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation]: 'RingPins' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RingPins
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def rolling_ring_assemblies(self) -> 'List[_7144.RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[RollingRingAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation]: 'RollingRingAssemblies' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RollingRingAssemblies
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shaft_hub_connections(self) -> 'List[_7149.ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation]: 'ShaftHubConnections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftHubConnections
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shafts(self) -> 'List[_7148.ShaftCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[ShaftCompoundAdvancedTimeSteppingAnalysisForModulation]: 'Shafts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Shafts
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spiral_bevel_gear_sets(self) -> 'List[_7154.SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[SpiralBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation]: 'SpiralBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpiralBevelGearSets
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def spring_dampers(self) -> 'List[_7155.SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[SpringDamperCompoundAdvancedTimeSteppingAnalysisForModulation]: 'SpringDampers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpringDampers
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_diff_gear_sets(self) -> 'List[_7160.StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[StraightBevelDiffGearSetCompoundAdvancedTimeSteppingAnalysisForModulation]: 'StraightBevelDiffGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelDiffGearSets
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def straight_bevel_gear_sets(self) -> 'List[_7163.StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[StraightBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation]: 'StraightBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StraightBevelGearSets
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def synchronisers(self) -> 'List[_7166.SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[SynchroniserCompoundAdvancedTimeSteppingAnalysisForModulation]: 'Synchronisers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Synchronisers
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def torque_converters(self) -> 'List[_7170.TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[TorqueConverterCompoundAdvancedTimeSteppingAnalysisForModulation]: 'TorqueConverters' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorqueConverters
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def unbalanced_masses(self) -> 'List[_7174.UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation]: 'UnbalancedMasses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.UnbalancedMasses
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def worm_gear_sets(self) -> 'List[_7178.WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[WormGearSetCompoundAdvancedTimeSteppingAnalysisForModulation]: 'WormGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WormGearSets
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def zerol_bevel_gear_sets(self) -> 'List[_7181.ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation]':
        """List[ZerolBevelGearSetCompoundAdvancedTimeSteppingAnalysisForModulation]: 'ZerolBevelGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZerolBevelGearSets
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_6929.AssemblyAdvancedTimeSteppingAnalysisForModulation]':
        """List[AssemblyAdvancedTimeSteppingAnalysisForModulation]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

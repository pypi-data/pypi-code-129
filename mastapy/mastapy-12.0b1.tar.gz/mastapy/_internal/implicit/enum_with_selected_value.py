"""enum_with_selected_value.py

Implementations of 'EnumWithSelectedValue' in Python.
As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""


from enum import Enum
from typing import List

from mastapy._internal import (
    mixins, enum_with_selected_value_runtime, constructor, conversion
)
from mastapy.shafts import _34, _45
from mastapy._internal.python_net import python_net_import
from mastapy.nodal_analysis import (
    _71, _90, _77, _86,
    _53
)
from mastapy.nodal_analysis.varying_input_components import _97
from mastapy.math_utility import (
    _1485, _1468, _1464, _1451,
    _1450, _1454, _1463
)
from mastapy.nodal_analysis.elmer import _169, _166
from mastapy.fe_tools.enums import _1228
from mastapy.materials import _252, _256, _242
from mastapy.gears import _328, _326, _329
from mastapy.gears.rating.cylindrical import _471, _472
from mastapy.gears.micro_geometry import (
    _563, _564, _565, _566
)
from mastapy.gears.manufacturing.cylindrical import (
    _613, _614, _617, _599
)
from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _635, _636, _633
from mastapy.gears.manufacturing.cylindrical.hobbing_process_simulation_new import _648
from mastapy.geometry.two_d.curves import _304
from mastapy.gears.gear_designs.cylindrical import _1069, _1040, _1061
from mastapy.gears.gear_designs.conical import _1145, _1146, _1157
from mastapy.gears.gear_set_pareto_optimiser import _893
from mastapy.utility.model_validation import _1750, _1753
from mastapy.gears.ltca import _817
from mastapy.gears.gear_designs.creation_options import _1134
from mastapy.gears.gear_designs.bevel import _1178, _1167
from mastapy.fe_tools.vfx_tools.vfx_enums import _1225, _1226
from mastapy.electric_machines import _1237
from mastapy.electric_machines.load_cases_and_analyses import _1326
from mastapy.electric_machines.harmonic_load_data import _1345, _1342
from mastapy.bearings.tolerances import (
    _1859, _1872, _1852, _1851,
    _1853
)
from mastapy.detailed_rigid_connectors.splines import (
    _1355, _1378, _1364, _1365,
    _1373, _1379, _1356
)
from mastapy.detailed_rigid_connectors.interference_fits import _1409
from mastapy.utility import _1541
from mastapy.utility.report import _1703
from mastapy.bearings import (
    _1833, _1840, _1841, _1819,
    _1820, _1844, _1846, _1826
)
from mastapy.bearings.bearing_results import (
    _1910, _1909, _1911, _1912
)
from mastapy.bearings.bearing_designs.rolling import _2095
from mastapy.materials.efficiency import _283, _291
from mastapy.system_model.part_model import _2415
from mastapy.system_model.drawing.options import _2202
from mastapy.utility.enums import _1778, _1779, _1777
from mastapy.system_model.fe import (
    _2306, _2350, _2327, _2303,
    _2337
)
from mastapy.system_model import (
    _2148, _2162, _2157, _2160
)
from mastapy.nodal_analysis.fe_export_utility import _165, _164
from mastapy.system_model.part_model.couplings import _2530, _2533, _2534
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4279
from mastapy.system_model.analyses_and_results.static_loads import (
    _6732, _6890, _6811, _6852,
    _6891
)
from mastapy.system_model.analyses_and_results.modal_analyses import _4556
from mastapy.system_model.analyses_and_results.mbd_analyses import (
    _5311, _5363, _5408, _5433
)
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5667, _5685
from mastapy.bearings.bearing_results.rolling import _1920, _1914
from mastapy.nodal_analysis.nodal_entities import _129
from mastapy.bearings.bearing_results.rolling.iso_rating_results import _2053
from mastapy.math_utility.hertzian_contact import _1533
from mastapy.system_model.analyses_and_results.static_loads.duty_cycle_definition import _6905

_ARRAY = python_net_import('System', 'Array')
_ENUM_WITH_SELECTED_VALUE = python_net_import('SMT.MastaAPI.Utility.Property', 'EnumWithSelectedValue')


__docformat__ = 'restructuredtext en'
__all__ = (
    'EnumWithSelectedValue_ShaftRatingMethod', 'EnumWithSelectedValue_SurfaceFinishes',
    'EnumWithSelectedValue_IntegrationMethod', 'EnumWithSelectedValue_ValueInputOption',
    'EnumWithSelectedValue_SinglePointSelectionMethod', 'EnumWithSelectedValue_ResultOptionsFor3DVector',
    'EnumWithSelectedValue_ElmerResultType', 'EnumWithSelectedValue_ModeInputType',
    'EnumWithSelectedValue_MaterialPropertyClass', 'EnumWithSelectedValue_LubricantDefinition',
    'EnumWithSelectedValue_LubricantViscosityClassISO', 'EnumWithSelectedValue_MicroGeometryModel',
    'EnumWithSelectedValue_ExtrapolationOptions', 'EnumWithSelectedValue_CylindricalGearRatingMethods',
    'EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod', 'EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod',
    'EnumWithSelectedValue_LocationOfEvaluationLowerLimit', 'EnumWithSelectedValue_LocationOfEvaluationUpperLimit',
    'EnumWithSelectedValue_LocationOfRootReliefEvaluation', 'EnumWithSelectedValue_LocationOfTipReliefEvaluation',
    'EnumWithSelectedValue_CylindricalMftFinishingMethods', 'EnumWithSelectedValue_CylindricalMftRoughingMethods',
    'EnumWithSelectedValue_MicroGeometryDefinitionMethod', 'EnumWithSelectedValue_MicroGeometryDefinitionType',
    'EnumWithSelectedValue_ChartType', 'EnumWithSelectedValue_Flank',
    'EnumWithSelectedValue_ActiveProcessMethod', 'EnumWithSelectedValue_CutterFlankSections',
    'EnumWithSelectedValue_BasicCurveTypes', 'EnumWithSelectedValue_ThicknessType',
    'EnumWithSelectedValue_ConicalMachineSettingCalculationMethods', 'EnumWithSelectedValue_ConicalManufactureMethods',
    'EnumWithSelectedValue_CandidateDisplayChoice', 'EnumWithSelectedValue_Severity',
    'EnumWithSelectedValue_GeometrySpecificationType', 'EnumWithSelectedValue_StatusItemSeverity',
    'EnumWithSelectedValue_LubricationMethods', 'EnumWithSelectedValue_MicropittingCoefficientOfFrictionCalculationMethod',
    'EnumWithSelectedValue_ScuffingCoefficientOfFrictionMethods', 'EnumWithSelectedValue_ContactResultType',
    'EnumWithSelectedValue_StressResultsType', 'EnumWithSelectedValue_CylindricalGearPairCreationOptions_DerivedParameterOption',
    'EnumWithSelectedValue_ToothThicknessSpecificationMethod', 'EnumWithSelectedValue_LoadDistributionFactorMethods',
    'EnumWithSelectedValue_AGMAGleasonConicalGearGeometryMethods', 'EnumWithSelectedValue_ProSolveMpcType',
    'EnumWithSelectedValue_ProSolveSolverType', 'EnumWithSelectedValue_CoilPositionInSlot',
    'EnumWithSelectedValue_ElectricMachineAnalysisPeriod', 'EnumWithSelectedValue_LoadCaseType',
    'EnumWithSelectedValue_HarmonicLoadDataType', 'EnumWithSelectedValue_ForceDisplayOption',
    'EnumWithSelectedValue_ITDesignation', 'EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption',
    'EnumWithSelectedValue_SplineRatingTypes', 'EnumWithSelectedValue_Modules',
    'EnumWithSelectedValue_PressureAngleTypes', 'EnumWithSelectedValue_SplineFitClassType',
    'EnumWithSelectedValue_SplineToleranceClassTypes', 'EnumWithSelectedValue_Table4JointInterfaceTypes',
    'EnumWithSelectedValue_DynamicsResponseScaling', 'EnumWithSelectedValue_ExecutableDirectoryCopier_Option',
    'EnumWithSelectedValue_CadPageOrientation', 'EnumWithSelectedValue_FluidFilmTemperatureOptions',
    'EnumWithSelectedValue_SupportToleranceLocationDesignation', 'EnumWithSelectedValue_LoadedBallElementPropertyType',
    'EnumWithSelectedValue_RollerBearingProfileTypes', 'EnumWithSelectedValue_RollingBearingArrangement',
    'EnumWithSelectedValue_BasicDynamicLoadRatingCalculationMethod', 'EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod',
    'EnumWithSelectedValue_FatigueLoadLimitCalculationMethodEnum', 'EnumWithSelectedValue_RollingBearingRaceType',
    'EnumWithSelectedValue_RotationalDirections', 'EnumWithSelectedValue_BearingEfficiencyRatingMethod',
    'EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing', 'EnumWithSelectedValue_ExcitationAnalysisViewOption',
    'EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection', 'EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection',
    'EnumWithSelectedValue_ComponentOrientationOption', 'EnumWithSelectedValue_Axis',
    'EnumWithSelectedValue_AlignmentAxis', 'EnumWithSelectedValue_DesignEntityId',
    'EnumWithSelectedValue_ThermalExpansionOption', 'EnumWithSelectedValue_FESubstructureType',
    'EnumWithSelectedValue_FEExportFormat', 'EnumWithSelectedValue_ThreeDViewContourOption',
    'EnumWithSelectedValue_BoundaryConditionType', 'EnumWithSelectedValue_BearingNodeOption',
    'EnumWithSelectedValue_LinkNodeSource', 'EnumWithSelectedValue_BearingToleranceClass',
    'EnumWithSelectedValue_BearingModel', 'EnumWithSelectedValue_PreloadType',
    'EnumWithSelectedValue_RaceAxialMountingType', 'EnumWithSelectedValue_RaceRadialMountingType',
    'EnumWithSelectedValue_InternalClearanceClass', 'EnumWithSelectedValue_BearingToleranceDefinitionOptions',
    'EnumWithSelectedValue_OilSealLossCalculationMethod', 'EnumWithSelectedValue_PowerLoadType',
    'EnumWithSelectedValue_RigidConnectorStiffnessType', 'EnumWithSelectedValue_RigidConnectorToothSpacingType',
    'EnumWithSelectedValue_RigidConnectorTypes', 'EnumWithSelectedValue_FitTypes',
    'EnumWithSelectedValue_DoeValueSpecificationOption', 'EnumWithSelectedValue_AnalysisType',
    'EnumWithSelectedValue_BarModelExportType', 'EnumWithSelectedValue_ComplexPartDisplayOption',
    'EnumWithSelectedValue_DynamicsResponseType', 'EnumWithSelectedValue_BearingStiffnessModel',
    'EnumWithSelectedValue_GearMeshStiffnessModel', 'EnumWithSelectedValue_ShaftAndHousingFlexibilityOption',
    'EnumWithSelectedValue_ExportOutputType', 'EnumWithSelectedValue_HarmonicAnalysisFEExportOptions_ComplexNumberOutput',
    'EnumWithSelectedValue_FrictionModelForGyroscopicMoment', 'EnumWithSelectedValue_MeshStiffnessModel',
    'EnumWithSelectedValue_ShearAreaFactorMethod', 'EnumWithSelectedValue_StressConcentrationMethod',
    'EnumWithSelectedValue_BallBearingAnalysisMethod', 'EnumWithSelectedValue_HertzianContactDeflectionCalculationMethod',
    'EnumWithSelectedValue_TorqueRippleInputType', 'EnumWithSelectedValue_HarmonicExcitationType',
    'EnumWithSelectedValue_PointLoadLoadCase_ForceSpecification', 'EnumWithSelectedValue_TorqueSpecificationForSystemDeflection',
    'EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod', 'EnumWithSelectedValue_TorqueConverterLockupRule',
    'EnumWithSelectedValue_DegreesOfFreedom', 'EnumWithSelectedValue_DestinationDesignState'
)


class EnumWithSelectedValue_ShaftRatingMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ShaftRatingMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ShaftRatingMethod' types.
    """

    __hash__ = None
    __qualname__ = 'ShaftRatingMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_34.ShaftRatingMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _34.ShaftRatingMethod

    @classmethod
    def implicit_type(cls) -> '_34.ShaftRatingMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _34.ShaftRatingMethod.type_()

    @property
    def selected_value(self) -> '_34.ShaftRatingMethod':
        """ShaftRatingMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_34.ShaftRatingMethod]':
        """List[ShaftRatingMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_SurfaceFinishes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_SurfaceFinishes

    A specific implementation of 'EnumWithSelectedValue' for 'SurfaceFinishes' types.
    """

    __hash__ = None
    __qualname__ = 'SurfaceFinishes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_45.SurfaceFinishes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _45.SurfaceFinishes

    @classmethod
    def implicit_type(cls) -> '_45.SurfaceFinishes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _45.SurfaceFinishes.type_()

    @property
    def selected_value(self) -> '_45.SurfaceFinishes':
        """SurfaceFinishes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_45.SurfaceFinishes]':
        """List[SurfaceFinishes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_IntegrationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_IntegrationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'IntegrationMethod' types.
    """

    __hash__ = None
    __qualname__ = 'IntegrationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_71.IntegrationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _71.IntegrationMethod

    @classmethod
    def implicit_type(cls) -> '_71.IntegrationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _71.IntegrationMethod.type_()

    @property
    def selected_value(self) -> '_71.IntegrationMethod':
        """IntegrationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_71.IntegrationMethod]':
        """List[IntegrationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ValueInputOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ValueInputOption

    A specific implementation of 'EnumWithSelectedValue' for 'ValueInputOption' types.
    """

    __hash__ = None
    __qualname__ = 'ValueInputOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_90.ValueInputOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _90.ValueInputOption

    @classmethod
    def implicit_type(cls) -> '_90.ValueInputOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _90.ValueInputOption.type_()

    @property
    def selected_value(self) -> '_90.ValueInputOption':
        """ValueInputOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_90.ValueInputOption]':
        """List[ValueInputOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_SinglePointSelectionMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_SinglePointSelectionMethod

    A specific implementation of 'EnumWithSelectedValue' for 'SinglePointSelectionMethod' types.
    """

    __hash__ = None
    __qualname__ = 'SinglePointSelectionMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_97.SinglePointSelectionMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _97.SinglePointSelectionMethod

    @classmethod
    def implicit_type(cls) -> '_97.SinglePointSelectionMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _97.SinglePointSelectionMethod.type_()

    @property
    def selected_value(self) -> '_97.SinglePointSelectionMethod':
        """SinglePointSelectionMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_97.SinglePointSelectionMethod]':
        """List[SinglePointSelectionMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ResultOptionsFor3DVector(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ResultOptionsFor3DVector

    A specific implementation of 'EnumWithSelectedValue' for 'ResultOptionsFor3DVector' types.
    """

    __hash__ = None
    __qualname__ = 'ResultOptionsFor3DVector'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1485.ResultOptionsFor3DVector':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1485.ResultOptionsFor3DVector

    @classmethod
    def implicit_type(cls) -> '_1485.ResultOptionsFor3DVector.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1485.ResultOptionsFor3DVector.type_()

    @property
    def selected_value(self) -> '_1485.ResultOptionsFor3DVector':
        """ResultOptionsFor3DVector: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1485.ResultOptionsFor3DVector]':
        """List[ResultOptionsFor3DVector]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ElmerResultType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ElmerResultType

    A specific implementation of 'EnumWithSelectedValue' for 'ElmerResultType' types.
    """

    __hash__ = None
    __qualname__ = 'ElmerResultType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_169.ElmerResultType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _169.ElmerResultType

    @classmethod
    def implicit_type(cls) -> '_169.ElmerResultType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _169.ElmerResultType.type_()

    @property
    def selected_value(self) -> '_169.ElmerResultType':
        """ElmerResultType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_169.ElmerResultType]':
        """List[ElmerResultType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ModeInputType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ModeInputType

    A specific implementation of 'EnumWithSelectedValue' for 'ModeInputType' types.
    """

    __hash__ = None
    __qualname__ = 'ModeInputType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_77.ModeInputType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _77.ModeInputType

    @classmethod
    def implicit_type(cls) -> '_77.ModeInputType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _77.ModeInputType.type_()

    @property
    def selected_value(self) -> '_77.ModeInputType':
        """ModeInputType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_77.ModeInputType]':
        """List[ModeInputType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_MaterialPropertyClass(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_MaterialPropertyClass

    A specific implementation of 'EnumWithSelectedValue' for 'MaterialPropertyClass' types.
    """

    __hash__ = None
    __qualname__ = 'MaterialPropertyClass'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1228.MaterialPropertyClass':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1228.MaterialPropertyClass

    @classmethod
    def implicit_type(cls) -> '_1228.MaterialPropertyClass.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1228.MaterialPropertyClass.type_()

    @property
    def selected_value(self) -> '_1228.MaterialPropertyClass':
        """MaterialPropertyClass: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1228.MaterialPropertyClass]':
        """List[MaterialPropertyClass]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LubricantDefinition(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LubricantDefinition

    A specific implementation of 'EnumWithSelectedValue' for 'LubricantDefinition' types.
    """

    __hash__ = None
    __qualname__ = 'LubricantDefinition'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_252.LubricantDefinition':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _252.LubricantDefinition

    @classmethod
    def implicit_type(cls) -> '_252.LubricantDefinition.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _252.LubricantDefinition.type_()

    @property
    def selected_value(self) -> '_252.LubricantDefinition':
        """LubricantDefinition: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_252.LubricantDefinition]':
        """List[LubricantDefinition]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LubricantViscosityClassISO(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LubricantViscosityClassISO

    A specific implementation of 'EnumWithSelectedValue' for 'LubricantViscosityClassISO' types.
    """

    __hash__ = None
    __qualname__ = 'LubricantViscosityClassISO'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_256.LubricantViscosityClassISO':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _256.LubricantViscosityClassISO

    @classmethod
    def implicit_type(cls) -> '_256.LubricantViscosityClassISO.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _256.LubricantViscosityClassISO.type_()

    @property
    def selected_value(self) -> '_256.LubricantViscosityClassISO':
        """LubricantViscosityClassISO: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_256.LubricantViscosityClassISO]':
        """List[LubricantViscosityClassISO]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_MicroGeometryModel(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_MicroGeometryModel

    A specific implementation of 'EnumWithSelectedValue' for 'MicroGeometryModel' types.
    """

    __hash__ = None
    __qualname__ = 'MicroGeometryModel'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_328.MicroGeometryModel':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _328.MicroGeometryModel

    @classmethod
    def implicit_type(cls) -> '_328.MicroGeometryModel.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _328.MicroGeometryModel.type_()

    @property
    def selected_value(self) -> '_328.MicroGeometryModel':
        """MicroGeometryModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_328.MicroGeometryModel]':
        """List[MicroGeometryModel]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ExtrapolationOptions(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ExtrapolationOptions

    A specific implementation of 'EnumWithSelectedValue' for 'ExtrapolationOptions' types.
    """

    __hash__ = None
    __qualname__ = 'ExtrapolationOptions'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1468.ExtrapolationOptions':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1468.ExtrapolationOptions

    @classmethod
    def implicit_type(cls) -> '_1468.ExtrapolationOptions.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1468.ExtrapolationOptions.type_()

    @property
    def selected_value(self) -> '_1468.ExtrapolationOptions':
        """ExtrapolationOptions: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1468.ExtrapolationOptions]':
        """List[ExtrapolationOptions]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_CylindricalGearRatingMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_CylindricalGearRatingMethods

    A specific implementation of 'EnumWithSelectedValue' for 'CylindricalGearRatingMethods' types.
    """

    __hash__ = None
    __qualname__ = 'CylindricalGearRatingMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_242.CylindricalGearRatingMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _242.CylindricalGearRatingMethods

    @classmethod
    def implicit_type(cls) -> '_242.CylindricalGearRatingMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _242.CylindricalGearRatingMethods.type_()

    @property
    def selected_value(self) -> '_242.CylindricalGearRatingMethods':
        """CylindricalGearRatingMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_242.CylindricalGearRatingMethods]':
        """List[CylindricalGearRatingMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ScuffingFlashTemperatureRatingMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ScuffingFlashTemperatureRatingMethod' types.
    """

    __hash__ = None
    __qualname__ = 'ScuffingFlashTemperatureRatingMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_471.ScuffingFlashTemperatureRatingMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _471.ScuffingFlashTemperatureRatingMethod

    @classmethod
    def implicit_type(cls) -> '_471.ScuffingFlashTemperatureRatingMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _471.ScuffingFlashTemperatureRatingMethod.type_()

    @property
    def selected_value(self) -> '_471.ScuffingFlashTemperatureRatingMethod':
        """ScuffingFlashTemperatureRatingMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_471.ScuffingFlashTemperatureRatingMethod]':
        """List[ScuffingFlashTemperatureRatingMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ScuffingIntegralTemperatureRatingMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ScuffingIntegralTemperatureRatingMethod' types.
    """

    __hash__ = None
    __qualname__ = 'ScuffingIntegralTemperatureRatingMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_472.ScuffingIntegralTemperatureRatingMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _472.ScuffingIntegralTemperatureRatingMethod

    @classmethod
    def implicit_type(cls) -> '_472.ScuffingIntegralTemperatureRatingMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _472.ScuffingIntegralTemperatureRatingMethod.type_()

    @property
    def selected_value(self) -> '_472.ScuffingIntegralTemperatureRatingMethod':
        """ScuffingIntegralTemperatureRatingMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_472.ScuffingIntegralTemperatureRatingMethod]':
        """List[ScuffingIntegralTemperatureRatingMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LocationOfEvaluationLowerLimit(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LocationOfEvaluationLowerLimit

    A specific implementation of 'EnumWithSelectedValue' for 'LocationOfEvaluationLowerLimit' types.
    """

    __hash__ = None
    __qualname__ = 'LocationOfEvaluationLowerLimit'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_563.LocationOfEvaluationLowerLimit':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _563.LocationOfEvaluationLowerLimit

    @classmethod
    def implicit_type(cls) -> '_563.LocationOfEvaluationLowerLimit.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _563.LocationOfEvaluationLowerLimit.type_()

    @property
    def selected_value(self) -> '_563.LocationOfEvaluationLowerLimit':
        """LocationOfEvaluationLowerLimit: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_563.LocationOfEvaluationLowerLimit]':
        """List[LocationOfEvaluationLowerLimit]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LocationOfEvaluationUpperLimit(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LocationOfEvaluationUpperLimit

    A specific implementation of 'EnumWithSelectedValue' for 'LocationOfEvaluationUpperLimit' types.
    """

    __hash__ = None
    __qualname__ = 'LocationOfEvaluationUpperLimit'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_564.LocationOfEvaluationUpperLimit':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _564.LocationOfEvaluationUpperLimit

    @classmethod
    def implicit_type(cls) -> '_564.LocationOfEvaluationUpperLimit.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _564.LocationOfEvaluationUpperLimit.type_()

    @property
    def selected_value(self) -> '_564.LocationOfEvaluationUpperLimit':
        """LocationOfEvaluationUpperLimit: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_564.LocationOfEvaluationUpperLimit]':
        """List[LocationOfEvaluationUpperLimit]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LocationOfRootReliefEvaluation(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LocationOfRootReliefEvaluation

    A specific implementation of 'EnumWithSelectedValue' for 'LocationOfRootReliefEvaluation' types.
    """

    __hash__ = None
    __qualname__ = 'LocationOfRootReliefEvaluation'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_565.LocationOfRootReliefEvaluation':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _565.LocationOfRootReliefEvaluation

    @classmethod
    def implicit_type(cls) -> '_565.LocationOfRootReliefEvaluation.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _565.LocationOfRootReliefEvaluation.type_()

    @property
    def selected_value(self) -> '_565.LocationOfRootReliefEvaluation':
        """LocationOfRootReliefEvaluation: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_565.LocationOfRootReliefEvaluation]':
        """List[LocationOfRootReliefEvaluation]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LocationOfTipReliefEvaluation(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LocationOfTipReliefEvaluation

    A specific implementation of 'EnumWithSelectedValue' for 'LocationOfTipReliefEvaluation' types.
    """

    __hash__ = None
    __qualname__ = 'LocationOfTipReliefEvaluation'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_566.LocationOfTipReliefEvaluation':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _566.LocationOfTipReliefEvaluation

    @classmethod
    def implicit_type(cls) -> '_566.LocationOfTipReliefEvaluation.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _566.LocationOfTipReliefEvaluation.type_()

    @property
    def selected_value(self) -> '_566.LocationOfTipReliefEvaluation':
        """LocationOfTipReliefEvaluation: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_566.LocationOfTipReliefEvaluation]':
        """List[LocationOfTipReliefEvaluation]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_CylindricalMftFinishingMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_CylindricalMftFinishingMethods

    A specific implementation of 'EnumWithSelectedValue' for 'CylindricalMftFinishingMethods' types.
    """

    __hash__ = None
    __qualname__ = 'CylindricalMftFinishingMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_613.CylindricalMftFinishingMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _613.CylindricalMftFinishingMethods

    @classmethod
    def implicit_type(cls) -> '_613.CylindricalMftFinishingMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _613.CylindricalMftFinishingMethods.type_()

    @property
    def selected_value(self) -> '_613.CylindricalMftFinishingMethods':
        """CylindricalMftFinishingMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_613.CylindricalMftFinishingMethods]':
        """List[CylindricalMftFinishingMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_CylindricalMftRoughingMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_CylindricalMftRoughingMethods

    A specific implementation of 'EnumWithSelectedValue' for 'CylindricalMftRoughingMethods' types.
    """

    __hash__ = None
    __qualname__ = 'CylindricalMftRoughingMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_614.CylindricalMftRoughingMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _614.CylindricalMftRoughingMethods

    @classmethod
    def implicit_type(cls) -> '_614.CylindricalMftRoughingMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _614.CylindricalMftRoughingMethods.type_()

    @property
    def selected_value(self) -> '_614.CylindricalMftRoughingMethods':
        """CylindricalMftRoughingMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_614.CylindricalMftRoughingMethods]':
        """List[CylindricalMftRoughingMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_MicroGeometryDefinitionMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_MicroGeometryDefinitionMethod

    A specific implementation of 'EnumWithSelectedValue' for 'MicroGeometryDefinitionMethod' types.
    """

    __hash__ = None
    __qualname__ = 'MicroGeometryDefinitionMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_635.MicroGeometryDefinitionMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _635.MicroGeometryDefinitionMethod

    @classmethod
    def implicit_type(cls) -> '_635.MicroGeometryDefinitionMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _635.MicroGeometryDefinitionMethod.type_()

    @property
    def selected_value(self) -> '_635.MicroGeometryDefinitionMethod':
        """MicroGeometryDefinitionMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_635.MicroGeometryDefinitionMethod]':
        """List[MicroGeometryDefinitionMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_MicroGeometryDefinitionType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_MicroGeometryDefinitionType

    A specific implementation of 'EnumWithSelectedValue' for 'MicroGeometryDefinitionType' types.
    """

    __hash__ = None
    __qualname__ = 'MicroGeometryDefinitionType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_636.MicroGeometryDefinitionType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _636.MicroGeometryDefinitionType

    @classmethod
    def implicit_type(cls) -> '_636.MicroGeometryDefinitionType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _636.MicroGeometryDefinitionType.type_()

    @property
    def selected_value(self) -> '_636.MicroGeometryDefinitionType':
        """MicroGeometryDefinitionType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_636.MicroGeometryDefinitionType]':
        """List[MicroGeometryDefinitionType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ChartType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ChartType

    A specific implementation of 'EnumWithSelectedValue' for 'ChartType' types.
    """

    __hash__ = None
    __qualname__ = 'ChartType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_633.ChartType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _633.ChartType

    @classmethod
    def implicit_type(cls) -> '_633.ChartType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _633.ChartType.type_()

    @property
    def selected_value(self) -> '_633.ChartType':
        """ChartType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_633.ChartType]':
        """List[ChartType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_Flank(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_Flank

    A specific implementation of 'EnumWithSelectedValue' for 'Flank' types.
    """

    __hash__ = None
    __qualname__ = 'Flank'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_617.Flank':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _617.Flank

    @classmethod
    def implicit_type(cls) -> '_617.Flank.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _617.Flank.type_()

    @property
    def selected_value(self) -> '_617.Flank':
        """Flank: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_617.Flank]':
        """List[Flank]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ActiveProcessMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ActiveProcessMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ActiveProcessMethod' types.
    """

    __hash__ = None
    __qualname__ = 'ActiveProcessMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_648.ActiveProcessMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _648.ActiveProcessMethod

    @classmethod
    def implicit_type(cls) -> '_648.ActiveProcessMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _648.ActiveProcessMethod.type_()

    @property
    def selected_value(self) -> '_648.ActiveProcessMethod':
        """ActiveProcessMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_648.ActiveProcessMethod]':
        """List[ActiveProcessMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_CutterFlankSections(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_CutterFlankSections

    A specific implementation of 'EnumWithSelectedValue' for 'CutterFlankSections' types.
    """

    __hash__ = None
    __qualname__ = 'CutterFlankSections'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_599.CutterFlankSections':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _599.CutterFlankSections

    @classmethod
    def implicit_type(cls) -> '_599.CutterFlankSections.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _599.CutterFlankSections.type_()

    @property
    def selected_value(self) -> '_599.CutterFlankSections':
        """CutterFlankSections: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_599.CutterFlankSections]':
        """List[CutterFlankSections]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BasicCurveTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BasicCurveTypes

    A specific implementation of 'EnumWithSelectedValue' for 'BasicCurveTypes' types.
    """

    __hash__ = None
    __qualname__ = 'BasicCurveTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_304.BasicCurveTypes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _304.BasicCurveTypes

    @classmethod
    def implicit_type(cls) -> '_304.BasicCurveTypes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _304.BasicCurveTypes.type_()

    @property
    def selected_value(self) -> '_304.BasicCurveTypes':
        """BasicCurveTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_304.BasicCurveTypes]':
        """List[BasicCurveTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ThicknessType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ThicknessType

    A specific implementation of 'EnumWithSelectedValue' for 'ThicknessType' types.
    """

    __hash__ = None
    __qualname__ = 'ThicknessType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1069.ThicknessType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1069.ThicknessType

    @classmethod
    def implicit_type(cls) -> '_1069.ThicknessType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1069.ThicknessType.type_()

    @property
    def selected_value(self) -> '_1069.ThicknessType':
        """ThicknessType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1069.ThicknessType]':
        """List[ThicknessType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ConicalMachineSettingCalculationMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ConicalMachineSettingCalculationMethods

    A specific implementation of 'EnumWithSelectedValue' for 'ConicalMachineSettingCalculationMethods' types.
    """

    __hash__ = None
    __qualname__ = 'ConicalMachineSettingCalculationMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1145.ConicalMachineSettingCalculationMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1145.ConicalMachineSettingCalculationMethods

    @classmethod
    def implicit_type(cls) -> '_1145.ConicalMachineSettingCalculationMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1145.ConicalMachineSettingCalculationMethods.type_()

    @property
    def selected_value(self) -> '_1145.ConicalMachineSettingCalculationMethods':
        """ConicalMachineSettingCalculationMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1145.ConicalMachineSettingCalculationMethods]':
        """List[ConicalMachineSettingCalculationMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ConicalManufactureMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ConicalManufactureMethods

    A specific implementation of 'EnumWithSelectedValue' for 'ConicalManufactureMethods' types.
    """

    __hash__ = None
    __qualname__ = 'ConicalManufactureMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1146.ConicalManufactureMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1146.ConicalManufactureMethods

    @classmethod
    def implicit_type(cls) -> '_1146.ConicalManufactureMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1146.ConicalManufactureMethods.type_()

    @property
    def selected_value(self) -> '_1146.ConicalManufactureMethods':
        """ConicalManufactureMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1146.ConicalManufactureMethods]':
        """List[ConicalManufactureMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_CandidateDisplayChoice(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_CandidateDisplayChoice

    A specific implementation of 'EnumWithSelectedValue' for 'CandidateDisplayChoice' types.
    """

    __hash__ = None
    __qualname__ = 'CandidateDisplayChoice'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_893.CandidateDisplayChoice':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _893.CandidateDisplayChoice

    @classmethod
    def implicit_type(cls) -> '_893.CandidateDisplayChoice.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _893.CandidateDisplayChoice.type_()

    @property
    def selected_value(self) -> '_893.CandidateDisplayChoice':
        """CandidateDisplayChoice: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_893.CandidateDisplayChoice]':
        """List[CandidateDisplayChoice]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_Severity(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_Severity

    A specific implementation of 'EnumWithSelectedValue' for 'Severity' types.
    """

    __hash__ = None
    __qualname__ = 'Severity'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1750.Severity':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1750.Severity

    @classmethod
    def implicit_type(cls) -> '_1750.Severity.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1750.Severity.type_()

    @property
    def selected_value(self) -> '_1750.Severity':
        """Severity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1750.Severity]':
        """List[Severity]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_GeometrySpecificationType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_GeometrySpecificationType

    A specific implementation of 'EnumWithSelectedValue' for 'GeometrySpecificationType' types.
    """

    __hash__ = None
    __qualname__ = 'GeometrySpecificationType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1040.GeometrySpecificationType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1040.GeometrySpecificationType

    @classmethod
    def implicit_type(cls) -> '_1040.GeometrySpecificationType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1040.GeometrySpecificationType.type_()

    @property
    def selected_value(self) -> '_1040.GeometrySpecificationType':
        """GeometrySpecificationType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1040.GeometrySpecificationType]':
        """List[GeometrySpecificationType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_StatusItemSeverity(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_StatusItemSeverity

    A specific implementation of 'EnumWithSelectedValue' for 'StatusItemSeverity' types.
    """

    __hash__ = None
    __qualname__ = 'StatusItemSeverity'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1753.StatusItemSeverity':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1753.StatusItemSeverity

    @classmethod
    def implicit_type(cls) -> '_1753.StatusItemSeverity.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1753.StatusItemSeverity.type_()

    @property
    def selected_value(self) -> '_1753.StatusItemSeverity':
        """StatusItemSeverity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1753.StatusItemSeverity]':
        """List[StatusItemSeverity]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LubricationMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LubricationMethods

    A specific implementation of 'EnumWithSelectedValue' for 'LubricationMethods' types.
    """

    __hash__ = None
    __qualname__ = 'LubricationMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_326.LubricationMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _326.LubricationMethods

    @classmethod
    def implicit_type(cls) -> '_326.LubricationMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _326.LubricationMethods.type_()

    @property
    def selected_value(self) -> '_326.LubricationMethods':
        """LubricationMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_326.LubricationMethods]':
        """List[LubricationMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_MicropittingCoefficientOfFrictionCalculationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_MicropittingCoefficientOfFrictionCalculationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'MicropittingCoefficientOfFrictionCalculationMethod' types.
    """

    __hash__ = None
    __qualname__ = 'MicropittingCoefficientOfFrictionCalculationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_329.MicropittingCoefficientOfFrictionCalculationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _329.MicropittingCoefficientOfFrictionCalculationMethod

    @classmethod
    def implicit_type(cls) -> '_329.MicropittingCoefficientOfFrictionCalculationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _329.MicropittingCoefficientOfFrictionCalculationMethod.type_()

    @property
    def selected_value(self) -> '_329.MicropittingCoefficientOfFrictionCalculationMethod':
        """MicropittingCoefficientOfFrictionCalculationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_329.MicropittingCoefficientOfFrictionCalculationMethod]':
        """List[MicropittingCoefficientOfFrictionCalculationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ScuffingCoefficientOfFrictionMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ScuffingCoefficientOfFrictionMethods

    A specific implementation of 'EnumWithSelectedValue' for 'ScuffingCoefficientOfFrictionMethods' types.
    """

    __hash__ = None
    __qualname__ = 'ScuffingCoefficientOfFrictionMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1061.ScuffingCoefficientOfFrictionMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1061.ScuffingCoefficientOfFrictionMethods

    @classmethod
    def implicit_type(cls) -> '_1061.ScuffingCoefficientOfFrictionMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1061.ScuffingCoefficientOfFrictionMethods.type_()

    @property
    def selected_value(self) -> '_1061.ScuffingCoefficientOfFrictionMethods':
        """ScuffingCoefficientOfFrictionMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1061.ScuffingCoefficientOfFrictionMethods]':
        """List[ScuffingCoefficientOfFrictionMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ContactResultType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ContactResultType

    A specific implementation of 'EnumWithSelectedValue' for 'ContactResultType' types.
    """

    __hash__ = None
    __qualname__ = 'ContactResultType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_817.ContactResultType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _817.ContactResultType

    @classmethod
    def implicit_type(cls) -> '_817.ContactResultType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _817.ContactResultType.type_()

    @property
    def selected_value(self) -> '_817.ContactResultType':
        """ContactResultType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_817.ContactResultType]':
        """List[ContactResultType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_StressResultsType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_StressResultsType

    A specific implementation of 'EnumWithSelectedValue' for 'StressResultsType' types.
    """

    __hash__ = None
    __qualname__ = 'StressResultsType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_86.StressResultsType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _86.StressResultsType

    @classmethod
    def implicit_type(cls) -> '_86.StressResultsType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _86.StressResultsType.type_()

    @property
    def selected_value(self) -> '_86.StressResultsType':
        """StressResultsType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_86.StressResultsType]':
        """List[StressResultsType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_CylindricalGearPairCreationOptions_DerivedParameterOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_CylindricalGearPairCreationOptions_DerivedParameterOption

    A specific implementation of 'EnumWithSelectedValue' for 'CylindricalGearPairCreationOptions.DerivedParameterOption' types.
    """

    __hash__ = None
    __qualname__ = 'CylindricalGearPairCreationOptions.DerivedParameterOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1134.CylindricalGearPairCreationOptions.DerivedParameterOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1134.CylindricalGearPairCreationOptions.DerivedParameterOption

    @classmethod
    def implicit_type(cls) -> '_1134.CylindricalGearPairCreationOptions.DerivedParameterOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1134.CylindricalGearPairCreationOptions.DerivedParameterOption.type_()

    @property
    def selected_value(self) -> '_1134.CylindricalGearPairCreationOptions.DerivedParameterOption':
        """CylindricalGearPairCreationOptions.DerivedParameterOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1134.CylindricalGearPairCreationOptions.DerivedParameterOption]':
        """List[CylindricalGearPairCreationOptions.DerivedParameterOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ToothThicknessSpecificationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ToothThicknessSpecificationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ToothThicknessSpecificationMethod' types.
    """

    __hash__ = None
    __qualname__ = 'ToothThicknessSpecificationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1178.ToothThicknessSpecificationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1178.ToothThicknessSpecificationMethod

    @classmethod
    def implicit_type(cls) -> '_1178.ToothThicknessSpecificationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1178.ToothThicknessSpecificationMethod.type_()

    @property
    def selected_value(self) -> '_1178.ToothThicknessSpecificationMethod':
        """ToothThicknessSpecificationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1178.ToothThicknessSpecificationMethod]':
        """List[ToothThicknessSpecificationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LoadDistributionFactorMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LoadDistributionFactorMethods

    A specific implementation of 'EnumWithSelectedValue' for 'LoadDistributionFactorMethods' types.
    """

    __hash__ = None
    __qualname__ = 'LoadDistributionFactorMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1157.LoadDistributionFactorMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1157.LoadDistributionFactorMethods

    @classmethod
    def implicit_type(cls) -> '_1157.LoadDistributionFactorMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1157.LoadDistributionFactorMethods.type_()

    @property
    def selected_value(self) -> '_1157.LoadDistributionFactorMethods':
        """LoadDistributionFactorMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1157.LoadDistributionFactorMethods]':
        """List[LoadDistributionFactorMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_AGMAGleasonConicalGearGeometryMethods(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_AGMAGleasonConicalGearGeometryMethods

    A specific implementation of 'EnumWithSelectedValue' for 'AGMAGleasonConicalGearGeometryMethods' types.
    """

    __hash__ = None
    __qualname__ = 'AGMAGleasonConicalGearGeometryMethods'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1167.AGMAGleasonConicalGearGeometryMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1167.AGMAGleasonConicalGearGeometryMethods

    @classmethod
    def implicit_type(cls) -> '_1167.AGMAGleasonConicalGearGeometryMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1167.AGMAGleasonConicalGearGeometryMethods.type_()

    @property
    def selected_value(self) -> '_1167.AGMAGleasonConicalGearGeometryMethods':
        """AGMAGleasonConicalGearGeometryMethods: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1167.AGMAGleasonConicalGearGeometryMethods]':
        """List[AGMAGleasonConicalGearGeometryMethods]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ProSolveMpcType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ProSolveMpcType

    A specific implementation of 'EnumWithSelectedValue' for 'ProSolveMpcType' types.
    """

    __hash__ = None
    __qualname__ = 'ProSolveMpcType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1225.ProSolveMpcType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1225.ProSolveMpcType

    @classmethod
    def implicit_type(cls) -> '_1225.ProSolveMpcType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1225.ProSolveMpcType.type_()

    @property
    def selected_value(self) -> '_1225.ProSolveMpcType':
        """ProSolveMpcType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1225.ProSolveMpcType]':
        """List[ProSolveMpcType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ProSolveSolverType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ProSolveSolverType

    A specific implementation of 'EnumWithSelectedValue' for 'ProSolveSolverType' types.
    """

    __hash__ = None
    __qualname__ = 'ProSolveSolverType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1226.ProSolveSolverType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1226.ProSolveSolverType

    @classmethod
    def implicit_type(cls) -> '_1226.ProSolveSolverType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1226.ProSolveSolverType.type_()

    @property
    def selected_value(self) -> '_1226.ProSolveSolverType':
        """ProSolveSolverType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1226.ProSolveSolverType]':
        """List[ProSolveSolverType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_CoilPositionInSlot(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_CoilPositionInSlot

    A specific implementation of 'EnumWithSelectedValue' for 'CoilPositionInSlot' types.
    """

    __hash__ = None
    __qualname__ = 'CoilPositionInSlot'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1237.CoilPositionInSlot':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1237.CoilPositionInSlot

    @classmethod
    def implicit_type(cls) -> '_1237.CoilPositionInSlot.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1237.CoilPositionInSlot.type_()

    @property
    def selected_value(self) -> '_1237.CoilPositionInSlot':
        """CoilPositionInSlot: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1237.CoilPositionInSlot]':
        """List[CoilPositionInSlot]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ElectricMachineAnalysisPeriod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ElectricMachineAnalysisPeriod

    A specific implementation of 'EnumWithSelectedValue' for 'ElectricMachineAnalysisPeriod' types.
    """

    __hash__ = None
    __qualname__ = 'ElectricMachineAnalysisPeriod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_166.ElectricMachineAnalysisPeriod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _166.ElectricMachineAnalysisPeriod

    @classmethod
    def implicit_type(cls) -> '_166.ElectricMachineAnalysisPeriod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _166.ElectricMachineAnalysisPeriod.type_()

    @property
    def selected_value(self) -> '_166.ElectricMachineAnalysisPeriod':
        """ElectricMachineAnalysisPeriod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_166.ElectricMachineAnalysisPeriod]':
        """List[ElectricMachineAnalysisPeriod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LoadCaseType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LoadCaseType

    A specific implementation of 'EnumWithSelectedValue' for 'LoadCaseType' types.
    """

    __hash__ = None
    __qualname__ = 'LoadCaseType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1326.LoadCaseType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1326.LoadCaseType

    @classmethod
    def implicit_type(cls) -> '_1326.LoadCaseType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1326.LoadCaseType.type_()

    @property
    def selected_value(self) -> '_1326.LoadCaseType':
        """LoadCaseType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1326.LoadCaseType]':
        """List[LoadCaseType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_HarmonicLoadDataType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_HarmonicLoadDataType

    A specific implementation of 'EnumWithSelectedValue' for 'HarmonicLoadDataType' types.
    """

    __hash__ = None
    __qualname__ = 'HarmonicLoadDataType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1345.HarmonicLoadDataType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1345.HarmonicLoadDataType

    @classmethod
    def implicit_type(cls) -> '_1345.HarmonicLoadDataType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1345.HarmonicLoadDataType.type_()

    @property
    def selected_value(self) -> '_1345.HarmonicLoadDataType':
        """HarmonicLoadDataType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1345.HarmonicLoadDataType]':
        """List[HarmonicLoadDataType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ForceDisplayOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ForceDisplayOption

    A specific implementation of 'EnumWithSelectedValue' for 'ForceDisplayOption' types.
    """

    __hash__ = None
    __qualname__ = 'ForceDisplayOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1342.ForceDisplayOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1342.ForceDisplayOption

    @classmethod
    def implicit_type(cls) -> '_1342.ForceDisplayOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1342.ForceDisplayOption.type_()

    @property
    def selected_value(self) -> '_1342.ForceDisplayOption':
        """ForceDisplayOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1342.ForceDisplayOption]':
        """List[ForceDisplayOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ITDesignation(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ITDesignation

    A specific implementation of 'EnumWithSelectedValue' for 'ITDesignation' types.
    """

    __hash__ = None
    __qualname__ = 'ITDesignation'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1859.ITDesignation':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1859.ITDesignation

    @classmethod
    def implicit_type(cls) -> '_1859.ITDesignation.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1859.ITDesignation.type_()

    @property
    def selected_value(self) -> '_1859.ITDesignation':
        """ITDesignation: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1859.ITDesignation]':
        """List[ITDesignation]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_DudleyEffectiveLengthApproximationOption

    A specific implementation of 'EnumWithSelectedValue' for 'DudleyEffectiveLengthApproximationOption' types.
    """

    __hash__ = None
    __qualname__ = 'DudleyEffectiveLengthApproximationOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1355.DudleyEffectiveLengthApproximationOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1355.DudleyEffectiveLengthApproximationOption

    @classmethod
    def implicit_type(cls) -> '_1355.DudleyEffectiveLengthApproximationOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1355.DudleyEffectiveLengthApproximationOption.type_()

    @property
    def selected_value(self) -> '_1355.DudleyEffectiveLengthApproximationOption':
        """DudleyEffectiveLengthApproximationOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1355.DudleyEffectiveLengthApproximationOption]':
        """List[DudleyEffectiveLengthApproximationOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_SplineRatingTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_SplineRatingTypes

    A specific implementation of 'EnumWithSelectedValue' for 'SplineRatingTypes' types.
    """

    __hash__ = None
    __qualname__ = 'SplineRatingTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1378.SplineRatingTypes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1378.SplineRatingTypes

    @classmethod
    def implicit_type(cls) -> '_1378.SplineRatingTypes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1378.SplineRatingTypes.type_()

    @property
    def selected_value(self) -> '_1378.SplineRatingTypes':
        """SplineRatingTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1378.SplineRatingTypes]':
        """List[SplineRatingTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_Modules(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_Modules

    A specific implementation of 'EnumWithSelectedValue' for 'Modules' types.
    """

    __hash__ = None
    __qualname__ = 'Modules'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1364.Modules':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1364.Modules

    @classmethod
    def implicit_type(cls) -> '_1364.Modules.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1364.Modules.type_()

    @property
    def selected_value(self) -> '_1364.Modules':
        """Modules: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1364.Modules]':
        """List[Modules]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_PressureAngleTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_PressureAngleTypes

    A specific implementation of 'EnumWithSelectedValue' for 'PressureAngleTypes' types.
    """

    __hash__ = None
    __qualname__ = 'PressureAngleTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1365.PressureAngleTypes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1365.PressureAngleTypes

    @classmethod
    def implicit_type(cls) -> '_1365.PressureAngleTypes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1365.PressureAngleTypes.type_()

    @property
    def selected_value(self) -> '_1365.PressureAngleTypes':
        """PressureAngleTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1365.PressureAngleTypes]':
        """List[PressureAngleTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_SplineFitClassType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_SplineFitClassType

    A specific implementation of 'EnumWithSelectedValue' for 'SplineFitClassType' types.
    """

    __hash__ = None
    __qualname__ = 'SplineFitClassType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1373.SplineFitClassType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1373.SplineFitClassType

    @classmethod
    def implicit_type(cls) -> '_1373.SplineFitClassType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1373.SplineFitClassType.type_()

    @property
    def selected_value(self) -> '_1373.SplineFitClassType':
        """SplineFitClassType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1373.SplineFitClassType]':
        """List[SplineFitClassType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_SplineToleranceClassTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_SplineToleranceClassTypes

    A specific implementation of 'EnumWithSelectedValue' for 'SplineToleranceClassTypes' types.
    """

    __hash__ = None
    __qualname__ = 'SplineToleranceClassTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1379.SplineToleranceClassTypes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1379.SplineToleranceClassTypes

    @classmethod
    def implicit_type(cls) -> '_1379.SplineToleranceClassTypes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1379.SplineToleranceClassTypes.type_()

    @property
    def selected_value(self) -> '_1379.SplineToleranceClassTypes':
        """SplineToleranceClassTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1379.SplineToleranceClassTypes]':
        """List[SplineToleranceClassTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_Table4JointInterfaceTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_Table4JointInterfaceTypes

    A specific implementation of 'EnumWithSelectedValue' for 'Table4JointInterfaceTypes' types.
    """

    __hash__ = None
    __qualname__ = 'Table4JointInterfaceTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1409.Table4JointInterfaceTypes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1409.Table4JointInterfaceTypes

    @classmethod
    def implicit_type(cls) -> '_1409.Table4JointInterfaceTypes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1409.Table4JointInterfaceTypes.type_()

    @property
    def selected_value(self) -> '_1409.Table4JointInterfaceTypes':
        """Table4JointInterfaceTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1409.Table4JointInterfaceTypes]':
        """List[Table4JointInterfaceTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_DynamicsResponseScaling(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_DynamicsResponseScaling

    A specific implementation of 'EnumWithSelectedValue' for 'DynamicsResponseScaling' types.
    """

    __hash__ = None
    __qualname__ = 'DynamicsResponseScaling'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1464.DynamicsResponseScaling':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1464.DynamicsResponseScaling

    @classmethod
    def implicit_type(cls) -> '_1464.DynamicsResponseScaling.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1464.DynamicsResponseScaling.type_()

    @property
    def selected_value(self) -> '_1464.DynamicsResponseScaling':
        """DynamicsResponseScaling: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1464.DynamicsResponseScaling]':
        """List[DynamicsResponseScaling]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ExecutableDirectoryCopier_Option(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ExecutableDirectoryCopier_Option

    A specific implementation of 'EnumWithSelectedValue' for 'ExecutableDirectoryCopier.Option' types.
    """

    __hash__ = None
    __qualname__ = 'ExecutableDirectoryCopier.Option'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1541.ExecutableDirectoryCopier.Option':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1541.ExecutableDirectoryCopier.Option

    @classmethod
    def implicit_type(cls) -> '_1541.ExecutableDirectoryCopier.Option.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1541.ExecutableDirectoryCopier.Option.type_()

    @property
    def selected_value(self) -> '_1541.ExecutableDirectoryCopier.Option':
        """ExecutableDirectoryCopier.Option: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1541.ExecutableDirectoryCopier.Option]':
        """List[ExecutableDirectoryCopier.Option]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_CadPageOrientation(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_CadPageOrientation

    A specific implementation of 'EnumWithSelectedValue' for 'CadPageOrientation' types.
    """

    __hash__ = None
    __qualname__ = 'CadPageOrientation'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1703.CadPageOrientation':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1703.CadPageOrientation

    @classmethod
    def implicit_type(cls) -> '_1703.CadPageOrientation.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1703.CadPageOrientation.type_()

    @property
    def selected_value(self) -> '_1703.CadPageOrientation':
        """CadPageOrientation: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1703.CadPageOrientation]':
        """List[CadPageOrientation]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_FluidFilmTemperatureOptions(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_FluidFilmTemperatureOptions

    A specific implementation of 'EnumWithSelectedValue' for 'FluidFilmTemperatureOptions' types.
    """

    __hash__ = None
    __qualname__ = 'FluidFilmTemperatureOptions'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1833.FluidFilmTemperatureOptions':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1833.FluidFilmTemperatureOptions

    @classmethod
    def implicit_type(cls) -> '_1833.FluidFilmTemperatureOptions.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1833.FluidFilmTemperatureOptions.type_()

    @property
    def selected_value(self) -> '_1833.FluidFilmTemperatureOptions':
        """FluidFilmTemperatureOptions: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1833.FluidFilmTemperatureOptions]':
        """List[FluidFilmTemperatureOptions]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_SupportToleranceLocationDesignation(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_SupportToleranceLocationDesignation

    A specific implementation of 'EnumWithSelectedValue' for 'SupportToleranceLocationDesignation' types.
    """

    __hash__ = None
    __qualname__ = 'SupportToleranceLocationDesignation'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1872.SupportToleranceLocationDesignation':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1872.SupportToleranceLocationDesignation

    @classmethod
    def implicit_type(cls) -> '_1872.SupportToleranceLocationDesignation.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1872.SupportToleranceLocationDesignation.type_()

    @property
    def selected_value(self) -> '_1872.SupportToleranceLocationDesignation':
        """SupportToleranceLocationDesignation: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1872.SupportToleranceLocationDesignation]':
        """List[SupportToleranceLocationDesignation]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LoadedBallElementPropertyType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LoadedBallElementPropertyType

    A specific implementation of 'EnumWithSelectedValue' for 'LoadedBallElementPropertyType' types.
    """

    __hash__ = None
    __qualname__ = 'LoadedBallElementPropertyType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1910.LoadedBallElementPropertyType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1910.LoadedBallElementPropertyType

    @classmethod
    def implicit_type(cls) -> '_1910.LoadedBallElementPropertyType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1910.LoadedBallElementPropertyType.type_()

    @property
    def selected_value(self) -> '_1910.LoadedBallElementPropertyType':
        """LoadedBallElementPropertyType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1910.LoadedBallElementPropertyType]':
        """List[LoadedBallElementPropertyType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RollerBearingProfileTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RollerBearingProfileTypes

    A specific implementation of 'EnumWithSelectedValue' for 'RollerBearingProfileTypes' types.
    """

    __hash__ = None
    __qualname__ = 'RollerBearingProfileTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1840.RollerBearingProfileTypes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1840.RollerBearingProfileTypes

    @classmethod
    def implicit_type(cls) -> '_1840.RollerBearingProfileTypes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1840.RollerBearingProfileTypes.type_()

    @property
    def selected_value(self) -> '_1840.RollerBearingProfileTypes':
        """RollerBearingProfileTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1840.RollerBearingProfileTypes]':
        """List[RollerBearingProfileTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RollingBearingArrangement(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RollingBearingArrangement

    A specific implementation of 'EnumWithSelectedValue' for 'RollingBearingArrangement' types.
    """

    __hash__ = None
    __qualname__ = 'RollingBearingArrangement'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1841.RollingBearingArrangement':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1841.RollingBearingArrangement

    @classmethod
    def implicit_type(cls) -> '_1841.RollingBearingArrangement.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1841.RollingBearingArrangement.type_()

    @property
    def selected_value(self) -> '_1841.RollingBearingArrangement':
        """RollingBearingArrangement: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1841.RollingBearingArrangement]':
        """List[RollingBearingArrangement]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BasicDynamicLoadRatingCalculationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BasicDynamicLoadRatingCalculationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'BasicDynamicLoadRatingCalculationMethod' types.
    """

    __hash__ = None
    __qualname__ = 'BasicDynamicLoadRatingCalculationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1819.BasicDynamicLoadRatingCalculationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1819.BasicDynamicLoadRatingCalculationMethod

    @classmethod
    def implicit_type(cls) -> '_1819.BasicDynamicLoadRatingCalculationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1819.BasicDynamicLoadRatingCalculationMethod.type_()

    @property
    def selected_value(self) -> '_1819.BasicDynamicLoadRatingCalculationMethod':
        """BasicDynamicLoadRatingCalculationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1819.BasicDynamicLoadRatingCalculationMethod]':
        """List[BasicDynamicLoadRatingCalculationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BasicStaticLoadRatingCalculationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'BasicStaticLoadRatingCalculationMethod' types.
    """

    __hash__ = None
    __qualname__ = 'BasicStaticLoadRatingCalculationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1820.BasicStaticLoadRatingCalculationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1820.BasicStaticLoadRatingCalculationMethod

    @classmethod
    def implicit_type(cls) -> '_1820.BasicStaticLoadRatingCalculationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1820.BasicStaticLoadRatingCalculationMethod.type_()

    @property
    def selected_value(self) -> '_1820.BasicStaticLoadRatingCalculationMethod':
        """BasicStaticLoadRatingCalculationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1820.BasicStaticLoadRatingCalculationMethod]':
        """List[BasicStaticLoadRatingCalculationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_FatigueLoadLimitCalculationMethodEnum(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_FatigueLoadLimitCalculationMethodEnum

    A specific implementation of 'EnumWithSelectedValue' for 'FatigueLoadLimitCalculationMethodEnum' types.
    """

    __hash__ = None
    __qualname__ = 'FatigueLoadLimitCalculationMethodEnum'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2095.FatigueLoadLimitCalculationMethodEnum':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2095.FatigueLoadLimitCalculationMethodEnum

    @classmethod
    def implicit_type(cls) -> '_2095.FatigueLoadLimitCalculationMethodEnum.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2095.FatigueLoadLimitCalculationMethodEnum.type_()

    @property
    def selected_value(self) -> '_2095.FatigueLoadLimitCalculationMethodEnum':
        """FatigueLoadLimitCalculationMethodEnum: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2095.FatigueLoadLimitCalculationMethodEnum]':
        """List[FatigueLoadLimitCalculationMethodEnum]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RollingBearingRaceType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RollingBearingRaceType

    A specific implementation of 'EnumWithSelectedValue' for 'RollingBearingRaceType' types.
    """

    __hash__ = None
    __qualname__ = 'RollingBearingRaceType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1844.RollingBearingRaceType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1844.RollingBearingRaceType

    @classmethod
    def implicit_type(cls) -> '_1844.RollingBearingRaceType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1844.RollingBearingRaceType.type_()

    @property
    def selected_value(self) -> '_1844.RollingBearingRaceType':
        """RollingBearingRaceType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1844.RollingBearingRaceType]':
        """List[RollingBearingRaceType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RotationalDirections(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RotationalDirections

    A specific implementation of 'EnumWithSelectedValue' for 'RotationalDirections' types.
    """

    __hash__ = None
    __qualname__ = 'RotationalDirections'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1846.RotationalDirections':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1846.RotationalDirections

    @classmethod
    def implicit_type(cls) -> '_1846.RotationalDirections.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1846.RotationalDirections.type_()

    @property
    def selected_value(self) -> '_1846.RotationalDirections':
        """RotationalDirections: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1846.RotationalDirections]':
        """List[RotationalDirections]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BearingEfficiencyRatingMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BearingEfficiencyRatingMethod

    A specific implementation of 'EnumWithSelectedValue' for 'BearingEfficiencyRatingMethod' types.
    """

    __hash__ = None
    __qualname__ = 'BearingEfficiencyRatingMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_283.BearingEfficiencyRatingMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _283.BearingEfficiencyRatingMethod

    @classmethod
    def implicit_type(cls) -> '_283.BearingEfficiencyRatingMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _283.BearingEfficiencyRatingMethod.type_()

    @property
    def selected_value(self) -> '_283.BearingEfficiencyRatingMethod':
        """BearingEfficiencyRatingMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_283.BearingEfficiencyRatingMethod]':
        """List[BearingEfficiencyRatingMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ShaftDiameterModificationDueToRollingBearingRing

    A specific implementation of 'EnumWithSelectedValue' for 'ShaftDiameterModificationDueToRollingBearingRing' types.
    """

    __hash__ = None
    __qualname__ = 'ShaftDiameterModificationDueToRollingBearingRing'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2415.ShaftDiameterModificationDueToRollingBearingRing':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2415.ShaftDiameterModificationDueToRollingBearingRing

    @classmethod
    def implicit_type(cls) -> '_2415.ShaftDiameterModificationDueToRollingBearingRing.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2415.ShaftDiameterModificationDueToRollingBearingRing.type_()

    @property
    def selected_value(self) -> '_2415.ShaftDiameterModificationDueToRollingBearingRing':
        """ShaftDiameterModificationDueToRollingBearingRing: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2415.ShaftDiameterModificationDueToRollingBearingRing]':
        """List[ShaftDiameterModificationDueToRollingBearingRing]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ExcitationAnalysisViewOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ExcitationAnalysisViewOption

    A specific implementation of 'EnumWithSelectedValue' for 'ExcitationAnalysisViewOption' types.
    """

    __hash__ = None
    __qualname__ = 'ExcitationAnalysisViewOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2202.ExcitationAnalysisViewOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2202.ExcitationAnalysisViewOption

    @classmethod
    def implicit_type(cls) -> '_2202.ExcitationAnalysisViewOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2202.ExcitationAnalysisViewOption.type_()

    @property
    def selected_value(self) -> '_2202.ExcitationAnalysisViewOption':
        """ExcitationAnalysisViewOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2202.ExcitationAnalysisViewOption]':
        """List[ExcitationAnalysisViewOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ThreeDViewContourOptionFirstSelection

    A specific implementation of 'EnumWithSelectedValue' for 'ThreeDViewContourOptionFirstSelection' types.
    """

    __hash__ = None
    __qualname__ = 'ThreeDViewContourOptionFirstSelection'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1778.ThreeDViewContourOptionFirstSelection':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1778.ThreeDViewContourOptionFirstSelection

    @classmethod
    def implicit_type(cls) -> '_1778.ThreeDViewContourOptionFirstSelection.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1778.ThreeDViewContourOptionFirstSelection.type_()

    @property
    def selected_value(self) -> '_1778.ThreeDViewContourOptionFirstSelection':
        """ThreeDViewContourOptionFirstSelection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1778.ThreeDViewContourOptionFirstSelection]':
        """List[ThreeDViewContourOptionFirstSelection]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ThreeDViewContourOptionSecondSelection

    A specific implementation of 'EnumWithSelectedValue' for 'ThreeDViewContourOptionSecondSelection' types.
    """

    __hash__ = None
    __qualname__ = 'ThreeDViewContourOptionSecondSelection'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1779.ThreeDViewContourOptionSecondSelection':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1779.ThreeDViewContourOptionSecondSelection

    @classmethod
    def implicit_type(cls) -> '_1779.ThreeDViewContourOptionSecondSelection.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1779.ThreeDViewContourOptionSecondSelection.type_()

    @property
    def selected_value(self) -> '_1779.ThreeDViewContourOptionSecondSelection':
        """ThreeDViewContourOptionSecondSelection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1779.ThreeDViewContourOptionSecondSelection]':
        """List[ThreeDViewContourOptionSecondSelection]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ComponentOrientationOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ComponentOrientationOption

    A specific implementation of 'EnumWithSelectedValue' for 'ComponentOrientationOption' types.
    """

    __hash__ = None
    __qualname__ = 'ComponentOrientationOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2306.ComponentOrientationOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2306.ComponentOrientationOption

    @classmethod
    def implicit_type(cls) -> '_2306.ComponentOrientationOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2306.ComponentOrientationOption.type_()

    @property
    def selected_value(self) -> '_2306.ComponentOrientationOption':
        """ComponentOrientationOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2306.ComponentOrientationOption]':
        """List[ComponentOrientationOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_Axis(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_Axis

    A specific implementation of 'EnumWithSelectedValue' for 'Axis' types.
    """

    __hash__ = None
    __qualname__ = 'Axis'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1451.Axis':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1451.Axis

    @classmethod
    def implicit_type(cls) -> '_1451.Axis.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1451.Axis.type_()

    @property
    def selected_value(self) -> '_1451.Axis':
        """Axis: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1451.Axis]':
        """List[Axis]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_AlignmentAxis(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_AlignmentAxis

    A specific implementation of 'EnumWithSelectedValue' for 'AlignmentAxis' types.
    """

    __hash__ = None
    __qualname__ = 'AlignmentAxis'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1450.AlignmentAxis':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1450.AlignmentAxis

    @classmethod
    def implicit_type(cls) -> '_1450.AlignmentAxis.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1450.AlignmentAxis.type_()

    @property
    def selected_value(self) -> '_1450.AlignmentAxis':
        """AlignmentAxis: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1450.AlignmentAxis]':
        """List[AlignmentAxis]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_DesignEntityId(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_DesignEntityId

    A specific implementation of 'EnumWithSelectedValue' for 'DesignEntityId' types.
    """

    __hash__ = None
    __qualname__ = 'DesignEntityId'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2148.DesignEntityId':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2148.DesignEntityId

    @classmethod
    def implicit_type(cls) -> '_2148.DesignEntityId.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2148.DesignEntityId.type_()

    @property
    def selected_value(self) -> '_2148.DesignEntityId':
        """DesignEntityId: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2148.DesignEntityId]':
        """List[DesignEntityId]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ThermalExpansionOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ThermalExpansionOption

    A specific implementation of 'EnumWithSelectedValue' for 'ThermalExpansionOption' types.
    """

    __hash__ = None
    __qualname__ = 'ThermalExpansionOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2350.ThermalExpansionOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2350.ThermalExpansionOption

    @classmethod
    def implicit_type(cls) -> '_2350.ThermalExpansionOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2350.ThermalExpansionOption.type_()

    @property
    def selected_value(self) -> '_2350.ThermalExpansionOption':
        """ThermalExpansionOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2350.ThermalExpansionOption]':
        """List[ThermalExpansionOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_FESubstructureType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_FESubstructureType

    A specific implementation of 'EnumWithSelectedValue' for 'FESubstructureType' types.
    """

    __hash__ = None
    __qualname__ = 'FESubstructureType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2327.FESubstructureType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2327.FESubstructureType

    @classmethod
    def implicit_type(cls) -> '_2327.FESubstructureType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2327.FESubstructureType.type_()

    @property
    def selected_value(self) -> '_2327.FESubstructureType':
        """FESubstructureType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2327.FESubstructureType]':
        """List[FESubstructureType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_FEExportFormat(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_FEExportFormat

    A specific implementation of 'EnumWithSelectedValue' for 'FEExportFormat' types.
    """

    __hash__ = None
    __qualname__ = 'FEExportFormat'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_165.FEExportFormat':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _165.FEExportFormat

    @classmethod
    def implicit_type(cls) -> '_165.FEExportFormat.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _165.FEExportFormat.type_()

    @property
    def selected_value(self) -> '_165.FEExportFormat':
        """FEExportFormat: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_165.FEExportFormat]':
        """List[FEExportFormat]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ThreeDViewContourOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ThreeDViewContourOption

    A specific implementation of 'EnumWithSelectedValue' for 'ThreeDViewContourOption' types.
    """

    __hash__ = None
    __qualname__ = 'ThreeDViewContourOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1777.ThreeDViewContourOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1777.ThreeDViewContourOption

    @classmethod
    def implicit_type(cls) -> '_1777.ThreeDViewContourOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1777.ThreeDViewContourOption.type_()

    @property
    def selected_value(self) -> '_1777.ThreeDViewContourOption':
        """ThreeDViewContourOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1777.ThreeDViewContourOption]':
        """List[ThreeDViewContourOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BoundaryConditionType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BoundaryConditionType

    A specific implementation of 'EnumWithSelectedValue' for 'BoundaryConditionType' types.
    """

    __hash__ = None
    __qualname__ = 'BoundaryConditionType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_164.BoundaryConditionType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _164.BoundaryConditionType

    @classmethod
    def implicit_type(cls) -> '_164.BoundaryConditionType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _164.BoundaryConditionType.type_()

    @property
    def selected_value(self) -> '_164.BoundaryConditionType':
        """BoundaryConditionType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_164.BoundaryConditionType]':
        """List[BoundaryConditionType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BearingNodeOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BearingNodeOption

    A specific implementation of 'EnumWithSelectedValue' for 'BearingNodeOption' types.
    """

    __hash__ = None
    __qualname__ = 'BearingNodeOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2303.BearingNodeOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2303.BearingNodeOption

    @classmethod
    def implicit_type(cls) -> '_2303.BearingNodeOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2303.BearingNodeOption.type_()

    @property
    def selected_value(self) -> '_2303.BearingNodeOption':
        """BearingNodeOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2303.BearingNodeOption]':
        """List[BearingNodeOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_LinkNodeSource(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_LinkNodeSource

    A specific implementation of 'EnumWithSelectedValue' for 'LinkNodeSource' types.
    """

    __hash__ = None
    __qualname__ = 'LinkNodeSource'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2337.LinkNodeSource':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2337.LinkNodeSource

    @classmethod
    def implicit_type(cls) -> '_2337.LinkNodeSource.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2337.LinkNodeSource.type_()

    @property
    def selected_value(self) -> '_2337.LinkNodeSource':
        """LinkNodeSource: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2337.LinkNodeSource]':
        """List[LinkNodeSource]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BearingToleranceClass(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BearingToleranceClass

    A specific implementation of 'EnumWithSelectedValue' for 'BearingToleranceClass' types.
    """

    __hash__ = None
    __qualname__ = 'BearingToleranceClass'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1852.BearingToleranceClass':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1852.BearingToleranceClass

    @classmethod
    def implicit_type(cls) -> '_1852.BearingToleranceClass.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1852.BearingToleranceClass.type_()

    @property
    def selected_value(self) -> '_1852.BearingToleranceClass':
        """BearingToleranceClass: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1852.BearingToleranceClass]':
        """List[BearingToleranceClass]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BearingModel(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BearingModel

    A specific implementation of 'EnumWithSelectedValue' for 'BearingModel' types.
    """

    __hash__ = None
    __qualname__ = 'BearingModel'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1826.BearingModel':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1826.BearingModel

    @classmethod
    def implicit_type(cls) -> '_1826.BearingModel.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1826.BearingModel.type_()

    @property
    def selected_value(self) -> '_1826.BearingModel':
        """BearingModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1826.BearingModel]':
        """List[BearingModel]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_PreloadType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_PreloadType

    A specific implementation of 'EnumWithSelectedValue' for 'PreloadType' types.
    """

    __hash__ = None
    __qualname__ = 'PreloadType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1909.PreloadType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1909.PreloadType

    @classmethod
    def implicit_type(cls) -> '_1909.PreloadType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1909.PreloadType.type_()

    @property
    def selected_value(self) -> '_1909.PreloadType':
        """PreloadType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1909.PreloadType]':
        """List[PreloadType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RaceAxialMountingType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RaceAxialMountingType

    A specific implementation of 'EnumWithSelectedValue' for 'RaceAxialMountingType' types.
    """

    __hash__ = None
    __qualname__ = 'RaceAxialMountingType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1911.RaceAxialMountingType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1911.RaceAxialMountingType

    @classmethod
    def implicit_type(cls) -> '_1911.RaceAxialMountingType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1911.RaceAxialMountingType.type_()

    @property
    def selected_value(self) -> '_1911.RaceAxialMountingType':
        """RaceAxialMountingType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1911.RaceAxialMountingType]':
        """List[RaceAxialMountingType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RaceRadialMountingType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RaceRadialMountingType

    A specific implementation of 'EnumWithSelectedValue' for 'RaceRadialMountingType' types.
    """

    __hash__ = None
    __qualname__ = 'RaceRadialMountingType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1912.RaceRadialMountingType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1912.RaceRadialMountingType

    @classmethod
    def implicit_type(cls) -> '_1912.RaceRadialMountingType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1912.RaceRadialMountingType.type_()

    @property
    def selected_value(self) -> '_1912.RaceRadialMountingType':
        """RaceRadialMountingType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1912.RaceRadialMountingType]':
        """List[RaceRadialMountingType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_InternalClearanceClass(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_InternalClearanceClass

    A specific implementation of 'EnumWithSelectedValue' for 'InternalClearanceClass' types.
    """

    __hash__ = None
    __qualname__ = 'InternalClearanceClass'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1851.InternalClearanceClass':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1851.InternalClearanceClass

    @classmethod
    def implicit_type(cls) -> '_1851.InternalClearanceClass.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1851.InternalClearanceClass.type_()

    @property
    def selected_value(self) -> '_1851.InternalClearanceClass':
        """InternalClearanceClass: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1851.InternalClearanceClass]':
        """List[InternalClearanceClass]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BearingToleranceDefinitionOptions(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BearingToleranceDefinitionOptions

    A specific implementation of 'EnumWithSelectedValue' for 'BearingToleranceDefinitionOptions' types.
    """

    __hash__ = None
    __qualname__ = 'BearingToleranceDefinitionOptions'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1853.BearingToleranceDefinitionOptions':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1853.BearingToleranceDefinitionOptions

    @classmethod
    def implicit_type(cls) -> '_1853.BearingToleranceDefinitionOptions.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1853.BearingToleranceDefinitionOptions.type_()

    @property
    def selected_value(self) -> '_1853.BearingToleranceDefinitionOptions':
        """BearingToleranceDefinitionOptions: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1853.BearingToleranceDefinitionOptions]':
        """List[BearingToleranceDefinitionOptions]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_OilSealLossCalculationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_OilSealLossCalculationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'OilSealLossCalculationMethod' types.
    """

    __hash__ = None
    __qualname__ = 'OilSealLossCalculationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_291.OilSealLossCalculationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _291.OilSealLossCalculationMethod

    @classmethod
    def implicit_type(cls) -> '_291.OilSealLossCalculationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _291.OilSealLossCalculationMethod.type_()

    @property
    def selected_value(self) -> '_291.OilSealLossCalculationMethod':
        """OilSealLossCalculationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_291.OilSealLossCalculationMethod]':
        """List[OilSealLossCalculationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_PowerLoadType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_PowerLoadType

    A specific implementation of 'EnumWithSelectedValue' for 'PowerLoadType' types.
    """

    __hash__ = None
    __qualname__ = 'PowerLoadType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2162.PowerLoadType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2162.PowerLoadType

    @classmethod
    def implicit_type(cls) -> '_2162.PowerLoadType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2162.PowerLoadType.type_()

    @property
    def selected_value(self) -> '_2162.PowerLoadType':
        """PowerLoadType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2162.PowerLoadType]':
        """List[PowerLoadType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RigidConnectorStiffnessType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RigidConnectorStiffnessType

    A specific implementation of 'EnumWithSelectedValue' for 'RigidConnectorStiffnessType' types.
    """

    __hash__ = None
    __qualname__ = 'RigidConnectorStiffnessType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2530.RigidConnectorStiffnessType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2530.RigidConnectorStiffnessType

    @classmethod
    def implicit_type(cls) -> '_2530.RigidConnectorStiffnessType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2530.RigidConnectorStiffnessType.type_()

    @property
    def selected_value(self) -> '_2530.RigidConnectorStiffnessType':
        """RigidConnectorStiffnessType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2530.RigidConnectorStiffnessType]':
        """List[RigidConnectorStiffnessType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RigidConnectorToothSpacingType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RigidConnectorToothSpacingType

    A specific implementation of 'EnumWithSelectedValue' for 'RigidConnectorToothSpacingType' types.
    """

    __hash__ = None
    __qualname__ = 'RigidConnectorToothSpacingType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2533.RigidConnectorToothSpacingType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2533.RigidConnectorToothSpacingType

    @classmethod
    def implicit_type(cls) -> '_2533.RigidConnectorToothSpacingType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2533.RigidConnectorToothSpacingType.type_()

    @property
    def selected_value(self) -> '_2533.RigidConnectorToothSpacingType':
        """RigidConnectorToothSpacingType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2533.RigidConnectorToothSpacingType]':
        """List[RigidConnectorToothSpacingType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_RigidConnectorTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_RigidConnectorTypes

    A specific implementation of 'EnumWithSelectedValue' for 'RigidConnectorTypes' types.
    """

    __hash__ = None
    __qualname__ = 'RigidConnectorTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2534.RigidConnectorTypes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2534.RigidConnectorTypes

    @classmethod
    def implicit_type(cls) -> '_2534.RigidConnectorTypes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2534.RigidConnectorTypes.type_()

    @property
    def selected_value(self) -> '_2534.RigidConnectorTypes':
        """RigidConnectorTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2534.RigidConnectorTypes]':
        """List[RigidConnectorTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_FitTypes(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_FitTypes

    A specific implementation of 'EnumWithSelectedValue' for 'FitTypes' types.
    """

    __hash__ = None
    __qualname__ = 'FitTypes'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1356.FitTypes':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1356.FitTypes

    @classmethod
    def implicit_type(cls) -> '_1356.FitTypes.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1356.FitTypes.type_()

    @property
    def selected_value(self) -> '_1356.FitTypes':
        """FitTypes: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1356.FitTypes]':
        """List[FitTypes]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_DoeValueSpecificationOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_DoeValueSpecificationOption

    A specific implementation of 'EnumWithSelectedValue' for 'DoeValueSpecificationOption' types.
    """

    __hash__ = None
    __qualname__ = 'DoeValueSpecificationOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_4279.DoeValueSpecificationOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _4279.DoeValueSpecificationOption

    @classmethod
    def implicit_type(cls) -> '_4279.DoeValueSpecificationOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _4279.DoeValueSpecificationOption.type_()

    @property
    def selected_value(self) -> '_4279.DoeValueSpecificationOption':
        """DoeValueSpecificationOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_4279.DoeValueSpecificationOption]':
        """List[DoeValueSpecificationOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_AnalysisType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_AnalysisType

    A specific implementation of 'EnumWithSelectedValue' for 'AnalysisType' types.
    """

    __hash__ = None
    __qualname__ = 'AnalysisType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_6732.AnalysisType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _6732.AnalysisType

    @classmethod
    def implicit_type(cls) -> '_6732.AnalysisType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6732.AnalysisType.type_()

    @property
    def selected_value(self) -> '_6732.AnalysisType':
        """AnalysisType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_6732.AnalysisType]':
        """List[AnalysisType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BarModelExportType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BarModelExportType

    A specific implementation of 'EnumWithSelectedValue' for 'BarModelExportType' types.
    """

    __hash__ = None
    __qualname__ = 'BarModelExportType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_53.BarModelExportType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _53.BarModelExportType

    @classmethod
    def implicit_type(cls) -> '_53.BarModelExportType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _53.BarModelExportType.type_()

    @property
    def selected_value(self) -> '_53.BarModelExportType':
        """BarModelExportType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_53.BarModelExportType]':
        """List[BarModelExportType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ComplexPartDisplayOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ComplexPartDisplayOption

    A specific implementation of 'EnumWithSelectedValue' for 'ComplexPartDisplayOption' types.
    """

    __hash__ = None
    __qualname__ = 'ComplexPartDisplayOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1454.ComplexPartDisplayOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1454.ComplexPartDisplayOption

    @classmethod
    def implicit_type(cls) -> '_1454.ComplexPartDisplayOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1454.ComplexPartDisplayOption.type_()

    @property
    def selected_value(self) -> '_1454.ComplexPartDisplayOption':
        """ComplexPartDisplayOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1454.ComplexPartDisplayOption]':
        """List[ComplexPartDisplayOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_DynamicsResponseType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_DynamicsResponseType

    A specific implementation of 'EnumWithSelectedValue' for 'DynamicsResponseType' types.
    """

    __hash__ = None
    __qualname__ = 'DynamicsResponseType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_4556.DynamicsResponseType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _4556.DynamicsResponseType

    @classmethod
    def implicit_type(cls) -> '_4556.DynamicsResponseType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _4556.DynamicsResponseType.type_()

    @property
    def selected_value(self) -> '_4556.DynamicsResponseType':
        """DynamicsResponseType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_4556.DynamicsResponseType]':
        """List[DynamicsResponseType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BearingStiffnessModel(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BearingStiffnessModel

    A specific implementation of 'EnumWithSelectedValue' for 'BearingStiffnessModel' types.
    """

    __hash__ = None
    __qualname__ = 'BearingStiffnessModel'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_5311.BearingStiffnessModel':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5311.BearingStiffnessModel

    @classmethod
    def implicit_type(cls) -> '_5311.BearingStiffnessModel.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5311.BearingStiffnessModel.type_()

    @property
    def selected_value(self) -> '_5311.BearingStiffnessModel':
        """BearingStiffnessModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_5311.BearingStiffnessModel]':
        """List[BearingStiffnessModel]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_GearMeshStiffnessModel(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_GearMeshStiffnessModel

    A specific implementation of 'EnumWithSelectedValue' for 'GearMeshStiffnessModel' types.
    """

    __hash__ = None
    __qualname__ = 'GearMeshStiffnessModel'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_5363.GearMeshStiffnessModel':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5363.GearMeshStiffnessModel

    @classmethod
    def implicit_type(cls) -> '_5363.GearMeshStiffnessModel.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5363.GearMeshStiffnessModel.type_()

    @property
    def selected_value(self) -> '_5363.GearMeshStiffnessModel':
        """GearMeshStiffnessModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_5363.GearMeshStiffnessModel]':
        """List[GearMeshStiffnessModel]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ShaftAndHousingFlexibilityOption(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ShaftAndHousingFlexibilityOption

    A specific implementation of 'EnumWithSelectedValue' for 'ShaftAndHousingFlexibilityOption' types.
    """

    __hash__ = None
    __qualname__ = 'ShaftAndHousingFlexibilityOption'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_5408.ShaftAndHousingFlexibilityOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5408.ShaftAndHousingFlexibilityOption

    @classmethod
    def implicit_type(cls) -> '_5408.ShaftAndHousingFlexibilityOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5408.ShaftAndHousingFlexibilityOption.type_()

    @property
    def selected_value(self) -> '_5408.ShaftAndHousingFlexibilityOption':
        """ShaftAndHousingFlexibilityOption: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_5408.ShaftAndHousingFlexibilityOption]':
        """List[ShaftAndHousingFlexibilityOption]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ExportOutputType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ExportOutputType

    A specific implementation of 'EnumWithSelectedValue' for 'ExportOutputType' types.
    """

    __hash__ = None
    __qualname__ = 'ExportOutputType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_5667.ExportOutputType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5667.ExportOutputType

    @classmethod
    def implicit_type(cls) -> '_5667.ExportOutputType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5667.ExportOutputType.type_()

    @property
    def selected_value(self) -> '_5667.ExportOutputType':
        """ExportOutputType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_5667.ExportOutputType]':
        """List[ExportOutputType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_HarmonicAnalysisFEExportOptions_ComplexNumberOutput(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_HarmonicAnalysisFEExportOptions_ComplexNumberOutput

    A specific implementation of 'EnumWithSelectedValue' for 'HarmonicAnalysisFEExportOptions.ComplexNumberOutput' types.
    """

    __hash__ = None
    __qualname__ = 'HarmonicAnalysisFEExportOptions.ComplexNumberOutput'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_5685.HarmonicAnalysisFEExportOptions.ComplexNumberOutput':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5685.HarmonicAnalysisFEExportOptions.ComplexNumberOutput

    @classmethod
    def implicit_type(cls) -> '_5685.HarmonicAnalysisFEExportOptions.ComplexNumberOutput.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5685.HarmonicAnalysisFEExportOptions.ComplexNumberOutput.type_()

    @property
    def selected_value(self) -> '_5685.HarmonicAnalysisFEExportOptions.ComplexNumberOutput':
        """HarmonicAnalysisFEExportOptions.ComplexNumberOutput: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_5685.HarmonicAnalysisFEExportOptions.ComplexNumberOutput]':
        """List[HarmonicAnalysisFEExportOptions.ComplexNumberOutput]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_FrictionModelForGyroscopicMoment(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_FrictionModelForGyroscopicMoment

    A specific implementation of 'EnumWithSelectedValue' for 'FrictionModelForGyroscopicMoment' types.
    """

    __hash__ = None
    __qualname__ = 'FrictionModelForGyroscopicMoment'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1920.FrictionModelForGyroscopicMoment':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1920.FrictionModelForGyroscopicMoment

    @classmethod
    def implicit_type(cls) -> '_1920.FrictionModelForGyroscopicMoment.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1920.FrictionModelForGyroscopicMoment.type_()

    @property
    def selected_value(self) -> '_1920.FrictionModelForGyroscopicMoment':
        """FrictionModelForGyroscopicMoment: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1920.FrictionModelForGyroscopicMoment]':
        """List[FrictionModelForGyroscopicMoment]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_MeshStiffnessModel(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_MeshStiffnessModel

    A specific implementation of 'EnumWithSelectedValue' for 'MeshStiffnessModel' types.
    """

    __hash__ = None
    __qualname__ = 'MeshStiffnessModel'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2157.MeshStiffnessModel':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2157.MeshStiffnessModel

    @classmethod
    def implicit_type(cls) -> '_2157.MeshStiffnessModel.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2157.MeshStiffnessModel.type_()

    @property
    def selected_value(self) -> '_2157.MeshStiffnessModel':
        """MeshStiffnessModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2157.MeshStiffnessModel]':
        """List[MeshStiffnessModel]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_ShearAreaFactorMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_ShearAreaFactorMethod

    A specific implementation of 'EnumWithSelectedValue' for 'ShearAreaFactorMethod' types.
    """

    __hash__ = None
    __qualname__ = 'ShearAreaFactorMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_129.ShearAreaFactorMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _129.ShearAreaFactorMethod

    @classmethod
    def implicit_type(cls) -> '_129.ShearAreaFactorMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _129.ShearAreaFactorMethod.type_()

    @property
    def selected_value(self) -> '_129.ShearAreaFactorMethod':
        """ShearAreaFactorMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_129.ShearAreaFactorMethod]':
        """List[ShearAreaFactorMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_StressConcentrationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_StressConcentrationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'StressConcentrationMethod' types.
    """

    __hash__ = None
    __qualname__ = 'StressConcentrationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2053.StressConcentrationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2053.StressConcentrationMethod

    @classmethod
    def implicit_type(cls) -> '_2053.StressConcentrationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2053.StressConcentrationMethod.type_()

    @property
    def selected_value(self) -> '_2053.StressConcentrationMethod':
        """StressConcentrationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2053.StressConcentrationMethod]':
        """List[StressConcentrationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_BallBearingAnalysisMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_BallBearingAnalysisMethod

    A specific implementation of 'EnumWithSelectedValue' for 'BallBearingAnalysisMethod' types.
    """

    __hash__ = None
    __qualname__ = 'BallBearingAnalysisMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1914.BallBearingAnalysisMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1914.BallBearingAnalysisMethod

    @classmethod
    def implicit_type(cls) -> '_1914.BallBearingAnalysisMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1914.BallBearingAnalysisMethod.type_()

    @property
    def selected_value(self) -> '_1914.BallBearingAnalysisMethod':
        """BallBearingAnalysisMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1914.BallBearingAnalysisMethod]':
        """List[BallBearingAnalysisMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_HertzianContactDeflectionCalculationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_HertzianContactDeflectionCalculationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'HertzianContactDeflectionCalculationMethod' types.
    """

    __hash__ = None
    __qualname__ = 'HertzianContactDeflectionCalculationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1533.HertzianContactDeflectionCalculationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1533.HertzianContactDeflectionCalculationMethod

    @classmethod
    def implicit_type(cls) -> '_1533.HertzianContactDeflectionCalculationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1533.HertzianContactDeflectionCalculationMethod.type_()

    @property
    def selected_value(self) -> '_1533.HertzianContactDeflectionCalculationMethod':
        """HertzianContactDeflectionCalculationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1533.HertzianContactDeflectionCalculationMethod]':
        """List[HertzianContactDeflectionCalculationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_TorqueRippleInputType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_TorqueRippleInputType

    A specific implementation of 'EnumWithSelectedValue' for 'TorqueRippleInputType' types.
    """

    __hash__ = None
    __qualname__ = 'TorqueRippleInputType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_6890.TorqueRippleInputType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _6890.TorqueRippleInputType

    @classmethod
    def implicit_type(cls) -> '_6890.TorqueRippleInputType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6890.TorqueRippleInputType.type_()

    @property
    def selected_value(self) -> '_6890.TorqueRippleInputType':
        """TorqueRippleInputType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_6890.TorqueRippleInputType]':
        """List[TorqueRippleInputType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_HarmonicExcitationType(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_HarmonicExcitationType

    A specific implementation of 'EnumWithSelectedValue' for 'HarmonicExcitationType' types.
    """

    __hash__ = None
    __qualname__ = 'HarmonicExcitationType'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_6811.HarmonicExcitationType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _6811.HarmonicExcitationType

    @classmethod
    def implicit_type(cls) -> '_6811.HarmonicExcitationType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6811.HarmonicExcitationType.type_()

    @property
    def selected_value(self) -> '_6811.HarmonicExcitationType':
        """HarmonicExcitationType: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_6811.HarmonicExcitationType]':
        """List[HarmonicExcitationType]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_PointLoadLoadCase_ForceSpecification(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_PointLoadLoadCase_ForceSpecification

    A specific implementation of 'EnumWithSelectedValue' for 'PointLoadLoadCase.ForceSpecification' types.
    """

    __hash__ = None
    __qualname__ = 'PointLoadLoadCase.ForceSpecification'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_6852.PointLoadLoadCase.ForceSpecification':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _6852.PointLoadLoadCase.ForceSpecification

    @classmethod
    def implicit_type(cls) -> '_6852.PointLoadLoadCase.ForceSpecification.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6852.PointLoadLoadCase.ForceSpecification.type_()

    @property
    def selected_value(self) -> '_6852.PointLoadLoadCase.ForceSpecification':
        """PointLoadLoadCase.ForceSpecification: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_6852.PointLoadLoadCase.ForceSpecification]':
        """List[PointLoadLoadCase.ForceSpecification]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_TorqueSpecificationForSystemDeflection(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_TorqueSpecificationForSystemDeflection

    A specific implementation of 'EnumWithSelectedValue' for 'TorqueSpecificationForSystemDeflection' types.
    """

    __hash__ = None
    __qualname__ = 'TorqueSpecificationForSystemDeflection'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_6891.TorqueSpecificationForSystemDeflection':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _6891.TorqueSpecificationForSystemDeflection

    @classmethod
    def implicit_type(cls) -> '_6891.TorqueSpecificationForSystemDeflection.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6891.TorqueSpecificationForSystemDeflection.type_()

    @property
    def selected_value(self) -> '_6891.TorqueSpecificationForSystemDeflection':
        """TorqueSpecificationForSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_6891.TorqueSpecificationForSystemDeflection]':
        """List[TorqueSpecificationForSystemDeflection]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_PowerLoadInputTorqueSpecificationMethod

    A specific implementation of 'EnumWithSelectedValue' for 'PowerLoadInputTorqueSpecificationMethod' types.
    """

    __hash__ = None
    __qualname__ = 'PowerLoadInputTorqueSpecificationMethod'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_2160.PowerLoadInputTorqueSpecificationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2160.PowerLoadInputTorqueSpecificationMethod

    @classmethod
    def implicit_type(cls) -> '_2160.PowerLoadInputTorqueSpecificationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2160.PowerLoadInputTorqueSpecificationMethod.type_()

    @property
    def selected_value(self) -> '_2160.PowerLoadInputTorqueSpecificationMethod':
        """PowerLoadInputTorqueSpecificationMethod: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_2160.PowerLoadInputTorqueSpecificationMethod]':
        """List[PowerLoadInputTorqueSpecificationMethod]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_TorqueConverterLockupRule(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_TorqueConverterLockupRule

    A specific implementation of 'EnumWithSelectedValue' for 'TorqueConverterLockupRule' types.
    """

    __hash__ = None
    __qualname__ = 'TorqueConverterLockupRule'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_5433.TorqueConverterLockupRule':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _5433.TorqueConverterLockupRule

    @classmethod
    def implicit_type(cls) -> '_5433.TorqueConverterLockupRule.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5433.TorqueConverterLockupRule.type_()

    @property
    def selected_value(self) -> '_5433.TorqueConverterLockupRule':
        """TorqueConverterLockupRule: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_5433.TorqueConverterLockupRule]':
        """List[TorqueConverterLockupRule]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_DegreesOfFreedom(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_DegreesOfFreedom

    A specific implementation of 'EnumWithSelectedValue' for 'DegreesOfFreedom' types.
    """

    __hash__ = None
    __qualname__ = 'DegreesOfFreedom'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_1463.DegreesOfFreedom':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1463.DegreesOfFreedom

    @classmethod
    def implicit_type(cls) -> '_1463.DegreesOfFreedom.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1463.DegreesOfFreedom.type_()

    @property
    def selected_value(self) -> '_1463.DegreesOfFreedom':
        """DegreesOfFreedom: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_1463.DegreesOfFreedom]':
        """List[DegreesOfFreedom]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class EnumWithSelectedValue_DestinationDesignState(mixins.EnumWithSelectedValueMixin, Enum):
    """EnumWithSelectedValue_DestinationDesignState

    A specific implementation of 'EnumWithSelectedValue' for 'DestinationDesignState' types.
    """

    __hash__ = None
    __qualname__ = 'DestinationDesignState'

    @classmethod
    def wrapper_type(cls) -> '_ENUM_WITH_SELECTED_VALUE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _ENUM_WITH_SELECTED_VALUE

    @classmethod
    def wrapped_type(cls) -> '_6905.DestinationDesignState':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _6905.DestinationDesignState

    @classmethod
    def implicit_type(cls) -> '_6905.DestinationDesignState.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6905.DestinationDesignState.type_()

    @property
    def selected_value(self) -> '_6905.DestinationDesignState':
        """DestinationDesignState: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def available_values(self) -> 'List[_6905.DestinationDesignState]':
        """List[DestinationDesignState]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

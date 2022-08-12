"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1312 import DynamicForceAnalysis
    from ._1313 import DynamicForceLoadCase
    from ._1314 import EfficiencyMapAnalysis
    from ._1315 import EfficiencyMapLoadCase
    from ._1316 import ElectricMachineAnalysis
    from ._1317 import ElectricMachineBasicMechanicalLossSettings
    from ._1318 import ElectricMachineControlStrategy
    from ._1319 import ElectricMachineEfficiencyMapSettings
    from ._1320 import ElectricMachineFEAnalysis
    from ._1321 import ElectricMachineLoadCase
    from ._1322 import ElectricMachineLoadCaseBase
    from ._1323 import ElectricMachineLoadCaseGroup
    from ._1324 import EndWindingInductanceMethod
    from ._1325 import LeadingOrLagging
    from ._1326 import LoadCaseType
    from ._1327 import LoadCaseTypeSelector
    from ._1328 import MotoringOrGenerating
    from ._1329 import NonLinearDQModelMultipleOperatingPointsLoadCase
    from ._1330 import NumberOfStepsPerOperatingPointSpecificationMethod
    from ._1331 import OperatingPointsSpecificationMethod
    from ._1332 import SingleOperatingPointAnalysis
    from ._1333 import SlotDetailForAnalysis
    from ._1334 import SpecifyTorqueOrCurrent
    from ._1335 import SpeedPointsDistribution
    from ._1336 import SpeedTorqueCurveAnalysis
    from ._1337 import SpeedTorqueCurveLoadCase
    from ._1338 import SpeedTorqueLoadCase
    from ._1339 import SpeedTorqueOperatingPoint
    from ._1340 import Temperatures

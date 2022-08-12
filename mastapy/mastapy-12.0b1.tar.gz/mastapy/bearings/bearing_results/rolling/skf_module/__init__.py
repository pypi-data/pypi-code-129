"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._2020 import AdjustedSpeed
    from ._2021 import AdjustmentFactors
    from ._2022 import BearingLoads
    from ._2023 import BearingRatingLife
    from ._2024 import DynamicAxialLoadCarryingCapacity
    from ._2025 import Frequencies
    from ._2026 import FrequencyOfOverRolling
    from ._2027 import Friction
    from ._2028 import FrictionalMoment
    from ._2029 import FrictionSources
    from ._2030 import Grease
    from ._2031 import GreaseLifeAndRelubricationInterval
    from ._2032 import GreaseQuantity
    from ._2033 import InitialFill
    from ._2034 import LifeModel
    from ._2035 import MinimumLoad
    from ._2036 import OperatingViscosity
    from ._2037 import PermissibleAxialLoad
    from ._2038 import RotationalFrequency
    from ._2039 import SKFAuthentication
    from ._2040 import SKFCalculationResult
    from ._2041 import SKFCredentials
    from ._2042 import SKFModuleResults
    from ._2043 import StaticSafetyFactors
    from ._2044 import Viscosities

"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1404 import AssemblyMethods
    from ._1405 import CalculationMethods
    from ._1406 import InterferenceFitDesign
    from ._1407 import InterferenceFitHalfDesign
    from ._1408 import StressRegions
    from ._1409 import Table4JointInterfaceTypes

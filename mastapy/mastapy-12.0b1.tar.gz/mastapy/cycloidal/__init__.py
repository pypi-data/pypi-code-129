"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1412 import ContactSpecification
    from ._1413 import CrowningSpecificationMethod
    from ._1414 import CycloidalAssemblyDesign
    from ._1415 import CycloidalDiscDesign
    from ._1416 import CycloidalDiscMaterial
    from ._1417 import CycloidalDiscMaterialDatabase
    from ._1418 import CycloidalDiscModificationsSpecification
    from ._1419 import DirectionOfMeasuredModifications
    from ._1420 import NamedDiscPhase
    from ._1421 import RingPinsDesign
    from ._1422 import RingPinsMaterial
    from ._1423 import RingPinsMaterialDatabase

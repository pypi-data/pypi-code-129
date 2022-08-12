"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._2550 import ActiveFESubstructureSelection
    from ._2551 import ActiveFESubstructureSelectionGroup
    from ._2552 import ActiveShaftDesignSelection
    from ._2553 import ActiveShaftDesignSelectionGroup
    from ._2554 import BearingDetailConfiguration
    from ._2555 import BearingDetailSelection
    from ._2556 import PartDetailConfiguration
    from ._2557 import PartDetailSelection

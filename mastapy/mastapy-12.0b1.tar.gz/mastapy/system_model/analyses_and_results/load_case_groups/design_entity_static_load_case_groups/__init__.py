"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._5596 import AbstractAssemblyStaticLoadCaseGroup
    from ._5597 import ComponentStaticLoadCaseGroup
    from ._5598 import ConnectionStaticLoadCaseGroup
    from ._5599 import DesignEntityStaticLoadCaseGroup
    from ._5600 import GearSetStaticLoadCaseGroup
    from ._5601 import PartStaticLoadCaseGroup

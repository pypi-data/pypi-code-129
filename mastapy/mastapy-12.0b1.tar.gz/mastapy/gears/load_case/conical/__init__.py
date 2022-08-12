"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._875 import ConicalGearLoadCase
    from ._876 import ConicalGearSetLoadCase
    from ._877 import ConicalMeshLoadCase

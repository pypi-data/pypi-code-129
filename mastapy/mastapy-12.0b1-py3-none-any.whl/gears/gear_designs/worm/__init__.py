"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._947 import WormDesign
    from ._948 import WormGearDesign
    from ._949 import WormGearMeshDesign
    from ._950 import WormGearSetDesign
    from ._951 import WormWheelDesign

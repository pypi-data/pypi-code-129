"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._960 import SpiralBevelGearDesign
    from ._961 import SpiralBevelGearMeshDesign
    from ._962 import SpiralBevelGearSetDesign
    from ._963 import SpiralBevelMeshedGearDesign

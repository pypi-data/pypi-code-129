"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._976 import HypoidGearDesign
    from ._977 import HypoidGearMeshDesign
    from ._978 import HypoidGearSetDesign
    from ._979 import HypoidMeshedGearDesign

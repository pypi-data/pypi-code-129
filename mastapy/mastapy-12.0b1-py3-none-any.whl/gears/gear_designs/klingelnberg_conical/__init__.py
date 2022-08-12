"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._972 import KlingelnbergConicalGearDesign
    from ._973 import KlingelnbergConicalGearMeshDesign
    from ._974 import KlingelnbergConicalGearSetDesign
    from ._975 import KlingelnbergConicalMeshedGearDesign

"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1382 import FitAndTolerance
    from ._1383 import SAESplineTolerances

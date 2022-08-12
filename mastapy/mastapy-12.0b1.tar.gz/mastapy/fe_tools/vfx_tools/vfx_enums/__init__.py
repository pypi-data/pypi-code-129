"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._1225 import ProSolveMpcType
    from ._1226 import ProSolveSolverType

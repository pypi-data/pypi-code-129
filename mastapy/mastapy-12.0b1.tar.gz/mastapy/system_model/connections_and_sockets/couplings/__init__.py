"""__init__.py"""


from mastapy._internal.dummy_base_class_importer import _DummyBaseClassImport


with _DummyBaseClassImport():
    from ._2282 import ClutchConnection
    from ._2283 import ClutchSocket
    from ._2284 import ConceptCouplingConnection
    from ._2285 import ConceptCouplingSocket
    from ._2286 import CouplingConnection
    from ._2287 import CouplingSocket
    from ._2288 import PartToPartShearCouplingConnection
    from ._2289 import PartToPartShearCouplingSocket
    from ._2290 import SpringDamperConnection
    from ._2291 import SpringDamperSocket
    from ._2292 import TorqueConverterConnection
    from ._2293 import TorqueConverterPumpSocket
    from ._2294 import TorqueConverterTurbineSocket

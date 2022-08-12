"""_779.py

ConicalPinionMicroGeometryConfig
"""


from mastapy.gears.manufacturing.bevel import _773, _767
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import

_CONICAL_PINION_MICRO_GEOMETRY_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalPinionMicroGeometryConfig')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalPinionMicroGeometryConfig',)


class ConicalPinionMicroGeometryConfig(_767.ConicalGearMicroGeometryConfig):
    """ConicalPinionMicroGeometryConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_PINION_MICRO_GEOMETRY_CONFIG

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalPinionMicroGeometryConfig.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pinion_concave_ob_configuration(self) -> '_773.ConicalMeshFlankNurbsMicroGeometryConfig':
        """ConicalMeshFlankNurbsMicroGeometryConfig: 'PinionConcaveOBConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionConcaveOBConfiguration
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_convex_ib_configuration(self) -> '_773.ConicalMeshFlankNurbsMicroGeometryConfig':
        """ConicalMeshFlankNurbsMicroGeometryConfig: 'PinionConvexIBConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionConvexIBConfiguration
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

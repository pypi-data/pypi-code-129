"""_775.py

ConicalMeshManufacturingConfig
"""


from mastapy.gears.manufacturing.bevel import _778, _784, _777
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_MANUFACTURING_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalMeshManufacturingConfig')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshManufacturingConfig',)


class ConicalMeshManufacturingConfig(_777.ConicalMeshMicroGeometryConfigBase):
    """ConicalMeshManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_MANUFACTURING_CONFIG

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalMeshManufacturingConfig.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pinion_config(self) -> '_778.ConicalPinionManufacturingConfig':
        """ConicalPinionManufacturingConfig: 'PinionConfig' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionConfig
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def wheel_config(self) -> '_784.ConicalWheelManufacturingConfig':
        """ConicalWheelManufacturingConfig: 'WheelConfig' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelConfig
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

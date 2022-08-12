"""_771.py

ConicalMeshFlankManufacturingConfig
"""


from mastapy.gears.manufacturing.bevel.control_parameters import (
    _807, _808, _809, _810
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.gears.manufacturing.bevel.basic_machine_settings import _814, _813
from mastapy.gears.manufacturing.bevel import _772
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_FLANK_MANUFACTURING_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalMeshFlankManufacturingConfig')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshFlankManufacturingConfig',)


class ConicalMeshFlankManufacturingConfig(_772.ConicalMeshFlankMicroGeometryConfig):
    """ConicalMeshFlankManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_FLANK_MANUFACTURING_CONFIG

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalMeshFlankManufacturingConfig.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def control_parameters(self) -> '_807.ConicalGearManufacturingControlParameters':
        """ConicalGearManufacturingControlParameters: 'ControlParameters' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ControlParameters
        if _807.ConicalGearManufacturingControlParameters.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast control_parameters to ConicalGearManufacturingControlParameters. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def control_parameters_of_type_conical_manufacturing_sgm_control_parameters(self) -> '_808.ConicalManufacturingSGMControlParameters':
        """ConicalManufacturingSGMControlParameters: 'ControlParameters' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ControlParameters
        if _808.ConicalManufacturingSGMControlParameters.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast control_parameters to ConicalManufacturingSGMControlParameters. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def control_parameters_of_type_conical_manufacturing_sgt_control_parameters(self) -> '_809.ConicalManufacturingSGTControlParameters':
        """ConicalManufacturingSGTControlParameters: 'ControlParameters' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ControlParameters
        if _809.ConicalManufacturingSGTControlParameters.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast control_parameters to ConicalManufacturingSGTControlParameters. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def control_parameters_of_type_conical_manufacturing_smt_control_parameters(self) -> '_810.ConicalManufacturingSMTControlParameters':
        """ConicalManufacturingSMTControlParameters: 'ControlParameters' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ControlParameters
        if _810.ConicalManufacturingSMTControlParameters.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast control_parameters to ConicalManufacturingSMTControlParameters. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def specified_cradle_style_machine_settings(self) -> '_814.CradleStyleConicalMachineSettingsGenerated':
        """CradleStyleConicalMachineSettingsGenerated: 'SpecifiedCradleStyleMachineSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpecifiedCradleStyleMachineSettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def specified_phoenix_style_machine_settings(self) -> '_813.BasicConicalGearMachineSettingsGenerated':
        """BasicConicalGearMachineSettingsGenerated: 'SpecifiedPhoenixStyleMachineSettings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpecifiedPhoenixStyleMachineSettings
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

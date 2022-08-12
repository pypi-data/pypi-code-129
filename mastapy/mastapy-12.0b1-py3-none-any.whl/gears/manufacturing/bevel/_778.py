"""_778.py

ConicalPinionManufacturingConfig
"""


from mastapy._internal.python_net import python_net_import
from mastapy._internal import constructor
from mastapy.gears.manufacturing.bevel import (
    _775, _771, _796, _791,
    _792, _794, _797, _798,
    _799, _800, _766
)
from mastapy._internal.cast_exception import CastException
from mastapy.gears.manufacturing.bevel.cutters import _803, _804

_DATABASE_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.UtilityGUI.Databases', 'DatabaseWithSelectedItem')
_CONICAL_PINION_MANUFACTURING_CONFIG = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalPinionManufacturingConfig')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalPinionManufacturingConfig',)


class ConicalPinionManufacturingConfig(_766.ConicalGearManufacturingConfig):
    """ConicalPinionManufacturingConfig

    This is a mastapy class.
    """

    TYPE = _CONICAL_PINION_MANUFACTURING_CONFIG

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalPinionManufacturingConfig.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pinion_finish_manufacturing_machine(self) -> 'str':
        """str: 'PinionFinishManufacturingMachine' is the original name of this property."""

        temp = self.wrapped.PinionFinishManufacturingMachine.SelectedItemName
        return temp

    @pinion_finish_manufacturing_machine.setter
    def pinion_finish_manufacturing_machine(self, value: 'str'):
        self.wrapped.PinionFinishManufacturingMachine.SetSelectedItem(str(value) if value else '')

    @property
    def pinion_rough_manufacturing_machine(self) -> 'str':
        """str: 'PinionRoughManufacturingMachine' is the original name of this property."""

        temp = self.wrapped.PinionRoughManufacturingMachine.SelectedItemName
        return temp

    @pinion_rough_manufacturing_machine.setter
    def pinion_rough_manufacturing_machine(self, value: 'str'):
        self.wrapped.PinionRoughManufacturingMachine.SetSelectedItem(str(value) if value else '')

    @property
    def mesh_config(self) -> '_775.ConicalMeshManufacturingConfig':
        """ConicalMeshManufacturingConfig: 'MeshConfig' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshConfig
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_concave_ob_configuration(self) -> '_771.ConicalMeshFlankManufacturingConfig':
        """ConicalMeshFlankManufacturingConfig: 'PinionConcaveOBConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionConcaveOBConfiguration
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_convex_ib_configuration(self) -> '_771.ConicalMeshFlankManufacturingConfig':
        """ConicalMeshFlankManufacturingConfig: 'PinionConvexIBConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionConvexIBConfiguration
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_cutter_parameters_concave(self) -> '_796.PinionFinishMachineSettings':
        """PinionFinishMachineSettings: 'PinionCutterParametersConcave' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionCutterParametersConcave
        if _796.PinionFinishMachineSettings.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_concave to PinionFinishMachineSettings. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_cutter_parameters_concave_of_type_pinion_bevel_generating_modified_roll_machine_settings(self) -> '_791.PinionBevelGeneratingModifiedRollMachineSettings':
        """PinionBevelGeneratingModifiedRollMachineSettings: 'PinionCutterParametersConcave' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionCutterParametersConcave
        if _791.PinionBevelGeneratingModifiedRollMachineSettings.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_concave to PinionBevelGeneratingModifiedRollMachineSettings. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_cutter_parameters_concave_of_type_pinion_bevel_generating_tilt_machine_settings(self) -> '_792.PinionBevelGeneratingTiltMachineSettings':
        """PinionBevelGeneratingTiltMachineSettings: 'PinionCutterParametersConcave' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionCutterParametersConcave
        if _792.PinionBevelGeneratingTiltMachineSettings.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_concave to PinionBevelGeneratingTiltMachineSettings. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_cutter_parameters_concave_of_type_pinion_conical_machine_settings_specified(self) -> '_794.PinionConicalMachineSettingsSpecified':
        """PinionConicalMachineSettingsSpecified: 'PinionCutterParametersConcave' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionCutterParametersConcave
        if _794.PinionConicalMachineSettingsSpecified.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_concave to PinionConicalMachineSettingsSpecified. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_cutter_parameters_concave_of_type_pinion_hypoid_formate_tilt_machine_settings(self) -> '_797.PinionHypoidFormateTiltMachineSettings':
        """PinionHypoidFormateTiltMachineSettings: 'PinionCutterParametersConcave' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionCutterParametersConcave
        if _797.PinionHypoidFormateTiltMachineSettings.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_concave to PinionHypoidFormateTiltMachineSettings. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_cutter_parameters_concave_of_type_pinion_hypoid_generating_tilt_machine_settings(self) -> '_798.PinionHypoidGeneratingTiltMachineSettings':
        """PinionHypoidGeneratingTiltMachineSettings: 'PinionCutterParametersConcave' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionCutterParametersConcave
        if _798.PinionHypoidGeneratingTiltMachineSettings.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_concave to PinionHypoidGeneratingTiltMachineSettings. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_cutter_parameters_concave_of_type_pinion_machine_settings_smt(self) -> '_799.PinionMachineSettingsSMT':
        """PinionMachineSettingsSMT: 'PinionCutterParametersConcave' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionCutterParametersConcave
        if _799.PinionMachineSettingsSMT.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_concave to PinionMachineSettingsSMT. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_cutter_parameters_convex(self) -> '_796.PinionFinishMachineSettings':
        """PinionFinishMachineSettings: 'PinionCutterParametersConvex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionCutterParametersConvex
        if _796.PinionFinishMachineSettings.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_convex to PinionFinishMachineSettings. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_cutter_parameters_convex_of_type_pinion_bevel_generating_modified_roll_machine_settings(self) -> '_791.PinionBevelGeneratingModifiedRollMachineSettings':
        """PinionBevelGeneratingModifiedRollMachineSettings: 'PinionCutterParametersConvex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionCutterParametersConvex
        if _791.PinionBevelGeneratingModifiedRollMachineSettings.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_convex to PinionBevelGeneratingModifiedRollMachineSettings. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_cutter_parameters_convex_of_type_pinion_bevel_generating_tilt_machine_settings(self) -> '_792.PinionBevelGeneratingTiltMachineSettings':
        """PinionBevelGeneratingTiltMachineSettings: 'PinionCutterParametersConvex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionCutterParametersConvex
        if _792.PinionBevelGeneratingTiltMachineSettings.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_convex to PinionBevelGeneratingTiltMachineSettings. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_cutter_parameters_convex_of_type_pinion_conical_machine_settings_specified(self) -> '_794.PinionConicalMachineSettingsSpecified':
        """PinionConicalMachineSettingsSpecified: 'PinionCutterParametersConvex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionCutterParametersConvex
        if _794.PinionConicalMachineSettingsSpecified.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_convex to PinionConicalMachineSettingsSpecified. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_cutter_parameters_convex_of_type_pinion_hypoid_formate_tilt_machine_settings(self) -> '_797.PinionHypoidFormateTiltMachineSettings':
        """PinionHypoidFormateTiltMachineSettings: 'PinionCutterParametersConvex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionCutterParametersConvex
        if _797.PinionHypoidFormateTiltMachineSettings.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_convex to PinionHypoidFormateTiltMachineSettings. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_cutter_parameters_convex_of_type_pinion_hypoid_generating_tilt_machine_settings(self) -> '_798.PinionHypoidGeneratingTiltMachineSettings':
        """PinionHypoidGeneratingTiltMachineSettings: 'PinionCutterParametersConvex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionCutterParametersConvex
        if _798.PinionHypoidGeneratingTiltMachineSettings.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_convex to PinionHypoidGeneratingTiltMachineSettings. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_cutter_parameters_convex_of_type_pinion_machine_settings_smt(self) -> '_799.PinionMachineSettingsSMT':
        """PinionMachineSettingsSMT: 'PinionCutterParametersConvex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionCutterParametersConvex
        if _799.PinionMachineSettingsSMT.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast pinion_cutter_parameters_convex to PinionMachineSettingsSMT. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_finish_cutter(self) -> '_803.PinionFinishCutter':
        """PinionFinishCutter: 'PinionFinishCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionFinishCutter
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_rough_cutter(self) -> '_804.PinionRoughCutter':
        """PinionRoughCutter: 'PinionRoughCutter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionRoughCutter
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion_rough_machine_setting(self) -> '_800.PinionRoughMachineSetting':
        """PinionRoughMachineSetting: 'PinionRoughMachineSetting' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionRoughMachineSetting
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

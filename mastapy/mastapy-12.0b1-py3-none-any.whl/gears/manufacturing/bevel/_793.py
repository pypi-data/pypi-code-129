"""_793.py

PinionConcave
"""


from mastapy.gears.manufacturing.bevel.basic_machine_settings import _813
from mastapy._internal import constructor
from mastapy.gears.manufacturing.bevel import (
    _796, _791, _792, _794,
    _797, _798, _799
)
from mastapy._internal.cast_exception import CastException
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_PINION_CONCAVE = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'PinionConcave')


__docformat__ = 'restructuredtext en'
__all__ = ('PinionConcave',)


class PinionConcave(_0.APIBase):
    """PinionConcave

    This is a mastapy class.
    """

    TYPE = _PINION_CONCAVE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PinionConcave.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def pinion_concave_ob_configuration(self) -> '_813.BasicConicalGearMachineSettingsGenerated':
        """BasicConicalGearMachineSettingsGenerated: 'PinionConcaveOBConfiguration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionConcaveOBConfiguration
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

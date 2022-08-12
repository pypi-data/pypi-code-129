"""_713.py

CutterShapeDefinition
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.manufacturing.cylindrical.cutters import (
    _703, _697, _698, _699,
    _700, _702, _704, _705,
    _708
)
from mastapy._internal.cast_exception import CastException
from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _719
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_CUTTER_SHAPE_DEFINITION = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters.Tangibles', 'CutterShapeDefinition')


__docformat__ = 'restructuredtext en'
__all__ = ('CutterShapeDefinition',)


class CutterShapeDefinition(_0.APIBase):
    """CutterShapeDefinition

    This is a mastapy class.
    """

    TYPE = _CUTTER_SHAPE_DEFINITION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CutterShapeDefinition.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def normal_module(self) -> 'float':
        """float: 'NormalModule' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalModule
        return temp

    @property
    def normal_pitch(self) -> 'float':
        """float: 'NormalPitch' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalPitch
        return temp

    @property
    def normal_pressure_angle(self) -> 'float':
        """float: 'NormalPressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalPressureAngle
        return temp

    @property
    def design(self) -> '_703.CylindricalGearRealCutterDesign':
        """CylindricalGearRealCutterDesign: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design
        if _703.CylindricalGearRealCutterDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast design to CylindricalGearRealCutterDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def design_of_type_cylindrical_gear_form_grinding_wheel(self) -> '_697.CylindricalGearFormGrindingWheel':
        """CylindricalGearFormGrindingWheel: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design
        if _697.CylindricalGearFormGrindingWheel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast design to CylindricalGearFormGrindingWheel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def design_of_type_cylindrical_gear_grinding_worm(self) -> '_698.CylindricalGearGrindingWorm':
        """CylindricalGearGrindingWorm: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design
        if _698.CylindricalGearGrindingWorm.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast design to CylindricalGearGrindingWorm. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def design_of_type_cylindrical_gear_hob_design(self) -> '_699.CylindricalGearHobDesign':
        """CylindricalGearHobDesign: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design
        if _699.CylindricalGearHobDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast design to CylindricalGearHobDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def design_of_type_cylindrical_gear_plunge_shaver(self) -> '_700.CylindricalGearPlungeShaver':
        """CylindricalGearPlungeShaver: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design
        if _700.CylindricalGearPlungeShaver.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast design to CylindricalGearPlungeShaver. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def design_of_type_cylindrical_gear_rack_design(self) -> '_702.CylindricalGearRackDesign':
        """CylindricalGearRackDesign: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design
        if _702.CylindricalGearRackDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast design to CylindricalGearRackDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def design_of_type_cylindrical_gear_shaper(self) -> '_704.CylindricalGearShaper':
        """CylindricalGearShaper: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design
        if _704.CylindricalGearShaper.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast design to CylindricalGearShaper. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def design_of_type_cylindrical_gear_shaver(self) -> '_705.CylindricalGearShaver':
        """CylindricalGearShaver: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design
        if _705.CylindricalGearShaver.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast design to CylindricalGearShaver. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def design_of_type_involute_cutter_design(self) -> '_708.InvoluteCutterDesign':
        """InvoluteCutterDesign: 'Design' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Design
        if _708.InvoluteCutterDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast design to InvoluteCutterDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def fillet_points(self) -> 'List[_719.NamedPoint]':
        """List[NamedPoint]: 'FilletPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FilletPoints
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def main_blade_points(self) -> 'List[_719.NamedPoint]':
        """List[NamedPoint]: 'MainBladePoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MainBladePoints
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

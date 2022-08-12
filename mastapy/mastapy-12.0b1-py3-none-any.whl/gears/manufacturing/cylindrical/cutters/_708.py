"""_708.py

InvoluteCutterDesign
"""


from mastapy.gears import _324
from mastapy._internal import enum_with_selected_value_runtime, constructor, conversion
from mastapy.gears.gear_designs.cylindrical import (
    _1076, _1036, _1056, _1075
)
from mastapy._internal.cast_exception import CastException
from mastapy.gears.manufacturing.cylindrical.cutters import _703
from mastapy._internal.python_net import python_net_import

_INVOLUTE_CUTTER_DESIGN = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters', 'InvoluteCutterDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('InvoluteCutterDesign',)


class InvoluteCutterDesign(_703.CylindricalGearRealCutterDesign):
    """InvoluteCutterDesign

    This is a mastapy class.
    """

    TYPE = _INVOLUTE_CUTTER_DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'InvoluteCutterDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def hand(self) -> '_324.Hand':
        """Hand: 'Hand' is the original name of this property."""

        temp = self.wrapped.Hand
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_324.Hand)(value) if value is not None else None

    @hand.setter
    def hand(self, value: '_324.Hand'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.Hand = value

    @property
    def helix_angle(self) -> 'float':
        """float: 'HelixAngle' is the original name of this property."""

        temp = self.wrapped.HelixAngle
        return temp

    @helix_angle.setter
    def helix_angle(self, value: 'float'):
        self.wrapped.HelixAngle = float(value) if value else 0.0

    @property
    def number_of_teeth(self) -> 'float':
        """float: 'NumberOfTeeth' is the original name of this property."""

        temp = self.wrapped.NumberOfTeeth
        return temp

    @number_of_teeth.setter
    def number_of_teeth(self, value: 'float'):
        self.wrapped.NumberOfTeeth = float(value) if value else 0.0

    @property
    def tooth_thickness(self) -> '_1076.ToothThicknessSpecificationBase':
        """ToothThicknessSpecificationBase: 'ToothThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothThickness
        if _1076.ToothThicknessSpecificationBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast tooth_thickness to ToothThicknessSpecificationBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def tooth_thickness_of_type_finish_tooth_thickness_design_specification(self) -> '_1036.FinishToothThicknessDesignSpecification':
        """FinishToothThicknessDesignSpecification: 'ToothThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothThickness
        if _1036.FinishToothThicknessDesignSpecification.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast tooth_thickness to FinishToothThicknessDesignSpecification. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def tooth_thickness_of_type_readonly_tooth_thickness_specification(self) -> '_1056.ReadonlyToothThicknessSpecification':
        """ReadonlyToothThicknessSpecification: 'ToothThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothThickness
        if _1056.ReadonlyToothThicknessSpecification.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast tooth_thickness to ReadonlyToothThicknessSpecification. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def tooth_thickness_of_type_tooth_thickness_specification(self) -> '_1075.ToothThicknessSpecification':
        """ToothThicknessSpecification: 'ToothThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothThickness
        if _1075.ToothThicknessSpecification.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast tooth_thickness to ToothThicknessSpecification. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

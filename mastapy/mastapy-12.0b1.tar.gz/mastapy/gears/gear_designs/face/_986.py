"""_986.py

FaceGearSetDesign
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.face import (
    _987, _988, _985, _980,
    _982
)
from mastapy.gears.gear_designs import _941
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Face', 'FaceGearSetDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetDesign',)


class FaceGearSetDesign(_941.GearSetDesign):
    """FaceGearSetDesign

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearSetDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def module(self) -> 'float':
        """float: 'Module' is the original name of this property."""

        temp = self.wrapped.Module
        return temp

    @module.setter
    def module(self, value: 'float'):
        self.wrapped.Module = float(value) if value else 0.0

    @property
    def nominal_pressure_angle(self) -> 'float':
        """float: 'NominalPressureAngle' is the original name of this property."""

        temp = self.wrapped.NominalPressureAngle
        return temp

    @nominal_pressure_angle.setter
    def nominal_pressure_angle(self, value: 'float'):
        self.wrapped.NominalPressureAngle = float(value) if value else 0.0

    @property
    def normal_base_pitch(self) -> 'float':
        """float: 'NormalBasePitch' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalBasePitch
        return temp

    @property
    def shaft_angle(self) -> 'float':
        """float: 'ShaftAngle' is the original name of this property."""

        temp = self.wrapped.ShaftAngle
        return temp

    @shaft_angle.setter
    def shaft_angle(self, value: 'float'):
        self.wrapped.ShaftAngle = float(value) if value else 0.0

    @property
    def working_normal_pressure_angle(self) -> 'float':
        """float: 'WorkingNormalPressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorkingNormalPressureAngle
        return temp

    @property
    def cylindrical_gear_set_micro_geometry(self) -> '_987.FaceGearSetMicroGeometry':
        """FaceGearSetMicroGeometry: 'CylindricalGearSetMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSetMicroGeometry
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def face_gear(self) -> '_988.FaceGearWheelDesign':
        """FaceGearWheelDesign: 'FaceGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGear
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def pinion(self) -> '_985.FaceGearPinionDesign':
        """FaceGearPinionDesign: 'Pinion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Pinion
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gears(self) -> 'List[_980.FaceGearDesign]':
        """List[FaceGearDesign]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_gears(self) -> 'List[_980.FaceGearDesign]':
        """List[FaceGearDesign]: 'FaceGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_meshes(self) -> 'List[_982.FaceGearMeshDesign]':
        """List[FaceGearMeshDesign]: 'FaceMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceMeshes
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

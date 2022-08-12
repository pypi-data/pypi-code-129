"""_982.py

FaceGearMeshDesign
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.face import _986, _980
from mastapy.gears.gear_designs import _940
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Face', 'FaceGearMeshDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearMeshDesign',)


class FaceGearMeshDesign(_940.GearMeshDesign):
    """FaceGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearMeshDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def offset(self) -> 'float':
        """float: 'Offset' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Offset
        return temp

    @property
    def working_normal_pressure_angle(self) -> 'float':
        """float: 'WorkingNormalPressureAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WorkingNormalPressureAngle
        return temp

    @property
    def face_gear_set(self) -> '_986.FaceGearSetDesign':
        """FaceGearSetDesign: 'FaceGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearSet
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def face_gears(self) -> 'List[_980.FaceGearDesign]':
        """List[FaceGearDesign]: 'FaceGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

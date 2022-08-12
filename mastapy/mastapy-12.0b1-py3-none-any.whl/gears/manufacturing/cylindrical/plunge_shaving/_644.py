"""_644.py

RealPlungeShaverOutputs
"""


from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears.manufacturing.cylindrical.plunge_shaving import _635, _641
from mastapy.gears.manufacturing.cylindrical import _603
from mastapy.gears.manufacturing.cylindrical.cutters import _700
from mastapy._internal.python_net import python_net_import

_REAL_PLUNGE_SHAVER_OUTPUTS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.PlungeShaving', 'RealPlungeShaverOutputs')


__docformat__ = 'restructuredtext en'
__all__ = ('RealPlungeShaverOutputs',)


class RealPlungeShaverOutputs(_641.PlungeShaverOutputs):
    """RealPlungeShaverOutputs

    This is a mastapy class.
    """

    TYPE = _REAL_PLUNGE_SHAVER_OUTPUTS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RealPlungeShaverOutputs.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def face_width(self) -> 'float':
        """float: 'FaceWidth' is the original name of this property."""

        temp = self.wrapped.FaceWidth
        return temp

    @face_width.setter
    def face_width(self, value: 'float'):
        self.wrapped.FaceWidth = float(value) if value else 0.0

    @property
    def highest_shaver_tip_diameter(self) -> 'float':
        """float: 'HighestShaverTipDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HighestShaverTipDiameter
        return temp

    @property
    def lead_measurement_method(self) -> '_635.MicroGeometryDefinitionMethod':
        """MicroGeometryDefinitionMethod: 'LeadMeasurementMethod' is the original name of this property."""

        temp = self.wrapped.LeadMeasurementMethod
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_635.MicroGeometryDefinitionMethod)(value) if value is not None else None

    @lead_measurement_method.setter
    def lead_measurement_method(self, value: '_635.MicroGeometryDefinitionMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.LeadMeasurementMethod = value

    @property
    def lowest_shaver_tip_diameter(self) -> 'float':
        """float: 'LowestShaverTipDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LowestShaverTipDiameter
        return temp

    @property
    def profile_measurement_method(self) -> '_635.MicroGeometryDefinitionMethod':
        """MicroGeometryDefinitionMethod: 'ProfileMeasurementMethod' is the original name of this property."""

        temp = self.wrapped.ProfileMeasurementMethod
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_635.MicroGeometryDefinitionMethod)(value) if value is not None else None

    @profile_measurement_method.setter
    def profile_measurement_method(self, value: '_635.MicroGeometryDefinitionMethod'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.ProfileMeasurementMethod = value

    @property
    def specify_face_width(self) -> 'bool':
        """bool: 'SpecifyFaceWidth' is the original name of this property."""

        temp = self.wrapped.SpecifyFaceWidth
        return temp

    @specify_face_width.setter
    def specify_face_width(self, value: 'bool'):
        self.wrapped.SpecifyFaceWidth = bool(value) if value else False

    @property
    def left_flank_micro_geometry(self) -> '_603.CylindricalGearSpecifiedMicroGeometry':
        """CylindricalGearSpecifiedMicroGeometry: 'LeftFlankMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlankMicroGeometry
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def right_flank_micro_geometry(self) -> '_603.CylindricalGearSpecifiedMicroGeometry':
        """CylindricalGearSpecifiedMicroGeometry: 'RightFlankMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlankMicroGeometry
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shaver(self) -> '_700.CylindricalGearPlungeShaver':
        """CylindricalGearPlungeShaver: 'Shaver' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Shaver
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def micro_geometry(self) -> 'List[_603.CylindricalGearSpecifiedMicroGeometry]':
        """List[CylindricalGearSpecifiedMicroGeometry]: 'MicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicroGeometry
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def calculate_micro_geometry(self):
        """ 'CalculateMicroGeometry' is the original name of this method."""

        self.wrapped.CalculateMicroGeometry()

    def face_width_requires_calculation(self):
        """ 'FaceWidthRequiresCalculation' is the original name of this method."""

        self.wrapped.FaceWidthRequiresCalculation()

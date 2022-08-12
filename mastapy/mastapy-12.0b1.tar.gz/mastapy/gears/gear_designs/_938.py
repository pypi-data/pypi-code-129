"""_938.py

GearDesign
"""


from mastapy._internal import constructor
from mastapy.gears.fe_model import _1185
from mastapy.gears.fe_model.cylindrical import _1189
from mastapy._internal.cast_exception import CastException
from mastapy.gears.fe_model.conical import _1192
from mastapy.gears.gear_designs import _939
from mastapy._internal.python_net import python_net_import

_GEAR_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns', 'GearDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('GearDesign',)


class GearDesign(_939.GearDesignComponent):
    """GearDesign

    This is a mastapy class.
    """

    TYPE = _GEAR_DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def absolute_shaft_inner_diameter(self) -> 'float':
        """float: 'AbsoluteShaftInnerDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AbsoluteShaftInnerDiameter
        return temp

    @property
    def face_width(self) -> 'float':
        """float: 'FaceWidth' is the original name of this property."""

        temp = self.wrapped.FaceWidth
        return temp

    @face_width.setter
    def face_width(self, value: 'float'):
        self.wrapped.FaceWidth = float(value) if value else 0.0

    @property
    def mass(self) -> 'float':
        """float: 'Mass' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Mass
        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name
        return temp

    @property
    def names_of_meshing_gears(self) -> 'str':
        """str: 'NamesOfMeshingGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NamesOfMeshingGears
        return temp

    @property
    def number_of_teeth(self) -> 'int':
        """int: 'NumberOfTeeth' is the original name of this property."""

        temp = self.wrapped.NumberOfTeeth
        return temp

    @number_of_teeth.setter
    def number_of_teeth(self, value: 'int'):
        self.wrapped.NumberOfTeeth = int(value) if value else 0

    @property
    def number_of_teeth_maintaining_ratio(self) -> 'int':
        """int: 'NumberOfTeethMaintainingRatio' is the original name of this property."""

        temp = self.wrapped.NumberOfTeethMaintainingRatio
        return temp

    @number_of_teeth_maintaining_ratio.setter
    def number_of_teeth_maintaining_ratio(self, value: 'int'):
        self.wrapped.NumberOfTeethMaintainingRatio = int(value) if value else 0

    @property
    def shaft_inner_diameter(self) -> 'float':
        """float: 'ShaftInnerDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftInnerDiameter
        return temp

    @property
    def shaft_outer_diameter(self) -> 'float':
        """float: 'ShaftOuterDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftOuterDiameter
        return temp

    @property
    def tifffe_model(self) -> '_1185.GearFEModel':
        """GearFEModel: 'TIFFFEModel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TIFFFEModel
        if _1185.GearFEModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast tifffe_model to GearFEModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def tifffe_model_of_type_cylindrical_gear_fe_model(self) -> '_1189.CylindricalGearFEModel':
        """CylindricalGearFEModel: 'TIFFFEModel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TIFFFEModel
        if _1189.CylindricalGearFEModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast tifffe_model to CylindricalGearFEModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def tifffe_model_of_type_conical_gear_fe_model(self) -> '_1192.ConicalGearFEModel':
        """ConicalGearFEModel: 'TIFFFEModel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TIFFFEModel
        if _1192.ConicalGearFEModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast tifffe_model to ConicalGearFEModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

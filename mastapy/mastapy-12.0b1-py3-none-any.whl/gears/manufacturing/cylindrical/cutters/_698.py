"""_698.py

CylindricalGearGrindingWorm
"""


from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical.cutters.tangibles import _720, _715, _718
from mastapy._internal.cast_exception import CastException
from mastapy.gears.manufacturing.cylindrical.cutters import _702
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_GRINDING_WORM = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters', 'CylindricalGearGrindingWorm')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearGrindingWorm',)


class CylindricalGearGrindingWorm(_702.CylindricalGearRackDesign):
    """CylindricalGearGrindingWorm

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_GRINDING_WORM

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearGrindingWorm.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def edge_height(self) -> 'float':
        """float: 'EdgeHeight' is the original name of this property."""

        temp = self.wrapped.EdgeHeight
        return temp

    @edge_height.setter
    def edge_height(self, value: 'float'):
        self.wrapped.EdgeHeight = float(value) if value else 0.0

    @property
    def flat_tip_width(self) -> 'float':
        """float: 'FlatTipWidth' is the original name of this property."""

        temp = self.wrapped.FlatTipWidth
        return temp

    @flat_tip_width.setter
    def flat_tip_width(self, value: 'float'):
        self.wrapped.FlatTipWidth = float(value) if value else 0.0

    @property
    def has_tolerances(self) -> 'bool':
        """bool: 'HasTolerances' is the original name of this property."""

        temp = self.wrapped.HasTolerances
        return temp

    @has_tolerances.setter
    def has_tolerances(self, value: 'bool'):
        self.wrapped.HasTolerances = bool(value) if value else False

    @property
    def nominal_rack_shape(self) -> '_720.RackShape':
        """RackShape: 'NominalRackShape' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalRackShape
        if _720.RackShape.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast nominal_rack_shape to RackShape. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def nominal_rack_shape_of_type_cylindrical_gear_hob_shape(self) -> '_715.CylindricalGearHobShape':
        """CylindricalGearHobShape: 'NominalRackShape' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalRackShape
        if _715.CylindricalGearHobShape.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast nominal_rack_shape to CylindricalGearHobShape. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def nominal_rack_shape_of_type_cylindrical_gear_worm_grinder_shape(self) -> '_718.CylindricalGearWormGrinderShape':
        """CylindricalGearWormGrinderShape: 'NominalRackShape' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalRackShape
        if _718.CylindricalGearWormGrinderShape.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast nominal_rack_shape to CylindricalGearWormGrinderShape. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def nominal_worm_grinder_shape(self) -> '_718.CylindricalGearWormGrinderShape':
        """CylindricalGearWormGrinderShape: 'NominalWormGrinderShape' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NominalWormGrinderShape
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

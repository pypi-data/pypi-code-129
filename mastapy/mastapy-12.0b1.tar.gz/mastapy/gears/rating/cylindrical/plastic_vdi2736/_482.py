"""_482.py

PlasticGearVDI2736AbstractMeshSingleFlankRating
"""


from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears.gear_designs.cylindrical import _1077
from mastapy.gears.rating.cylindrical.plastic_vdi2736 import _481
from mastapy.gears.rating.cylindrical.iso6336 import _508
from mastapy._internal.python_net import python_net_import

_PLASTIC_GEAR_VDI2736_ABSTRACT_MESH_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.PlasticVDI2736', 'PlasticGearVDI2736AbstractMeshSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('PlasticGearVDI2736AbstractMeshSingleFlankRating',)


class PlasticGearVDI2736AbstractMeshSingleFlankRating(_508.ISO6336AbstractMeshSingleFlankRating):
    """PlasticGearVDI2736AbstractMeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _PLASTIC_GEAR_VDI2736_ABSTRACT_MESH_SINGLE_FLANK_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'PlasticGearVDI2736AbstractMeshSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def air_temperature_ambient_and_assembly(self) -> 'float':
        """float: 'AirTemperatureAmbientAndAssembly' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AirTemperatureAmbientAndAssembly
        return temp

    @property
    def coefficient_of_friction(self) -> 'float':
        """float: 'CoefficientOfFriction' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoefficientOfFriction
        return temp

    @property
    def degree_of_tooth_loss(self) -> 'float':
        """float: 'DegreeOfToothLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DegreeOfToothLoss
        return temp

    @property
    def face_load_factor_bending(self) -> 'float':
        """float: 'FaceLoadFactorBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceLoadFactorBending
        return temp

    @property
    def face_load_factor_contact(self) -> 'float':
        """float: 'FaceLoadFactorContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceLoadFactorContact
        return temp

    @property
    def factor_for_tooth_flank_loading(self) -> 'float':
        """float: 'FactorForToothFlankLoading' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FactorForToothFlankLoading
        return temp

    @property
    def factor_for_tooth_root_load(self) -> 'float':
        """float: 'FactorForToothRootLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FactorForToothRootLoad
        return temp

    @property
    def heat_dissipating_surface_of_housing(self) -> 'float':
        """float: 'HeatDissipatingSurfaceOfHousing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HeatDissipatingSurfaceOfHousing
        return temp

    @property
    def heat_transfer_resistance_of_housing(self) -> 'float':
        """float: 'HeatTransferResistanceOfHousing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HeatTransferResistanceOfHousing
        return temp

    @property
    def helix_angle_factor_contact(self) -> 'float':
        """float: 'HelixAngleFactorContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HelixAngleFactorContact
        return temp

    @property
    def percentage_of_openings_in_the_housing_surface(self) -> 'float':
        """float: 'PercentageOfOpeningsInTheHousingSurface' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PercentageOfOpeningsInTheHousingSurface
        return temp

    @property
    def rating_standard_name(self) -> 'str':
        """str: 'RatingStandardName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RatingStandardName
        return temp

    @property
    def relative_tooth_engagement_time(self) -> 'float':
        """float: 'RelativeToothEngagementTime' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RelativeToothEngagementTime
        return temp

    @property
    def transverse_load_factor_bending(self) -> 'float':
        """float: 'TransverseLoadFactorBending' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseLoadFactorBending
        return temp

    @property
    def transverse_load_factor_contact(self) -> 'float':
        """float: 'TransverseLoadFactorContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseLoadFactorContact
        return temp

    @property
    def type_of_mechanism_housing(self) -> '_1077.TypeOfMechanismHousing':
        """TypeOfMechanismHousing: 'TypeOfMechanismHousing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TypeOfMechanismHousing
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1077.TypeOfMechanismHousing)(value) if value is not None else None

    @property
    def wear_coefficient(self) -> 'float':
        """float: 'WearCoefficient' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WearCoefficient
        return temp

    @property
    def isodin_cylindrical_gear_single_flank_ratings(self) -> 'List[_481.PlasticGearVDI2736AbstractGearSingleFlankRating]':
        """List[PlasticGearVDI2736AbstractGearSingleFlankRating]: 'ISODINCylindricalGearSingleFlankRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ISODINCylindricalGearSingleFlankRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def plastic_vdi2736_cylindrical_gear_single_flank_ratings(self) -> 'List[_481.PlasticGearVDI2736AbstractGearSingleFlankRating]':
        """List[PlasticGearVDI2736AbstractGearSingleFlankRating]: 'PlasticVDI2736CylindricalGearSingleFlankRatings' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PlasticVDI2736CylindricalGearSingleFlankRatings
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

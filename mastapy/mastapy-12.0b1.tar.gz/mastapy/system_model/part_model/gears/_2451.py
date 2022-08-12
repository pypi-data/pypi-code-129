"""_2451.py

ActiveGearSetDesignSelectionGroup
"""


from mastapy._internal import constructor
from mastapy.system_model.part_model.configurations import _2556
from mastapy.system_model.part_model.gears import _2450, _2471
from mastapy.gears.gear_designs import _941
from mastapy._internal.python_net import python_net_import

_ACTIVE_GEAR_SET_DESIGN_SELECTION_GROUP = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'ActiveGearSetDesignSelectionGroup')


__docformat__ = 'restructuredtext en'
__all__ = ('ActiveGearSetDesignSelectionGroup',)


class ActiveGearSetDesignSelectionGroup(_2556.PartDetailConfiguration['_2450.ActiveGearSetDesignSelection', '_2471.GearSet', '_941.GearSetDesign']):
    """ActiveGearSetDesignSelectionGroup

    This is a mastapy class.
    """

    TYPE = _ACTIVE_GEAR_SET_DESIGN_SELECTION_GROUP

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ActiveGearSetDesignSelectionGroup.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_contact_ratio_rating_for_nvh(self) -> 'float':
        """float: 'AxialContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialContactRatioRatingForNVH
        return temp

    @property
    def face_width_of_widest_cylindrical_gear(self) -> 'float':
        """float: 'FaceWidthOfWidestCylindricalGear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceWidthOfWidestCylindricalGear
        return temp

    @property
    def minimum_cylindrical_axial_contact_ratio(self) -> 'float':
        """float: 'MinimumCylindricalAxialContactRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumCylindricalAxialContactRatio
        return temp

    @property
    def minimum_cylindrical_transverse_contact_ratio(self) -> 'float':
        """float: 'MinimumCylindricalTransverseContactRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumCylindricalTransverseContactRatio
        return temp

    @property
    def minimum_tip_thickness(self) -> 'float':
        """float: 'MinimumTipThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumTipThickness
        return temp

    @property
    def simple_mass_of_cylindrical_gears(self) -> 'float':
        """float: 'SimpleMassOfCylindricalGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SimpleMassOfCylindricalGears
        return temp

    @property
    def total_face_width_of_cylindrical_gears(self) -> 'float':
        """float: 'TotalFaceWidthOfCylindricalGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TotalFaceWidthOfCylindricalGears
        return temp

    @property
    def transverse_contact_ratio_rating_for_nvh(self) -> 'float':
        """float: 'TransverseContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseContactRatioRatingForNVH
        return temp

    @property
    def transverse_and_axial_contact_ratio_rating_for_nvh(self) -> 'float':
        """float: 'TransverseAndAxialContactRatioRatingForNVH' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseAndAxialContactRatioRatingForNVH
        return temp

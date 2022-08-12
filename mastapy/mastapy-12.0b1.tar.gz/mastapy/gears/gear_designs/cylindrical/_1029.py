"""_1029.py

CylindricalMeshedGearFlank
"""


from mastapy._internal import constructor
from mastapy.utility_gui.charts import (
    _1815, _1805, _1810, _1812
)
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.cylindrical import _1016
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MESHED_GEAR_FLANK = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'CylindricalMeshedGearFlank')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalMeshedGearFlank',)


class CylindricalMeshedGearFlank(_0.APIBase):
    """CylindricalMeshedGearFlank

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MESHED_GEAR_FLANK

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalMeshedGearFlank.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def clearance_from_form_diameter_to_sap_diameter(self) -> 'float':
        """float: 'ClearanceFromFormDiameterToSAPDiameter' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ClearanceFromFormDiameterToSAPDiameter
        return temp

    @property
    def dedendum_path_of_contact(self) -> 'float':
        """float: 'DedendumPathOfContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DedendumPathOfContact
        return temp

    @property
    def flank_name(self) -> 'str':
        """str: 'FlankName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlankName
        return temp

    @property
    def form_over_dimension(self) -> 'float':
        """float: 'FormOverDimension' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FormOverDimension
        return temp

    @property
    def length_of_addendum_path_of_contact(self) -> 'float':
        """float: 'LengthOfAddendumPathOfContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LengthOfAddendumPathOfContact
        return temp

    @property
    def load_direction_angle(self) -> 'float':
        """float: 'LoadDirectionAngle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadDirectionAngle
        return temp

    @property
    def partial_contact_ratio(self) -> 'float':
        """float: 'PartialContactRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PartialContactRatio
        return temp

    @property
    def profile_line_length_of_the_active_tooth_flank(self) -> 'float':
        """float: 'ProfileLineLengthOfTheActiveToothFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ProfileLineLengthOfTheActiveToothFlank
        return temp

    @property
    def sliding_factor_at_tooth_tip(self) -> 'float':
        """float: 'SlidingFactorAtToothTip' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingFactorAtToothTip
        return temp

    @property
    def specific_sliding_at_eap(self) -> 'float':
        """float: 'SpecificSlidingAtEAP' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpecificSlidingAtEAP
        return temp

    @property
    def specific_sliding_at_sap(self) -> 'float':
        """float: 'SpecificSlidingAtSAP' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpecificSlidingAtSAP
        return temp

    @property
    def specific_sliding_chart(self) -> '_1815.TwoDChartDefinition':
        """TwoDChartDefinition: 'SpecificSlidingChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SpecificSlidingChart
        if _1815.TwoDChartDefinition.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast specific_sliding_chart to TwoDChartDefinition. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def end_of_active_profile(self) -> '_1016.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'EndOfActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EndOfActiveProfile
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def highest_point_of_fewest_tooth_contacts(self) -> '_1016.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'HighestPointOfFewestToothContacts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.HighestPointOfFewestToothContacts
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def lowest_point_of_fewest_tooth_contacts(self) -> '_1016.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'LowestPointOfFewestToothContacts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LowestPointOfFewestToothContacts
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def start_of_active_profile(self) -> '_1016.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'StartOfActiveProfile' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StartOfActiveProfile
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

"""_1896.py

LoadedBearingDutyCycle
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_designs import (
    _2073, _2074, _2075, _2076,
    _2077
)
from mastapy._internal.cast_exception import CastException
from mastapy.bearings.bearing_designs.rolling import (
    _2078, _2079, _2080, _2081,
    _2082, _2083, _2085, _2091,
    _2092, _2093, _2097, _2102,
    _2103, _2104, _2105, _2108,
    _2109, _2112, _2113, _2114,
    _2115, _2116, _2117
)
from mastapy.bearings.bearing_designs.fluid_film import (
    _2130, _2132, _2134, _2136,
    _2137, _2138
)
from mastapy.bearings.bearing_designs.concept import _2140, _2141, _2142
from mastapy.utility.property import _1794
from mastapy.bearings import _1824
from mastapy.bearings.bearing_results import _1897
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_LOADED_BEARING_DUTY_CYCLE = python_net_import('SMT.MastaAPI.Bearings.BearingResults', 'LoadedBearingDutyCycle')


__docformat__ = 'restructuredtext en'
__all__ = ('LoadedBearingDutyCycle',)


class LoadedBearingDutyCycle(_0.APIBase):
    """LoadedBearingDutyCycle

    This is a mastapy class.
    """

    TYPE = _LOADED_BEARING_DUTY_CYCLE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'LoadedBearingDutyCycle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def duration(self) -> 'float':
        """float: 'Duration' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Duration
        return temp

    @property
    def duty_cycle_name(self) -> 'str':
        """str: 'DutyCycleName' is the original name of this property."""

        temp = self.wrapped.DutyCycleName
        return temp

    @duty_cycle_name.setter
    def duty_cycle_name(self, value: 'str'):
        self.wrapped.DutyCycleName = str(value) if value else ''

    @property
    def bearing_design(self) -> '_2073.BearingDesign':
        """BearingDesign: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2073.BearingDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to BearingDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_detailed_bearing(self) -> '_2074.DetailedBearing':
        """DetailedBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2074.DetailedBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to DetailedBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_dummy_rolling_bearing(self) -> '_2075.DummyRollingBearing':
        """DummyRollingBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2075.DummyRollingBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to DummyRollingBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_linear_bearing(self) -> '_2076.LinearBearing':
        """LinearBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2076.LinearBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to LinearBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_non_linear_bearing(self) -> '_2077.NonLinearBearing':
        """NonLinearBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2077.NonLinearBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to NonLinearBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_angular_contact_ball_bearing(self) -> '_2078.AngularContactBallBearing':
        """AngularContactBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2078.AngularContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to AngularContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_angular_contact_thrust_ball_bearing(self) -> '_2079.AngularContactThrustBallBearing':
        """AngularContactThrustBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2079.AngularContactThrustBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to AngularContactThrustBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_asymmetric_spherical_roller_bearing(self) -> '_2080.AsymmetricSphericalRollerBearing':
        """AsymmetricSphericalRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2080.AsymmetricSphericalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to AsymmetricSphericalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_axial_thrust_cylindrical_roller_bearing(self) -> '_2081.AxialThrustCylindricalRollerBearing':
        """AxialThrustCylindricalRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2081.AxialThrustCylindricalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to AxialThrustCylindricalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_axial_thrust_needle_roller_bearing(self) -> '_2082.AxialThrustNeedleRollerBearing':
        """AxialThrustNeedleRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2082.AxialThrustNeedleRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to AxialThrustNeedleRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_ball_bearing(self) -> '_2083.BallBearing':
        """BallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2083.BallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to BallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_barrel_roller_bearing(self) -> '_2085.BarrelRollerBearing':
        """BarrelRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2085.BarrelRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to BarrelRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_crossed_roller_bearing(self) -> '_2091.CrossedRollerBearing':
        """CrossedRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2091.CrossedRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to CrossedRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_cylindrical_roller_bearing(self) -> '_2092.CylindricalRollerBearing':
        """CylindricalRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2092.CylindricalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to CylindricalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_deep_groove_ball_bearing(self) -> '_2093.DeepGrooveBallBearing':
        """DeepGrooveBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2093.DeepGrooveBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to DeepGrooveBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_four_point_contact_ball_bearing(self) -> '_2097.FourPointContactBallBearing':
        """FourPointContactBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2097.FourPointContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to FourPointContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_multi_point_contact_ball_bearing(self) -> '_2102.MultiPointContactBallBearing':
        """MultiPointContactBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2102.MultiPointContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to MultiPointContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_needle_roller_bearing(self) -> '_2103.NeedleRollerBearing':
        """NeedleRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2103.NeedleRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to NeedleRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_non_barrel_roller_bearing(self) -> '_2104.NonBarrelRollerBearing':
        """NonBarrelRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2104.NonBarrelRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to NonBarrelRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_roller_bearing(self) -> '_2105.RollerBearing':
        """RollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2105.RollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to RollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_rolling_bearing(self) -> '_2108.RollingBearing':
        """RollingBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2108.RollingBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to RollingBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_self_aligning_ball_bearing(self) -> '_2109.SelfAligningBallBearing':
        """SelfAligningBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2109.SelfAligningBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to SelfAligningBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_spherical_roller_bearing(self) -> '_2112.SphericalRollerBearing':
        """SphericalRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2112.SphericalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to SphericalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_spherical_roller_thrust_bearing(self) -> '_2113.SphericalRollerThrustBearing':
        """SphericalRollerThrustBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2113.SphericalRollerThrustBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to SphericalRollerThrustBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_taper_roller_bearing(self) -> '_2114.TaperRollerBearing':
        """TaperRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2114.TaperRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to TaperRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_three_point_contact_ball_bearing(self) -> '_2115.ThreePointContactBallBearing':
        """ThreePointContactBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2115.ThreePointContactBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to ThreePointContactBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_thrust_ball_bearing(self) -> '_2116.ThrustBallBearing':
        """ThrustBallBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2116.ThrustBallBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to ThrustBallBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_toroidal_roller_bearing(self) -> '_2117.ToroidalRollerBearing':
        """ToroidalRollerBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2117.ToroidalRollerBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to ToroidalRollerBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_pad_fluid_film_bearing(self) -> '_2130.PadFluidFilmBearing':
        """PadFluidFilmBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2130.PadFluidFilmBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to PadFluidFilmBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_plain_grease_filled_journal_bearing(self) -> '_2132.PlainGreaseFilledJournalBearing':
        """PlainGreaseFilledJournalBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2132.PlainGreaseFilledJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to PlainGreaseFilledJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_plain_journal_bearing(self) -> '_2134.PlainJournalBearing':
        """PlainJournalBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2134.PlainJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to PlainJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_plain_oil_fed_journal_bearing(self) -> '_2136.PlainOilFedJournalBearing':
        """PlainOilFedJournalBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2136.PlainOilFedJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to PlainOilFedJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_tilting_pad_journal_bearing(self) -> '_2137.TiltingPadJournalBearing':
        """TiltingPadJournalBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2137.TiltingPadJournalBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to TiltingPadJournalBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_tilting_pad_thrust_bearing(self) -> '_2138.TiltingPadThrustBearing':
        """TiltingPadThrustBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2138.TiltingPadThrustBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to TiltingPadThrustBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_concept_axial_clearance_bearing(self) -> '_2140.ConceptAxialClearanceBearing':
        """ConceptAxialClearanceBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2140.ConceptAxialClearanceBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to ConceptAxialClearanceBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_concept_clearance_bearing(self) -> '_2141.ConceptClearanceBearing':
        """ConceptClearanceBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2141.ConceptClearanceBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to ConceptClearanceBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bearing_design_of_type_concept_radial_clearance_bearing(self) -> '_2142.ConceptRadialClearanceBearing':
        """ConceptRadialClearanceBearing: 'BearingDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingDesign
        if _2142.ConceptRadialClearanceBearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast bearing_design to ConceptRadialClearanceBearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def radial_load_summary(self) -> '_1794.DutyCyclePropertySummaryForce[_1824.BearingLoadCaseResultsLightweight]':
        """DutyCyclePropertySummaryForce[BearingLoadCaseResultsLightweight]: 'RadialLoadSummary' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadialLoadSummary
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1824.BearingLoadCaseResultsLightweight](temp) if temp is not None else None

    @property
    def z_thrust_reaction_summary(self) -> '_1794.DutyCyclePropertySummaryForce[_1824.BearingLoadCaseResultsLightweight]':
        """DutyCyclePropertySummaryForce[BearingLoadCaseResultsLightweight]: 'ZThrustReactionSummary' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ZThrustReactionSummary
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)[_1824.BearingLoadCaseResultsLightweight](temp) if temp is not None else None

    @property
    def bearing_load_case_results(self) -> 'List[_1897.LoadedBearingResults]':
        """List[LoadedBearingResults]: 'BearingLoadCaseResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BearingLoadCaseResults
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def report_names(self) -> 'List[str]':
        """List[str]: 'ReportNames' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ReportNames
        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value

    def output_default_report_to(self, file_path: 'str'):
        """ 'OutputDefaultReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputDefaultReportTo(file_path if file_path else '')

    def get_default_report_with_encoded_images(self) -> 'str':
        """ 'GetDefaultReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetDefaultReportWithEncodedImages()
        return method_result

    def output_active_report_to(self, file_path: 'str'):
        """ 'OutputActiveReportTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportTo(file_path if file_path else '')

    def output_active_report_as_text_to(self, file_path: 'str'):
        """ 'OutputActiveReportAsTextTo' is the original name of this method.

        Args:
            file_path (str)
        """

        file_path = str(file_path)
        self.wrapped.OutputActiveReportAsTextTo(file_path if file_path else '')

    def get_active_report_with_encoded_images(self) -> 'str':
        """ 'GetActiveReportWithEncodedImages' is the original name of this method.

        Returns:
            str
        """

        method_result = self.wrapped.GetActiveReportWithEncodedImages()
        return method_result

    def output_named_report_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportTo(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_masta_report(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsMastaReport' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsMastaReport(report_name if report_name else '', file_path if file_path else '')

    def output_named_report_as_text_to(self, report_name: 'str', file_path: 'str'):
        """ 'OutputNamedReportAsTextTo' is the original name of this method.

        Args:
            report_name (str)
            file_path (str)
        """

        report_name = str(report_name)
        file_path = str(file_path)
        self.wrapped.OutputNamedReportAsTextTo(report_name if report_name else '', file_path if file_path else '')

    def get_named_report_with_encoded_images(self, report_name: 'str') -> 'str':
        """ 'GetNamedReportWithEncodedImages' is the original name of this method.

        Args:
            report_name (str)

        Returns:
            str
        """

        report_name = str(report_name)
        method_result = self.wrapped.GetNamedReportWithEncodedImages(report_name if report_name else '')
        return method_result

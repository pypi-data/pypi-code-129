"""_849.py

CylindricalGearMeshLoadedContactPoint
"""


from mastapy._internal import constructor
from mastapy.gears.gear_designs.cylindrical import _1016
from mastapy.gears.rating.cylindrical.iso6336 import _516
from mastapy.gears.ltca import _834
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_LOADED_CONTACT_POINT = python_net_import('SMT.MastaAPI.Gears.LTCA.Cylindrical', 'CylindricalGearMeshLoadedContactPoint')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMeshLoadedContactPoint',)


class CylindricalGearMeshLoadedContactPoint(_834.GearMeshLoadedContactPoint):
    """CylindricalGearMeshLoadedContactPoint

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_LOADED_CONTACT_POINT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearMeshLoadedContactPoint.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def coefficient_of_friction_benedict_and_kelley(self) -> 'float':
        """float: 'CoefficientOfFrictionBenedictAndKelley' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CoefficientOfFrictionBenedictAndKelley
        return temp

    @property
    def depth_of_maximum_material_exposure_gear_aiso633642019(self) -> 'float':
        """float: 'DepthOfMaximumMaterialExposureGearAISO633642019' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DepthOfMaximumMaterialExposureGearAISO633642019
        return temp

    @property
    def depth_of_maximum_material_exposure_gear_biso633642019(self) -> 'float':
        """float: 'DepthOfMaximumMaterialExposureGearBISO633642019' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.DepthOfMaximumMaterialExposureGearBISO633642019
        return temp

    @property
    def face_width_position_gear_a(self) -> 'float':
        """float: 'FaceWidthPositionGearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceWidthPositionGearA
        return temp

    @property
    def face_width_position_gear_b(self) -> 'float':
        """float: 'FaceWidthPositionGearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceWidthPositionGearB
        return temp

    @property
    def is_gear_a_tip_contact_point(self) -> 'bool':
        """bool: 'IsGearATipContactPoint' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsGearATipContactPoint
        return temp

    @property
    def is_gear_b_tip_contact_point(self) -> 'bool':
        """bool: 'IsGearBTipContactPoint' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsGearBTipContactPoint
        return temp

    @property
    def is_tip_contact_point(self) -> 'bool':
        """bool: 'IsTipContactPoint' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IsTipContactPoint
        return temp

    @property
    def maximum_material_exposure_gear_aiso633642019(self) -> 'float':
        """float: 'MaximumMaterialExposureGearAISO633642019' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumMaterialExposureGearAISO633642019
        return temp

    @property
    def maximum_material_exposure_gear_biso633642019(self) -> 'float':
        """float: 'MaximumMaterialExposureGearBISO633642019' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumMaterialExposureGearBISO633642019
        return temp

    @property
    def micropitting_contact_temperature(self) -> 'float':
        """float: 'MicropittingContactTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicropittingContactTemperature
        return temp

    @property
    def micropitting_flash_temperature(self) -> 'float':
        """float: 'MicropittingFlashTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicropittingFlashTemperature
        return temp

    @property
    def micropitting_minimum_lubricant_film_thickness(self) -> 'float':
        """float: 'MicropittingMinimumLubricantFilmThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicropittingMinimumLubricantFilmThickness
        return temp

    @property
    def micropitting_safety_factor(self) -> 'float':
        """float: 'MicropittingSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicropittingSafetyFactor
        return temp

    @property
    def micropitting_specific_lubricant_film_thickness(self) -> 'float':
        """float: 'MicropittingSpecificLubricantFilmThickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MicropittingSpecificLubricantFilmThickness
        return temp

    @property
    def pressure_velocity_pv(self) -> 'float':
        """float: 'PressureVelocityPV' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PressureVelocityPV
        return temp

    @property
    def scuffing_contact_temperature(self) -> 'float':
        """float: 'ScuffingContactTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ScuffingContactTemperature
        return temp

    @property
    def scuffing_contact_temperature_agma925a03(self) -> 'float':
        """float: 'ScuffingContactTemperatureAGMA925A03' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ScuffingContactTemperatureAGMA925A03
        return temp

    @property
    def scuffing_contact_temperature_agma925b22(self) -> 'float':
        """float: 'ScuffingContactTemperatureAGMA925B22' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ScuffingContactTemperatureAGMA925B22
        return temp

    @property
    def scuffing_contact_temperature_din399041987(self) -> 'float':
        """float: 'ScuffingContactTemperatureDIN399041987' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ScuffingContactTemperatureDIN399041987
        return temp

    @property
    def scuffing_flash_temperature(self) -> 'float':
        """float: 'ScuffingFlashTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ScuffingFlashTemperature
        return temp

    @property
    def scuffing_flash_temperature_agma925a03(self) -> 'float':
        """float: 'ScuffingFlashTemperatureAGMA925A03' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ScuffingFlashTemperatureAGMA925A03
        return temp

    @property
    def scuffing_flash_temperature_agma925b22(self) -> 'float':
        """float: 'ScuffingFlashTemperatureAGMA925B22' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ScuffingFlashTemperatureAGMA925B22
        return temp

    @property
    def scuffing_flash_temperature_din399041987(self) -> 'float':
        """float: 'ScuffingFlashTemperatureDIN399041987' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ScuffingFlashTemperatureDIN399041987
        return temp

    @property
    def scuffing_safety_factor(self) -> 'float':
        """float: 'ScuffingSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ScuffingSafetyFactor
        return temp

    @property
    def scuffing_safety_factor_agma925a03(self) -> 'float':
        """float: 'ScuffingSafetyFactorAGMA925A03' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ScuffingSafetyFactorAGMA925A03
        return temp

    @property
    def scuffing_safety_factor_agma925b22(self) -> 'float':
        """float: 'ScuffingSafetyFactorAGMA925B22' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ScuffingSafetyFactorAGMA925B22
        return temp

    @property
    def scuffing_safety_factor_din399041987(self) -> 'float':
        """float: 'ScuffingSafetyFactorDIN399041987' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ScuffingSafetyFactorDIN399041987
        return temp

    @property
    def sliding_power_loss(self) -> 'float':
        """float: 'SlidingPowerLoss' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingPowerLoss
        return temp

    @property
    def sliding_velocity(self) -> 'float':
        """float: 'SlidingVelocity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingVelocity
        return temp

    @property
    def gear_a_profile_measurement(self) -> '_1016.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'GearAProfileMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearAProfileMeasurement
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_profile_measurement(self) -> '_1016.CylindricalGearProfileMeasurement':
        """CylindricalGearProfileMeasurement: 'GearBProfileMeasurement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearBProfileMeasurement
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def tooth_flank_fracture_analysis_gear_a(self) -> '_516.ToothFlankFractureAnalysisContactPointMethodA':
        """ToothFlankFractureAnalysisContactPointMethodA: 'ToothFlankFractureAnalysisGearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothFlankFractureAnalysisGearA
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def tooth_flank_fracture_analysis_gear_b(self) -> '_516.ToothFlankFractureAnalysisContactPointMethodA':
        """ToothFlankFractureAnalysisContactPointMethodA: 'ToothFlankFractureAnalysisGearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ToothFlankFractureAnalysisGearB
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

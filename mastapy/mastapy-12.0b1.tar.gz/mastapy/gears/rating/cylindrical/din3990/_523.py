"""_523.py

DIN3990MeshSingleFlankRating
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.gears.rating.cylindrical import _471, _472
from mastapy.gears.rating.cylindrical.iso6336 import _502
from mastapy._internal.python_net import python_net_import

_DIN3990_MESH_SINGLE_FLANK_RATING = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.DIN3990', 'DIN3990MeshSingleFlankRating')


__docformat__ = 'restructuredtext en'
__all__ = ('DIN3990MeshSingleFlankRating',)


class DIN3990MeshSingleFlankRating(_502.ISO63361996MeshSingleFlankRating):
    """DIN3990MeshSingleFlankRating

    This is a mastapy class.
    """

    TYPE = _DIN3990_MESH_SINGLE_FLANK_RATING

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DIN3990MeshSingleFlankRating.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def basic_mean_flash_temperature(self) -> 'float':
        """float: 'BasicMeanFlashTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicMeanFlashTemperature
        return temp

    @property
    def estimated_bulk_temperature_flash(self) -> 'float':
        """float: 'EstimatedBulkTemperatureFlash' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EstimatedBulkTemperatureFlash
        return temp

    @property
    def estimated_bulk_temperature_integral(self) -> 'float':
        """float: 'EstimatedBulkTemperatureIntegral' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EstimatedBulkTemperatureIntegral
        return temp

    @property
    def flash_factor_integral(self) -> 'float':
        """float: 'FlashFactorIntegral' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlashFactorIntegral
        return temp

    @property
    def geometry_factor_at_maximum_flash_temperature(self) -> 'float':
        """float: 'GeometryFactorAtMaximumFlashTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GeometryFactorAtMaximumFlashTemperature
        return temp

    @property
    def integral_scuffing_temperature(self) -> 'float':
        """float: 'IntegralScuffingTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.IntegralScuffingTemperature
        return temp

    @property
    def load_distribution_factor_at_maximum_flash_temperature(self) -> 'float':
        """float: 'LoadDistributionFactorAtMaximumFlashTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadDistributionFactorAtMaximumFlashTemperature
        return temp

    @property
    def mean_coefficient_of_friction_integral_temperature_method(self) -> 'float':
        """float: 'MeanCoefficientOfFrictionIntegralTemperatureMethod' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanCoefficientOfFrictionIntegralTemperatureMethod
        return temp

    @property
    def mean_local_coefficient_of_friction_at_maximum_flash_temperature(self) -> 'float':
        """float: 'MeanLocalCoefficientOfFrictionAtMaximumFlashTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeanLocalCoefficientOfFrictionAtMaximumFlashTemperature
        return temp

    @property
    def parameter_on_line_of_action_at_maximum_flash_temperature(self) -> 'float':
        """float: 'ParameterOnLineOfActionAtMaximumFlashTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ParameterOnLineOfActionAtMaximumFlashTemperature
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
    def resonance_ratio_in_the_main_resonance_range(self) -> 'float':
        """float: 'ResonanceRatioInTheMainResonanceRange' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ResonanceRatioInTheMainResonanceRange
        return temp

    @property
    def scuffing_rating_method_flash_temperature_method(self) -> '_471.ScuffingFlashTemperatureRatingMethod':
        """ScuffingFlashTemperatureRatingMethod: 'ScuffingRatingMethodFlashTemperatureMethod' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ScuffingRatingMethodFlashTemperatureMethod
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_471.ScuffingFlashTemperatureRatingMethod)(value) if value is not None else None

    @property
    def scuffing_rating_method_integral_temperature_method(self) -> '_472.ScuffingIntegralTemperatureRatingMethod':
        """ScuffingIntegralTemperatureRatingMethod: 'ScuffingRatingMethodIntegralTemperatureMethod' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ScuffingRatingMethodIntegralTemperatureMethod
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_472.ScuffingIntegralTemperatureRatingMethod)(value) if value is not None else None

    @property
    def thermo_elastic_factor_at_maximum_flash_temperature(self) -> 'float':
        """float: 'ThermoElasticFactorAtMaximumFlashTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ThermoElasticFactorAtMaximumFlashTemperature
        return temp

    @property
    def tip_relief_factor_integral(self) -> 'float':
        """float: 'TipReliefFactorIntegral' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TipReliefFactorIntegral
        return temp

    @property
    def transverse_unit_load(self) -> 'float':
        """float: 'TransverseUnitLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TransverseUnitLoad
        return temp

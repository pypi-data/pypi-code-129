"""_846.py

CylindricalGearLoadDistributionAnalysis
"""


from mastapy.gears.rating.cylindrical import _451
from mastapy._internal import constructor
from mastapy.gears.gear_two_d_fe_analysis import _888
from mastapy.gears.ltca import _830
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_LOAD_DISTRIBUTION_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.LTCA.Cylindrical', 'CylindricalGearLoadDistributionAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearLoadDistributionAnalysis',)


class CylindricalGearLoadDistributionAnalysis(_830.GearLoadDistributionAnalysis):
    """CylindricalGearLoadDistributionAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_LOAD_DISTRIBUTION_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearLoadDistributionAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self) -> '_451.CylindricalGearRating':
        """CylindricalGearRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def tiff_analysis(self) -> '_888.CylindricalGearTIFFAnalysis':
        """CylindricalGearTIFFAnalysis: 'TIFFAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TIFFAnalysis
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

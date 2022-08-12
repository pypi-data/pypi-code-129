"""_2023.py

BearingRatingLife
"""


from mastapy._internal import constructor
from mastapy.bearings.bearing_results.rolling.skf_module import _2034, _2040
from mastapy._internal.python_net import python_net_import

_BEARING_RATING_LIFE = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule', 'BearingRatingLife')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingRatingLife',)


class BearingRatingLife(_2040.SKFCalculationResult):
    """BearingRatingLife

    This is a mastapy class.
    """

    TYPE = _BEARING_RATING_LIFE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BearingRatingLife.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contamination_factor(self) -> 'float':
        """float: 'ContaminationFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContaminationFactor
        return temp

    @property
    def skf_life_modification_factor(self) -> 'float':
        """float: 'SKFLifeModificationFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SKFLifeModificationFactor
        return temp

    @property
    def life_model(self) -> '_2034.LifeModel':
        """LifeModel: 'LifeModel' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LifeModel
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

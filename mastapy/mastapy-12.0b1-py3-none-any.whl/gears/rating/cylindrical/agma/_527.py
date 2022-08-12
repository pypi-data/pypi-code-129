"""_527.py

ThermalReductionFactorFactorsAndExponents
"""


from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_THERMAL_REDUCTION_FACTOR_FACTORS_AND_EXPONENTS = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.AGMA', 'ThermalReductionFactorFactorsAndExponents')


__docformat__ = 'restructuredtext en'
__all__ = ('ThermalReductionFactorFactorsAndExponents',)


class ThermalReductionFactorFactorsAndExponents(_0.APIBase):
    """ThermalReductionFactorFactorsAndExponents

    This is a mastapy class.
    """

    TYPE = _THERMAL_REDUCTION_FACTOR_FACTORS_AND_EXPONENTS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ThermalReductionFactorFactorsAndExponents.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def first_exponent(self) -> 'float':
        """float: 'FirstExponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FirstExponent
        return temp

    @property
    def first_factor(self) -> 'float':
        """float: 'FirstFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FirstFactor
        return temp

    @property
    def second_exponent(self) -> 'float':
        """float: 'SecondExponent' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SecondExponent
        return temp

    @property
    def second_factor(self) -> 'float':
        """float: 'SecondFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SecondFactor
        return temp

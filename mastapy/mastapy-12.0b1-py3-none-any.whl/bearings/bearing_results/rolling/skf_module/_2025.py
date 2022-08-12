"""_2025.py

Frequencies
"""


from mastapy.bearings.bearing_results.rolling.skf_module import _2026, _2038, _2040
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import

_FREQUENCIES = python_net_import('SMT.MastaAPI.Bearings.BearingResults.Rolling.SkfModule', 'Frequencies')


__docformat__ = 'restructuredtext en'
__all__ = ('Frequencies',)


class Frequencies(_2040.SKFCalculationResult):
    """Frequencies

    This is a mastapy class.
    """

    TYPE = _FREQUENCIES

    __hash__ = None

    def __init__(self, instance_to_wrap: 'Frequencies.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def frequency_of_over_rolling(self) -> '_2026.FrequencyOfOverRolling':
        """FrequencyOfOverRolling: 'FrequencyOfOverRolling' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FrequencyOfOverRolling
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rotational_frequency(self) -> '_2038.RotationalFrequency':
        """RotationalFrequency: 'RotationalFrequency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RotationalFrequency
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

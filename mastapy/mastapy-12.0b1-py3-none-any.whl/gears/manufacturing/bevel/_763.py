"""_763.py

BevelMachineSettingOptimizationResult
"""


from mastapy._internal import constructor
from mastapy.gears.manufacturing.bevel import _764
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_BEVEL_MACHINE_SETTING_OPTIMIZATION_RESULT = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'BevelMachineSettingOptimizationResult')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelMachineSettingOptimizationResult',)


class BevelMachineSettingOptimizationResult(_0.APIBase):
    """BevelMachineSettingOptimizationResult

    This is a mastapy class.
    """

    TYPE = _BEVEL_MACHINE_SETTING_OPTIMIZATION_RESULT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelMachineSettingOptimizationResult.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_absolute_residual(self) -> 'float':
        """float: 'MaximumAbsoluteResidual' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumAbsoluteResidual
        return temp

    @property
    def sum_of_squared_residuals(self) -> 'float':
        """float: 'SumOfSquaredResiduals' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SumOfSquaredResiduals
        return temp

    @property
    def calculated_deviations_concave(self) -> '_764.ConicalFlankDeviationsData':
        """ConicalFlankDeviationsData: 'CalculatedDeviationsConcave' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedDeviationsConcave
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def calculated_deviations_convex(self) -> '_764.ConicalFlankDeviationsData':
        """ConicalFlankDeviationsData: 'CalculatedDeviationsConvex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CalculatedDeviationsConvex
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def imported_deviations_concave(self) -> '_764.ConicalFlankDeviationsData':
        """ConicalFlankDeviationsData: 'ImportedDeviationsConcave' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ImportedDeviationsConcave
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def imported_deviations_convex(self) -> '_764.ConicalFlankDeviationsData':
        """ConicalFlankDeviationsData: 'ImportedDeviationsConvex' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ImportedDeviationsConvex
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

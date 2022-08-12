"""_1074.py

ToothFlankFractureAnalysisSettings
"""


from mastapy.math_utility import _1493
from mastapy._internal import constructor
from mastapy.utility import _1547
from mastapy._internal.python_net import python_net_import

_TOOTH_FLANK_FRACTURE_ANALYSIS_SETTINGS = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Cylindrical', 'ToothFlankFractureAnalysisSettings')


__docformat__ = 'restructuredtext en'
__all__ = ('ToothFlankFractureAnalysisSettings',)


class ToothFlankFractureAnalysisSettings(_1547.IndependentReportablePropertiesBase['ToothFlankFractureAnalysisSettings']):
    """ToothFlankFractureAnalysisSettings

    This is a mastapy class.
    """

    TYPE = _TOOTH_FLANK_FRACTURE_ANALYSIS_SETTINGS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ToothFlankFractureAnalysisSettings.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def measured_residual_stress_profile_property(self) -> '_1493.Vector2DListAccessor':
        """Vector2DListAccessor: 'MeasuredResidualStressProfileProperty' is the original name of this property."""

        temp = self.wrapped.MeasuredResidualStressProfileProperty
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @measured_residual_stress_profile_property.setter
    def measured_residual_stress_profile_property(self, value: '_1493.Vector2DListAccessor'):
        value = value.wrapped if value else None
        self.wrapped.MeasuredResidualStressProfileProperty = value

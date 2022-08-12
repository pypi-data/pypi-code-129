"""_5451.py

DynamicTorqueVector3DResult
"""


from mastapy.system_model.analyses_and_results.mbd_analyses.reporting import _5450
from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_DYNAMIC_TORQUE_VECTOR_3D_RESULT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Reporting', 'DynamicTorqueVector3DResult')


__docformat__ = 'restructuredtext en'
__all__ = ('DynamicTorqueVector3DResult',)


class DynamicTorqueVector3DResult(_0.APIBase):
    """DynamicTorqueVector3DResult

    This is a mastapy class.
    """

    TYPE = _DYNAMIC_TORQUE_VECTOR_3D_RESULT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'DynamicTorqueVector3DResult.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def magnitude(self) -> '_5450.DynamicTorqueResultAtTime':
        """DynamicTorqueResultAtTime: 'Magnitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Magnitude
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def radial_magnitude(self) -> '_5450.DynamicTorqueResultAtTime':
        """DynamicTorqueResultAtTime: 'RadialMagnitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadialMagnitude
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def x(self) -> '_5450.DynamicTorqueResultAtTime':
        """DynamicTorqueResultAtTime: 'X' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.X
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def y(self) -> '_5450.DynamicTorqueResultAtTime':
        """DynamicTorqueResultAtTime: 'Y' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Y
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def z(self) -> '_5450.DynamicTorqueResultAtTime':
        """DynamicTorqueResultAtTime: 'Z' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Z
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

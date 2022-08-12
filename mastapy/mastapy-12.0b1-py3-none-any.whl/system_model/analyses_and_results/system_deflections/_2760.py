"""_2760.py

SystemDeflectionDrawStyle
"""


from mastapy._internal import constructor
from mastapy.system_model.drawing import _2195, _2185
from mastapy._internal.python_net import python_net_import

_SYSTEM_DEFLECTION_DRAW_STYLE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'SystemDeflectionDrawStyle')


__docformat__ = 'restructuredtext en'
__all__ = ('SystemDeflectionDrawStyle',)


class SystemDeflectionDrawStyle(_2185.ContourDrawStyle):
    """SystemDeflectionDrawStyle

    This is a mastapy class.
    """

    TYPE = _SYSTEM_DEFLECTION_DRAW_STYLE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SystemDeflectionDrawStyle.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def show_arrows(self) -> 'bool':
        """bool: 'ShowArrows' is the original name of this property."""

        temp = self.wrapped.ShowArrows
        return temp

    @show_arrows.setter
    def show_arrows(self, value: 'bool'):
        self.wrapped.ShowArrows = bool(value) if value else False

    @property
    def force_arrow_scaling(self) -> '_2195.ScalingDrawStyle':
        """ScalingDrawStyle: 'ForceArrowScaling' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ForceArrowScaling
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

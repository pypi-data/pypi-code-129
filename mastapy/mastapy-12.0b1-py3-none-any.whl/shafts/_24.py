"""_24.py

ShaftMaterial
"""


from mastapy.materials import _239, _260
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import

_SHAFT_MATERIAL = python_net_import('SMT.MastaAPI.Shafts', 'ShaftMaterial')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftMaterial',)


class ShaftMaterial(_260.Material):
    """ShaftMaterial

    This is a mastapy class.
    """

    TYPE = _SHAFT_MATERIAL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShaftMaterial.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bh_curve_specification(self) -> '_239.BHCurveSpecification':
        """BHCurveSpecification: 'BHCurveSpecification' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BHCurveSpecification
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

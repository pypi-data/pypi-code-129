"""_1519.py

ForceAndDisplacementResults
"""


from mastapy.math_utility.measured_vectors import _1523, _1518
from mastapy._internal import constructor
from mastapy._internal.python_net import python_net_import

_FORCE_AND_DISPLACEMENT_RESULTS = python_net_import('SMT.MastaAPI.MathUtility.MeasuredVectors', 'ForceAndDisplacementResults')


__docformat__ = 'restructuredtext en'
__all__ = ('ForceAndDisplacementResults',)


class ForceAndDisplacementResults(_1518.AbstractForceAndDisplacementResults):
    """ForceAndDisplacementResults

    This is a mastapy class.
    """

    TYPE = _FORCE_AND_DISPLACEMENT_RESULTS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ForceAndDisplacementResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def displacement(self) -> '_1523.VectorWithLinearAndAngularComponents':
        """VectorWithLinearAndAngularComponents: 'Displacement' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Displacement
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

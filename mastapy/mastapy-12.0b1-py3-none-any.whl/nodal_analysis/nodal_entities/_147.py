"""_147.py

SurfaceToSurfaceContactStiffnessEntity
"""


from mastapy.math_utility.stiffness_calculators import _1496
from mastapy._internal import constructor
from mastapy.nodal_analysis.nodal_entities import _124
from mastapy._internal.python_net import python_net_import

_SURFACE_TO_SURFACE_CONTACT_STIFFNESS_ENTITY = python_net_import('SMT.MastaAPI.NodalAnalysis.NodalEntities', 'SurfaceToSurfaceContactStiffnessEntity')


__docformat__ = 'restructuredtext en'
__all__ = ('SurfaceToSurfaceContactStiffnessEntity',)


class SurfaceToSurfaceContactStiffnessEntity(_124.ArbitraryNodalComponent):
    """SurfaceToSurfaceContactStiffnessEntity

    This is a mastapy class.
    """

    TYPE = _SURFACE_TO_SURFACE_CONTACT_STIFFNESS_ENTITY

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SurfaceToSurfaceContactStiffnessEntity.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def contact(self) -> '_1496.SurfaceToSurfaceContact':
        """SurfaceToSurfaceContact: 'Contact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Contact
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

"""_774.py

ConicalMeshManufacturingAnalysis
"""


from typing import List

from mastapy.gears.load_case.conical import _877
from mastapy._internal import constructor, conversion
from mastapy.gears.load_case.bevel import _882
from mastapy._internal.cast_exception import CastException
from mastapy.gears.manufacturing.bevel import _785, _769
from mastapy.gears.analysis import _1209
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_MANUFACTURING_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Manufacturing.Bevel', 'ConicalMeshManufacturingAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('ConicalMeshManufacturingAnalysis',)


class ConicalMeshManufacturingAnalysis(_1209.GearMeshImplementationAnalysis):
    """ConicalMeshManufacturingAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_MANUFACTURING_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ConicalMeshManufacturingAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_mesh_load_case(self) -> '_877.ConicalMeshLoadCase':
        """ConicalMeshLoadCase: 'ConicalMeshLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalMeshLoadCase
        if _877.ConicalMeshLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast conical_mesh_load_case to ConicalMeshLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def tca(self) -> '_785.EaseOffBasedTCA':
        """EaseOffBasedTCA: 'TCA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TCA
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def meshed_gears(self) -> 'List[_769.ConicalMeshedGearManufacturingAnalysis]':
        """List[ConicalMeshedGearManufacturingAnalysis]: 'MeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshedGears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

"""_969.py

KlingelnbergCycloPalloidHypoidGearMeshDesign
"""


from typing import List

from mastapy.gears.gear_designs.klingelnberg_hypoid import _970, _968, _971
from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.klingelnberg_conical import _973
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_DESIGN = python_net_import('SMT.MastaAPI.Gears.GearDesigns.KlingelnbergHypoid', 'KlingelnbergCycloPalloidHypoidGearMeshDesign')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidHypoidGearMeshDesign',)


class KlingelnbergCycloPalloidHypoidGearMeshDesign(_973.KlingelnbergConicalGearMeshDesign):
    """KlingelnbergCycloPalloidHypoidGearMeshDesign

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_DESIGN

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidHypoidGearMeshDesign.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_set(self) -> '_970.KlingelnbergCycloPalloidHypoidGearSetDesign':
        """KlingelnbergCycloPalloidHypoidGearSetDesign: 'KlingelnbergCycloPalloidHypoidGearSet' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearSet
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears(self) -> 'List[_968.KlingelnbergCycloPalloidHypoidGearDesign]':
        """List[KlingelnbergCycloPalloidHypoidGearDesign]: 'KlingelnbergCycloPalloidHypoidGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshed_gears(self) -> 'List[_971.KlingelnbergCycloPalloidHypoidMeshedGearDesign]':
        """List[KlingelnbergCycloPalloidHypoidMeshedGearDesign]: 'KlingelnbergCycloPalloidHypoidMeshedGears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergCycloPalloidHypoidMeshedGears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

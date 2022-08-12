"""_2476.py

KlingelnbergCycloPalloidConicalGearSet
"""


from mastapy.gears.gear_designs.klingelnberg_conical import _974
from mastapy._internal import constructor
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _966
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.klingelnberg_hypoid import _970
from mastapy.system_model.part_model.gears import _2463
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET = python_net_import('SMT.MastaAPI.SystemModel.PartModel.Gears', 'KlingelnbergCycloPalloidConicalGearSet')


__docformat__ = 'restructuredtext en'
__all__ = ('KlingelnbergCycloPalloidConicalGearSet',)


class KlingelnbergCycloPalloidConicalGearSet(_2463.ConicalGearSet):
    """KlingelnbergCycloPalloidConicalGearSet

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KlingelnbergCycloPalloidConicalGearSet.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_set_design(self) -> '_974.KlingelnbergConicalGearSetDesign':
        """KlingelnbergConicalGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearSetDesign
        if _974.KlingelnbergConicalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_set_design to KlingelnbergConicalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gear_set_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(self) -> '_966.KlingelnbergCycloPalloidSpiralBevelGearSetDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearSetDesign
        if _966.KlingelnbergCycloPalloidSpiralBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_set_design to KlingelnbergCycloPalloidSpiralBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def conical_gear_set_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_design(self) -> '_970.KlingelnbergCycloPalloidHypoidGearSetDesign':
        """KlingelnbergCycloPalloidHypoidGearSetDesign: 'ConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConicalGearSetDesign
        if _970.KlingelnbergCycloPalloidHypoidGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast conical_gear_set_design to KlingelnbergCycloPalloidHypoidGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def klingelnberg_conical_gear_set_design(self) -> '_974.KlingelnbergConicalGearSetDesign':
        """KlingelnbergConicalGearSetDesign: 'KlingelnbergConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergConicalGearSetDesign
        if _974.KlingelnbergConicalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast klingelnberg_conical_gear_set_design to KlingelnbergConicalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def klingelnberg_conical_gear_set_design_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(self) -> '_966.KlingelnbergCycloPalloidSpiralBevelGearSetDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearSetDesign: 'KlingelnbergConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergConicalGearSetDesign
        if _966.KlingelnbergCycloPalloidSpiralBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast klingelnberg_conical_gear_set_design to KlingelnbergCycloPalloidSpiralBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def klingelnberg_conical_gear_set_design_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_design(self) -> '_970.KlingelnbergCycloPalloidHypoidGearSetDesign':
        """KlingelnbergCycloPalloidHypoidGearSetDesign: 'KlingelnbergConicalGearSetDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.KlingelnbergConicalGearSetDesign
        if _970.KlingelnbergCycloPalloidHypoidGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast klingelnberg_conical_gear_set_design to KlingelnbergCycloPalloidHypoidGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

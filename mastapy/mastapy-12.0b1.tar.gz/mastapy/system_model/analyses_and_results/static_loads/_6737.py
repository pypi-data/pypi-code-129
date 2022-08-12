"""_6737.py

BevelDifferentialGearLoadCase
"""


from mastapy.system_model.part_model.gears import _2454, _2456, _2457
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6742
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'BevelDifferentialGearLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearLoadCase',)


class BevelDifferentialGearLoadCase(_6742.BevelGearLoadCase):
    """BevelDifferentialGearLoadCase

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2454.BevelDifferentialGear':
        """BevelDifferentialGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        if _2454.BevelDifferentialGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to BevelDifferentialGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

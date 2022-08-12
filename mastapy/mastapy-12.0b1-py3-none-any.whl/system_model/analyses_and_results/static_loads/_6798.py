"""_6798.py

FaceGearLoadCase
"""


from mastapy.system_model.part_model.gears import _2467
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6804
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_LOAD_CASE = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'FaceGearLoadCase')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearLoadCase',)


class FaceGearLoadCase(_6804.GearLoadCase):
    """FaceGearLoadCase

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_LOAD_CASE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearLoadCase.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self) -> '_2467.FaceGear':
        """FaceGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

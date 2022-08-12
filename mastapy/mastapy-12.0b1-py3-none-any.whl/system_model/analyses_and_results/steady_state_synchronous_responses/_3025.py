"""_3025.py

SteadyStateSynchronousResponseOptions
"""


from mastapy._internal import constructor
from mastapy._internal.implicit import list_with_selected_item
from mastapy.system_model.part_model import _2412
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_STEADY_STATE_SYNCHRONOUS_RESPONSE_OPTIONS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses', 'SteadyStateSynchronousResponseOptions')


__docformat__ = 'restructuredtext en'
__all__ = ('SteadyStateSynchronousResponseOptions',)


class SteadyStateSynchronousResponseOptions(_0.APIBase):
    """SteadyStateSynchronousResponseOptions

    This is a mastapy class.
    """

    TYPE = _STEADY_STATE_SYNCHRONOUS_RESPONSE_OPTIONS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'SteadyStateSynchronousResponseOptions.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def end_speed(self) -> 'float':
        """float: 'EndSpeed' is the original name of this property."""

        temp = self.wrapped.EndSpeed
        return temp

    @end_speed.setter
    def end_speed(self, value: 'float'):
        self.wrapped.EndSpeed = float(value) if value else 0.0

    @property
    def include_damping_effects(self) -> 'bool':
        """bool: 'IncludeDampingEffects' is the original name of this property."""

        temp = self.wrapped.IncludeDampingEffects
        return temp

    @include_damping_effects.setter
    def include_damping_effects(self, value: 'bool'):
        self.wrapped.IncludeDampingEffects = bool(value) if value else False

    @property
    def include_disk_skew_effects(self) -> 'bool':
        """bool: 'IncludeDiskSkewEffects' is the original name of this property."""

        temp = self.wrapped.IncludeDiskSkewEffects
        return temp

    @include_disk_skew_effects.setter
    def include_disk_skew_effects(self, value: 'bool'):
        self.wrapped.IncludeDiskSkewEffects = bool(value) if value else False

    @property
    def include_gyroscopic_effects(self) -> 'bool':
        """bool: 'IncludeGyroscopicEffects' is the original name of this property."""

        temp = self.wrapped.IncludeGyroscopicEffects
        return temp

    @include_gyroscopic_effects.setter
    def include_gyroscopic_effects(self, value: 'bool'):
        self.wrapped.IncludeGyroscopicEffects = bool(value) if value else False

    @property
    def include_shaft_bow_effects(self) -> 'bool':
        """bool: 'IncludeShaftBowEffects' is the original name of this property."""

        temp = self.wrapped.IncludeShaftBowEffects
        return temp

    @include_shaft_bow_effects.setter
    def include_shaft_bow_effects(self, value: 'bool'):
        self.wrapped.IncludeShaftBowEffects = bool(value) if value else False

    @property
    def include_unbalanced_effects(self) -> 'bool':
        """bool: 'IncludeUnbalancedEffects' is the original name of this property."""

        temp = self.wrapped.IncludeUnbalancedEffects
        return temp

    @include_unbalanced_effects.setter
    def include_unbalanced_effects(self, value: 'bool'):
        self.wrapped.IncludeUnbalancedEffects = bool(value) if value else False

    @property
    def number_of_speeds(self) -> 'int':
        """int: 'NumberOfSpeeds' is the original name of this property."""

        temp = self.wrapped.NumberOfSpeeds
        return temp

    @number_of_speeds.setter
    def number_of_speeds(self, value: 'int'):
        self.wrapped.NumberOfSpeeds = int(value) if value else 0

    @property
    def reference_power_load(self) -> 'list_with_selected_item.ListWithSelectedItem_PowerLoad':
        """list_with_selected_item.ListWithSelectedItem_PowerLoad: 'ReferencePowerLoad' is the original name of this property."""

        temp = self.wrapped.ReferencePowerLoad
        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_PowerLoad)(temp) if temp is not None else None

    @reference_power_load.setter
    def reference_power_load(self, value: 'list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_PowerLoad.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_PowerLoad.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.ReferencePowerLoad = value

    @property
    def start_speed(self) -> 'float':
        """float: 'StartSpeed' is the original name of this property."""

        temp = self.wrapped.StartSpeed
        return temp

    @start_speed.setter
    def start_speed(self, value: 'float'):
        self.wrapped.StartSpeed = float(value) if value else 0.0

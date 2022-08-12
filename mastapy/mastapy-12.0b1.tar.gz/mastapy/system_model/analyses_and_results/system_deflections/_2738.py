"""_2738.py

ShaftSystemDeflection
"""


from typing import Iterable, List

from PIL.Image import Image

from mastapy._internal import constructor, conversion, enum_with_selected_value_runtime
from mastapy._math.vector_3d import Vector3D
from mastapy.shafts import _34, _19
from mastapy.system_model.part_model.shaft_model import _2422
from mastapy.system_model.analyses_and_results.static_loads import _6864
from mastapy.system_model.analyses_and_results.power_flows import _4063
from mastapy.system_model.analyses_and_results.system_deflections import _2736, _2737, _2626
from mastapy.math_utility.measured_vectors import _1520
from mastapy._internal.python_net import python_net_import

_SHAFT_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'ShaftSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftSystemDeflection',)


class ShaftSystemDeflection(_2626.AbstractShaftSystemDeflection):
    """ShaftSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SHAFT_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShaftSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_drawing_showing_axial_forces_with_mounted_components(self) -> 'Image':
        """Image: 'TwoDDrawingShowingAxialForcesWithMountedComponents' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TwoDDrawingShowingAxialForcesWithMountedComponents
        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def first_node_deflection_angular(self) -> 'Vector3D':
        """Vector3D: 'FirstNodeDeflectionAngular' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FirstNodeDeflectionAngular
        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def first_node_deflection_linear(self) -> 'Vector3D':
        """Vector3D: 'FirstNodeDeflectionLinear' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FirstNodeDeflectionLinear
        value = conversion.pn_to_mp_vector3d(temp)
        return value

    @property
    def flexible_pin_additional_deflection_amplitude(self) -> 'Iterable[Vector3D]':
        """Iterable[Vector3D]: 'FlexiblePinAdditionalDeflectionAmplitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlexiblePinAdditionalDeflectionAmplitude
        value = conversion.pn_to_mp_objects_in_iterable(temp)
        return value

    @property
    def number_of_cycles_for_fatigue(self) -> 'float':
        """float: 'NumberOfCyclesForFatigue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfCyclesForFatigue
        return temp

    @property
    def pin_tangential_oscillation_amplitude(self) -> 'float':
        """float: 'PinTangentialOscillationAmplitude' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinTangentialOscillationAmplitude
        return temp

    @property
    def shaft_rating_method(self) -> '_34.ShaftRatingMethod':
        """ShaftRatingMethod: 'ShaftRatingMethod' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftRatingMethod
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_34.ShaftRatingMethod)(value) if value is not None else None

    @property
    def component_design(self) -> '_2422.Shaft':
        """Shaft: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_19.ShaftDamageResults':
        """ShaftDamageResults: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6864.ShaftLoadCase':
        """ShaftLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4063.ShaftPowerFlow':
        """ShaftPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shaft_section_end_with_worst_fatigue_safety_factor(self) -> '_2736.ShaftSectionEndResultsSystemDeflection':
        """ShaftSectionEndResultsSystemDeflection: 'ShaftSectionEndWithWorstFatigueSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftSectionEndWithWorstFatigueSafetyFactor
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shaft_section_end_with_worst_fatigue_safety_factor_for_infinite_life(self) -> '_2736.ShaftSectionEndResultsSystemDeflection':
        """ShaftSectionEndResultsSystemDeflection: 'ShaftSectionEndWithWorstFatigueSafetyFactorForInfiniteLife' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftSectionEndWithWorstFatigueSafetyFactorForInfiniteLife
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def shaft_section_end_with_worst_static_safety_factor(self) -> '_2736.ShaftSectionEndResultsSystemDeflection':
        """ShaftSectionEndResultsSystemDeflection: 'ShaftSectionEndWithWorstStaticSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftSectionEndWithWorstStaticSafetyFactor
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mounted_components_applying_torque(self) -> 'List[_1520.ForceResults]':
        """List[ForceResults]: 'MountedComponentsApplyingTorque' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MountedComponentsApplyingTorque
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[ShaftSystemDeflection]':
        """List[ShaftSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shaft_section_end_results_by_offset_with_worst_safety_factor(self) -> 'List[_2736.ShaftSectionEndResultsSystemDeflection]':
        """List[ShaftSectionEndResultsSystemDeflection]: 'ShaftSectionEndResultsByOffsetWithWorstSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftSectionEndResultsByOffsetWithWorstSafetyFactor
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def shaft_section_results(self) -> 'List[_2737.ShaftSectionSystemDeflection]':
        """List[ShaftSectionSystemDeflection]: 'ShaftSectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ShaftSectionResults
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def calculate_outer_diameter_to_achieve_fatigue_safety_factor_requirement(self):
        """ 'CalculateOuterDiameterToAchieveFatigueSafetyFactorRequirement' is the original name of this method."""

        self.wrapped.CalculateOuterDiameterToAchieveFatigueSafetyFactorRequirement()

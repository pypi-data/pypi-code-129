"""_7242.py

FaceGearSetAdvancedSystemDeflection
"""


from typing import List

from mastapy.system_model.part_model.gears import _2468
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6800
from mastapy.gears.rating.face import _441
from mastapy.system_model.analyses_and_results.system_deflections import _2689
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7240, _7241, _7247
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'FaceGearSetAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('FaceGearSetAdvancedSystemDeflection',)


class FaceGearSetAdvancedSystemDeflection(_7247.GearSetAdvancedSystemDeflection):
    """FaceGearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'FaceGearSetAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2468.FaceGearSet':
        """FaceGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6800.FaceGearSetLoadCase':
        """FaceGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def rating(self) -> '_441.FaceGearSetRating':
        """FaceGearSetRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_441.FaceGearSetRating':
        """FaceGearSetRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_system_deflection_results(self) -> 'List[_2689.FaceGearSetSystemDeflection]':
        """List[FaceGearSetSystemDeflection]: 'AssemblySystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblySystemDeflectionResults
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_gears_advanced_system_deflection(self) -> 'List[_7240.FaceGearAdvancedSystemDeflection]':
        """List[FaceGearAdvancedSystemDeflection]: 'FaceGearsAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceGearsAdvancedSystemDeflection
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def face_meshes_advanced_system_deflection(self) -> 'List[_7241.FaceGearMeshAdvancedSystemDeflection]':
        """List[FaceGearMeshAdvancedSystemDeflection]: 'FaceMeshesAdvancedSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FaceMeshesAdvancedSystemDeflection
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

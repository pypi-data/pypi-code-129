"""_7233.py

CylindricalGearAdvancedSystemDeflection
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2464, _2466
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.cylindrical import _451
from mastapy.system_model.analyses_and_results.static_loads import _6775, _6780
from mastapy.gears.gear_designs.cylindrical import _1003, _1032
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7234, _7236, _7245
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'CylindricalGearAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearAdvancedSystemDeflection',)


class CylindricalGearAdvancedSystemDeflection(_7245.GearAdvancedSystemDeflection):
    """CylindricalGearAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_principal_root_stress_compression(self) -> 'float':
        """float: 'MaximumPrincipalRootStressCompression' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumPrincipalRootStressCompression
        return temp

    @property
    def maximum_principal_root_stress_tension(self) -> 'float':
        """float: 'MaximumPrincipalRootStressTension' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumPrincipalRootStressTension
        return temp

    @property
    def maximum_von_mises_root_stress_compression(self) -> 'float':
        """float: 'MaximumVonMisesRootStressCompression' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumVonMisesRootStressCompression
        return temp

    @property
    def maximum_von_mises_root_stress_tension(self) -> 'float':
        """float: 'MaximumVonMisesRootStressTension' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumVonMisesRootStressTension
        return temp

    @property
    def component_design(self) -> '_2464.CylindricalGear':
        """CylindricalGear: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        if _2464.CylindricalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CylindricalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_451.CylindricalGearRating':
        """CylindricalGearRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6775.CylindricalGearLoadCase':
        """CylindricalGearLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        if _6775.CylindricalGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_load_case to CylindricalGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_design(self) -> '_1003.CylindricalGearDesign':
        """CylindricalGearDesign: 'GearDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearDesign
        if _1003.CylindricalGearDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_design to CylindricalGearDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_advanced_system_deflection_meshes(self) -> 'List[_7234.CylindricalGearMeshAdvancedSystemDeflection]':
        """List[CylindricalGearMeshAdvancedSystemDeflection]: 'CylindricalGearAdvancedSystemDeflectionMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearAdvancedSystemDeflectionMeshes
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_gear_advanced_system_deflections_in_meshes(self) -> 'List[_7236.CylindricalMeshedGearAdvancedSystemDeflection]':
        """List[CylindricalMeshedGearAdvancedSystemDeflection]: 'CylindricalGearAdvancedSystemDeflectionsInMeshes' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearAdvancedSystemDeflectionsInMeshes
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_meshed_gear_advanced_system_deflections(self) -> 'List[_7236.CylindricalMeshedGearAdvancedSystemDeflection]':
        """List[CylindricalMeshedGearAdvancedSystemDeflection]: 'CylindricalMeshedGearAdvancedSystemDeflections' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalMeshedGearAdvancedSystemDeflections
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[CylindricalGearAdvancedSystemDeflection]':
        """List[CylindricalGearAdvancedSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

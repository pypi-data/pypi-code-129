"""_2834.py

CylindricalGearSetCompoundSystemDeflection
"""


from typing import List

from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1098
from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.gears import _2465, _2481
from mastapy._internal.cast_exception import CastException
from mastapy.gears.rating.cylindrical import _454, _455
from mastapy.system_model.analyses_and_results.system_deflections import _2678
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2832, _2833, _2846
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound', 'CylindricalGearSetCompoundSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetCompoundSystemDeflection',)


class CylindricalGearSetCompoundSystemDeflection(_2846.GearSetCompoundSystemDeflection):
    """CylindricalGearSetCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_COMPOUND_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetCompoundSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def advanced_ltca_results(self) -> '_1098.CylindricalGearSetMicroGeometryDutyCycle':
        """CylindricalGearSetMicroGeometryDutyCycle: 'AdvancedLTCAResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdvancedLTCAResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def advanced_ltca_results_only_first_planetary_mesh(self) -> '_1098.CylindricalGearSetMicroGeometryDutyCycle':
        """CylindricalGearSetMicroGeometryDutyCycle: 'AdvancedLTCAResultsOnlyFirstPlanetaryMesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdvancedLTCAResultsOnlyFirstPlanetaryMesh
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_design(self) -> '_2465.CylindricalGearSet':
        """CylindricalGearSet: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        if _2465.CylindricalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_design to CylindricalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2465.CylindricalGearSet':
        """CylindricalGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        if _2465.CylindricalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_design to CylindricalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def basic_ltca_results(self) -> '_1098.CylindricalGearSetMicroGeometryDutyCycle':
        """CylindricalGearSetMicroGeometryDutyCycle: 'BasicLTCAResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicLTCAResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def basic_ltca_results_only_first_planetary_mesh(self) -> '_1098.CylindricalGearSetMicroGeometryDutyCycle':
        """CylindricalGearSetMicroGeometryDutyCycle: 'BasicLTCAResultsOnlyFirstPlanetaryMesh' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BasicLTCAResultsOnlyFirstPlanetaryMesh
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_set_rating(self) -> '_454.CylindricalGearSetDutyCycleRating':
        """CylindricalGearSetDutyCycleRating: 'CylindricalGearSetRating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSetRating
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def cylindrical_gear_set_rating_using_basic_ltca(self) -> '_454.CylindricalGearSetDutyCycleRating':
        """CylindricalGearSetDutyCycleRating: 'CylindricalGearSetRatingUsingBasicLTCA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearSetRatingUsingBasicLTCA
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def load_case_rating_with_lowest_safety_factor_for_scuffing(self) -> '_455.CylindricalGearSetRating':
        """CylindricalGearSetRating: 'LoadCaseRatingWithLowestSafetyFactorForScuffing' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadCaseRatingWithLowestSafetyFactorForScuffing
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_analysis_cases_ready(self) -> 'List[_2678.CylindricalGearSetSystemDeflectionWithLTCAResults]':
        """List[CylindricalGearSetSystemDeflectionWithLTCAResults]: 'AssemblyAnalysisCasesReady' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCasesReady
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_gears_compound_system_deflection(self) -> 'List[_2832.CylindricalGearCompoundSystemDeflection]':
        """List[CylindricalGearCompoundSystemDeflection]: 'CylindricalGearsCompoundSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearsCompoundSystemDeflection
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_meshes_compound_system_deflection(self) -> 'List[_2833.CylindricalGearMeshCompoundSystemDeflection]':
        """List[CylindricalGearMeshCompoundSystemDeflection]: 'CylindricalMeshesCompoundSystemDeflection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalMeshesCompoundSystemDeflection
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def assembly_analysis_cases(self) -> 'List[_2678.CylindricalGearSetSystemDeflectionWithLTCAResults]':
        """List[CylindricalGearSetSystemDeflectionWithLTCAResults]: 'AssemblyAnalysisCases' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyAnalysisCases
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

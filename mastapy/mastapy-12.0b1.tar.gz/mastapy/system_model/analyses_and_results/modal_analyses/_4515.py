"""_4515.py

BevelDifferentialGearSetModalAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2455
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6739
from mastapy.system_model.analyses_and_results.system_deflections import _2636
from mastapy.system_model.analyses_and_results.modal_analyses import _4514, _4513, _4520
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_MODAL_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses', 'BevelDifferentialGearSetModalAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('BevelDifferentialGearSetModalAnalysis',)


class BevelDifferentialGearSetModalAnalysis(_4520.BevelGearSetModalAnalysis):
    """BevelDifferentialGearSetModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_MODAL_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BevelDifferentialGearSetModalAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self) -> '_2455.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_load_case(self) -> '_6739.BevelDifferentialGearSetLoadCase':
        """BevelDifferentialGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def system_deflection_results(self) -> '_2636.BevelDifferentialGearSetSystemDeflection':
        """BevelDifferentialGearSetSystemDeflection: 'SystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SystemDeflectionResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def bevel_differential_gears_modal_analysis(self) -> 'List[_4514.BevelDifferentialGearModalAnalysis]':
        """List[BevelDifferentialGearModalAnalysis]: 'BevelDifferentialGearsModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialGearsModalAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def bevel_differential_meshes_modal_analysis(self) -> 'List[_4513.BevelDifferentialGearMeshModalAnalysis]':
        """List[BevelDifferentialGearMeshModalAnalysis]: 'BevelDifferentialMeshesModalAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BevelDifferentialMeshesModalAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

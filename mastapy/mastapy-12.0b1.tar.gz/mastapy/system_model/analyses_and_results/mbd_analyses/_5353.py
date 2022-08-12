"""_5353.py

CylindricalGearSetMultibodyDynamicsAnalysis
"""


from typing import List

from mastapy.system_model.part_model.gears import _2465, _2481
from mastapy._internal import constructor, conversion
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6779, _6847
from mastapy.system_model.analyses_and_results.mbd_analyses import _5352, _5351, _5365
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses', 'CylindricalGearSetMultibodyDynamicsAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearSetMultibodyDynamicsAnalysis',)


class CylindricalGearSetMultibodyDynamicsAnalysis(_5365.GearSetMultibodyDynamicsAnalysis):
    """CylindricalGearSetMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_MULTIBODY_DYNAMICS_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearSetMultibodyDynamicsAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def assembly_load_case(self) -> '_6779.CylindricalGearSetLoadCase':
        """CylindricalGearSetLoadCase: 'AssemblyLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyLoadCase
        if _6779.CylindricalGearSetLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast assembly_load_case to CylindricalGearSetLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gears(self) -> 'List[_5352.CylindricalGearMultibodyDynamicsAnalysis]':
        """List[CylindricalGearMultibodyDynamicsAnalysis]: 'Gears' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Gears
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_gears_multibody_dynamics_analysis(self) -> 'List[_5352.CylindricalGearMultibodyDynamicsAnalysis]':
        """List[CylindricalGearMultibodyDynamicsAnalysis]: 'CylindricalGearsMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalGearsMultibodyDynamicsAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def cylindrical_meshes_multibody_dynamics_analysis(self) -> 'List[_5351.CylindricalGearMeshMultibodyDynamicsAnalysis]':
        """List[CylindricalGearMeshMultibodyDynamicsAnalysis]: 'CylindricalMeshesMultibodyDynamicsAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CylindricalMeshesMultibodyDynamicsAnalysis
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

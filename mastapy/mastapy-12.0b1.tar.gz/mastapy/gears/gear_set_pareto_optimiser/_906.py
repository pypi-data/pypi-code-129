"""_906.py

MicroGeometryDesignSpaceSearch
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy._internal.implicit import list_with_selected_item
from mastapy.gears.ltca.cylindrical import (
    _846, _847, _850, _852
)
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal.cast_exception import CastException
from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1097
from mastapy.gears.gear_set_pareto_optimiser import _896, _907
from mastapy._internal.python_net import python_net_import

_MICRO_GEOMETRY_DESIGN_SPACE_SEARCH = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'MicroGeometryDesignSpaceSearch')


__docformat__ = 'restructuredtext en'
__all__ = ('MicroGeometryDesignSpaceSearch',)


class MicroGeometryDesignSpaceSearch(_896.DesignSpaceSearchBase['_850.CylindricalGearSetLoadDistributionAnalysis', '_907.MicroGeometryDesignSpaceSearchCandidate']):
    """MicroGeometryDesignSpaceSearch

    This is a mastapy class.
    """

    TYPE = _MICRO_GEOMETRY_DESIGN_SPACE_SEARCH

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MicroGeometryDesignSpaceSearch.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name
        return temp

    @property
    def run_all_planetary_meshes(self) -> 'bool':
        """bool: 'RunAllPlanetaryMeshes' is the original name of this property."""

        temp = self.wrapped.RunAllPlanetaryMeshes
        return temp

    @run_all_planetary_meshes.setter
    def run_all_planetary_meshes(self, value: 'bool'):
        self.wrapped.RunAllPlanetaryMeshes = bool(value) if value else False

    @property
    def select_gear(self) -> 'list_with_selected_item.ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis':
        """list_with_selected_item.ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis: 'SelectGear' is the original name of this property."""

        temp = self.wrapped.SelectGear
        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis)(temp) if temp is not None else None

    @select_gear.setter
    def select_gear(self, value: 'list_with_selected_item.ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.SelectGear = value

    @property
    def select_mesh(self) -> 'list_with_selected_item.ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis':
        """list_with_selected_item.ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis: 'SelectMesh' is the original name of this property."""

        temp = self.wrapped.SelectMesh
        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis)(temp) if temp is not None else None

    @select_mesh.setter
    def select_mesh(self, value: 'list_with_selected_item.ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis.implicit_type()
        value = wrapper_type[enclosed_type](value.wrapped if value is not None else None)
        self.wrapped.SelectMesh = value

    @property
    def load_case_duty_cycle(self) -> '_850.CylindricalGearSetLoadDistributionAnalysis':
        """CylindricalGearSetLoadDistributionAnalysis: 'LoadCaseDutyCycle' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LoadCaseDutyCycle
        if _850.CylindricalGearSetLoadDistributionAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast load_case_duty_cycle to CylindricalGearSetLoadDistributionAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_candidate_micro_geometry(self) -> '_1097.CylindricalGearSetMicroGeometry':
        """CylindricalGearSetMicroGeometry: 'SelectedCandidateMicroGeometry' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SelectedCandidateMicroGeometry
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def all_candidate_gear_sets(self) -> 'List[_1097.CylindricalGearSetMicroGeometry]':
        """List[CylindricalGearSetMicroGeometry]: 'AllCandidateGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AllCandidateGearSets
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def candidate_gear_sets(self) -> 'List[_1097.CylindricalGearSetMicroGeometry]':
        """List[CylindricalGearSetMicroGeometry]: 'CandidateGearSets' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CandidateGearSets
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def add_chart(self):
        """ 'AddChart' is the original name of this method."""

        self.wrapped.AddChart()

    def reset_charts(self):
        """ 'ResetCharts' is the original name of this method."""

        self.wrapped.ResetCharts()

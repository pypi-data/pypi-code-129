"""_6808.py

GearSetHarmonicLoadData
"""


from typing import List

from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6807
from mastapy._internal.implicit import list_with_selected_item
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy.math_utility import _1471
from mastapy.electric_machines.harmonic_load_data import _1343
from mastapy._internal.python_net import python_net_import

_GEAR_SET_HARMONIC_LOAD_DATA = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'GearSetHarmonicLoadData')


__docformat__ = 'restructuredtext en'
__all__ = ('GearSetHarmonicLoadData',)


class GearSetHarmonicLoadData(_1343.HarmonicLoadDataBase):
    """GearSetHarmonicLoadData

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_HARMONIC_LOAD_DATA

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearSetHarmonicLoadData.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def excitation_order_as_rotational_order_of_shaft(self) -> 'float':
        """float: 'ExcitationOrderAsRotationalOrderOfShaft' is the original name of this property."""

        temp = self.wrapped.ExcitationOrderAsRotationalOrderOfShaft
        return temp

    @excitation_order_as_rotational_order_of_shaft.setter
    def excitation_order_as_rotational_order_of_shaft(self, value: 'float'):
        self.wrapped.ExcitationOrderAsRotationalOrderOfShaft = float(value) if value else 0.0

    @property
    def gear_mesh_te_order_type(self) -> '_6807.GearMeshTEOrderType':
        """GearMeshTEOrderType: 'GearMeshTEOrderType' is the original name of this property."""

        temp = self.wrapped.GearMeshTEOrderType
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_6807.GearMeshTEOrderType)(value) if value is not None else None

    @gear_mesh_te_order_type.setter
    def gear_mesh_te_order_type(self, value: '_6807.GearMeshTEOrderType'):
        value = value if value else None
        value = conversion.mp_to_pn_enum(value)
        self.wrapped.GearMeshTEOrderType = value

    @property
    def reference_shaft(self) -> 'list_with_selected_item.ListWithSelectedItem_str':
        """list_with_selected_item.ListWithSelectedItem_str: 'ReferenceShaft' is the original name of this property."""

        temp = self.wrapped.ReferenceShaft
        return constructor.new_from_mastapy_type(list_with_selected_item.ListWithSelectedItem_str)(temp) if temp is not None else None

    @reference_shaft.setter
    def reference_shaft(self, value: 'list_with_selected_item.ListWithSelectedItem_str.implicit_type()'):
        wrapper_type = list_with_selected_item.ListWithSelectedItem_str.wrapper_type()
        enclosed_type = list_with_selected_item.ListWithSelectedItem_str.implicit_type()
        value = wrapper_type[enclosed_type](enclosed_type(value) if value is not None else '')
        self.wrapped.ReferenceShaft = value

    @property
    def excitations(self) -> 'List[_1471.FourierSeries]':
        """List[FourierSeries]: 'Excitations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Excitations
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    def copy_data_to_duplicate_planetary_meshes(self):
        """ 'CopyDataToDuplicatePlanetaryMeshes' is the original name of this method."""

        self.wrapped.CopyDataToDuplicatePlanetaryMeshes()

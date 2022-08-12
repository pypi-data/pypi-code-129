"""_5090.py

CylindricalGearMeshModalAnalysisAtASpeed
"""


from typing import List

from mastapy.system_model.connections_and_sockets.gears import _2249
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6777
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5101
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed', 'CylindricalGearMeshModalAnalysisAtASpeed')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearMeshModalAnalysisAtASpeed',)


class CylindricalGearMeshModalAnalysisAtASpeed(_5101.GearMeshModalAnalysisAtASpeed):
    """CylindricalGearMeshModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_MODAL_ANALYSIS_AT_A_SPEED

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearMeshModalAnalysisAtASpeed.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2249.CylindricalGearMesh':
        """CylindricalGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6777.CylindricalGearMeshLoadCase':
        """CylindricalGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def planetaries(self) -> 'List[CylindricalGearMeshModalAnalysisAtASpeed]':
        """List[CylindricalGearMeshModalAnalysisAtASpeed]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

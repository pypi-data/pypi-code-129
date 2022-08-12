"""_4094.py

ZerolBevelGearMeshPowerFlow
"""


from mastapy.gears.rating.zerol_bevel import _360
from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2271
from mastapy.system_model.analyses_and_results.static_loads import _6900
from mastapy.system_model.analyses_and_results.power_flows import _3980
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_POWER_FLOW = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows', 'ZerolBevelGearMeshPowerFlow')


__docformat__ = 'restructuredtext en'
__all__ = ('ZerolBevelGearMeshPowerFlow',)


class ZerolBevelGearMeshPowerFlow(_3980.BevelGearMeshPowerFlow):
    """ZerolBevelGearMeshPowerFlow

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_POWER_FLOW

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ZerolBevelGearMeshPowerFlow.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self) -> '_360.ZerolBevelGearMeshRating':
        """ZerolBevelGearMeshRating: 'Rating' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rating
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_360.ZerolBevelGearMeshRating':
        """ZerolBevelGearMeshRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_design(self) -> '_2271.ZerolBevelGearMesh':
        """ZerolBevelGearMesh: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6900.ZerolBevelGearMeshLoadCase':
        """ZerolBevelGearMeshLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

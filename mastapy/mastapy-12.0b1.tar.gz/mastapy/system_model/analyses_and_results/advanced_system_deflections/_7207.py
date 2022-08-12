"""_7207.py

ClutchConnectionAdvancedSystemDeflection
"""


from typing import List

from mastapy.system_model.connections_and_sockets.couplings import _2282
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6747
from mastapy.system_model.analyses_and_results.system_deflections import _2645
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7224
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'ClutchConnectionAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ClutchConnectionAdvancedSystemDeflection',)


class ClutchConnectionAdvancedSystemDeflection(_7224.CouplingConnectionAdvancedSystemDeflection):
    """ClutchConnectionAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ClutchConnectionAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2282.ClutchConnection':
        """ClutchConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6747.ClutchConnectionLoadCase':
        """ClutchConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_system_deflection_results(self) -> 'List[_2645.ClutchConnectionSystemDeflection]':
        """List[ClutchConnectionSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionSystemDeflectionResults
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

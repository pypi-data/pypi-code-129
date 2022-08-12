"""_4250.py

CoaxialConnectionParametricStudyTool
"""


from typing import List

from mastapy.system_model.connections_and_sockets import _2209
from mastapy._internal import constructor, conversion
from mastapy.system_model.connections_and_sockets.cycloidal import _2275
from mastapy._internal.cast_exception import CastException
from mastapy.system_model.analyses_and_results.static_loads import _6750, _6772
from mastapy.system_model.analyses_and_results.system_deflections import _2648
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4341
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_PARAMETRIC_STUDY_TOOL = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools', 'CoaxialConnectionParametricStudyTool')


__docformat__ = 'restructuredtext en'
__all__ = ('CoaxialConnectionParametricStudyTool',)


class CoaxialConnectionParametricStudyTool(_4341.ShaftToMountableComponentConnectionParametricStudyTool):
    """CoaxialConnectionParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_PARAMETRIC_STUDY_TOOL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CoaxialConnectionParametricStudyTool.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self) -> '_2209.CoaxialConnection':
        """CoaxialConnection: 'ConnectionDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionDesign
        if _2209.CoaxialConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_design to CoaxialConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_load_case(self) -> '_6750.CoaxialConnectionLoadCase':
        """CoaxialConnectionLoadCase: 'ConnectionLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionLoadCase
        if _6750.CoaxialConnectionLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast connection_load_case to CoaxialConnectionLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def connection_system_deflection_results(self) -> 'List[_2648.CoaxialConnectionSystemDeflection]':
        """List[CoaxialConnectionSystemDeflection]: 'ConnectionSystemDeflectionResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ConnectionSystemDeflectionResults
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

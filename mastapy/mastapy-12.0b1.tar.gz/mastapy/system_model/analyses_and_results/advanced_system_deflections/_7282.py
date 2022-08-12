"""_7282.py

RootAssemblyAdvancedSystemDeflection
"""


from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7186, _7192
from mastapy._internal import constructor
from mastapy.system_model.part_model import _2414
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_ADVANCED_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections', 'RootAssemblyAdvancedSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('RootAssemblyAdvancedSystemDeflection',)


class RootAssemblyAdvancedSystemDeflection(_7192.AssemblyAdvancedSystemDeflection):
    """RootAssemblyAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_ADVANCED_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'RootAssemblyAdvancedSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def advanced_system_deflection_inputs(self) -> '_7186.AdvancedSystemDeflection':
        """AdvancedSystemDeflection: 'AdvancedSystemDeflectionInputs' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AdvancedSystemDeflectionInputs
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def assembly_design(self) -> '_2414.RootAssembly':
        """RootAssembly: 'AssemblyDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AssemblyDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

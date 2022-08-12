"""_205.py

ElementPropertiesShell
"""


from mastapy._internal import constructor, enum_with_selected_value_runtime, conversion
from mastapy.fe_tools.vis_tools_global.vis_tools_global_enums import _1223
from mastapy.nodal_analysis.dev_tools_analyses.full_fe_reporting import _208
from mastapy._internal.python_net import python_net_import

_ELEMENT_PROPERTIES_SHELL = python_net_import('SMT.MastaAPI.NodalAnalysis.DevToolsAnalyses.FullFEReporting', 'ElementPropertiesShell')


__docformat__ = 'restructuredtext en'
__all__ = ('ElementPropertiesShell',)


class ElementPropertiesShell(_208.ElementPropertiesWithMaterial):
    """ElementPropertiesShell

    This is a mastapy class.
    """

    TYPE = _ELEMENT_PROPERTIES_SHELL

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ElementPropertiesShell.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def effective_shear_ratio(self) -> 'float':
        """float: 'EffectiveShearRatio' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.EffectiveShearRatio
        return temp

    @property
    def layer_thicknesses(self) -> 'str':
        """str: 'LayerThicknesses' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LayerThicknesses
        return temp

    @property
    def number_of_layers(self) -> 'int':
        """int: 'NumberOfLayers' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfLayers
        return temp

    @property
    def thickness(self) -> 'float':
        """float: 'Thickness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Thickness
        return temp

    @property
    def wall_type(self) -> '_1223.ElementPropertiesShellWallType':
        """ElementPropertiesShellWallType: 'WallType' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WallType
        value = conversion.pn_to_mp_enum(temp)
        return constructor.new_from_mastapy_type(_1223.ElementPropertiesShellWallType)(value) if value is not None else None

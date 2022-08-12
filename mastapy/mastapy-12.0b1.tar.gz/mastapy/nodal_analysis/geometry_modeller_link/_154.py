"""_154.py

GeometryModellerDesignInformation
"""


from mastapy._internal import constructor
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_GEOMETRY_MODELLER_DESIGN_INFORMATION = python_net_import('SMT.MastaAPI.NodalAnalysis.GeometryModellerLink', 'GeometryModellerDesignInformation')


__docformat__ = 'restructuredtext en'
__all__ = ('GeometryModellerDesignInformation',)


class GeometryModellerDesignInformation(_0.APIBase):
    """GeometryModellerDesignInformation

    This is a mastapy class.
    """

    TYPE = _GEOMETRY_MODELLER_DESIGN_INFORMATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GeometryModellerDesignInformation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def file_name(self) -> 'str':
        """str: 'FileName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FileName
        return temp

    @property
    def tab_name(self) -> 'str':
        """str: 'TabName' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TabName
        return temp

    @property
    def main_part_moniker(self) -> 'str':
        """str: 'MainPartMoniker' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MainPartMoniker
        return temp

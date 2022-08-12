"""_1808.py

LegacyChartMathChartDefinition
"""


from mastapy.utility.report import _1706
from mastapy._internal.python_net import python_net_import

_LEGACY_CHART_MATH_CHART_DEFINITION = python_net_import('SMT.MastaAPI.UtilityGUI.Charts', 'LegacyChartMathChartDefinition')


__docformat__ = 'restructuredtext en'
__all__ = ('LegacyChartMathChartDefinition',)


class LegacyChartMathChartDefinition(_1706.ChartDefinition):
    """LegacyChartMathChartDefinition

    This is a mastapy class.
    """

    TYPE = _LEGACY_CHART_MATH_CHART_DEFINITION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'LegacyChartMathChartDefinition.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

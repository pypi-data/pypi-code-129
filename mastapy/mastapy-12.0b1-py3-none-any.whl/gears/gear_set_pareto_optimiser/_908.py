"""_908.py

MicroGeometryDesignSpaceSearchChartInformation
"""


from mastapy.gears.gear_set_pareto_optimiser import (
    _906, _909, _894, _907
)
from mastapy._internal import constructor
from mastapy._internal.cast_exception import CastException
from mastapy.gears.ltca.cylindrical import _850
from mastapy._internal.python_net import python_net_import

_MICRO_GEOMETRY_DESIGN_SPACE_SEARCH_CHART_INFORMATION = python_net_import('SMT.MastaAPI.Gears.GearSetParetoOptimiser', 'MicroGeometryDesignSpaceSearchChartInformation')


__docformat__ = 'restructuredtext en'
__all__ = ('MicroGeometryDesignSpaceSearchChartInformation',)


class MicroGeometryDesignSpaceSearchChartInformation(_894.ChartInfoBase['_850.CylindricalGearSetLoadDistributionAnalysis', '_907.MicroGeometryDesignSpaceSearchCandidate']):
    """MicroGeometryDesignSpaceSearchChartInformation

    This is a mastapy class.
    """

    TYPE = _MICRO_GEOMETRY_DESIGN_SPACE_SEARCH_CHART_INFORMATION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'MicroGeometryDesignSpaceSearchChartInformation.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def optimiser(self) -> '_906.MicroGeometryDesignSpaceSearch':
        """MicroGeometryDesignSpaceSearch: 'Optimiser' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Optimiser
        if _906.MicroGeometryDesignSpaceSearch.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast optimiser to MicroGeometryDesignSpaceSearch. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def optimiser_of_type_micro_geometry_gear_set_design_space_search(self) -> '_909.MicroGeometryGearSetDesignSpaceSearch':
        """MicroGeometryGearSetDesignSpaceSearch: 'Optimiser' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Optimiser
        if _909.MicroGeometryGearSetDesignSpaceSearch.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast optimiser to MicroGeometryGearSetDesignSpaceSearch. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

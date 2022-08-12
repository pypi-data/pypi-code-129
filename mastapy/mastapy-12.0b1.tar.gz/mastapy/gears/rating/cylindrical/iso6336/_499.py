"""_499.py

CylindricalGearToothFatigueFractureResultsN1457
"""


from typing import List

from mastapy.utility_gui.charts import _1813
from mastapy._internal import constructor, conversion
from mastapy.gears.rating.cylindrical.iso6336 import _520, _517
from mastapy._internal.cast_exception import CastException
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_TOOTH_FATIGUE_FRACTURE_RESULTS_N1457 = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336', 'CylindricalGearToothFatigueFractureResultsN1457')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearToothFatigueFractureResultsN1457',)


class CylindricalGearToothFatigueFractureResultsN1457(_0.APIBase):
    """CylindricalGearToothFatigueFractureResultsN1457

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_TOOTH_FATIGUE_FRACTURE_RESULTS_N1457

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearToothFatigueFractureResultsN1457.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def fatigue_damage_chart(self) -> '_1813.ThreeDChartDefinition':
        """ThreeDChartDefinition: 'FatigueDamageChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FatigueDamageChart
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def maximum_fatigue_damage(self) -> 'float':
        """float: 'MaximumFatigueDamage' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumFatigueDamage
        return temp

    @property
    def critical_section(self) -> '_520.ToothFlankFractureAnalysisRowN1457':
        """ToothFlankFractureAnalysisRowN1457: 'CriticalSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CriticalSection
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_contact_point_a_section(self) -> '_520.ToothFlankFractureAnalysisRowN1457':
        """ToothFlankFractureAnalysisRowN1457: 'MeshContactPointASection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshContactPointASection
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_contact_point_ab_section(self) -> '_517.ToothFlankFractureAnalysisContactPointN1457':
        """ToothFlankFractureAnalysisContactPointN1457: 'MeshContactPointABSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshContactPointABSection
        if _517.ToothFlankFractureAnalysisContactPointN1457.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh_contact_point_ab_section to ToothFlankFractureAnalysisContactPointN1457. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_contact_point_b_section(self) -> '_517.ToothFlankFractureAnalysisContactPointN1457':
        """ToothFlankFractureAnalysisContactPointN1457: 'MeshContactPointBSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshContactPointBSection
        if _517.ToothFlankFractureAnalysisContactPointN1457.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh_contact_point_b_section to ToothFlankFractureAnalysisContactPointN1457. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_contact_point_c_section(self) -> '_517.ToothFlankFractureAnalysisContactPointN1457':
        """ToothFlankFractureAnalysisContactPointN1457: 'MeshContactPointCSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshContactPointCSection
        if _517.ToothFlankFractureAnalysisContactPointN1457.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh_contact_point_c_section to ToothFlankFractureAnalysisContactPointN1457. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_contact_point_d_section(self) -> '_517.ToothFlankFractureAnalysisContactPointN1457':
        """ToothFlankFractureAnalysisContactPointN1457: 'MeshContactPointDSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshContactPointDSection
        if _517.ToothFlankFractureAnalysisContactPointN1457.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh_contact_point_d_section to ToothFlankFractureAnalysisContactPointN1457. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_contact_point_de_section(self) -> '_517.ToothFlankFractureAnalysisContactPointN1457':
        """ToothFlankFractureAnalysisContactPointN1457: 'MeshContactPointDESection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshContactPointDESection
        if _517.ToothFlankFractureAnalysisContactPointN1457.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh_contact_point_de_section to ToothFlankFractureAnalysisContactPointN1457. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_contact_point_e_section(self) -> '_517.ToothFlankFractureAnalysisContactPointN1457':
        """ToothFlankFractureAnalysisContactPointN1457: 'MeshContactPointESection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshContactPointESection
        if _517.ToothFlankFractureAnalysisContactPointN1457.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast mesh_contact_point_e_section to ToothFlankFractureAnalysisContactPointN1457. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def analysis_rows(self) -> 'List[_520.ToothFlankFractureAnalysisRowN1457]':
        """List[ToothFlankFractureAnalysisRowN1457]: 'AnalysisRows' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AnalysisRows
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def contact_points(self) -> 'List[_517.ToothFlankFractureAnalysisContactPointN1457]':
        """List[ToothFlankFractureAnalysisContactPointN1457]: 'ContactPoints' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactPoints
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

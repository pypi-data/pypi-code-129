"""_498.py

CylindricalGearToothFatigueFractureResults
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.gears.rating.cylindrical.iso6336 import _514
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_TOOTH_FATIGUE_FRACTURE_RESULTS = python_net_import('SMT.MastaAPI.Gears.Rating.Cylindrical.ISO6336', 'CylindricalGearToothFatigueFractureResults')


__docformat__ = 'restructuredtext en'
__all__ = ('CylindricalGearToothFatigueFractureResults',)


class CylindricalGearToothFatigueFractureResults(_0.APIBase):
    """CylindricalGearToothFatigueFractureResults

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_TOOTH_FATIGUE_FRACTURE_RESULTS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'CylindricalGearToothFatigueFractureResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_material_exposure(self) -> 'float':
        """float: 'MaximumMaterialExposure' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumMaterialExposure
        return temp

    @property
    def witzigs_safety_factor(self) -> 'float':
        """float: 'WitzigsSafetyFactor' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WitzigsSafetyFactor
        return temp

    @property
    def critical_section(self) -> '_514.ToothFlankFractureAnalysisContactPoint':
        """ToothFlankFractureAnalysisContactPoint: 'CriticalSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.CriticalSection
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_contact_point_a_section(self) -> '_514.ToothFlankFractureAnalysisContactPoint':
        """ToothFlankFractureAnalysisContactPoint: 'MeshContactPointASection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshContactPointASection
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_contact_point_ab_section(self) -> '_514.ToothFlankFractureAnalysisContactPoint':
        """ToothFlankFractureAnalysisContactPoint: 'MeshContactPointABSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshContactPointABSection
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_contact_point_b_section(self) -> '_514.ToothFlankFractureAnalysisContactPoint':
        """ToothFlankFractureAnalysisContactPoint: 'MeshContactPointBSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshContactPointBSection
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_contact_point_c_section(self) -> '_514.ToothFlankFractureAnalysisContactPoint':
        """ToothFlankFractureAnalysisContactPoint: 'MeshContactPointCSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshContactPointCSection
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_contact_point_d_section(self) -> '_514.ToothFlankFractureAnalysisContactPoint':
        """ToothFlankFractureAnalysisContactPoint: 'MeshContactPointDSection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshContactPointDSection
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_contact_point_de_section(self) -> '_514.ToothFlankFractureAnalysisContactPoint':
        """ToothFlankFractureAnalysisContactPoint: 'MeshContactPointDESection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshContactPointDESection
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def mesh_contact_point_e_section(self) -> '_514.ToothFlankFractureAnalysisContactPoint':
        """ToothFlankFractureAnalysisContactPoint: 'MeshContactPointESection' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MeshContactPointESection
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def analysis_rows(self) -> 'List[_514.ToothFlankFractureAnalysisContactPoint]':
        """List[ToothFlankFractureAnalysisContactPoint]: 'AnalysisRows' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AnalysisRows
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

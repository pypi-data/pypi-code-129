"""_1154.py

KimosBevelHypoidSingleLoadCaseResultsData
"""


from typing import List

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.gears.gear_designs.conical import _1155
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_KIMOS_BEVEL_HYPOID_SINGLE_LOAD_CASE_RESULTS_DATA = python_net_import('SMT.MastaAPI.Gears.GearDesigns.Conical', 'KimosBevelHypoidSingleLoadCaseResultsData')


__docformat__ = 'restructuredtext en'
__all__ = ('KimosBevelHypoidSingleLoadCaseResultsData',)


class KimosBevelHypoidSingleLoadCaseResultsData(_0.APIBase):
    """KimosBevelHypoidSingleLoadCaseResultsData

    This is a mastapy class.
    """

    TYPE = _KIMOS_BEVEL_HYPOID_SINGLE_LOAD_CASE_RESULTS_DATA

    __hash__ = None

    def __init__(self, instance_to_wrap: 'KimosBevelHypoidSingleLoadCaseResultsData.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def average_mesh_stiffness_per_unit_face_width(self) -> 'float':
        """float: 'AverageMeshStiffnessPerUnitFaceWidth' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AverageMeshStiffnessPerUnitFaceWidth
        return temp

    @property
    def contact_pressure_chart(self) -> 'Image':
        """Image: 'ContactPressureChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactPressureChart
        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def contact_ratio_under_load(self) -> 'float':
        """float: 'ContactRatioUnderLoad' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ContactRatioUnderLoad
        return temp

    @property
    def efficiency(self) -> 'float':
        """float: 'Efficiency' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Efficiency
        return temp

    @property
    def flash_temperature_chart(self) -> 'Image':
        """Image: 'FlashTemperatureChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FlashTemperatureChart
        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def friction_coefficient_chart(self) -> 'Image':
        """Image: 'FrictionCoefficientChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.FrictionCoefficientChart
        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def maximum_contact_pressure(self) -> 'float':
        """float: 'MaximumContactPressure' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumContactPressure
        return temp

    @property
    def maximum_flash_temperature(self) -> 'float':
        """float: 'MaximumFlashTemperature' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumFlashTemperature
        return temp

    @property
    def maximum_friction_coefficient(self) -> 'float':
        """float: 'MaximumFrictionCoefficient' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumFrictionCoefficient
        return temp

    @property
    def maximum_pinion_root_stress(self) -> 'float':
        """float: 'MaximumPinionRootStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumPinionRootStress
        return temp

    @property
    def maximum_sliding_velocity(self) -> 'float':
        """float: 'MaximumSlidingVelocity' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumSlidingVelocity
        return temp

    @property
    def maximum_wheel_root_stress(self) -> 'float':
        """float: 'MaximumWheelRootStress' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumWheelRootStress
        return temp

    @property
    def peak_to_peak_te_linear_loaded(self) -> 'float':
        """float: 'PeakToPeakTELinearLoaded' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakToPeakTELinearLoaded
        return temp

    @property
    def peak_to_peak_te_linear_unloaded(self) -> 'float':
        """float: 'PeakToPeakTELinearUnloaded' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PeakToPeakTELinearUnloaded
        return temp

    @property
    def pinion_root_stress_chart(self) -> 'Image':
        """Image: 'PinionRootStressChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PinionRootStressChart
        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def pressure_velocity_pv_chart(self) -> 'Image':
        """Image: 'PressureVelocityPVChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PressureVelocityPVChart
        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def sliding_velocity_chart(self) -> 'Image':
        """Image: 'SlidingVelocityChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SlidingVelocityChart
        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def wheel_root_stress_chart(self) -> 'Image':
        """Image: 'WheelRootStressChart' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WheelRootStressChart
        value = conversion.pn_to_mp_smt_bitmap(temp)
        return value

    @property
    def single_rotation_angle_results(self) -> 'List[_1155.KimosBevelHypoidSingleRotationAngleResult]':
        """List[KimosBevelHypoidSingleRotationAngleResult]: 'SingleRotationAngleResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.SingleRotationAngleResults
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

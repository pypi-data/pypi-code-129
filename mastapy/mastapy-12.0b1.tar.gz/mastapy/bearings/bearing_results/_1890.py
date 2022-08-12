"""_1890.py

BearingStiffnessMatrixReporter
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.bearings.bearing_results import _1913
from mastapy import _0
from mastapy._internal.python_net import python_net_import

_BEARING_STIFFNESS_MATRIX_REPORTER = python_net_import('SMT.MastaAPI.Bearings.BearingResults', 'BearingStiffnessMatrixReporter')


__docformat__ = 'restructuredtext en'
__all__ = ('BearingStiffnessMatrixReporter',)


class BearingStiffnessMatrixReporter(_0.APIBase):
    """BearingStiffnessMatrixReporter

    This is a mastapy class.
    """

    TYPE = _BEARING_STIFFNESS_MATRIX_REPORTER

    __hash__ = None

    def __init__(self, instance_to_wrap: 'BearingStiffnessMatrixReporter.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_stiffness(self) -> 'float':
        """float: 'AxialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.AxialStiffness
        return temp

    @property
    def maximum_radial_stiffness(self) -> 'float':
        """float: 'MaximumRadialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumRadialStiffness
        return temp

    @property
    def maximum_tilt_stiffness(self) -> 'float':
        """float: 'MaximumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MaximumTiltStiffness
        return temp

    @property
    def minimum_radial_stiffness(self) -> 'float':
        """float: 'MinimumRadialStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumRadialStiffness
        return temp

    @property
    def minimum_tilt_stiffness(self) -> 'float':
        """float: 'MinimumTiltStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.MinimumTiltStiffness
        return temp

    @property
    def name(self) -> 'str':
        """str: 'Name' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Name
        return temp

    @property
    def radial_stiffness_variation(self) -> 'float':
        """float: 'RadialStiffnessVariation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RadialStiffnessVariation
        return temp

    @property
    def stiffness_xx(self) -> 'float':
        """float: 'StiffnessXX' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessXX
        return temp

    @property
    def stiffness_xy(self) -> 'float':
        """float: 'StiffnessXY' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessXY
        return temp

    @property
    def stiffness_xz(self) -> 'float':
        """float: 'StiffnessXZ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessXZ
        return temp

    @property
    def stiffness_x_theta_x(self) -> 'float':
        """float: 'StiffnessXThetaX' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessXThetaX
        return temp

    @property
    def stiffness_x_theta_y(self) -> 'float':
        """float: 'StiffnessXThetaY' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessXThetaY
        return temp

    @property
    def stiffness_x_theta_z(self) -> 'float':
        """float: 'StiffnessXThetaZ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessXThetaZ
        return temp

    @property
    def stiffness_yx(self) -> 'float':
        """float: 'StiffnessYX' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessYX
        return temp

    @property
    def stiffness_yy(self) -> 'float':
        """float: 'StiffnessYY' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessYY
        return temp

    @property
    def stiffness_yz(self) -> 'float':
        """float: 'StiffnessYZ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessYZ
        return temp

    @property
    def stiffness_y_theta_x(self) -> 'float':
        """float: 'StiffnessYThetaX' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessYThetaX
        return temp

    @property
    def stiffness_y_theta_y(self) -> 'float':
        """float: 'StiffnessYThetaY' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessYThetaY
        return temp

    @property
    def stiffness_y_theta_z(self) -> 'float':
        """float: 'StiffnessYThetaZ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessYThetaZ
        return temp

    @property
    def stiffness_zx(self) -> 'float':
        """float: 'StiffnessZX' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessZX
        return temp

    @property
    def stiffness_zy(self) -> 'float':
        """float: 'StiffnessZY' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessZY
        return temp

    @property
    def stiffness_zz(self) -> 'float':
        """float: 'StiffnessZZ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessZZ
        return temp

    @property
    def stiffness_z_theta_x(self) -> 'float':
        """float: 'StiffnessZThetaX' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessZThetaX
        return temp

    @property
    def stiffness_z_theta_y(self) -> 'float':
        """float: 'StiffnessZThetaY' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessZThetaY
        return temp

    @property
    def stiffness_z_theta_z(self) -> 'float':
        """float: 'StiffnessZThetaZ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessZThetaZ
        return temp

    @property
    def stiffness_theta_xx(self) -> 'float':
        """float: 'StiffnessThetaXX' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessThetaXX
        return temp

    @property
    def stiffness_theta_xy(self) -> 'float':
        """float: 'StiffnessThetaXY' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessThetaXY
        return temp

    @property
    def stiffness_theta_xz(self) -> 'float':
        """float: 'StiffnessThetaXZ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessThetaXZ
        return temp

    @property
    def stiffness_theta_x_theta_x(self) -> 'float':
        """float: 'StiffnessThetaXThetaX' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessThetaXThetaX
        return temp

    @property
    def stiffness_theta_x_theta_y(self) -> 'float':
        """float: 'StiffnessThetaXThetaY' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessThetaXThetaY
        return temp

    @property
    def stiffness_theta_x_theta_z(self) -> 'float':
        """float: 'StiffnessThetaXThetaZ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessThetaXThetaZ
        return temp

    @property
    def stiffness_theta_yx(self) -> 'float':
        """float: 'StiffnessThetaYX' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessThetaYX
        return temp

    @property
    def stiffness_theta_yy(self) -> 'float':
        """float: 'StiffnessThetaYY' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessThetaYY
        return temp

    @property
    def stiffness_theta_yz(self) -> 'float':
        """float: 'StiffnessThetaYZ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessThetaYZ
        return temp

    @property
    def stiffness_theta_y_theta_x(self) -> 'float':
        """float: 'StiffnessThetaYThetaX' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessThetaYThetaX
        return temp

    @property
    def stiffness_theta_y_theta_y(self) -> 'float':
        """float: 'StiffnessThetaYThetaY' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessThetaYThetaY
        return temp

    @property
    def stiffness_theta_y_theta_z(self) -> 'float':
        """float: 'StiffnessThetaYThetaZ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessThetaYThetaZ
        return temp

    @property
    def stiffness_theta_zx(self) -> 'float':
        """float: 'StiffnessThetaZX' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessThetaZX
        return temp

    @property
    def stiffness_theta_zy(self) -> 'float':
        """float: 'StiffnessThetaZY' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessThetaZY
        return temp

    @property
    def stiffness_theta_zz(self) -> 'float':
        """float: 'StiffnessThetaZZ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessThetaZZ
        return temp

    @property
    def stiffness_theta_z_theta_x(self) -> 'float':
        """float: 'StiffnessThetaZThetaX' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessThetaZThetaX
        return temp

    @property
    def stiffness_theta_z_theta_y(self) -> 'float':
        """float: 'StiffnessThetaZThetaY' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessThetaZThetaY
        return temp

    @property
    def stiffness_theta_z_theta_z(self) -> 'float':
        """float: 'StiffnessThetaZThetaZ' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessThetaZThetaZ
        return temp

    @property
    def tilt_stiffness_variation(self) -> 'float':
        """float: 'TiltStiffnessVariation' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TiltStiffnessVariation
        return temp

    @property
    def torsional_stiffness(self) -> 'float':
        """float: 'TorsionalStiffness' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TorsionalStiffness
        return temp

    @property
    def rows(self) -> 'List[_1913.StiffnessRow]':
        """List[StiffnessRow]: 'Rows' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Rows
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

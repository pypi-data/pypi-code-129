"""_2735.py

ShaftHubConnectionSystemDeflection
"""


from typing import List

from mastapy._internal import constructor, conversion
from mastapy.system_model.part_model.couplings import _2537
from mastapy.detailed_rigid_connectors.rating import _1397
from mastapy.detailed_rigid_connectors.splines.ratings import (
    _1385, _1387, _1389, _1391,
    _1393
)
from mastapy._internal.cast_exception import CastException
from mastapy.detailed_rigid_connectors.keyed_joints.rating import _1403
from mastapy.detailed_rigid_connectors.interference_fits.rating import _1410
from mastapy.system_model.analyses_and_results.static_loads import _6863
from mastapy.system_model.analyses_and_results.power_flows import _4062
from mastapy.bearings.bearing_results import _1890
from mastapy.system_model.analyses_and_results.system_deflections.reporting import _2784
from mastapy.system_model.analyses_and_results.system_deflections import _2662
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_SYSTEM_DEFLECTION = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections', 'ShaftHubConnectionSystemDeflection')


__docformat__ = 'restructuredtext en'
__all__ = ('ShaftHubConnectionSystemDeflection',)


class ShaftHubConnectionSystemDeflection(_2662.ConnectorSystemDeflection):
    """ShaftHubConnectionSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_SYSTEM_DEFLECTION

    __hash__ = None

    def __init__(self, instance_to_wrap: 'ShaftHubConnectionSystemDeflection.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def limiting_friction(self) -> 'float':
        """float: 'LimitingFriction' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LimitingFriction
        return temp

    @property
    def node_pair_separations(self) -> 'List[float]':
        """List[float]: 'NodePairSeparations' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodePairSeparations
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def node_radial_forces_on_inner(self) -> 'List[float]':
        """List[float]: 'NodeRadialForcesOnInner' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NodeRadialForcesOnInner
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def normal_deflection_left_flank(self) -> 'List[float]':
        """List[float]: 'NormalDeflectionLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalDeflectionLeftFlank
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def normal_deflection_right_flank(self) -> 'List[float]':
        """List[float]: 'NormalDeflectionRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalDeflectionRightFlank
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def normal_deflection_tooth_centre(self) -> 'List[float]':
        """List[float]: 'NormalDeflectionToothCentre' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalDeflectionToothCentre
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def normal_force_left_flank(self) -> 'List[float]':
        """List[float]: 'NormalForceLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalForceLeftFlank
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def normal_force_right_flank(self) -> 'List[float]':
        """List[float]: 'NormalForceRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalForceRightFlank
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def normal_force_tooth_centre(self) -> 'List[float]':
        """List[float]: 'NormalForceToothCentre' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalForceToothCentre
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def normal_stiffness_left_flank(self) -> 'List[float]':
        """List[float]: 'NormalStiffnessLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalStiffnessLeftFlank
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def normal_stiffness_right_flank(self) -> 'List[float]':
        """List[float]: 'NormalStiffnessRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalStiffnessRightFlank
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def normal_stiffness_tooth_centre(self) -> 'List[float]':
        """List[float]: 'NormalStiffnessToothCentre' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NormalStiffnessToothCentre
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def number_of_major_diameter_contacts(self) -> 'int':
        """int: 'NumberOfMajorDiameterContacts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfMajorDiameterContacts
        return temp

    @property
    def number_of_teeth_in_contact(self) -> 'int':
        """int: 'NumberOfTeethInContact' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.NumberOfTeethInContact
        return temp

    @property
    def tangential_force_left_flank(self) -> 'List[float]':
        """List[float]: 'TangentialForceLeftFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TangentialForceLeftFlank
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def tangential_force_right_flank(self) -> 'List[float]':
        """List[float]: 'TangentialForceRightFlank' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TangentialForceRightFlank
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def tangential_force_tooth_centre(self) -> 'List[float]':
        """List[float]: 'TangentialForceToothCentre' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TangentialForceToothCentre
        value = conversion.pn_to_mp_list_float(temp)
        return value

    @property
    def tangential_force_on_spline(self) -> 'float':
        """float: 'TangentialForceOnSpline' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TangentialForceOnSpline
        return temp

    @property
    def will_spline_slip(self) -> 'bool':
        """bool: 'WillSplineSlip' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.WillSplineSlip
        return temp

    @property
    def component_design(self) -> '_2537.ShaftHubConnection':
        """ShaftHubConnection: 'ComponentDesign' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDesign
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis(self) -> '_1397.ShaftHubConnectionRating':
        """ShaftHubConnectionRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1397.ShaftHubConnectionRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to ShaftHubConnectionRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_agma6123_spline_joint_rating(self) -> '_1385.AGMA6123SplineJointRating':
        """AGMA6123SplineJointRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1385.AGMA6123SplineJointRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to AGMA6123SplineJointRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_din5466_spline_rating(self) -> '_1387.DIN5466SplineRating':
        """DIN5466SplineRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1387.DIN5466SplineRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to DIN5466SplineRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_gbt17855_spline_joint_rating(self) -> '_1389.GBT17855SplineJointRating':
        """GBT17855SplineJointRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1389.GBT17855SplineJointRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to GBT17855SplineJointRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_sae_spline_joint_rating(self) -> '_1391.SAESplineJointRating':
        """SAESplineJointRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1391.SAESplineJointRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to SAESplineJointRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_spline_joint_rating(self) -> '_1393.SplineJointRating':
        """SplineJointRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1393.SplineJointRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to SplineJointRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_keyway_rating(self) -> '_1403.KeywayRating':
        """KeywayRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1403.KeywayRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to KeywayRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_detailed_analysis_of_type_interference_fit_rating(self) -> '_1410.InterferenceFitRating':
        """InterferenceFitRating: 'ComponentDetailedAnalysis' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentDetailedAnalysis
        if _1410.InterferenceFitRating.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast component_detailed_analysis to InterferenceFitRating. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def component_load_case(self) -> '_6863.ShaftHubConnectionLoadCase':
        """ShaftHubConnectionLoadCase: 'ComponentLoadCase' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ComponentLoadCase
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def power_flow_results(self) -> '_4062.ShaftHubConnectionPowerFlow':
        """ShaftHubConnectionPowerFlow: 'PowerFlowResults' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PowerFlowResults
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stiffness_matrix_in_local_coordinate_system(self) -> '_1890.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'StiffnessMatrixInLocalCoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessMatrixInLocalCoordinateSystem
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def stiffness_matrix_in_unrotated_coordinate_system(self) -> '_1890.BearingStiffnessMatrixReporter':
        """BearingStiffnessMatrixReporter: 'StiffnessMatrixInUnrotatedCoordinateSystem' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.StiffnessMatrixInUnrotatedCoordinateSystem
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def left_flank_contacts(self) -> 'List[_2784.SplineFlankContactReporting]':
        """List[SplineFlankContactReporting]: 'LeftFlankContacts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LeftFlankContacts
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def planetaries(self) -> 'List[ShaftHubConnectionSystemDeflection]':
        """List[ShaftHubConnectionSystemDeflection]: 'Planetaries' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.Planetaries
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def right_flank_contacts(self) -> 'List[_2784.SplineFlankContactReporting]':
        """List[SplineFlankContactReporting]: 'RightFlankContacts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.RightFlankContacts
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

    @property
    def tip_contacts(self) -> 'List[_2784.SplineFlankContactReporting]':
        """List[SplineFlankContactReporting]: 'TipContacts' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.TipContacts
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

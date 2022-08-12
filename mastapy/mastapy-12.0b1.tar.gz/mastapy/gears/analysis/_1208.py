"""_1208.py

GearMeshDesignAnalysis
"""


from mastapy.gears.analysis import (
    _1204, _1205, _1206, _1207,
    _1202
)
from mastapy._internal import constructor
from mastapy.gears.manufacturing.cylindrical import _602, _606, _607
from mastapy._internal.cast_exception import CastException
from mastapy.gears.manufacturing.bevel import (
    _765, _766, _767, _768,
    _778, _779, _784
)
from mastapy.gears.ltca import _830
from mastapy.gears.ltca.cylindrical import _846
from mastapy.gears.ltca.conical import _857
from mastapy.gears.load_case import _863
from mastapy.gears.load_case.worm import _866
from mastapy.gears.load_case.face import _869
from mastapy.gears.load_case.cylindrical import _872
from mastapy.gears.load_case.conical import _875
from mastapy.gears.load_case.concept import _878
from mastapy.gears.load_case.bevel import _881
from mastapy.gears.gear_two_d_fe_analysis import _888, _889
from mastapy.gears.gear_designs.face import _984
from mastapy.gears.gear_designs.cylindrical.micro_geometry import (
    _1090, _1091, _1092, _1094
)
from mastapy.gears.fe_model import _1185
from mastapy.gears.fe_model.cylindrical import _1189
from mastapy.gears.fe_model.conical import _1192
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_DESIGN_ANALYSIS = python_net_import('SMT.MastaAPI.Gears.Analysis', 'GearMeshDesignAnalysis')


__docformat__ = 'restructuredtext en'
__all__ = ('GearMeshDesignAnalysis',)


class GearMeshDesignAnalysis(_1202.AbstractGearMeshAnalysis):
    """GearMeshDesignAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_DESIGN_ANALYSIS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'GearMeshDesignAnalysis.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def gear_a(self) -> '_1204.GearDesignAnalysis':
        """GearDesignAnalysis: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _1204.GearDesignAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to GearDesignAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_manufacturing_config(self) -> '_602.CylindricalGearManufacturingConfig':
        """CylindricalGearManufacturingConfig: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _602.CylindricalGearManufacturingConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearManufacturingConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_manufactured_gear_duty_cycle(self) -> '_606.CylindricalManufacturedGearDutyCycle':
        """CylindricalManufacturedGearDutyCycle: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _606.CylindricalManufacturedGearDutyCycle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalManufacturedGearDutyCycle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_manufactured_gear_load_case(self) -> '_607.CylindricalManufacturedGearLoadCase':
        """CylindricalManufacturedGearLoadCase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _607.CylindricalManufacturedGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalManufacturedGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_conical_gear_manufacturing_analysis(self) -> '_765.ConicalGearManufacturingAnalysis':
        """ConicalGearManufacturingAnalysis: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _765.ConicalGearManufacturingAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConicalGearManufacturingAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_conical_gear_manufacturing_config(self) -> '_766.ConicalGearManufacturingConfig':
        """ConicalGearManufacturingConfig: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _766.ConicalGearManufacturingConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConicalGearManufacturingConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_conical_gear_micro_geometry_config(self) -> '_767.ConicalGearMicroGeometryConfig':
        """ConicalGearMicroGeometryConfig: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _767.ConicalGearMicroGeometryConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConicalGearMicroGeometryConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_conical_gear_micro_geometry_config_base(self) -> '_768.ConicalGearMicroGeometryConfigBase':
        """ConicalGearMicroGeometryConfigBase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _768.ConicalGearMicroGeometryConfigBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConicalGearMicroGeometryConfigBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_conical_pinion_manufacturing_config(self) -> '_778.ConicalPinionManufacturingConfig':
        """ConicalPinionManufacturingConfig: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _778.ConicalPinionManufacturingConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConicalPinionManufacturingConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_conical_pinion_micro_geometry_config(self) -> '_779.ConicalPinionMicroGeometryConfig':
        """ConicalPinionMicroGeometryConfig: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _779.ConicalPinionMicroGeometryConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConicalPinionMicroGeometryConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_conical_wheel_manufacturing_config(self) -> '_784.ConicalWheelManufacturingConfig':
        """ConicalWheelManufacturingConfig: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _784.ConicalWheelManufacturingConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConicalWheelManufacturingConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_gear_load_distribution_analysis(self) -> '_830.GearLoadDistributionAnalysis':
        """GearLoadDistributionAnalysis: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _830.GearLoadDistributionAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to GearLoadDistributionAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_load_distribution_analysis(self) -> '_846.CylindricalGearLoadDistributionAnalysis':
        """CylindricalGearLoadDistributionAnalysis: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _846.CylindricalGearLoadDistributionAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearLoadDistributionAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_conical_gear_load_distribution_analysis(self) -> '_857.ConicalGearLoadDistributionAnalysis':
        """ConicalGearLoadDistributionAnalysis: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _857.ConicalGearLoadDistributionAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConicalGearLoadDistributionAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_gear_load_case_base(self) -> '_863.GearLoadCaseBase':
        """GearLoadCaseBase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _863.GearLoadCaseBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to GearLoadCaseBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_worm_gear_load_case(self) -> '_866.WormGearLoadCase':
        """WormGearLoadCase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _866.WormGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to WormGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_face_gear_load_case(self) -> '_869.FaceGearLoadCase':
        """FaceGearLoadCase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _869.FaceGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to FaceGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_load_case(self) -> '_872.CylindricalGearLoadCase':
        """CylindricalGearLoadCase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _872.CylindricalGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_conical_gear_load_case(self) -> '_875.ConicalGearLoadCase':
        """ConicalGearLoadCase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _875.ConicalGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConicalGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_concept_gear_load_case(self) -> '_878.ConceptGearLoadCase':
        """ConceptGearLoadCase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _878.ConceptGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConceptGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_bevel_load_case(self) -> '_881.BevelLoadCase':
        """BevelLoadCase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _881.BevelLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to BevelLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_tiff_analysis(self) -> '_888.CylindricalGearTIFFAnalysis':
        """CylindricalGearTIFFAnalysis: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _888.CylindricalGearTIFFAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearTIFFAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_tiff_analysis_duty_cycle(self) -> '_889.CylindricalGearTIFFAnalysisDutyCycle':
        """CylindricalGearTIFFAnalysisDutyCycle: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _889.CylindricalGearTIFFAnalysisDutyCycle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearTIFFAnalysisDutyCycle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_face_gear_micro_geometry(self) -> '_984.FaceGearMicroGeometry':
        """FaceGearMicroGeometry: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _984.FaceGearMicroGeometry.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to FaceGearMicroGeometry. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_micro_geometry(self) -> '_1090.CylindricalGearMicroGeometry':
        """CylindricalGearMicroGeometry: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _1090.CylindricalGearMicroGeometry.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearMicroGeometry. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_micro_geometry_base(self) -> '_1091.CylindricalGearMicroGeometryBase':
        """CylindricalGearMicroGeometryBase: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _1091.CylindricalGearMicroGeometryBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearMicroGeometryBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_micro_geometry_duty_cycle(self) -> '_1092.CylindricalGearMicroGeometryDutyCycle':
        """CylindricalGearMicroGeometryDutyCycle: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _1092.CylindricalGearMicroGeometryDutyCycle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearMicroGeometryDutyCycle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_micro_geometry_per_tooth(self) -> '_1094.CylindricalGearMicroGeometryPerTooth':
        """CylindricalGearMicroGeometryPerTooth: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _1094.CylindricalGearMicroGeometryPerTooth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearMicroGeometryPerTooth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_gear_fe_model(self) -> '_1185.GearFEModel':
        """GearFEModel: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _1185.GearFEModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to GearFEModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_cylindrical_gear_fe_model(self) -> '_1189.CylindricalGearFEModel':
        """CylindricalGearFEModel: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _1189.CylindricalGearFEModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to CylindricalGearFEModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_conical_gear_fe_model(self) -> '_1192.ConicalGearFEModel':
        """ConicalGearFEModel: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _1192.ConicalGearFEModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to ConicalGearFEModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_gear_implementation_analysis(self) -> '_1205.GearImplementationAnalysis':
        """GearImplementationAnalysis: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _1205.GearImplementationAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to GearImplementationAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_gear_implementation_analysis_duty_cycle(self) -> '_1206.GearImplementationAnalysisDutyCycle':
        """GearImplementationAnalysisDutyCycle: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _1206.GearImplementationAnalysisDutyCycle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to GearImplementationAnalysisDutyCycle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_a_of_type_gear_implementation_detail(self) -> '_1207.GearImplementationDetail':
        """GearImplementationDetail: 'GearA' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearA
        if _1207.GearImplementationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_a to GearImplementationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b(self) -> '_1204.GearDesignAnalysis':
        """GearDesignAnalysis: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _1204.GearDesignAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to GearDesignAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_manufacturing_config(self) -> '_602.CylindricalGearManufacturingConfig':
        """CylindricalGearManufacturingConfig: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _602.CylindricalGearManufacturingConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearManufacturingConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_manufactured_gear_duty_cycle(self) -> '_606.CylindricalManufacturedGearDutyCycle':
        """CylindricalManufacturedGearDutyCycle: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _606.CylindricalManufacturedGearDutyCycle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalManufacturedGearDutyCycle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_manufactured_gear_load_case(self) -> '_607.CylindricalManufacturedGearLoadCase':
        """CylindricalManufacturedGearLoadCase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _607.CylindricalManufacturedGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalManufacturedGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_conical_gear_manufacturing_analysis(self) -> '_765.ConicalGearManufacturingAnalysis':
        """ConicalGearManufacturingAnalysis: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _765.ConicalGearManufacturingAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConicalGearManufacturingAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_conical_gear_manufacturing_config(self) -> '_766.ConicalGearManufacturingConfig':
        """ConicalGearManufacturingConfig: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _766.ConicalGearManufacturingConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConicalGearManufacturingConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_conical_gear_micro_geometry_config(self) -> '_767.ConicalGearMicroGeometryConfig':
        """ConicalGearMicroGeometryConfig: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _767.ConicalGearMicroGeometryConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConicalGearMicroGeometryConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_conical_gear_micro_geometry_config_base(self) -> '_768.ConicalGearMicroGeometryConfigBase':
        """ConicalGearMicroGeometryConfigBase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _768.ConicalGearMicroGeometryConfigBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConicalGearMicroGeometryConfigBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_conical_pinion_manufacturing_config(self) -> '_778.ConicalPinionManufacturingConfig':
        """ConicalPinionManufacturingConfig: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _778.ConicalPinionManufacturingConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConicalPinionManufacturingConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_conical_pinion_micro_geometry_config(self) -> '_779.ConicalPinionMicroGeometryConfig':
        """ConicalPinionMicroGeometryConfig: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _779.ConicalPinionMicroGeometryConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConicalPinionMicroGeometryConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_conical_wheel_manufacturing_config(self) -> '_784.ConicalWheelManufacturingConfig':
        """ConicalWheelManufacturingConfig: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _784.ConicalWheelManufacturingConfig.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConicalWheelManufacturingConfig. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_gear_load_distribution_analysis(self) -> '_830.GearLoadDistributionAnalysis':
        """GearLoadDistributionAnalysis: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _830.GearLoadDistributionAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to GearLoadDistributionAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_load_distribution_analysis(self) -> '_846.CylindricalGearLoadDistributionAnalysis':
        """CylindricalGearLoadDistributionAnalysis: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _846.CylindricalGearLoadDistributionAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearLoadDistributionAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_conical_gear_load_distribution_analysis(self) -> '_857.ConicalGearLoadDistributionAnalysis':
        """ConicalGearLoadDistributionAnalysis: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _857.ConicalGearLoadDistributionAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConicalGearLoadDistributionAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_gear_load_case_base(self) -> '_863.GearLoadCaseBase':
        """GearLoadCaseBase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _863.GearLoadCaseBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to GearLoadCaseBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_worm_gear_load_case(self) -> '_866.WormGearLoadCase':
        """WormGearLoadCase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _866.WormGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to WormGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_face_gear_load_case(self) -> '_869.FaceGearLoadCase':
        """FaceGearLoadCase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _869.FaceGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to FaceGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_load_case(self) -> '_872.CylindricalGearLoadCase':
        """CylindricalGearLoadCase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _872.CylindricalGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_conical_gear_load_case(self) -> '_875.ConicalGearLoadCase':
        """ConicalGearLoadCase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _875.ConicalGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConicalGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_concept_gear_load_case(self) -> '_878.ConceptGearLoadCase':
        """ConceptGearLoadCase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _878.ConceptGearLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConceptGearLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_bevel_load_case(self) -> '_881.BevelLoadCase':
        """BevelLoadCase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _881.BevelLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to BevelLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_tiff_analysis(self) -> '_888.CylindricalGearTIFFAnalysis':
        """CylindricalGearTIFFAnalysis: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _888.CylindricalGearTIFFAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearTIFFAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_tiff_analysis_duty_cycle(self) -> '_889.CylindricalGearTIFFAnalysisDutyCycle':
        """CylindricalGearTIFFAnalysisDutyCycle: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _889.CylindricalGearTIFFAnalysisDutyCycle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearTIFFAnalysisDutyCycle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_face_gear_micro_geometry(self) -> '_984.FaceGearMicroGeometry':
        """FaceGearMicroGeometry: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _984.FaceGearMicroGeometry.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to FaceGearMicroGeometry. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_micro_geometry(self) -> '_1090.CylindricalGearMicroGeometry':
        """CylindricalGearMicroGeometry: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _1090.CylindricalGearMicroGeometry.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearMicroGeometry. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_micro_geometry_base(self) -> '_1091.CylindricalGearMicroGeometryBase':
        """CylindricalGearMicroGeometryBase: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _1091.CylindricalGearMicroGeometryBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearMicroGeometryBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_micro_geometry_duty_cycle(self) -> '_1092.CylindricalGearMicroGeometryDutyCycle':
        """CylindricalGearMicroGeometryDutyCycle: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _1092.CylindricalGearMicroGeometryDutyCycle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearMicroGeometryDutyCycle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_micro_geometry_per_tooth(self) -> '_1094.CylindricalGearMicroGeometryPerTooth':
        """CylindricalGearMicroGeometryPerTooth: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _1094.CylindricalGearMicroGeometryPerTooth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearMicroGeometryPerTooth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_gear_fe_model(self) -> '_1185.GearFEModel':
        """GearFEModel: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _1185.GearFEModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to GearFEModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_cylindrical_gear_fe_model(self) -> '_1189.CylindricalGearFEModel':
        """CylindricalGearFEModel: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _1189.CylindricalGearFEModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to CylindricalGearFEModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_conical_gear_fe_model(self) -> '_1192.ConicalGearFEModel':
        """ConicalGearFEModel: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _1192.ConicalGearFEModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to ConicalGearFEModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_gear_implementation_analysis(self) -> '_1205.GearImplementationAnalysis':
        """GearImplementationAnalysis: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _1205.GearImplementationAnalysis.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to GearImplementationAnalysis. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_gear_implementation_analysis_duty_cycle(self) -> '_1206.GearImplementationAnalysisDutyCycle':
        """GearImplementationAnalysisDutyCycle: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _1206.GearImplementationAnalysisDutyCycle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to GearImplementationAnalysisDutyCycle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def gear_b_of_type_gear_implementation_detail(self) -> '_1207.GearImplementationDetail':
        """GearImplementationDetail: 'GearB' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.GearB
        if _1207.GearImplementationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast gear_b to GearImplementationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

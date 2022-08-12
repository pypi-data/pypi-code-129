"""overridable.py

Implementations of 'Overridable' in Python.
As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""


from enum import Enum
from typing import Generic, TypeVar

from mastapy._internal import (
    mixins, constructor, enum_with_selected_value_runtime, conversion
)
from mastapy._internal.python_net import python_net_import
from mastapy.gears import (
    _325, _310, _313, _328
)
from mastapy.materials import _242
from mastapy.electric_machines import _1243
from mastapy.bearings.bearing_designs.rolling import _2094, _2101, _2118
from mastapy.bearings import _1847
from mastapy.nodal_analysis.dev_tools_analyses import _194
from mastapy.nodal_analysis.fe_export_utility import _164
from mastapy.system_model.fe import _2341
from mastapy.materials.efficiency import _283, _285
from mastapy.bearings.bearing_results import _1891
from mastapy.system_model.part_model import _2418
from mastapy.bearings.bearing_results.rolling import _1915, _1920, _2013
from mastapy.gears.rating.cylindrical.iso6336 import _500
from mastapy.system_model.analyses_and_results.static_loads import _6837

_OVERRIDABLE = python_net_import('SMT.MastaAPI.Utility.Property', 'Overridable')


__docformat__ = 'restructuredtext en'
__all__ = (
    'Overridable_float', 'Overridable_int',
    'Overridable_ISOToleranceStandard', 'Overridable_CylindricalGearRatingMethods',
    'Overridable_CoefficientOfFrictionCalculationMethod', 'Overridable_DQAxisConvention',
    'Overridable_T', 'Overridable_bool',
    'Overridable_DiameterSeries', 'Overridable_HeightSeries',
    'Overridable_WidthSeries', 'Overridable_SealLocation',
    'Overridable_RigidCouplingType', 'Overridable_BoundaryConditionType',
    'Overridable_NodeSelectionDepthOption', 'Overridable_BearingEfficiencyRatingMethod',
    'Overridable_CylindricalRollerMaxAxialLoadMethod', 'Overridable_ContactRatioRequirements',
    'Overridable_MicroGeometryModel', 'Overridable_UnbalancedMassInclusionOption',
    'Overridable_BallBearingContactCalculation', 'Overridable_FrictionModelForGyroscopicMoment',
    'Overridable_RollerAnalysisMethod', 'Overridable_HelicalGearMicroGeometryOption',
    'Overridable_EfficiencyRatingMethod', 'Overridable_MeshStiffnessSource'
)


T = TypeVar('T')


class Overridable_float(float, mixins.OverridableMixin):
    """Overridable_float

    A specific implementation of 'Overridable' for 'float' types.
    """

    __hash__ = None
    __qualname__ = 'float'

    def __new__(cls, instance_to_wrap: 'Overridable_float.TYPE'):
        return float.__new__(cls, instance_to_wrap.Value if instance_to_wrap.Value is not None else 0.0)

    def __init__(self, instance_to_wrap: 'Overridable_float.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.Value
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_OVERRIDABLE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def implicit_type(cls) -> 'float':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return float

    @property
    def value(self) -> 'float':
        """float: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.Value
        return temp

    @property
    def overridden(self) -> 'bool':
        """bool: 'Overridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.Overridden
        return temp

    @property
    def override_value(self) -> 'float':
        """float: 'OverrideValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.OverrideValue
        return temp

    @property
    def calculated_value(self) -> 'float':
        """float: 'CalculatedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.CalculatedValue
        return temp


class Overridable_int(int, mixins.OverridableMixin):
    """Overridable_int

    A specific implementation of 'Overridable' for 'int' types.
    """

    __hash__ = None
    __qualname__ = 'int'

    def __new__(cls, instance_to_wrap: 'Overridable_int.TYPE'):
        return int.__new__(cls, instance_to_wrap.Value if instance_to_wrap.Value is not None else 0)

    def __init__(self, instance_to_wrap: 'Overridable_int.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.Value
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_OVERRIDABLE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def implicit_type(cls) -> 'int':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return int

    @property
    def value(self) -> 'int':
        """int: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.Value
        return temp

    @property
    def overridden(self) -> 'bool':
        """bool: 'Overridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.Overridden
        return temp

    @property
    def override_value(self) -> 'int':
        """int: 'OverrideValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.OverrideValue
        return temp

    @property
    def calculated_value(self) -> 'int':
        """int: 'CalculatedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.CalculatedValue
        return temp


class Overridable_ISOToleranceStandard(mixins.OverridableMixin, Enum):
    """Overridable_ISOToleranceStandard

    A specific implementation of 'Overridable' for 'ISOToleranceStandard' types.
    """

    __hash__ = None
    __qualname__ = 'ISOToleranceStandard'

    @classmethod
    def wrapper_type(cls) -> '_OVERRIDABLE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> '_325.ISOToleranceStandard':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _325.ISOToleranceStandard

    @classmethod
    def implicit_type(cls) -> '_325.ISOToleranceStandard.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _325.ISOToleranceStandard.type_()

    @property
    def value(self) -> '_325.ISOToleranceStandard':
        """ISOToleranceStandard: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def overridden(self) -> 'bool':
        """bool: 'Overridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def override_value(self) -> '_325.ISOToleranceStandard':
        """ISOToleranceStandard: 'OverrideValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def calculated_value(self) -> '_325.ISOToleranceStandard':
        """ISOToleranceStandard: 'CalculatedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class Overridable_CylindricalGearRatingMethods(mixins.OverridableMixin, Enum):
    """Overridable_CylindricalGearRatingMethods

    A specific implementation of 'Overridable' for 'CylindricalGearRatingMethods' types.
    """

    __hash__ = None
    __qualname__ = 'CylindricalGearRatingMethods'

    @classmethod
    def wrapper_type(cls) -> '_OVERRIDABLE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> '_242.CylindricalGearRatingMethods':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _242.CylindricalGearRatingMethods

    @classmethod
    def implicit_type(cls) -> '_242.CylindricalGearRatingMethods.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _242.CylindricalGearRatingMethods.type_()

    @property
    def value(self) -> '_242.CylindricalGearRatingMethods':
        """CylindricalGearRatingMethods: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def overridden(self) -> 'bool':
        """bool: 'Overridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def override_value(self) -> '_242.CylindricalGearRatingMethods':
        """CylindricalGearRatingMethods: 'OverrideValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def calculated_value(self) -> '_242.CylindricalGearRatingMethods':
        """CylindricalGearRatingMethods: 'CalculatedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class Overridable_CoefficientOfFrictionCalculationMethod(mixins.OverridableMixin, Enum):
    """Overridable_CoefficientOfFrictionCalculationMethod

    A specific implementation of 'Overridable' for 'CoefficientOfFrictionCalculationMethod' types.
    """

    __hash__ = None
    __qualname__ = 'CoefficientOfFrictionCalculationMethod'

    @classmethod
    def wrapper_type(cls) -> '_OVERRIDABLE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> '_310.CoefficientOfFrictionCalculationMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _310.CoefficientOfFrictionCalculationMethod

    @classmethod
    def implicit_type(cls) -> '_310.CoefficientOfFrictionCalculationMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _310.CoefficientOfFrictionCalculationMethod.type_()

    @property
    def value(self) -> '_310.CoefficientOfFrictionCalculationMethod':
        """CoefficientOfFrictionCalculationMethod: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def overridden(self) -> 'bool':
        """bool: 'Overridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def override_value(self) -> '_310.CoefficientOfFrictionCalculationMethod':
        """CoefficientOfFrictionCalculationMethod: 'OverrideValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def calculated_value(self) -> '_310.CoefficientOfFrictionCalculationMethod':
        """CoefficientOfFrictionCalculationMethod: 'CalculatedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class Overridable_DQAxisConvention(mixins.OverridableMixin, Enum):
    """Overridable_DQAxisConvention

    A specific implementation of 'Overridable' for 'DQAxisConvention' types.
    """

    __hash__ = None
    __qualname__ = 'DQAxisConvention'

    @classmethod
    def wrapper_type(cls) -> '_OVERRIDABLE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> '_1243.DQAxisConvention':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1243.DQAxisConvention

    @classmethod
    def implicit_type(cls) -> '_1243.DQAxisConvention.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1243.DQAxisConvention.type_()

    @property
    def value(self) -> '_1243.DQAxisConvention':
        """DQAxisConvention: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def overridden(self) -> 'bool':
        """bool: 'Overridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def override_value(self) -> '_1243.DQAxisConvention':
        """DQAxisConvention: 'OverrideValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def calculated_value(self) -> '_1243.DQAxisConvention':
        """DQAxisConvention: 'CalculatedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class Overridable_T(Generic[T], mixins.OverridableMixin):
    """Overridable_T

    A specific implementation of 'Overridable' for 'T' types.
    """

    __hash__ = None
    __qualname__ = 'T'

    def __init__(self, instance_to_wrap: 'Overridable_T.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.Value
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_OVERRIDABLE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def implicit_type(cls) -> 'T':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return T

    @property
    def value(self) -> 'T':
        """T: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.Value
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def overridden(self) -> 'bool':
        """bool: 'Overridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.Overridden
        return temp

    @property
    def override_value(self) -> 'T':
        """T: 'OverrideValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.OverrideValue
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def calculated_value(self) -> 'T':
        """T: 'CalculatedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.CalculatedValue
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None


class Overridable_bool(mixins.OverridableMixin):
    """Overridable_bool

    A specific implementation of 'Overridable' for 'bool' types.
    """

    __hash__ = None
    __qualname__ = 'bool'

    def __new__(cls, instance_to_wrap: 'Overridable_bool.TYPE'):
        return bool.__new__(cls, instance_to_wrap.Value if instance_to_wrap.Value is not None else False)

    def __init__(self, instance_to_wrap: 'Overridable_bool.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.Value
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_OVERRIDABLE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def implicit_type(cls) -> 'bool':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return bool

    @property
    def value(self) -> 'bool':
        """bool: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.Value
        return temp

    @property
    def overridden(self) -> 'bool':
        """bool: 'Overridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.Overridden
        return temp

    @property
    def override_value(self) -> 'bool':
        """bool: 'OverrideValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.OverrideValue
        return temp

    @property
    def calculated_value(self) -> 'bool':
        """bool: 'CalculatedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.CalculatedValue
        return temp

    def __bool__(self):
        return self.value


class Overridable_DiameterSeries(mixins.OverridableMixin, Enum):
    """Overridable_DiameterSeries

    A specific implementation of 'Overridable' for 'DiameterSeries' types.
    """

    __hash__ = None
    __qualname__ = 'DiameterSeries'

    @classmethod
    def wrapper_type(cls) -> '_OVERRIDABLE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> '_2094.DiameterSeries':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2094.DiameterSeries

    @classmethod
    def implicit_type(cls) -> '_2094.DiameterSeries.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2094.DiameterSeries.type_()

    @property
    def value(self) -> '_2094.DiameterSeries':
        """DiameterSeries: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def overridden(self) -> 'bool':
        """bool: 'Overridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def override_value(self) -> '_2094.DiameterSeries':
        """DiameterSeries: 'OverrideValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def calculated_value(self) -> '_2094.DiameterSeries':
        """DiameterSeries: 'CalculatedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class Overridable_HeightSeries(mixins.OverridableMixin, Enum):
    """Overridable_HeightSeries

    A specific implementation of 'Overridable' for 'HeightSeries' types.
    """

    __hash__ = None
    __qualname__ = 'HeightSeries'

    @classmethod
    def wrapper_type(cls) -> '_OVERRIDABLE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> '_2101.HeightSeries':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2101.HeightSeries

    @classmethod
    def implicit_type(cls) -> '_2101.HeightSeries.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2101.HeightSeries.type_()

    @property
    def value(self) -> '_2101.HeightSeries':
        """HeightSeries: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def overridden(self) -> 'bool':
        """bool: 'Overridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def override_value(self) -> '_2101.HeightSeries':
        """HeightSeries: 'OverrideValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def calculated_value(self) -> '_2101.HeightSeries':
        """HeightSeries: 'CalculatedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class Overridable_WidthSeries(mixins.OverridableMixin, Enum):
    """Overridable_WidthSeries

    A specific implementation of 'Overridable' for 'WidthSeries' types.
    """

    __hash__ = None
    __qualname__ = 'WidthSeries'

    @classmethod
    def wrapper_type(cls) -> '_OVERRIDABLE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> '_2118.WidthSeries':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2118.WidthSeries

    @classmethod
    def implicit_type(cls) -> '_2118.WidthSeries.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2118.WidthSeries.type_()

    @property
    def value(self) -> '_2118.WidthSeries':
        """WidthSeries: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def overridden(self) -> 'bool':
        """bool: 'Overridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def override_value(self) -> '_2118.WidthSeries':
        """WidthSeries: 'OverrideValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def calculated_value(self) -> '_2118.WidthSeries':
        """WidthSeries: 'CalculatedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class Overridable_SealLocation(mixins.OverridableMixin, Enum):
    """Overridable_SealLocation

    A specific implementation of 'Overridable' for 'SealLocation' types.
    """

    __hash__ = None
    __qualname__ = 'SealLocation'

    @classmethod
    def wrapper_type(cls) -> '_OVERRIDABLE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> '_1847.SealLocation':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1847.SealLocation

    @classmethod
    def implicit_type(cls) -> '_1847.SealLocation.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1847.SealLocation.type_()

    @property
    def value(self) -> '_1847.SealLocation':
        """SealLocation: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def overridden(self) -> 'bool':
        """bool: 'Overridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def override_value(self) -> '_1847.SealLocation':
        """SealLocation: 'OverrideValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def calculated_value(self) -> '_1847.SealLocation':
        """SealLocation: 'CalculatedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class Overridable_RigidCouplingType(mixins.OverridableMixin, Enum):
    """Overridable_RigidCouplingType

    A specific implementation of 'Overridable' for 'RigidCouplingType' types.
    """

    __hash__ = None
    __qualname__ = 'RigidCouplingType'

    @classmethod
    def wrapper_type(cls) -> '_OVERRIDABLE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> '_194.RigidCouplingType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _194.RigidCouplingType

    @classmethod
    def implicit_type(cls) -> '_194.RigidCouplingType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _194.RigidCouplingType.type_()

    @property
    def value(self) -> '_194.RigidCouplingType':
        """RigidCouplingType: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def overridden(self) -> 'bool':
        """bool: 'Overridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def override_value(self) -> '_194.RigidCouplingType':
        """RigidCouplingType: 'OverrideValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def calculated_value(self) -> '_194.RigidCouplingType':
        """RigidCouplingType: 'CalculatedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class Overridable_BoundaryConditionType(mixins.OverridableMixin, Enum):
    """Overridable_BoundaryConditionType

    A specific implementation of 'Overridable' for 'BoundaryConditionType' types.
    """

    __hash__ = None
    __qualname__ = 'BoundaryConditionType'

    @classmethod
    def wrapper_type(cls) -> '_OVERRIDABLE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> '_164.BoundaryConditionType':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _164.BoundaryConditionType

    @classmethod
    def implicit_type(cls) -> '_164.BoundaryConditionType.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _164.BoundaryConditionType.type_()

    @property
    def value(self) -> '_164.BoundaryConditionType':
        """BoundaryConditionType: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def overridden(self) -> 'bool':
        """bool: 'Overridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def override_value(self) -> '_164.BoundaryConditionType':
        """BoundaryConditionType: 'OverrideValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def calculated_value(self) -> '_164.BoundaryConditionType':
        """BoundaryConditionType: 'CalculatedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class Overridable_NodeSelectionDepthOption(mixins.OverridableMixin, Enum):
    """Overridable_NodeSelectionDepthOption

    A specific implementation of 'Overridable' for 'NodeSelectionDepthOption' types.
    """

    __hash__ = None
    __qualname__ = 'NodeSelectionDepthOption'

    @classmethod
    def wrapper_type(cls) -> '_OVERRIDABLE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> '_2341.NodeSelectionDepthOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2341.NodeSelectionDepthOption

    @classmethod
    def implicit_type(cls) -> '_2341.NodeSelectionDepthOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2341.NodeSelectionDepthOption.type_()

    @property
    def value(self) -> '_2341.NodeSelectionDepthOption':
        """NodeSelectionDepthOption: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def overridden(self) -> 'bool':
        """bool: 'Overridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def override_value(self) -> '_2341.NodeSelectionDepthOption':
        """NodeSelectionDepthOption: 'OverrideValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def calculated_value(self) -> '_2341.NodeSelectionDepthOption':
        """NodeSelectionDepthOption: 'CalculatedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class Overridable_BearingEfficiencyRatingMethod(mixins.OverridableMixin, Enum):
    """Overridable_BearingEfficiencyRatingMethod

    A specific implementation of 'Overridable' for 'BearingEfficiencyRatingMethod' types.
    """

    __hash__ = None
    __qualname__ = 'BearingEfficiencyRatingMethod'

    @classmethod
    def wrapper_type(cls) -> '_OVERRIDABLE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> '_283.BearingEfficiencyRatingMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _283.BearingEfficiencyRatingMethod

    @classmethod
    def implicit_type(cls) -> '_283.BearingEfficiencyRatingMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _283.BearingEfficiencyRatingMethod.type_()

    @property
    def value(self) -> '_283.BearingEfficiencyRatingMethod':
        """BearingEfficiencyRatingMethod: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def overridden(self) -> 'bool':
        """bool: 'Overridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def override_value(self) -> '_283.BearingEfficiencyRatingMethod':
        """BearingEfficiencyRatingMethod: 'OverrideValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def calculated_value(self) -> '_283.BearingEfficiencyRatingMethod':
        """BearingEfficiencyRatingMethod: 'CalculatedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class Overridable_CylindricalRollerMaxAxialLoadMethod(mixins.OverridableMixin, Enum):
    """Overridable_CylindricalRollerMaxAxialLoadMethod

    A specific implementation of 'Overridable' for 'CylindricalRollerMaxAxialLoadMethod' types.
    """

    __hash__ = None
    __qualname__ = 'CylindricalRollerMaxAxialLoadMethod'

    @classmethod
    def wrapper_type(cls) -> '_OVERRIDABLE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> '_1891.CylindricalRollerMaxAxialLoadMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1891.CylindricalRollerMaxAxialLoadMethod

    @classmethod
    def implicit_type(cls) -> '_1891.CylindricalRollerMaxAxialLoadMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1891.CylindricalRollerMaxAxialLoadMethod.type_()

    @property
    def value(self) -> '_1891.CylindricalRollerMaxAxialLoadMethod':
        """CylindricalRollerMaxAxialLoadMethod: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def overridden(self) -> 'bool':
        """bool: 'Overridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def override_value(self) -> '_1891.CylindricalRollerMaxAxialLoadMethod':
        """CylindricalRollerMaxAxialLoadMethod: 'OverrideValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def calculated_value(self) -> '_1891.CylindricalRollerMaxAxialLoadMethod':
        """CylindricalRollerMaxAxialLoadMethod: 'CalculatedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class Overridable_ContactRatioRequirements(mixins.OverridableMixin, Enum):
    """Overridable_ContactRatioRequirements

    A specific implementation of 'Overridable' for 'ContactRatioRequirements' types.
    """

    __hash__ = None
    __qualname__ = 'ContactRatioRequirements'

    @classmethod
    def wrapper_type(cls) -> '_OVERRIDABLE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> '_313.ContactRatioRequirements':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _313.ContactRatioRequirements

    @classmethod
    def implicit_type(cls) -> '_313.ContactRatioRequirements.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _313.ContactRatioRequirements.type_()

    @property
    def value(self) -> '_313.ContactRatioRequirements':
        """ContactRatioRequirements: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def overridden(self) -> 'bool':
        """bool: 'Overridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def override_value(self) -> '_313.ContactRatioRequirements':
        """ContactRatioRequirements: 'OverrideValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def calculated_value(self) -> '_313.ContactRatioRequirements':
        """ContactRatioRequirements: 'CalculatedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class Overridable_MicroGeometryModel(mixins.OverridableMixin, Enum):
    """Overridable_MicroGeometryModel

    A specific implementation of 'Overridable' for 'MicroGeometryModel' types.
    """

    __hash__ = None
    __qualname__ = 'MicroGeometryModel'

    @classmethod
    def wrapper_type(cls) -> '_OVERRIDABLE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> '_328.MicroGeometryModel':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _328.MicroGeometryModel

    @classmethod
    def implicit_type(cls) -> '_328.MicroGeometryModel.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _328.MicroGeometryModel.type_()

    @property
    def value(self) -> '_328.MicroGeometryModel':
        """MicroGeometryModel: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def overridden(self) -> 'bool':
        """bool: 'Overridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def override_value(self) -> '_328.MicroGeometryModel':
        """MicroGeometryModel: 'OverrideValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def calculated_value(self) -> '_328.MicroGeometryModel':
        """MicroGeometryModel: 'CalculatedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class Overridable_UnbalancedMassInclusionOption(mixins.OverridableMixin, Enum):
    """Overridable_UnbalancedMassInclusionOption

    A specific implementation of 'Overridable' for 'UnbalancedMassInclusionOption' types.
    """

    __hash__ = None
    __qualname__ = 'UnbalancedMassInclusionOption'

    @classmethod
    def wrapper_type(cls) -> '_OVERRIDABLE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> '_2418.UnbalancedMassInclusionOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2418.UnbalancedMassInclusionOption

    @classmethod
    def implicit_type(cls) -> '_2418.UnbalancedMassInclusionOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2418.UnbalancedMassInclusionOption.type_()

    @property
    def value(self) -> '_2418.UnbalancedMassInclusionOption':
        """UnbalancedMassInclusionOption: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def overridden(self) -> 'bool':
        """bool: 'Overridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def override_value(self) -> '_2418.UnbalancedMassInclusionOption':
        """UnbalancedMassInclusionOption: 'OverrideValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def calculated_value(self) -> '_2418.UnbalancedMassInclusionOption':
        """UnbalancedMassInclusionOption: 'CalculatedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class Overridable_BallBearingContactCalculation(mixins.OverridableMixin, Enum):
    """Overridable_BallBearingContactCalculation

    A specific implementation of 'Overridable' for 'BallBearingContactCalculation' types.
    """

    __hash__ = None
    __qualname__ = 'BallBearingContactCalculation'

    @classmethod
    def wrapper_type(cls) -> '_OVERRIDABLE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> '_1915.BallBearingContactCalculation':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1915.BallBearingContactCalculation

    @classmethod
    def implicit_type(cls) -> '_1915.BallBearingContactCalculation.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1915.BallBearingContactCalculation.type_()

    @property
    def value(self) -> '_1915.BallBearingContactCalculation':
        """BallBearingContactCalculation: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def overridden(self) -> 'bool':
        """bool: 'Overridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def override_value(self) -> '_1915.BallBearingContactCalculation':
        """BallBearingContactCalculation: 'OverrideValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def calculated_value(self) -> '_1915.BallBearingContactCalculation':
        """BallBearingContactCalculation: 'CalculatedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class Overridable_FrictionModelForGyroscopicMoment(mixins.OverridableMixin, Enum):
    """Overridable_FrictionModelForGyroscopicMoment

    A specific implementation of 'Overridable' for 'FrictionModelForGyroscopicMoment' types.
    """

    __hash__ = None
    __qualname__ = 'FrictionModelForGyroscopicMoment'

    @classmethod
    def wrapper_type(cls) -> '_OVERRIDABLE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> '_1920.FrictionModelForGyroscopicMoment':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _1920.FrictionModelForGyroscopicMoment

    @classmethod
    def implicit_type(cls) -> '_1920.FrictionModelForGyroscopicMoment.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1920.FrictionModelForGyroscopicMoment.type_()

    @property
    def value(self) -> '_1920.FrictionModelForGyroscopicMoment':
        """FrictionModelForGyroscopicMoment: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def overridden(self) -> 'bool':
        """bool: 'Overridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def override_value(self) -> '_1920.FrictionModelForGyroscopicMoment':
        """FrictionModelForGyroscopicMoment: 'OverrideValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def calculated_value(self) -> '_1920.FrictionModelForGyroscopicMoment':
        """FrictionModelForGyroscopicMoment: 'CalculatedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class Overridable_RollerAnalysisMethod(mixins.OverridableMixin, Enum):
    """Overridable_RollerAnalysisMethod

    A specific implementation of 'Overridable' for 'RollerAnalysisMethod' types.
    """

    __hash__ = None
    __qualname__ = 'RollerAnalysisMethod'

    @classmethod
    def wrapper_type(cls) -> '_OVERRIDABLE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> '_2013.RollerAnalysisMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _2013.RollerAnalysisMethod

    @classmethod
    def implicit_type(cls) -> '_2013.RollerAnalysisMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2013.RollerAnalysisMethod.type_()

    @property
    def value(self) -> '_2013.RollerAnalysisMethod':
        """RollerAnalysisMethod: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def overridden(self) -> 'bool':
        """bool: 'Overridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def override_value(self) -> '_2013.RollerAnalysisMethod':
        """RollerAnalysisMethod: 'OverrideValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def calculated_value(self) -> '_2013.RollerAnalysisMethod':
        """RollerAnalysisMethod: 'CalculatedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class Overridable_HelicalGearMicroGeometryOption(mixins.OverridableMixin, Enum):
    """Overridable_HelicalGearMicroGeometryOption

    A specific implementation of 'Overridable' for 'HelicalGearMicroGeometryOption' types.
    """

    __hash__ = None
    __qualname__ = 'HelicalGearMicroGeometryOption'

    @classmethod
    def wrapper_type(cls) -> '_OVERRIDABLE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> '_500.HelicalGearMicroGeometryOption':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _500.HelicalGearMicroGeometryOption

    @classmethod
    def implicit_type(cls) -> '_500.HelicalGearMicroGeometryOption.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _500.HelicalGearMicroGeometryOption.type_()

    @property
    def value(self) -> '_500.HelicalGearMicroGeometryOption':
        """HelicalGearMicroGeometryOption: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def overridden(self) -> 'bool':
        """bool: 'Overridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def override_value(self) -> '_500.HelicalGearMicroGeometryOption':
        """HelicalGearMicroGeometryOption: 'OverrideValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def calculated_value(self) -> '_500.HelicalGearMicroGeometryOption':
        """HelicalGearMicroGeometryOption: 'CalculatedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class Overridable_EfficiencyRatingMethod(mixins.OverridableMixin, Enum):
    """Overridable_EfficiencyRatingMethod

    A specific implementation of 'Overridable' for 'EfficiencyRatingMethod' types.
    """

    __hash__ = None
    __qualname__ = 'EfficiencyRatingMethod'

    @classmethod
    def wrapper_type(cls) -> '_OVERRIDABLE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> '_285.EfficiencyRatingMethod':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _285.EfficiencyRatingMethod

    @classmethod
    def implicit_type(cls) -> '_285.EfficiencyRatingMethod.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _285.EfficiencyRatingMethod.type_()

    @property
    def value(self) -> '_285.EfficiencyRatingMethod':
        """EfficiencyRatingMethod: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def overridden(self) -> 'bool':
        """bool: 'Overridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def override_value(self) -> '_285.EfficiencyRatingMethod':
        """EfficiencyRatingMethod: 'OverrideValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def calculated_value(self) -> '_285.EfficiencyRatingMethod':
        """EfficiencyRatingMethod: 'CalculatedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None


class Overridable_MeshStiffnessSource(mixins.OverridableMixin, Enum):
    """Overridable_MeshStiffnessSource

    A specific implementation of 'Overridable' for 'MeshStiffnessSource' types.
    """

    __hash__ = None
    __qualname__ = 'MeshStiffnessSource'

    @classmethod
    def wrapper_type(cls) -> '_OVERRIDABLE':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _OVERRIDABLE

    @classmethod
    def wrapped_type(cls) -> '_6837.MeshStiffnessSource':
        """Wrapped Pythonnet type of this class.

        Note:
            This property is readonly
        """

        return _6837.MeshStiffnessSource

    @classmethod
    def implicit_type(cls) -> '_6837.MeshStiffnessSource.type_()':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6837.MeshStiffnessSource.type_()

    @property
    def value(self) -> '_6837.MeshStiffnessSource':
        """MeshStiffnessSource: 'Value' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def overridden(self) -> 'bool':
        """bool: 'Overridden' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def override_value(self) -> '_6837.MeshStiffnessSource':
        """MeshStiffnessSource: 'OverrideValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

    @property
    def calculated_value(self) -> '_6837.MeshStiffnessSource':
        """MeshStiffnessSource: 'CalculatedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        return None

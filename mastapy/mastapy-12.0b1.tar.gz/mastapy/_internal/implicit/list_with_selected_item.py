"""list_with_selected_item.py

Implementations of 'ListWithSelectedItem' in Python.
As Python does not have an implicit operator, this is the next
best solution for implementing these types properly.
"""


from typing import List, Generic, TypeVar

from mastapy._internal import mixins, constructor, conversion
from mastapy._internal.python_net import python_net_import
from mastapy.gears.ltca.cylindrical import _846, _847
from mastapy.gears.manufacturing.cylindrical import _615
from mastapy.gears.manufacturing.bevel import _781
from mastapy.electric_machines import (
    _1248, _1272, _1245, _1231,
    _1255, _1263, _1266, _1279,
    _1281
)
from mastapy.electric_machines.results import _1294, _1310, _1311
from mastapy._internal.cast_exception import CastException
from mastapy.utility import _1560
from mastapy.utility.units_and_measurements import (
    _1570, _1562, _1563, _1564,
    _1568, _1569, _1571, _1565
)
from mastapy.utility.units_and_measurements.measurements import (
    _1572, _1573, _1574, _1575,
    _1576, _1577, _1578, _1579,
    _1580, _1581, _1582, _1583,
    _1584, _1585, _1586, _1587,
    _1588, _1589, _1590, _1591,
    _1592, _1593, _1594, _1595,
    _1596, _1597, _1598, _1599,
    _1600, _1601, _1602, _1603,
    _1604, _1605, _1606, _1607,
    _1608, _1609, _1610, _1611,
    _1612, _1613, _1614, _1615,
    _1616, _1617, _1618, _1619,
    _1620, _1621, _1622, _1623,
    _1624, _1625, _1626, _1627,
    _1628, _1629, _1630, _1631,
    _1632, _1633, _1634, _1635,
    _1636, _1637, _1638, _1639,
    _1640, _1641, _1642, _1643,
    _1644, _1645, _1646, _1647,
    _1648, _1649, _1650, _1651,
    _1652, _1653, _1654, _1655,
    _1656, _1657, _1658, _1659,
    _1660, _1661, _1662, _1663,
    _1664, _1665, _1666, _1667,
    _1668, _1669, _1670, _1671,
    _1672, _1673, _1674, _1675,
    _1676, _1677, _1678, _1679,
    _1680, _1681, _1682, _1683,
    _1684, _1685, _1686, _1687,
    _1688, _1689, _1690, _1691,
    _1692, _1693, _1694, _1695,
    _1696, _1697
)
from mastapy.utility.file_access_helpers import _1773
from mastapy.system_model.part_model import (
    _2412, _2384, _2376, _2377,
    _2380, _2382, _2387, _2388,
    _2392, _2393, _2395, _2402,
    _2403, _2404, _2406, _2409,
    _2411, _2417, _2419
)
from mastapy.system_model.analyses_and_results.harmonic_analyses import (
    _5603, _5656, _5657, _5658,
    _5659, _5660, _5661, _5662,
    _5663, _5664, _5665, _5666,
    _5676, _5678, _5679, _5681,
    _5710, _5727, _5752
)
from mastapy._internal.tuple_with_name import TupleWithName
from mastapy.system_model.analyses_and_results.system_deflections import (
    _2693, _2628, _2635, _2640,
    _2654, _2658, _2673, _2674,
    _2675, _2688, _2697, _2702,
    _2705, _2708, _2741, _2747,
    _2750, _2770, _2773, _2679,
    _2680, _2681, _2684
)
from mastapy.system_model.part_model.gears import (
    _2471, _2453, _2455, _2459,
    _2461, _2463, _2465, _2468,
    _2474, _2476, _2478, _2480,
    _2481, _2483, _2485, _2487,
    _2491, _2493, _2452, _2454,
    _2456, _2457, _2458, _2460,
    _2462, _2464, _2466, _2467,
    _2469, _2473, _2475, _2477,
    _2479, _2482, _2484, _2486,
    _2488, _2489, _2490, _2492
)
from mastapy.system_model.fe import _2324, _2322, _2313
from mastapy.system_model.part_model.shaft_model import _2422
from mastapy.system_model.part_model.cycloidal import _2508, _2509
from mastapy.system_model.part_model.couplings import (
    _2518, _2521, _2523, _2526,
    _2528, _2529, _2535, _2537,
    _2540, _2543, _2544, _2545,
    _2547, _2549
)
from mastapy.system_model.fe.links import (
    _2357, _2358, _2360, _2361,
    _2362, _2363, _2364, _2365,
    _2366, _2367, _2368, _2369,
    _2370, _2371
)
from mastapy.system_model.part_model.part_groups import _2427
from mastapy.gears.gear_designs import _941
from mastapy.gears.gear_designs.zerol_bevel import _945
from mastapy.gears.gear_designs.worm import _950
from mastapy.gears.gear_designs.straight_bevel import _954
from mastapy.gears.gear_designs.straight_bevel_diff import _958
from mastapy.gears.gear_designs.spiral_bevel import _962
from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _966
from mastapy.gears.gear_designs.klingelnberg_hypoid import _970
from mastapy.gears.gear_designs.klingelnberg_conical import _974
from mastapy.gears.gear_designs.hypoid import _978
from mastapy.gears.gear_designs.face import _986
from mastapy.gears.gear_designs.cylindrical import _1019, _1031
from mastapy.gears.gear_designs.conical import _1144
from mastapy.gears.gear_designs.concept import _1166
from mastapy.gears.gear_designs.bevel import _1170
from mastapy.gears.gear_designs.agma_gleason_conical import _1183
from mastapy.system_model.analyses_and_results.load_case_groups import _5587, _5588
from mastapy.nodal_analysis.component_mode_synthesis import _216, _217
from mastapy.system_model.analyses_and_results.harmonic_analyses.results import _5768
from mastapy.system_model.analyses_and_results.static_loads import _6719, _6726
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4317

_ARRAY = python_net_import('System', 'Array')
_LIST_WITH_SELECTED_ITEM = python_net_import('SMT.MastaAPI.Utility.Property', 'ListWithSelectedItem')


__docformat__ = 'restructuredtext en'
__all__ = (
    'ListWithSelectedItem_str', 'ListWithSelectedItem_int',
    'ListWithSelectedItem_T', 'ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis',
    'ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis', 'ListWithSelectedItem_CylindricalSetManufacturingConfig',
    'ListWithSelectedItem_ConicalSetManufacturingConfig', 'ListWithSelectedItem_ElectricMachineSetup',
    'ListWithSelectedItem_float', 'ListWithSelectedItem_ElectricMachineResults',
    'ListWithSelectedItem_RotorSkewSlice', 'ListWithSelectedItem_SystemDirectory',
    'ListWithSelectedItem_Unit', 'ListWithSelectedItem_MeasurementBase',
    'ListWithSelectedItem_ColumnTitle', 'ListWithSelectedItem_PowerLoad',
    'ListWithSelectedItem_AbstractPeriodicExcitationDetail', 'ListWithSelectedItem_TupleWithName',
    'ListWithSelectedItem_GearMeshSystemDeflection', 'ListWithSelectedItem_GearSet',
    'ListWithSelectedItem_FESubstructureNode', 'ListWithSelectedItem_Component',
    'ListWithSelectedItem_Datum', 'ListWithSelectedItem_FELink',
    'ListWithSelectedItem_FESubstructure', 'ListWithSelectedItem_CylindricalGear',
    'ListWithSelectedItem_ElectricMachineDetail', 'ListWithSelectedItem_GuideDxfModel',
    'ListWithSelectedItem_ConcentricPartGroup', 'ListWithSelectedItem_CylindricalGearSet',
    'ListWithSelectedItem_GearSetDesign', 'ListWithSelectedItem_ShaftHubConnection',
    'ListWithSelectedItem_TSelectableItem', 'ListWithSelectedItem_CylindricalGearSystemDeflection',
    'ListWithSelectedItem_DesignState', 'ListWithSelectedItem_FEPart',
    'ListWithSelectedItem_TPartAnalysis', 'ListWithSelectedItem_CMSElementFaceGroup',
    'ListWithSelectedItem_ResultLocationSelectionGroup', 'ListWithSelectedItem_StaticLoadCase',
    'ListWithSelectedItem_DutyCycle', 'ListWithSelectedItem_ElectricMachineDataSet',
    'ListWithSelectedItem_PointLoad'
)


T = TypeVar('T')
TSelectableItem = TypeVar('TSelectableItem')
TPartAnalysis = TypeVar('TPartAnalysis')


class ListWithSelectedItem_str(str, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_str

    A specific implementation of 'ListWithSelectedItem' for 'str' types.
    """

    __hash__ = None
    __qualname__ = 'str'

    def __new__(cls, instance_to_wrap: 'ListWithSelectedItem_str.TYPE'):
        return str.__new__(cls, instance_to_wrap.SelectedValue if instance_to_wrap.SelectedValue is not None else '')

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_str.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'str':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return str

    @property
    def selected_value(self) -> 'str':
        """str: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        return temp

    @property
    def available_values(self) -> 'List[str]':
        """List[str]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp, str)
        return value


class ListWithSelectedItem_int(int, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_int

    A specific implementation of 'ListWithSelectedItem' for 'int' types.
    """

    __hash__ = None
    __qualname__ = 'int'

    def __new__(cls, instance_to_wrap: 'ListWithSelectedItem_int.TYPE'):
        return int.__new__(cls, instance_to_wrap.SelectedValue if instance_to_wrap.SelectedValue is not None else 0)

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_int.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'int':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return int

    @property
    def selected_value(self) -> 'int':
        """int: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        return temp

    @property
    def available_values(self) -> 'List[int]':
        """List[int]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp, int)
        return value


class ListWithSelectedItem_T(Generic[T], mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_T

    A specific implementation of 'ListWithSelectedItem' for 'T' types.
    """

    __hash__ = None
    __qualname__ = 'T'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_T.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'T':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return T

    @property
    def selected_value(self) -> 'T':
        """T: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[T]':
        """List[T]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis(_846.CylindricalGearLoadDistributionAnalysis, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalGearLoadDistributionAnalysis' types.
    """

    __hash__ = None
    __qualname__ = 'CylindricalGearLoadDistributionAnalysis'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalGearLoadDistributionAnalysis.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_846.CylindricalGearLoadDistributionAnalysis.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _846.CylindricalGearLoadDistributionAnalysis.TYPE

    @property
    def selected_value(self) -> '_846.CylindricalGearLoadDistributionAnalysis':
        """CylindricalGearLoadDistributionAnalysis: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_846.CylindricalGearLoadDistributionAnalysis]':
        """List[CylindricalGearLoadDistributionAnalysis]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis(_847.CylindricalGearMeshLoadDistributionAnalysis, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalGearMeshLoadDistributionAnalysis' types.
    """

    __hash__ = None
    __qualname__ = 'CylindricalGearMeshLoadDistributionAnalysis'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalGearMeshLoadDistributionAnalysis.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_847.CylindricalGearMeshLoadDistributionAnalysis.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _847.CylindricalGearMeshLoadDistributionAnalysis.TYPE

    @property
    def selected_value(self) -> '_847.CylindricalGearMeshLoadDistributionAnalysis':
        """CylindricalGearMeshLoadDistributionAnalysis: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_847.CylindricalGearMeshLoadDistributionAnalysis]':
        """List[CylindricalGearMeshLoadDistributionAnalysis]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CylindricalSetManufacturingConfig(_615.CylindricalSetManufacturingConfig, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CylindricalSetManufacturingConfig

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalSetManufacturingConfig' types.
    """

    __hash__ = None
    __qualname__ = 'CylindricalSetManufacturingConfig'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalSetManufacturingConfig.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_615.CylindricalSetManufacturingConfig.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _615.CylindricalSetManufacturingConfig.TYPE

    @property
    def selected_value(self) -> '_615.CylindricalSetManufacturingConfig':
        """CylindricalSetManufacturingConfig: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_615.CylindricalSetManufacturingConfig]':
        """List[CylindricalSetManufacturingConfig]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ConicalSetManufacturingConfig(_781.ConicalSetManufacturingConfig, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ConicalSetManufacturingConfig

    A specific implementation of 'ListWithSelectedItem' for 'ConicalSetManufacturingConfig' types.
    """

    __hash__ = None
    __qualname__ = 'ConicalSetManufacturingConfig'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ConicalSetManufacturingConfig.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_781.ConicalSetManufacturingConfig.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _781.ConicalSetManufacturingConfig.TYPE

    @property
    def selected_value(self) -> '_781.ConicalSetManufacturingConfig':
        """ConicalSetManufacturingConfig: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_781.ConicalSetManufacturingConfig]':
        """List[ConicalSetManufacturingConfig]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ElectricMachineSetup(_1248.ElectricMachineSetup, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ElectricMachineSetup

    A specific implementation of 'ListWithSelectedItem' for 'ElectricMachineSetup' types.
    """

    __hash__ = None
    __qualname__ = 'ElectricMachineSetup'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ElectricMachineSetup.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1248.ElectricMachineSetup.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1248.ElectricMachineSetup.TYPE

    @property
    def selected_value(self) -> '_1248.ElectricMachineSetup':
        """ElectricMachineSetup: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1248.ElectricMachineSetup]':
        """List[ElectricMachineSetup]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_float(float, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_float

    A specific implementation of 'ListWithSelectedItem' for 'float' types.
    """

    __hash__ = None
    __qualname__ = 'float'

    def __new__(cls, instance_to_wrap: 'ListWithSelectedItem_float.TYPE'):
        return float.__new__(cls, instance_to_wrap.SelectedValue if instance_to_wrap.SelectedValue is not None else 0.0)

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_float.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'float':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return float

    @property
    def selected_value(self) -> 'float':
        """float: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        return temp

    @property
    def available_values(self) -> 'List[float]':
        """List[float]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_list_float(temp)
        return value


class ListWithSelectedItem_ElectricMachineResults(_1294.ElectricMachineResults, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ElectricMachineResults

    A specific implementation of 'ListWithSelectedItem' for 'ElectricMachineResults' types.
    """

    __hash__ = None
    __qualname__ = 'ElectricMachineResults'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ElectricMachineResults.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1294.ElectricMachineResults.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1294.ElectricMachineResults.TYPE

    @property
    def selected_value(self) -> '_1294.ElectricMachineResults':
        """ElectricMachineResults: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1294.ElectricMachineResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachineResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_on_load_electric_machine_results(self) -> '_1310.OnLoadElectricMachineResults':
        """OnLoadElectricMachineResults: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1310.OnLoadElectricMachineResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to OnLoadElectricMachineResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_open_circuit_electric_machine_results(self) -> '_1311.OpenCircuitElectricMachineResults':
        """OpenCircuitElectricMachineResults: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1311.OpenCircuitElectricMachineResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to OpenCircuitElectricMachineResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1294.ElectricMachineResults]':
        """List[ElectricMachineResults]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_RotorSkewSlice(_1272.RotorSkewSlice, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_RotorSkewSlice

    A specific implementation of 'ListWithSelectedItem' for 'RotorSkewSlice' types.
    """

    __hash__ = None
    __qualname__ = 'RotorSkewSlice'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_RotorSkewSlice.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1272.RotorSkewSlice.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1272.RotorSkewSlice.TYPE

    @property
    def selected_value(self) -> '_1272.RotorSkewSlice':
        """RotorSkewSlice: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1272.RotorSkewSlice]':
        """List[RotorSkewSlice]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_SystemDirectory(_1560.SystemDirectory, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_SystemDirectory

    A specific implementation of 'ListWithSelectedItem' for 'SystemDirectory' types.
    """

    __hash__ = None
    __qualname__ = 'SystemDirectory'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_SystemDirectory.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1560.SystemDirectory.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1560.SystemDirectory.TYPE

    @property
    def selected_value(self) -> '_1560.SystemDirectory':
        """SystemDirectory: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1560.SystemDirectory]':
        """List[SystemDirectory]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_Unit(_1570.Unit, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_Unit

    A specific implementation of 'ListWithSelectedItem' for 'Unit' types.
    """

    __hash__ = None
    __qualname__ = 'Unit'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_Unit.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1570.Unit.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1570.Unit.TYPE

    @property
    def selected_value(self) -> '_1570.Unit':
        """Unit: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1570.Unit.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Unit. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1570.Unit]':
        """List[Unit]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_MeasurementBase(_1565.MeasurementBase, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_MeasurementBase

    A specific implementation of 'ListWithSelectedItem' for 'MeasurementBase' types.
    """

    __hash__ = None
    __qualname__ = 'MeasurementBase'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_MeasurementBase.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1565.MeasurementBase.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1565.MeasurementBase.TYPE

    @property
    def selected_value(self) -> '_1565.MeasurementBase':
        """MeasurementBase: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1565.MeasurementBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MeasurementBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_acceleration(self) -> '_1572.Acceleration':
        """Acceleration: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1572.Acceleration.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Acceleration. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_angle(self) -> '_1573.Angle':
        """Angle: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1573.Angle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Angle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_angle_per_unit_temperature(self) -> '_1574.AnglePerUnitTemperature':
        """AnglePerUnitTemperature: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1574.AnglePerUnitTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AnglePerUnitTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_angle_small(self) -> '_1575.AngleSmall':
        """AngleSmall: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1575.AngleSmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AngleSmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_angle_very_small(self) -> '_1576.AngleVerySmall':
        """AngleVerySmall: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1576.AngleVerySmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AngleVerySmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_angular_acceleration(self) -> '_1577.AngularAcceleration':
        """AngularAcceleration: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1577.AngularAcceleration.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AngularAcceleration. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_angular_compliance(self) -> '_1578.AngularCompliance':
        """AngularCompliance: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1578.AngularCompliance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AngularCompliance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_angular_jerk(self) -> '_1579.AngularJerk':
        """AngularJerk: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1579.AngularJerk.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AngularJerk. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_angular_stiffness(self) -> '_1580.AngularStiffness':
        """AngularStiffness: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1580.AngularStiffness.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AngularStiffness. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_angular_velocity(self) -> '_1581.AngularVelocity':
        """AngularVelocity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1581.AngularVelocity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AngularVelocity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_area(self) -> '_1582.Area':
        """Area: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1582.Area.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Area. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_area_small(self) -> '_1583.AreaSmall':
        """AreaSmall: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1583.AreaSmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AreaSmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_current_density(self) -> '_1584.CurrentDensity':
        """CurrentDensity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1584.CurrentDensity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CurrentDensity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_current_per_length(self) -> '_1585.CurrentPerLength':
        """CurrentPerLength: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1585.CurrentPerLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CurrentPerLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cycles(self) -> '_1586.Cycles':
        """Cycles: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1586.Cycles.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Cycles. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_damage(self) -> '_1587.Damage':
        """Damage: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1587.Damage.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Damage. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_damage_rate(self) -> '_1588.DamageRate':
        """DamageRate: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1588.DamageRate.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to DamageRate. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_data_size(self) -> '_1589.DataSize':
        """DataSize: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1589.DataSize.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to DataSize. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_decibel(self) -> '_1590.Decibel':
        """Decibel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1590.Decibel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Decibel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_density(self) -> '_1591.Density':
        """Density: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1591.Density.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Density. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electrical_resistance(self) -> '_1592.ElectricalResistance':
        """ElectricalResistance: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1592.ElectricalResistance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricalResistance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electrical_resistivity(self) -> '_1593.ElectricalResistivity':
        """ElectricalResistivity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1593.ElectricalResistivity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricalResistivity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electric_current(self) -> '_1594.ElectricCurrent':
        """ElectricCurrent: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1594.ElectricCurrent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricCurrent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_energy(self) -> '_1595.Energy':
        """Energy: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1595.Energy.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Energy. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_energy_per_unit_area(self) -> '_1596.EnergyPerUnitArea':
        """EnergyPerUnitArea: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1596.EnergyPerUnitArea.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to EnergyPerUnitArea. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_energy_per_unit_area_small(self) -> '_1597.EnergyPerUnitAreaSmall':
        """EnergyPerUnitAreaSmall: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1597.EnergyPerUnitAreaSmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to EnergyPerUnitAreaSmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_energy_small(self) -> '_1598.EnergySmall':
        """EnergySmall: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1598.EnergySmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to EnergySmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_enum(self) -> '_1599.Enum':
        """Enum: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1599.Enum.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Enum. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_flow_rate(self) -> '_1600.FlowRate':
        """FlowRate: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1600.FlowRate.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FlowRate. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_force(self) -> '_1601.Force':
        """Force: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1601.Force.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Force. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_force_per_unit_length(self) -> '_1602.ForcePerUnitLength':
        """ForcePerUnitLength: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1602.ForcePerUnitLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ForcePerUnitLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_force_per_unit_pressure(self) -> '_1603.ForcePerUnitPressure':
        """ForcePerUnitPressure: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1603.ForcePerUnitPressure.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ForcePerUnitPressure. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_force_per_unit_temperature(self) -> '_1604.ForcePerUnitTemperature':
        """ForcePerUnitTemperature: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1604.ForcePerUnitTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ForcePerUnitTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_fraction_measurement_base(self) -> '_1605.FractionMeasurementBase':
        """FractionMeasurementBase: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1605.FractionMeasurementBase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FractionMeasurementBase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_fraction_per_temperature(self) -> '_1606.FractionPerTemperature':
        """FractionPerTemperature: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1606.FractionPerTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FractionPerTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_frequency(self) -> '_1607.Frequency':
        """Frequency: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1607.Frequency.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Frequency. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_fuel_consumption_engine(self) -> '_1608.FuelConsumptionEngine':
        """FuelConsumptionEngine: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1608.FuelConsumptionEngine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FuelConsumptionEngine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_fuel_efficiency_vehicle(self) -> '_1609.FuelEfficiencyVehicle':
        """FuelEfficiencyVehicle: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1609.FuelEfficiencyVehicle.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FuelEfficiencyVehicle. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_gradient(self) -> '_1610.Gradient':
        """Gradient: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1610.Gradient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Gradient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_heat_conductivity(self) -> '_1611.HeatConductivity':
        """HeatConductivity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1611.HeatConductivity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to HeatConductivity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_heat_transfer(self) -> '_1612.HeatTransfer':
        """HeatTransfer: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1612.HeatTransfer.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to HeatTransfer. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_heat_transfer_coefficient_for_plastic_gear_tooth(self) -> '_1613.HeatTransferCoefficientForPlasticGearTooth':
        """HeatTransferCoefficientForPlasticGearTooth: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1613.HeatTransferCoefficientForPlasticGearTooth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to HeatTransferCoefficientForPlasticGearTooth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_heat_transfer_resistance(self) -> '_1614.HeatTransferResistance':
        """HeatTransferResistance: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1614.HeatTransferResistance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to HeatTransferResistance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_impulse(self) -> '_1615.Impulse':
        """Impulse: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1615.Impulse.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Impulse. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_index(self) -> '_1616.Index':
        """Index: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1616.Index.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Index. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_inductance(self) -> '_1617.Inductance':
        """Inductance: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1617.Inductance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Inductance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_integer(self) -> '_1618.Integer':
        """Integer: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1618.Integer.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Integer. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_inverse_short_length(self) -> '_1619.InverseShortLength':
        """InverseShortLength: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1619.InverseShortLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to InverseShortLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_inverse_short_time(self) -> '_1620.InverseShortTime':
        """InverseShortTime: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1620.InverseShortTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to InverseShortTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_jerk(self) -> '_1621.Jerk':
        """Jerk: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1621.Jerk.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Jerk. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_kinematic_viscosity(self) -> '_1622.KinematicViscosity':
        """KinematicViscosity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1622.KinematicViscosity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KinematicViscosity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_length_long(self) -> '_1623.LengthLong':
        """LengthLong: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1623.LengthLong.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LengthLong. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_length_medium(self) -> '_1624.LengthMedium':
        """LengthMedium: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1624.LengthMedium.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LengthMedium. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_length_per_unit_temperature(self) -> '_1625.LengthPerUnitTemperature':
        """LengthPerUnitTemperature: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1625.LengthPerUnitTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LengthPerUnitTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_length_short(self) -> '_1626.LengthShort':
        """LengthShort: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1626.LengthShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LengthShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_length_to_the_fourth(self) -> '_1627.LengthToTheFourth':
        """LengthToTheFourth: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1627.LengthToTheFourth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LengthToTheFourth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_length_very_long(self) -> '_1628.LengthVeryLong':
        """LengthVeryLong: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1628.LengthVeryLong.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LengthVeryLong. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_length_very_short(self) -> '_1629.LengthVeryShort':
        """LengthVeryShort: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1629.LengthVeryShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LengthVeryShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_length_very_short_per_length_short(self) -> '_1630.LengthVeryShortPerLengthShort':
        """LengthVeryShortPerLengthShort: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1630.LengthVeryShortPerLengthShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LengthVeryShortPerLengthShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_linear_angular_damping(self) -> '_1631.LinearAngularDamping':
        """LinearAngularDamping: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1631.LinearAngularDamping.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LinearAngularDamping. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_linear_angular_stiffness_cross_term(self) -> '_1632.LinearAngularStiffnessCrossTerm':
        """LinearAngularStiffnessCrossTerm: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1632.LinearAngularStiffnessCrossTerm.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LinearAngularStiffnessCrossTerm. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_linear_damping(self) -> '_1633.LinearDamping':
        """LinearDamping: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1633.LinearDamping.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LinearDamping. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_linear_flexibility(self) -> '_1634.LinearFlexibility':
        """LinearFlexibility: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1634.LinearFlexibility.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LinearFlexibility. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_linear_stiffness(self) -> '_1635.LinearStiffness':
        """LinearStiffness: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1635.LinearStiffness.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to LinearStiffness. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_magnetic_field_strength(self) -> '_1636.MagneticFieldStrength':
        """MagneticFieldStrength: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1636.MagneticFieldStrength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MagneticFieldStrength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_magnetic_flux(self) -> '_1637.MagneticFlux':
        """MagneticFlux: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1637.MagneticFlux.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MagneticFlux. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_magnetic_flux_density(self) -> '_1638.MagneticFluxDensity':
        """MagneticFluxDensity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1638.MagneticFluxDensity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MagneticFluxDensity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_magnetic_vector_potential(self) -> '_1639.MagneticVectorPotential':
        """MagneticVectorPotential: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1639.MagneticVectorPotential.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MagneticVectorPotential. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_magnetomotive_force(self) -> '_1640.MagnetomotiveForce':
        """MagnetomotiveForce: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1640.MagnetomotiveForce.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MagnetomotiveForce. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_mass(self) -> '_1641.Mass':
        """Mass: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1641.Mass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Mass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_mass_per_unit_length(self) -> '_1642.MassPerUnitLength':
        """MassPerUnitLength: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1642.MassPerUnitLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MassPerUnitLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_mass_per_unit_time(self) -> '_1643.MassPerUnitTime':
        """MassPerUnitTime: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1643.MassPerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MassPerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_moment_of_inertia(self) -> '_1644.MomentOfInertia':
        """MomentOfInertia: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1644.MomentOfInertia.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MomentOfInertia. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_moment_of_inertia_per_unit_length(self) -> '_1645.MomentOfInertiaPerUnitLength':
        """MomentOfInertiaPerUnitLength: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1645.MomentOfInertiaPerUnitLength.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MomentOfInertiaPerUnitLength. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_moment_per_unit_pressure(self) -> '_1646.MomentPerUnitPressure':
        """MomentPerUnitPressure: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1646.MomentPerUnitPressure.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MomentPerUnitPressure. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_number(self) -> '_1647.Number':
        """Number: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1647.Number.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Number. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_percentage(self) -> '_1648.Percentage':
        """Percentage: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1648.Percentage.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Percentage. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_power(self) -> '_1649.Power':
        """Power: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1649.Power.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Power. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_power_per_small_area(self) -> '_1650.PowerPerSmallArea':
        """PowerPerSmallArea: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1650.PowerPerSmallArea.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PowerPerSmallArea. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_power_per_unit_time(self) -> '_1651.PowerPerUnitTime':
        """PowerPerUnitTime: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1651.PowerPerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PowerPerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_power_small(self) -> '_1652.PowerSmall':
        """PowerSmall: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1652.PowerSmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PowerSmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_power_small_per_area(self) -> '_1653.PowerSmallPerArea':
        """PowerSmallPerArea: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1653.PowerSmallPerArea.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PowerSmallPerArea. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_power_small_per_mass(self) -> '_1654.PowerSmallPerMass':
        """PowerSmallPerMass: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1654.PowerSmallPerMass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PowerSmallPerMass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_power_small_per_unit_area_per_unit_time(self) -> '_1655.PowerSmallPerUnitAreaPerUnitTime':
        """PowerSmallPerUnitAreaPerUnitTime: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1655.PowerSmallPerUnitAreaPerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PowerSmallPerUnitAreaPerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_power_small_per_unit_time(self) -> '_1656.PowerSmallPerUnitTime':
        """PowerSmallPerUnitTime: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1656.PowerSmallPerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PowerSmallPerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_power_small_per_volume(self) -> '_1657.PowerSmallPerVolume':
        """PowerSmallPerVolume: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1657.PowerSmallPerVolume.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PowerSmallPerVolume. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_pressure(self) -> '_1658.Pressure':
        """Pressure: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1658.Pressure.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Pressure. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_pressure_per_unit_time(self) -> '_1659.PressurePerUnitTime':
        """PressurePerUnitTime: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1659.PressurePerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PressurePerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_pressure_velocity_product(self) -> '_1660.PressureVelocityProduct':
        """PressureVelocityProduct: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1660.PressureVelocityProduct.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PressureVelocityProduct. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_pressure_viscosity_coefficient(self) -> '_1661.PressureViscosityCoefficient':
        """PressureViscosityCoefficient: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1661.PressureViscosityCoefficient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PressureViscosityCoefficient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_price(self) -> '_1662.Price':
        """Price: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1662.Price.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Price. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_price_per_unit_mass(self) -> '_1663.PricePerUnitMass':
        """PricePerUnitMass: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1663.PricePerUnitMass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PricePerUnitMass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_quadratic_angular_damping(self) -> '_1664.QuadraticAngularDamping':
        """QuadraticAngularDamping: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1664.QuadraticAngularDamping.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to QuadraticAngularDamping. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_quadratic_drag(self) -> '_1665.QuadraticDrag':
        """QuadraticDrag: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1665.QuadraticDrag.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to QuadraticDrag. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_rescaled_measurement(self) -> '_1666.RescaledMeasurement':
        """RescaledMeasurement: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1666.RescaledMeasurement.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to RescaledMeasurement. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_rotatum(self) -> '_1667.Rotatum':
        """Rotatum: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1667.Rotatum.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Rotatum. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_safety_factor(self) -> '_1668.SafetyFactor':
        """SafetyFactor: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1668.SafetyFactor.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SafetyFactor. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_specific_acoustic_impedance(self) -> '_1669.SpecificAcousticImpedance':
        """SpecificAcousticImpedance: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1669.SpecificAcousticImpedance.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SpecificAcousticImpedance. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_specific_heat(self) -> '_1670.SpecificHeat':
        """SpecificHeat: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1670.SpecificHeat.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SpecificHeat. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_square_root_of_unit_force_per_unit_area(self) -> '_1671.SquareRootOfUnitForcePerUnitArea':
        """SquareRootOfUnitForcePerUnitArea: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1671.SquareRootOfUnitForcePerUnitArea.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SquareRootOfUnitForcePerUnitArea. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_stiffness_per_unit_face_width(self) -> '_1672.StiffnessPerUnitFaceWidth':
        """StiffnessPerUnitFaceWidth: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1672.StiffnessPerUnitFaceWidth.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StiffnessPerUnitFaceWidth. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_stress(self) -> '_1673.Stress':
        """Stress: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1673.Stress.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Stress. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_temperature(self) -> '_1674.Temperature':
        """Temperature: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1674.Temperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Temperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_temperature_difference(self) -> '_1675.TemperatureDifference':
        """TemperatureDifference: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1675.TemperatureDifference.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TemperatureDifference. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_temperature_per_unit_time(self) -> '_1676.TemperaturePerUnitTime':
        """TemperaturePerUnitTime: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1676.TemperaturePerUnitTime.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TemperaturePerUnitTime. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_text(self) -> '_1677.Text':
        """Text: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1677.Text.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Text. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_thermal_contact_coefficient(self) -> '_1678.ThermalContactCoefficient':
        """ThermalContactCoefficient: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1678.ThermalContactCoefficient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ThermalContactCoefficient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_thermal_expansion_coefficient(self) -> '_1679.ThermalExpansionCoefficient':
        """ThermalExpansionCoefficient: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1679.ThermalExpansionCoefficient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ThermalExpansionCoefficient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_thermo_elastic_factor(self) -> '_1680.ThermoElasticFactor':
        """ThermoElasticFactor: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1680.ThermoElasticFactor.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ThermoElasticFactor. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_time(self) -> '_1681.Time':
        """Time: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1681.Time.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Time. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_time_short(self) -> '_1682.TimeShort':
        """TimeShort: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1682.TimeShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TimeShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_time_very_short(self) -> '_1683.TimeVeryShort':
        """TimeVeryShort: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1683.TimeVeryShort.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TimeVeryShort. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_torque(self) -> '_1684.Torque':
        """Torque: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1684.Torque.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Torque. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_torque_converter_inverse_k(self) -> '_1685.TorqueConverterInverseK':
        """TorqueConverterInverseK: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1685.TorqueConverterInverseK.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TorqueConverterInverseK. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_torque_converter_k(self) -> '_1686.TorqueConverterK':
        """TorqueConverterK: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1686.TorqueConverterK.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TorqueConverterK. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_torque_per_current(self) -> '_1687.TorquePerCurrent':
        """TorquePerCurrent: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1687.TorquePerCurrent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TorquePerCurrent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_torque_per_square_root_of_power(self) -> '_1688.TorquePerSquareRootOfPower':
        """TorquePerSquareRootOfPower: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1688.TorquePerSquareRootOfPower.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TorquePerSquareRootOfPower. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_torque_per_unit_temperature(self) -> '_1689.TorquePerUnitTemperature':
        """TorquePerUnitTemperature: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1689.TorquePerUnitTemperature.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TorquePerUnitTemperature. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_velocity(self) -> '_1690.Velocity':
        """Velocity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1690.Velocity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Velocity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_velocity_small(self) -> '_1691.VelocitySmall':
        """VelocitySmall: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1691.VelocitySmall.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to VelocitySmall. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_viscosity(self) -> '_1692.Viscosity':
        """Viscosity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1692.Viscosity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Viscosity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_voltage(self) -> '_1693.Voltage':
        """Voltage: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1693.Voltage.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Voltage. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_voltage_per_angular_velocity(self) -> '_1694.VoltagePerAngularVelocity':
        """VoltagePerAngularVelocity: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1694.VoltagePerAngularVelocity.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to VoltagePerAngularVelocity. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_volume(self) -> '_1695.Volume':
        """Volume: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1695.Volume.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Volume. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_wear_coefficient(self) -> '_1696.WearCoefficient':
        """WearCoefficient: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1696.WearCoefficient.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to WearCoefficient. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_yank(self) -> '_1697.Yank':
        """Yank: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1697.Yank.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Yank. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1565.MeasurementBase]':
        """List[MeasurementBase]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ColumnTitle(_1773.ColumnTitle, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ColumnTitle

    A specific implementation of 'ListWithSelectedItem' for 'ColumnTitle' types.
    """

    __hash__ = None
    __qualname__ = 'ColumnTitle'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ColumnTitle.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1773.ColumnTitle.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1773.ColumnTitle.TYPE

    @property
    def selected_value(self) -> '_1773.ColumnTitle':
        """ColumnTitle: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1773.ColumnTitle]':
        """List[ColumnTitle]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_PowerLoad(_2412.PowerLoad, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_PowerLoad

    A specific implementation of 'ListWithSelectedItem' for 'PowerLoad' types.
    """

    __hash__ = None
    __qualname__ = 'PowerLoad'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_PowerLoad.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2412.PowerLoad.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2412.PowerLoad.TYPE

    @property
    def selected_value(self) -> '_2412.PowerLoad':
        """PowerLoad: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2412.PowerLoad]':
        """List[PowerLoad]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_AbstractPeriodicExcitationDetail(_5603.AbstractPeriodicExcitationDetail, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_AbstractPeriodicExcitationDetail

    A specific implementation of 'ListWithSelectedItem' for 'AbstractPeriodicExcitationDetail' types.
    """

    __hash__ = None
    __qualname__ = 'AbstractPeriodicExcitationDetail'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_AbstractPeriodicExcitationDetail.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_5603.AbstractPeriodicExcitationDetail.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5603.AbstractPeriodicExcitationDetail.TYPE

    @property
    def selected_value(self) -> '_5603.AbstractPeriodicExcitationDetail':
        """AbstractPeriodicExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _5603.AbstractPeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AbstractPeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electric_machine_periodic_excitation_detail(self) -> '_5656.ElectricMachinePeriodicExcitationDetail':
        """ElectricMachinePeriodicExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _5656.ElectricMachinePeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachinePeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electric_machine_rotor_x_force_periodic_excitation_detail(self) -> '_5657.ElectricMachineRotorXForcePeriodicExcitationDetail':
        """ElectricMachineRotorXForcePeriodicExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _5657.ElectricMachineRotorXForcePeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachineRotorXForcePeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electric_machine_rotor_x_moment_periodic_excitation_detail(self) -> '_5658.ElectricMachineRotorXMomentPeriodicExcitationDetail':
        """ElectricMachineRotorXMomentPeriodicExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _5658.ElectricMachineRotorXMomentPeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachineRotorXMomentPeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electric_machine_rotor_y_force_periodic_excitation_detail(self) -> '_5659.ElectricMachineRotorYForcePeriodicExcitationDetail':
        """ElectricMachineRotorYForcePeriodicExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _5659.ElectricMachineRotorYForcePeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachineRotorYForcePeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electric_machine_rotor_y_moment_periodic_excitation_detail(self) -> '_5660.ElectricMachineRotorYMomentPeriodicExcitationDetail':
        """ElectricMachineRotorYMomentPeriodicExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _5660.ElectricMachineRotorYMomentPeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachineRotorYMomentPeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electric_machine_rotor_z_force_periodic_excitation_detail(self) -> '_5661.ElectricMachineRotorZForcePeriodicExcitationDetail':
        """ElectricMachineRotorZForcePeriodicExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _5661.ElectricMachineRotorZForcePeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachineRotorZForcePeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electric_machine_stator_tooth_axial_loads_excitation_detail(self) -> '_5662.ElectricMachineStatorToothAxialLoadsExcitationDetail':
        """ElectricMachineStatorToothAxialLoadsExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _5662.ElectricMachineStatorToothAxialLoadsExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachineStatorToothAxialLoadsExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electric_machine_stator_tooth_loads_excitation_detail(self) -> '_5663.ElectricMachineStatorToothLoadsExcitationDetail':
        """ElectricMachineStatorToothLoadsExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _5663.ElectricMachineStatorToothLoadsExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachineStatorToothLoadsExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electric_machine_stator_tooth_radial_loads_excitation_detail(self) -> '_5664.ElectricMachineStatorToothRadialLoadsExcitationDetail':
        """ElectricMachineStatorToothRadialLoadsExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _5664.ElectricMachineStatorToothRadialLoadsExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachineStatorToothRadialLoadsExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electric_machine_stator_tooth_tangential_loads_excitation_detail(self) -> '_5665.ElectricMachineStatorToothTangentialLoadsExcitationDetail':
        """ElectricMachineStatorToothTangentialLoadsExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _5665.ElectricMachineStatorToothTangentialLoadsExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachineStatorToothTangentialLoadsExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electric_machine_torque_ripple_periodic_excitation_detail(self) -> '_5666.ElectricMachineTorqueRipplePeriodicExcitationDetail':
        """ElectricMachineTorqueRipplePeriodicExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _5666.ElectricMachineTorqueRipplePeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachineTorqueRipplePeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_gear_mesh_excitation_detail(self) -> '_5676.GearMeshExcitationDetail':
        """GearMeshExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _5676.GearMeshExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to GearMeshExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_gear_mesh_misalignment_excitation_detail(self) -> '_5678.GearMeshMisalignmentExcitationDetail':
        """GearMeshMisalignmentExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _5678.GearMeshMisalignmentExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to GearMeshMisalignmentExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_gear_mesh_te_excitation_detail(self) -> '_5679.GearMeshTEExcitationDetail':
        """GearMeshTEExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _5679.GearMeshTEExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to GearMeshTEExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_general_periodic_excitation_detail(self) -> '_5681.GeneralPeriodicExcitationDetail':
        """GeneralPeriodicExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _5681.GeneralPeriodicExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to GeneralPeriodicExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_periodic_excitation_with_reference_shaft(self) -> '_5710.PeriodicExcitationWithReferenceShaft':
        """PeriodicExcitationWithReferenceShaft: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _5710.PeriodicExcitationWithReferenceShaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PeriodicExcitationWithReferenceShaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_single_node_periodic_excitation_with_reference_shaft(self) -> '_5727.SingleNodePeriodicExcitationWithReferenceShaft':
        """SingleNodePeriodicExcitationWithReferenceShaft: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _5727.SingleNodePeriodicExcitationWithReferenceShaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SingleNodePeriodicExcitationWithReferenceShaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_unbalanced_mass_excitation_detail(self) -> '_5752.UnbalancedMassExcitationDetail':
        """UnbalancedMassExcitationDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _5752.UnbalancedMassExcitationDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to UnbalancedMassExcitationDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_5603.AbstractPeriodicExcitationDetail]':
        """List[AbstractPeriodicExcitationDetail]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_TupleWithName(TupleWithName, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_TupleWithName

    A specific implementation of 'ListWithSelectedItem' for 'TupleWithName' types.
    """

    __hash__ = None
    __qualname__ = 'TupleWithName'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_TupleWithName.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'TupleWithName.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return TupleWithName.TYPE

    @property
    def selected_value(self) -> 'TupleWithName':
        """TupleWithName: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        value = conversion.pn_to_mp_tuple_with_name(temp, (None))
        return constructor.new_from_mastapy_type(TupleWithName)(value) if value is not None else None

    @property
    def available_values(self) -> 'TupleWithName':
        """TupleWithName: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return constructor.new_from_mastapy_type(TupleWithName)(value) if value is not None else None


class ListWithSelectedItem_GearMeshSystemDeflection(_2693.GearMeshSystemDeflection, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_GearMeshSystemDeflection

    A specific implementation of 'ListWithSelectedItem' for 'GearMeshSystemDeflection' types.
    """

    __hash__ = None
    __qualname__ = 'GearMeshSystemDeflection'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_GearMeshSystemDeflection.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2693.GearMeshSystemDeflection.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2693.GearMeshSystemDeflection.TYPE

    @property
    def selected_value(self) -> '_2693.GearMeshSystemDeflection':
        """GearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2693.GearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to GearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_agma_gleason_conical_gear_mesh_system_deflection(self) -> '_2628.AGMAGleasonConicalGearMeshSystemDeflection':
        """AGMAGleasonConicalGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2628.AGMAGleasonConicalGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AGMAGleasonConicalGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_bevel_differential_gear_mesh_system_deflection(self) -> '_2635.BevelDifferentialGearMeshSystemDeflection':
        """BevelDifferentialGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2635.BevelDifferentialGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to BevelDifferentialGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_bevel_gear_mesh_system_deflection(self) -> '_2640.BevelGearMeshSystemDeflection':
        """BevelGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2640.BevelGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to BevelGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_concept_gear_mesh_system_deflection(self) -> '_2654.ConceptGearMeshSystemDeflection':
        """ConceptGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2654.ConceptGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ConceptGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_conical_gear_mesh_system_deflection(self) -> '_2658.ConicalGearMeshSystemDeflection':
        """ConicalGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2658.ConicalGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ConicalGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cylindrical_gear_mesh_system_deflection(self) -> '_2673.CylindricalGearMeshSystemDeflection':
        """CylindricalGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2673.CylindricalGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cylindrical_gear_mesh_system_deflection_timestep(self) -> '_2674.CylindricalGearMeshSystemDeflectionTimestep':
        """CylindricalGearMeshSystemDeflectionTimestep: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2674.CylindricalGearMeshSystemDeflectionTimestep.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGearMeshSystemDeflectionTimestep. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cylindrical_gear_mesh_system_deflection_with_ltca_results(self) -> '_2675.CylindricalGearMeshSystemDeflectionWithLTCAResults':
        """CylindricalGearMeshSystemDeflectionWithLTCAResults: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2675.CylindricalGearMeshSystemDeflectionWithLTCAResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGearMeshSystemDeflectionWithLTCAResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_face_gear_mesh_system_deflection(self) -> '_2688.FaceGearMeshSystemDeflection':
        """FaceGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2688.FaceGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FaceGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_hypoid_gear_mesh_system_deflection(self) -> '_2697.HypoidGearMeshSystemDeflection':
        """HypoidGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2697.HypoidGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to HypoidGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_conical_gear_mesh_system_deflection(self) -> '_2702.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection':
        """KlingelnbergCycloPalloidConicalGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2702.KlingelnbergCycloPalloidConicalGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidConicalGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_hypoid_gear_mesh_system_deflection(self) -> '_2705.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection':
        """KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2705.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_system_deflection(self) -> '_2708.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection':
        """KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2708.KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidSpiralBevelGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_spiral_bevel_gear_mesh_system_deflection(self) -> '_2741.SpiralBevelGearMeshSystemDeflection':
        """SpiralBevelGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2741.SpiralBevelGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SpiralBevelGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_straight_bevel_diff_gear_mesh_system_deflection(self) -> '_2747.StraightBevelDiffGearMeshSystemDeflection':
        """StraightBevelDiffGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2747.StraightBevelDiffGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelDiffGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_straight_bevel_gear_mesh_system_deflection(self) -> '_2750.StraightBevelGearMeshSystemDeflection':
        """StraightBevelGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2750.StraightBevelGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_worm_gear_mesh_system_deflection(self) -> '_2770.WormGearMeshSystemDeflection':
        """WormGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2770.WormGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to WormGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_zerol_bevel_gear_mesh_system_deflection(self) -> '_2773.ZerolBevelGearMeshSystemDeflection':
        """ZerolBevelGearMeshSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2773.ZerolBevelGearMeshSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ZerolBevelGearMeshSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2693.GearMeshSystemDeflection]':
        """List[GearMeshSystemDeflection]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_GearSet(_2471.GearSet, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_GearSet

    A specific implementation of 'ListWithSelectedItem' for 'GearSet' types.
    """

    __hash__ = None
    __qualname__ = 'GearSet'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_GearSet.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2471.GearSet.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2471.GearSet.TYPE

    @property
    def selected_value(self) -> '_2471.GearSet':
        """GearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2471.GearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to GearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_agma_gleason_conical_gear_set(self) -> '_2453.AGMAGleasonConicalGearSet':
        """AGMAGleasonConicalGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2453.AGMAGleasonConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AGMAGleasonConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_bevel_differential_gear_set(self) -> '_2455.BevelDifferentialGearSet':
        """BevelDifferentialGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2455.BevelDifferentialGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to BevelDifferentialGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_bevel_gear_set(self) -> '_2459.BevelGearSet':
        """BevelGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2459.BevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to BevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_concept_gear_set(self) -> '_2461.ConceptGearSet':
        """ConceptGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2461.ConceptGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ConceptGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_conical_gear_set(self) -> '_2463.ConicalGearSet':
        """ConicalGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2463.ConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cylindrical_gear_set(self) -> '_2465.CylindricalGearSet':
        """CylindricalGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2465.CylindricalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_face_gear_set(self) -> '_2468.FaceGearSet':
        """FaceGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2468.FaceGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FaceGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_hypoid_gear_set(self) -> '_2474.HypoidGearSet':
        """HypoidGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2474.HypoidGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to HypoidGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_conical_gear_set(self) -> '_2476.KlingelnbergCycloPalloidConicalGearSet':
        """KlingelnbergCycloPalloidConicalGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2476.KlingelnbergCycloPalloidConicalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidConicalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set(self) -> '_2478.KlingelnbergCycloPalloidHypoidGearSet':
        """KlingelnbergCycloPalloidHypoidGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2478.KlingelnbergCycloPalloidHypoidGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidHypoidGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set(self) -> '_2480.KlingelnbergCycloPalloidSpiralBevelGearSet':
        """KlingelnbergCycloPalloidSpiralBevelGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2480.KlingelnbergCycloPalloidSpiralBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidSpiralBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_planetary_gear_set(self) -> '_2481.PlanetaryGearSet':
        """PlanetaryGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2481.PlanetaryGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PlanetaryGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_spiral_bevel_gear_set(self) -> '_2483.SpiralBevelGearSet':
        """SpiralBevelGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2483.SpiralBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SpiralBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_straight_bevel_diff_gear_set(self) -> '_2485.StraightBevelDiffGearSet':
        """StraightBevelDiffGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2485.StraightBevelDiffGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelDiffGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_straight_bevel_gear_set(self) -> '_2487.StraightBevelGearSet':
        """StraightBevelGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2487.StraightBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_worm_gear_set(self) -> '_2491.WormGearSet':
        """WormGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2491.WormGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to WormGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_zerol_bevel_gear_set(self) -> '_2493.ZerolBevelGearSet':
        """ZerolBevelGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2493.ZerolBevelGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ZerolBevelGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2471.GearSet]':
        """List[GearSet]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_FESubstructureNode(_2324.FESubstructureNode, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_FESubstructureNode

    A specific implementation of 'ListWithSelectedItem' for 'FESubstructureNode' types.
    """

    __hash__ = None
    __qualname__ = 'FESubstructureNode'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_FESubstructureNode.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2324.FESubstructureNode.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2324.FESubstructureNode.TYPE

    @property
    def selected_value(self) -> '_2324.FESubstructureNode':
        """FESubstructureNode: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2324.FESubstructureNode]':
        """List[FESubstructureNode]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_Component(_2384.Component, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_Component

    A specific implementation of 'ListWithSelectedItem' for 'Component' types.
    """

    __hash__ = None
    __qualname__ = 'Component'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_Component.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2384.Component.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2384.Component.TYPE

    @property
    def selected_value(self) -> '_2384.Component':
        """Component: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2384.Component.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Component. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_abstract_shaft(self) -> '_2376.AbstractShaft':
        """AbstractShaft: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2376.AbstractShaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AbstractShaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_abstract_shaft_or_housing(self) -> '_2377.AbstractShaftOrHousing':
        """AbstractShaftOrHousing: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2377.AbstractShaftOrHousing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AbstractShaftOrHousing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_bearing(self) -> '_2380.Bearing':
        """Bearing: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2380.Bearing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Bearing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_bolt(self) -> '_2382.Bolt':
        """Bolt: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2382.Bolt.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Bolt. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_connector(self) -> '_2387.Connector':
        """Connector: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2387.Connector.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Connector. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_datum(self) -> '_2388.Datum':
        """Datum: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2388.Datum.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Datum. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_external_cad_model(self) -> '_2392.ExternalCADModel':
        """ExternalCADModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2392.ExternalCADModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ExternalCADModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_fe_part(self) -> '_2393.FEPart':
        """FEPart: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2393.FEPart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FEPart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_guide_dxf_model(self) -> '_2395.GuideDxfModel':
        """GuideDxfModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2395.GuideDxfModel.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to GuideDxfModel. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_mass_disc(self) -> '_2402.MassDisc':
        """MassDisc: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2402.MassDisc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MassDisc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_measurement_component(self) -> '_2403.MeasurementComponent':
        """MeasurementComponent: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2403.MeasurementComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MeasurementComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_mountable_component(self) -> '_2404.MountableComponent':
        """MountableComponent: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2404.MountableComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MountableComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_oil_seal(self) -> '_2406.OilSeal':
        """OilSeal: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2406.OilSeal.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to OilSeal. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_planet_carrier(self) -> '_2409.PlanetCarrier':
        """PlanetCarrier: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2409.PlanetCarrier.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PlanetCarrier. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_point_load(self) -> '_2411.PointLoad':
        """PointLoad: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2411.PointLoad.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PointLoad. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_power_load(self) -> '_2412.PowerLoad':
        """PowerLoad: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2412.PowerLoad.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PowerLoad. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_unbalanced_mass(self) -> '_2417.UnbalancedMass':
        """UnbalancedMass: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2417.UnbalancedMass.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to UnbalancedMass. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_virtual_component(self) -> '_2419.VirtualComponent':
        """VirtualComponent: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2419.VirtualComponent.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to VirtualComponent. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_shaft(self) -> '_2422.Shaft':
        """Shaft: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2422.Shaft.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Shaft. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_agma_gleason_conical_gear(self) -> '_2452.AGMAGleasonConicalGear':
        """AGMAGleasonConicalGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2452.AGMAGleasonConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AGMAGleasonConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_bevel_differential_gear(self) -> '_2454.BevelDifferentialGear':
        """BevelDifferentialGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2454.BevelDifferentialGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to BevelDifferentialGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_bevel_differential_planet_gear(self) -> '_2456.BevelDifferentialPlanetGear':
        """BevelDifferentialPlanetGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2456.BevelDifferentialPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to BevelDifferentialPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_bevel_differential_sun_gear(self) -> '_2457.BevelDifferentialSunGear':
        """BevelDifferentialSunGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2457.BevelDifferentialSunGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to BevelDifferentialSunGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_bevel_gear(self) -> '_2458.BevelGear':
        """BevelGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2458.BevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to BevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_concept_gear(self) -> '_2460.ConceptGear':
        """ConceptGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2460.ConceptGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ConceptGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_conical_gear(self) -> '_2462.ConicalGear':
        """ConicalGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2462.ConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cylindrical_gear(self) -> '_2464.CylindricalGear':
        """CylindricalGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2464.CylindricalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cylindrical_planet_gear(self) -> '_2466.CylindricalPlanetGear':
        """CylindricalPlanetGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2466.CylindricalPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_face_gear(self) -> '_2467.FaceGear':
        """FaceGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2467.FaceGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FaceGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_gear(self) -> '_2469.Gear':
        """Gear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2469.Gear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Gear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_hypoid_gear(self) -> '_2473.HypoidGear':
        """HypoidGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2473.HypoidGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to HypoidGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_conical_gear(self) -> '_2475.KlingelnbergCycloPalloidConicalGear':
        """KlingelnbergCycloPalloidConicalGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2475.KlingelnbergCycloPalloidConicalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidConicalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_hypoid_gear(self) -> '_2477.KlingelnbergCycloPalloidHypoidGear':
        """KlingelnbergCycloPalloidHypoidGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2477.KlingelnbergCycloPalloidHypoidGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidHypoidGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear(self) -> '_2479.KlingelnbergCycloPalloidSpiralBevelGear':
        """KlingelnbergCycloPalloidSpiralBevelGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2479.KlingelnbergCycloPalloidSpiralBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidSpiralBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_spiral_bevel_gear(self) -> '_2482.SpiralBevelGear':
        """SpiralBevelGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2482.SpiralBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SpiralBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_straight_bevel_diff_gear(self) -> '_2484.StraightBevelDiffGear':
        """StraightBevelDiffGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2484.StraightBevelDiffGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelDiffGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_straight_bevel_gear(self) -> '_2486.StraightBevelGear':
        """StraightBevelGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2486.StraightBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_straight_bevel_planet_gear(self) -> '_2488.StraightBevelPlanetGear':
        """StraightBevelPlanetGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2488.StraightBevelPlanetGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelPlanetGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_straight_bevel_sun_gear(self) -> '_2489.StraightBevelSunGear':
        """StraightBevelSunGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2489.StraightBevelSunGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelSunGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_worm_gear(self) -> '_2490.WormGear':
        """WormGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2490.WormGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to WormGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_zerol_bevel_gear(self) -> '_2492.ZerolBevelGear':
        """ZerolBevelGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2492.ZerolBevelGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ZerolBevelGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cycloidal_disc(self) -> '_2508.CycloidalDisc':
        """CycloidalDisc: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2508.CycloidalDisc.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CycloidalDisc. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_ring_pins(self) -> '_2509.RingPins':
        """RingPins: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2509.RingPins.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to RingPins. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_clutch_half(self) -> '_2518.ClutchHalf':
        """ClutchHalf: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2518.ClutchHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ClutchHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_concept_coupling_half(self) -> '_2521.ConceptCouplingHalf':
        """ConceptCouplingHalf: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2521.ConceptCouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ConceptCouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_coupling_half(self) -> '_2523.CouplingHalf':
        """CouplingHalf: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2523.CouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cvt_pulley(self) -> '_2526.CVTPulley':
        """CVTPulley: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2526.CVTPulley.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CVTPulley. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_part_to_part_shear_coupling_half(self) -> '_2528.PartToPartShearCouplingHalf':
        """PartToPartShearCouplingHalf: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2528.PartToPartShearCouplingHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PartToPartShearCouplingHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_pulley(self) -> '_2529.Pulley':
        """Pulley: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2529.Pulley.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to Pulley. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_rolling_ring(self) -> '_2535.RollingRing':
        """RollingRing: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2535.RollingRing.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to RollingRing. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_shaft_hub_connection(self) -> '_2537.ShaftHubConnection':
        """ShaftHubConnection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2537.ShaftHubConnection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ShaftHubConnection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_spring_damper_half(self) -> '_2540.SpringDamperHalf':
        """SpringDamperHalf: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2540.SpringDamperHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SpringDamperHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_synchroniser_half(self) -> '_2543.SynchroniserHalf':
        """SynchroniserHalf: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2543.SynchroniserHalf.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SynchroniserHalf. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_synchroniser_part(self) -> '_2544.SynchroniserPart':
        """SynchroniserPart: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2544.SynchroniserPart.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SynchroniserPart. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_synchroniser_sleeve(self) -> '_2545.SynchroniserSleeve':
        """SynchroniserSleeve: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2545.SynchroniserSleeve.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SynchroniserSleeve. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_torque_converter_pump(self) -> '_2547.TorqueConverterPump':
        """TorqueConverterPump: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2547.TorqueConverterPump.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TorqueConverterPump. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_torque_converter_turbine(self) -> '_2549.TorqueConverterTurbine':
        """TorqueConverterTurbine: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2549.TorqueConverterTurbine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to TorqueConverterTurbine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2384.Component]':
        """List[Component]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_Datum(_2388.Datum, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_Datum

    A specific implementation of 'ListWithSelectedItem' for 'Datum' types.
    """

    __hash__ = None
    __qualname__ = 'Datum'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_Datum.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2388.Datum.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2388.Datum.TYPE

    @property
    def selected_value(self) -> '_2388.Datum':
        """Datum: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2388.Datum]':
        """List[Datum]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_FELink(_2357.FELink, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_FELink

    A specific implementation of 'ListWithSelectedItem' for 'FELink' types.
    """

    __hash__ = None
    __qualname__ = 'FELink'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_FELink.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2357.FELink.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2357.FELink.TYPE

    @property
    def selected_value(self) -> '_2357.FELink':
        """FELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2357.FELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_electric_machine_stator_fe_link(self) -> '_2358.ElectricMachineStatorFELink':
        """ElectricMachineStatorFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2358.ElectricMachineStatorFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachineStatorFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_gear_mesh_fe_link(self) -> '_2360.GearMeshFELink':
        """GearMeshFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2360.GearMeshFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to GearMeshFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_gear_with_duplicated_meshes_fe_link(self) -> '_2361.GearWithDuplicatedMeshesFELink':
        """GearWithDuplicatedMeshesFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2361.GearWithDuplicatedMeshesFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to GearWithDuplicatedMeshesFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_multi_angle_connection_fe_link(self) -> '_2362.MultiAngleConnectionFELink':
        """MultiAngleConnectionFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2362.MultiAngleConnectionFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MultiAngleConnectionFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_multi_node_connector_fe_link(self) -> '_2363.MultiNodeConnectorFELink':
        """MultiNodeConnectorFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2363.MultiNodeConnectorFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MultiNodeConnectorFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_multi_node_fe_link(self) -> '_2364.MultiNodeFELink':
        """MultiNodeFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2364.MultiNodeFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to MultiNodeFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_planetary_connector_multi_node_fe_link(self) -> '_2365.PlanetaryConnectorMultiNodeFELink':
        """PlanetaryConnectorMultiNodeFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2365.PlanetaryConnectorMultiNodeFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PlanetaryConnectorMultiNodeFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_planet_based_fe_link(self) -> '_2366.PlanetBasedFELink':
        """PlanetBasedFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2366.PlanetBasedFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PlanetBasedFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_planet_carrier_fe_link(self) -> '_2367.PlanetCarrierFELink':
        """PlanetCarrierFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2367.PlanetCarrierFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PlanetCarrierFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_point_load_fe_link(self) -> '_2368.PointLoadFELink':
        """PointLoadFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2368.PointLoadFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PointLoadFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_rolling_ring_connection_fe_link(self) -> '_2369.RollingRingConnectionFELink':
        """RollingRingConnectionFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2369.RollingRingConnectionFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to RollingRingConnectionFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_shaft_hub_connection_fe_link(self) -> '_2370.ShaftHubConnectionFELink':
        """ShaftHubConnectionFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2370.ShaftHubConnectionFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ShaftHubConnectionFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_single_node_fe_link(self) -> '_2371.SingleNodeFELink':
        """SingleNodeFELink: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2371.SingleNodeFELink.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SingleNodeFELink. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2357.FELink]':
        """List[FELink]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_FESubstructure(_2322.FESubstructure, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_FESubstructure

    A specific implementation of 'ListWithSelectedItem' for 'FESubstructure' types.
    """

    __hash__ = None
    __qualname__ = 'FESubstructure'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_FESubstructure.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2322.FESubstructure.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2322.FESubstructure.TYPE

    @property
    def selected_value(self) -> '_2322.FESubstructure':
        """FESubstructure: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2322.FESubstructure]':
        """List[FESubstructure]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CylindricalGear(_2464.CylindricalGear, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CylindricalGear

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalGear' types.
    """

    __hash__ = None
    __qualname__ = 'CylindricalGear'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalGear.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2464.CylindricalGear.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2464.CylindricalGear.TYPE

    @property
    def selected_value(self) -> '_2464.CylindricalGear':
        """CylindricalGear: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2464.CylindricalGear.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGear. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2464.CylindricalGear]':
        """List[CylindricalGear]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ElectricMachineDetail(_1245.ElectricMachineDetail, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ElectricMachineDetail

    A specific implementation of 'ListWithSelectedItem' for 'ElectricMachineDetail' types.
    """

    __hash__ = None
    __qualname__ = 'ElectricMachineDetail'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ElectricMachineDetail.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_1245.ElectricMachineDetail.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _1245.ElectricMachineDetail.TYPE

    @property
    def selected_value(self) -> '_1245.ElectricMachineDetail':
        """ElectricMachineDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1245.ElectricMachineDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ElectricMachineDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cad_electric_machine_detail(self) -> '_1231.CADElectricMachineDetail':
        """CADElectricMachineDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1231.CADElectricMachineDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CADElectricMachineDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_interior_permanent_magnet_machine(self) -> '_1255.InteriorPermanentMagnetMachine':
        """InteriorPermanentMagnetMachine: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1255.InteriorPermanentMagnetMachine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to InteriorPermanentMagnetMachine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_non_cad_electric_machine_detail(self) -> '_1263.NonCADElectricMachineDetail':
        """NonCADElectricMachineDetail: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1263.NonCADElectricMachineDetail.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to NonCADElectricMachineDetail. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_permanent_magnet_assisted_synchronous_reluctance_machine(self) -> '_1266.PermanentMagnetAssistedSynchronousReluctanceMachine':
        """PermanentMagnetAssistedSynchronousReluctanceMachine: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1266.PermanentMagnetAssistedSynchronousReluctanceMachine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to PermanentMagnetAssistedSynchronousReluctanceMachine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_surface_permanent_magnet_machine(self) -> '_1279.SurfacePermanentMagnetMachine':
        """SurfacePermanentMagnetMachine: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1279.SurfacePermanentMagnetMachine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SurfacePermanentMagnetMachine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_synchronous_reluctance_machine(self) -> '_1281.SynchronousReluctanceMachine':
        """SynchronousReluctanceMachine: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1281.SynchronousReluctanceMachine.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SynchronousReluctanceMachine. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_1245.ElectricMachineDetail]':
        """List[ElectricMachineDetail]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_GuideDxfModel(_2395.GuideDxfModel, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_GuideDxfModel

    A specific implementation of 'ListWithSelectedItem' for 'GuideDxfModel' types.
    """

    __hash__ = None
    __qualname__ = 'GuideDxfModel'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_GuideDxfModel.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2395.GuideDxfModel.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2395.GuideDxfModel.TYPE

    @property
    def selected_value(self) -> '_2395.GuideDxfModel':
        """GuideDxfModel: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2395.GuideDxfModel]':
        """List[GuideDxfModel]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ConcentricPartGroup(_2427.ConcentricPartGroup, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ConcentricPartGroup

    A specific implementation of 'ListWithSelectedItem' for 'ConcentricPartGroup' types.
    """

    __hash__ = None
    __qualname__ = 'ConcentricPartGroup'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ConcentricPartGroup.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2427.ConcentricPartGroup.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2427.ConcentricPartGroup.TYPE

    @property
    def selected_value(self) -> '_2427.ConcentricPartGroup':
        """ConcentricPartGroup: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2427.ConcentricPartGroup]':
        """List[ConcentricPartGroup]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CylindricalGearSet(_2465.CylindricalGearSet, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CylindricalGearSet

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalGearSet' types.
    """

    __hash__ = None
    __qualname__ = 'CylindricalGearSet'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalGearSet.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2465.CylindricalGearSet.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2465.CylindricalGearSet.TYPE

    @property
    def selected_value(self) -> '_2465.CylindricalGearSet':
        """CylindricalGearSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2465.CylindricalGearSet.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGearSet. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2465.CylindricalGearSet]':
        """List[CylindricalGearSet]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_GearSetDesign(_941.GearSetDesign, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_GearSetDesign

    A specific implementation of 'ListWithSelectedItem' for 'GearSetDesign' types.
    """

    __hash__ = None
    __qualname__ = 'GearSetDesign'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_GearSetDesign.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_941.GearSetDesign.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _941.GearSetDesign.TYPE

    @property
    def selected_value(self) -> '_941.GearSetDesign':
        """GearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _941.GearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to GearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_zerol_bevel_gear_set_design(self) -> '_945.ZerolBevelGearSetDesign':
        """ZerolBevelGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _945.ZerolBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ZerolBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_worm_gear_set_design(self) -> '_950.WormGearSetDesign':
        """WormGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _950.WormGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to WormGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_straight_bevel_gear_set_design(self) -> '_954.StraightBevelGearSetDesign':
        """StraightBevelGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _954.StraightBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_straight_bevel_diff_gear_set_design(self) -> '_958.StraightBevelDiffGearSetDesign':
        """StraightBevelDiffGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _958.StraightBevelDiffGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StraightBevelDiffGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_spiral_bevel_gear_set_design(self) -> '_962.SpiralBevelGearSetDesign':
        """SpiralBevelGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _962.SpiralBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to SpiralBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_spiral_bevel_gear_set_design(self) -> '_966.KlingelnbergCycloPalloidSpiralBevelGearSetDesign':
        """KlingelnbergCycloPalloidSpiralBevelGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _966.KlingelnbergCycloPalloidSpiralBevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidSpiralBevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_klingelnberg_cyclo_palloid_hypoid_gear_set_design(self) -> '_970.KlingelnbergCycloPalloidHypoidGearSetDesign':
        """KlingelnbergCycloPalloidHypoidGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _970.KlingelnbergCycloPalloidHypoidGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergCycloPalloidHypoidGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_klingelnberg_conical_gear_set_design(self) -> '_974.KlingelnbergConicalGearSetDesign':
        """KlingelnbergConicalGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _974.KlingelnbergConicalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to KlingelnbergConicalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_hypoid_gear_set_design(self) -> '_978.HypoidGearSetDesign':
        """HypoidGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _978.HypoidGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to HypoidGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_face_gear_set_design(self) -> '_986.FaceGearSetDesign':
        """FaceGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _986.FaceGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to FaceGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cylindrical_gear_set_design(self) -> '_1019.CylindricalGearSetDesign':
        """CylindricalGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1019.CylindricalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cylindrical_planetary_gear_set_design(self) -> '_1031.CylindricalPlanetaryGearSetDesign':
        """CylindricalPlanetaryGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1031.CylindricalPlanetaryGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalPlanetaryGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_conical_gear_set_design(self) -> '_1144.ConicalGearSetDesign':
        """ConicalGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1144.ConicalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ConicalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_concept_gear_set_design(self) -> '_1166.ConceptGearSetDesign':
        """ConceptGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1166.ConceptGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to ConceptGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_bevel_gear_set_design(self) -> '_1170.BevelGearSetDesign':
        """BevelGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1170.BevelGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to BevelGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_agma_gleason_conical_gear_set_design(self) -> '_1183.AGMAGleasonConicalGearSetDesign':
        """AGMAGleasonConicalGearSetDesign: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _1183.AGMAGleasonConicalGearSetDesign.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to AGMAGleasonConicalGearSetDesign. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_941.GearSetDesign]':
        """List[GearSetDesign]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ShaftHubConnection(_2537.ShaftHubConnection, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ShaftHubConnection

    A specific implementation of 'ListWithSelectedItem' for 'ShaftHubConnection' types.
    """

    __hash__ = None
    __qualname__ = 'ShaftHubConnection'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ShaftHubConnection.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2537.ShaftHubConnection.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2537.ShaftHubConnection.TYPE

    @property
    def selected_value(self) -> '_2537.ShaftHubConnection':
        """ShaftHubConnection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2537.ShaftHubConnection]':
        """List[ShaftHubConnection]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_TSelectableItem(Generic[TSelectableItem], mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_TSelectableItem

    A specific implementation of 'ListWithSelectedItem' for 'TSelectableItem' types.
    """

    __hash__ = None
    __qualname__ = 'TSelectableItem'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_TSelectableItem.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'TSelectableItem':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return TSelectableItem

    @property
    def selected_value(self) -> 'TSelectableItem':
        """TSelectableItem: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[TSelectableItem]':
        """List[TSelectableItem]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CylindricalGearSystemDeflection(_2679.CylindricalGearSystemDeflection, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CylindricalGearSystemDeflection

    A specific implementation of 'ListWithSelectedItem' for 'CylindricalGearSystemDeflection' types.
    """

    __hash__ = None
    __qualname__ = 'CylindricalGearSystemDeflection'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CylindricalGearSystemDeflection.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2679.CylindricalGearSystemDeflection.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2679.CylindricalGearSystemDeflection.TYPE

    @property
    def selected_value(self) -> '_2679.CylindricalGearSystemDeflection':
        """CylindricalGearSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2679.CylindricalGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cylindrical_gear_system_deflection_timestep(self) -> '_2680.CylindricalGearSystemDeflectionTimestep':
        """CylindricalGearSystemDeflectionTimestep: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2680.CylindricalGearSystemDeflectionTimestep.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGearSystemDeflectionTimestep. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cylindrical_gear_system_deflection_with_ltca_results(self) -> '_2681.CylindricalGearSystemDeflectionWithLTCAResults':
        """CylindricalGearSystemDeflectionWithLTCAResults: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2681.CylindricalGearSystemDeflectionWithLTCAResults.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalGearSystemDeflectionWithLTCAResults. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def selected_value_of_type_cylindrical_planet_gear_system_deflection(self) -> '_2684.CylindricalPlanetGearSystemDeflection':
        """CylindricalPlanetGearSystemDeflection: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _2684.CylindricalPlanetGearSystemDeflection.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CylindricalPlanetGearSystemDeflection. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2679.CylindricalGearSystemDeflection]':
        """List[CylindricalGearSystemDeflection]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_DesignState(_5587.DesignState, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_DesignState

    A specific implementation of 'ListWithSelectedItem' for 'DesignState' types.
    """

    __hash__ = None
    __qualname__ = 'DesignState'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_DesignState.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_5587.DesignState.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5587.DesignState.TYPE

    @property
    def selected_value(self) -> '_5587.DesignState':
        """DesignState: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_5587.DesignState]':
        """List[DesignState]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_FEPart(_2393.FEPart, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_FEPart

    A specific implementation of 'ListWithSelectedItem' for 'FEPart' types.
    """

    __hash__ = None
    __qualname__ = 'FEPart'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_FEPart.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2393.FEPart.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2393.FEPart.TYPE

    @property
    def selected_value(self) -> '_2393.FEPart':
        """FEPart: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2393.FEPart]':
        """List[FEPart]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_TPartAnalysis(Generic[TPartAnalysis], mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_TPartAnalysis

    A specific implementation of 'ListWithSelectedItem' for 'TPartAnalysis' types.
    """

    __hash__ = None
    __qualname__ = 'TPartAnalysis'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_TPartAnalysis.TYPE'):
        try:
            self.enclosing = instance_to_wrap
            self.wrapped = instance_to_wrap.SelectedValue
        except (TypeError, AttributeError):
            pass

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> 'TPartAnalysis':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return TPartAnalysis

    @property
    def selected_value(self) -> 'TPartAnalysis':
        """TPartAnalysis: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[TPartAnalysis]':
        """List[TPartAnalysis]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_CMSElementFaceGroup(_216.CMSElementFaceGroup, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_CMSElementFaceGroup

    A specific implementation of 'ListWithSelectedItem' for 'CMSElementFaceGroup' types.
    """

    __hash__ = None
    __qualname__ = 'CMSElementFaceGroup'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_CMSElementFaceGroup.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_216.CMSElementFaceGroup.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _216.CMSElementFaceGroup.TYPE

    @property
    def selected_value(self) -> '_216.CMSElementFaceGroup':
        """CMSElementFaceGroup: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _216.CMSElementFaceGroup.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to CMSElementFaceGroup. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_216.CMSElementFaceGroup]':
        """List[CMSElementFaceGroup]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ResultLocationSelectionGroup(_5768.ResultLocationSelectionGroup, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ResultLocationSelectionGroup

    A specific implementation of 'ListWithSelectedItem' for 'ResultLocationSelectionGroup' types.
    """

    __hash__ = None
    __qualname__ = 'ResultLocationSelectionGroup'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ResultLocationSelectionGroup.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_5768.ResultLocationSelectionGroup.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5768.ResultLocationSelectionGroup.TYPE

    @property
    def selected_value(self) -> '_5768.ResultLocationSelectionGroup':
        """ResultLocationSelectionGroup: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_5768.ResultLocationSelectionGroup]':
        """List[ResultLocationSelectionGroup]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_StaticLoadCase(_6719.StaticLoadCase, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_StaticLoadCase

    A specific implementation of 'ListWithSelectedItem' for 'StaticLoadCase' types.
    """

    __hash__ = None
    __qualname__ = 'StaticLoadCase'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_StaticLoadCase.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_6719.StaticLoadCase.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _6719.StaticLoadCase.TYPE

    @property
    def selected_value(self) -> '_6719.StaticLoadCase':
        """StaticLoadCase: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        if _6719.StaticLoadCase.TYPE not in temp.__class__.__mro__:
            raise CastException('Failed to cast selected_value to StaticLoadCase. Expected: {}.'.format(temp.__class__.__qualname__))

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_6719.StaticLoadCase]':
        """List[StaticLoadCase]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_DutyCycle(_5588.DutyCycle, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_DutyCycle

    A specific implementation of 'ListWithSelectedItem' for 'DutyCycle' types.
    """

    __hash__ = None
    __qualname__ = 'DutyCycle'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_DutyCycle.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_5588.DutyCycle.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _5588.DutyCycle.TYPE

    @property
    def selected_value(self) -> '_5588.DutyCycle':
        """DutyCycle: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_5588.DutyCycle]':
        """List[DutyCycle]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_ElectricMachineDataSet(_2313.ElectricMachineDataSet, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_ElectricMachineDataSet

    A specific implementation of 'ListWithSelectedItem' for 'ElectricMachineDataSet' types.
    """

    __hash__ = None
    __qualname__ = 'ElectricMachineDataSet'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_ElectricMachineDataSet.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2313.ElectricMachineDataSet.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2313.ElectricMachineDataSet.TYPE

    @property
    def selected_value(self) -> '_2313.ElectricMachineDataSet':
        """ElectricMachineDataSet: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2313.ElectricMachineDataSet]':
        """List[ElectricMachineDataSet]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value


class ListWithSelectedItem_PointLoad(_2411.PointLoad, mixins.ListWithSelectedItemMixin):
    """ListWithSelectedItem_PointLoad

    A specific implementation of 'ListWithSelectedItem' for 'PointLoad' types.
    """

    __hash__ = None
    __qualname__ = 'PointLoad'

    def __init__(self, instance_to_wrap: 'ListWithSelectedItem_PointLoad.TYPE'):
        try:
            self.enclosing = instance_to_wrap
        except (TypeError, AttributeError):
            pass
        super().__init__(instance_to_wrap.SelectedValue)

    @classmethod
    def wrapper_type(cls) -> '_LIST_WITH_SELECTED_ITEM':
        """Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _LIST_WITH_SELECTED_ITEM

    @classmethod
    def implicit_type(cls) -> '_2411.PointLoad.TYPE':
        """Implicit Pythonnet type of this class.

        Note:
            This property is readonly.
        """

        return _2411.PointLoad.TYPE

    @property
    def selected_value(self) -> '_2411.PointLoad':
        """PointLoad: 'SelectedValue' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.SelectedValue
        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp) if temp is not None else None

    @property
    def available_values(self) -> 'List[_2411.PointLoad]':
        """List[PointLoad]: 'AvailableValues' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.enclosing.AvailableValues
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

"""_6812.py

HarmonicLoadDataCSVImport
"""


from typing import List, Generic, TypeVar

from mastapy.system_model.analyses_and_results.static_loads import _6782, _6816, _6794
from mastapy._internal import constructor, conversion
from mastapy._internal.python_net import python_net_import

_HARMONIC_LOAD_DATA_CSV_IMPORT = python_net_import('SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads', 'HarmonicLoadDataCSVImport')


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicLoadDataCSVImport',)


T = TypeVar('T', bound='_6794.ElectricMachineHarmonicLoadImportOptionsBase')


class HarmonicLoadDataCSVImport(_6816.HarmonicLoadDataImportFromMotorPackages['T'], Generic[T]):
    """HarmonicLoadDataCSVImport

    This is a mastapy class.

    Generic Types:
        T
    """

    TYPE = _HARMONIC_LOAD_DATA_CSV_IMPORT

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HarmonicLoadDataCSVImport.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def electric_machine_data_per_speed(self) -> 'List[_6782.DataFromMotorPackagePerSpeed]':
        """List[DataFromMotorPackagePerSpeed]: 'ElectricMachineDataPerSpeed' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.ElectricMachineDataPerSpeed
        value = conversion.pn_to_mp_objects_in_list(temp)
        return value

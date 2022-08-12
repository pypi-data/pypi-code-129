"""_1311.py

OpenCircuitElectricMachineResults
"""


from mastapy._internal import constructor
from mastapy.electric_machines.results import _1294
from mastapy._internal.python_net import python_net_import

_OPEN_CIRCUIT_ELECTRIC_MACHINE_RESULTS = python_net_import('SMT.MastaAPI.ElectricMachines.Results', 'OpenCircuitElectricMachineResults')


__docformat__ = 'restructuredtext en'
__all__ = ('OpenCircuitElectricMachineResults',)


class OpenCircuitElectricMachineResults(_1294.ElectricMachineResults):
    """OpenCircuitElectricMachineResults

    This is a mastapy class.
    """

    TYPE = _OPEN_CIRCUIT_ELECTRIC_MACHINE_RESULTS

    __hash__ = None

    def __init__(self, instance_to_wrap: 'OpenCircuitElectricMachineResults.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def back_emf_constant(self) -> 'float':
        """float: 'BackEMFConstant' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.BackEMFConstant
        return temp

    @property
    def line_to_line_back_emf_peak(self) -> 'float':
        """float: 'LineToLineBackEMFPeak' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LineToLineBackEMFPeak
        return temp

    @property
    def line_to_line_back_emfrms(self) -> 'float':
        """float: 'LineToLineBackEMFRMS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LineToLineBackEMFRMS
        return temp

    @property
    def line_to_line_back_emf_total_harmonic_distortion(self) -> 'float':
        """float: 'LineToLineBackEMFTotalHarmonicDistortion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.LineToLineBackEMFTotalHarmonicDistortion
        return temp

    @property
    def phase_back_emf_peak(self) -> 'float':
        """float: 'PhaseBackEMFPeak' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseBackEMFPeak
        return temp

    @property
    def phase_back_emfrms(self) -> 'float':
        """float: 'PhaseBackEMFRMS' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseBackEMFRMS
        return temp

    @property
    def phase_back_emf_total_harmonic_distortion(self) -> 'float':
        """float: 'PhaseBackEMFTotalHarmonicDistortion' is the original name of this property.

        Note:
            This property is readonly.
        """

        temp = self.wrapped.PhaseBackEMFTotalHarmonicDistortion
        return temp

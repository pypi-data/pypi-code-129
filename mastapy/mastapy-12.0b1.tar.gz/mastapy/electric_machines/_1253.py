"""_1253.py

HarmonicLoadDataControlExcitationOptionForElectricMachineMode
"""


from mastapy.electric_machines.harmonic_load_data import _1344
from mastapy._internal.python_net import python_net_import

_HARMONIC_LOAD_DATA_CONTROL_EXCITATION_OPTION_FOR_ELECTRIC_MACHINE_MODE = python_net_import('SMT.MastaAPI.ElectricMachines', 'HarmonicLoadDataControlExcitationOptionForElectricMachineMode')


__docformat__ = 'restructuredtext en'
__all__ = ('HarmonicLoadDataControlExcitationOptionForElectricMachineMode',)


class HarmonicLoadDataControlExcitationOptionForElectricMachineMode(_1344.HarmonicLoadDataControlExcitationOptionBase):
    """HarmonicLoadDataControlExcitationOptionForElectricMachineMode

    This is a mastapy class.
    """

    TYPE = _HARMONIC_LOAD_DATA_CONTROL_EXCITATION_OPTION_FOR_ELECTRIC_MACHINE_MODE

    __hash__ = None

    def __init__(self, instance_to_wrap: 'HarmonicLoadDataControlExcitationOptionForElectricMachineMode.TYPE'):
        super().__init__(instance_to_wrap)
        self._freeze()

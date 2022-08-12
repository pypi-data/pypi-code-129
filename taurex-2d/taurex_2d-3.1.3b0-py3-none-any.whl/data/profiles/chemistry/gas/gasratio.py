from taurex.data.profiles.chemistry.gas.gas import Gas
from .constantgas import ConstantGas
from taurex.util import molecule_texlabel
from fractions import Fraction

class GasRatio(ConstantGas, Gas):
    """
    Gas profile computed as a ratio from another gas.

    Parameters
    -----------
    molecule_name : str
        Name of molecule

    day_mix_ratio : :obj:`array`
        Mixing ratio of the molecule on the day side

    night_mix_ratio : :obj:`array`
        Mixing ratio of the molecule on the night side
    """

    def __init__(self, molecule_name='CO',
                 ratio=1e-5,
                 molecule_reference='H2O',
                 ):
        Gas.__init__(self, self.__class__.__name__, molecule_name)
        self.ratio = float(Fraction(ratio))
        self.molecule_reference = molecule_reference
        self.add_active_gas_param()


    def initialize_profile(self, nlayers, temperature_profile,
                           pressure_profile, altitude_profile, gases=None):
        self._mix_array = self.ratio * gases[self.molecule_reference]

    def add_active_gas_param(self):
        """
        Adds the mixing ratio as a fitting parameter
        as the name of the molecule
        """
        mol_name = self.molecule
        bounds = [1.0e-12, 0.1]
        default_fit = False

        def read_mol(self):
            return self.ratio
        def write_mol(self, value):
            self.ratio = value
        self.add_fittable_param(self.molecule, molecule_texlabel(mol_name), read_mol, write_mol,
                                'log', default_fit, bounds)

    def write(self, output):
        gas_entry = Gas.write(self, output)
        gas_entry.write_scalar('ratio', self.ratio)
        gas_entry.write_scalar('molecule_reference', self.molecule_reference)
        return gas_entry

    @classmethod
    def input_keywords(cls):
        return ['ratio', ]
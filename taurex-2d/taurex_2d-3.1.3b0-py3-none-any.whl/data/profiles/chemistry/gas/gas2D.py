from taurex.data.profiles.chemistry.gas.gas import Gas
from .gas import SimpleGas
from .constantgas import ConstantGas
from taurex.util import molecule_texlabel
import numpy as np

class Gas2D(ConstantGas, Gas):
    """
    Gas profile based on a 2D polar grid (see :class:`~taurex.model.transmission2D.Transmission2DModel`).
    A volume mixing ratio can be set independently on the day and on the night side.

    Parameters
    -----------
    molecule_name : str
        Name of molecule

    day_mix_ratio : :obj:`array`
        Mixing ratio of the molecule on the day side

    night_mix_ratio : :obj:`array`
        Mixing ratio of the molecule on the night side
    """

    def __init__(self, molecule_name='H2O',
                 day_mix_ratio=1e-5,
                 night_mix_ratio=1e-5,
                 deep_mix_ratio=None,
                 mix_ratio=None,
                 dissociation=False, alpha=None, beta=None, gamma=None
                 ):
        SimpleGas.__init__(self, name=self.__class__.__name__, molecule_name=molecule_name, dissociation=dissociation, alpha=alpha, beta=beta, gamma=gamma)

        self.mix_ratio = mix_ratio
        if not self.mix_ratio:
            self.day_mix_ratio = day_mix_ratio
            self.night_mix_ratio = night_mix_ratio
            self.deep_mix_ratio = deep_mix_ratio
            if not deep_mix_ratio:
                self.deep_mix_ratio = night_mix_ratio
            self.p_iso = None
        self.add_active_gas_param()


    def initialize_profile(self, nlayers, temperature_profile,
                           pressure_profile, altitude_profile, model=None):
        self._mix_array = np.zeros(pressure_profile.shape)
        terminator = int(len(pressure_profile)/2)
        if not self.mix_ratio:
            self._mix_array[:terminator,:] = self.night_mix_ratio
            self._mix_array[terminator:,:] = self.day_mix_ratio
            if self.p_iso:
                p_iso_ids = np.where(pressure_profile[0] > self.p_iso) # pressure profile is the same in all columns
                self._mix_array[:,p_iso_ids] = self.deep_mix_ratio
        else:
            self._mix_array[:] = self.mix_ratio

    def add_active_gas_param(self):
        """
        Adds the mixing ratio as a fitting parameter
        as the name of the molecule
        """

        mol_name = self.molecule
        bounds = [1.0e-12, 0.1]
        default_fit = False

        param_tex = molecule_texlabel(mol_name)
        param_name = self.molecule
        def read_mol(self):
            return self.mix_ratio
        def write_mol(self, value):
            self.mix_ratio = value
        fget = read_mol
        fset = write_mol
        self.add_fittable_param(param_name, param_tex, fget, fset,
                                'log', default_fit, bounds)

        if not self.mix_ratio:
            param_tex = molecule_texlabel(mol_name)+"_day"
            param_name = self.molecule+"_day"
            def day_read_mol(self):
                return self.day_mix_ratio
            def day_write_mol(self, value):
                self.day_mix_ratio = value
            fget = day_read_mol
            fset = day_write_mol
            self.add_fittable_param(param_name, param_tex, fget, fset,
                                    'log', default_fit, bounds)

            param_tex = molecule_texlabel(mol_name)+"_night"
            param_name = self.molecule+"_night"
            def night_read_mol(self):
                return self.night_mix_ratio
            def night_write_mol(self, value):
                self.night_mix_ratio = value
            fget = night_read_mol
            fset = night_write_mol
            self.add_fittable_param(param_name, param_tex, fget, fset,
                                    'log', default_fit, bounds)

            param_tex = molecule_texlabel(mol_name)+"_deep"
            param_name = self.molecule+"_deep"
            def deep_read_mol(self):
                return self.deep_mix_ratio
            def deep_write_mol(self, value):
                self.deep_mix_ratio = value
            fget = deep_read_mol
            fset = deep_write_mol
            self.add_fittable_param(param_name, param_tex, fget, fset,
                                    'log', default_fit, bounds)

    def write(self, output):
        gas_entry = Gas.write(self, output)
        if not self.mix_ratio:
            gas_entry.write_scalar('day_mix_ratio', self.day_mix_ratio)
            gas_entry.write_scalar('night_mix_ratio', self.night_mix_ratio)
            gas_entry.write_scalar('deep_mix_ratio', self.deep_mix_ratio)
        else:
            gas_entry.write_scalar('mix_ratio', self.mix_ratio)
        if self.dissociation:
            gas_entry.write_string('alpha', self.alpha)
            gas_entry.write_string('beta', self.beta)
            gas_entry.write_string('gamma', self.gamma)

        return gas_entry

    @classmethod
    def input_keywords(cls):
        return ['2d', ]

__version__ = "0.3.2"

from pyemission import utility_functions
from pyemission.utility_functions import read_data, calculate_tractive_power, calculate_vsp, vsp_to_op_mod, op_mod_to_emission_rate, joule_to_kwh, convert_to_overall_mpg, energy_kj_to_ml, vsp_coeff, progress_bar
from pyemission.Car import Car
from pyemission.GV import GV
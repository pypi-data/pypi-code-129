import pyseafuel._constants as _constants
import numpy as np

# ──────────────────────────────────────────────────────────────────────────

def mcphy_piel(volume_h2o_in):
    """
    Estimating power consumption and outflows for electrolyzing pure water with an McPhy Piel series electrolyzer.

    Parameters
    ----------
    volume_h2o_in : float
        Pure water inflow; liters per second.

    Returns
    -------
    mass_h2_out : float
        Mass flow rate out of hydrogen gas; kilograms per second.
    mass_o2_out : float
        Mass flow rate out of oxygen gas; kilograms per second.
    power_consumed : float
        Power consumed during electrolysis; Watts.

    Notes
    -----
    The values to calculate the process of electrolysis come from the datasheet for the `McPhy Piel series H model electrolyzer. <https://mcphy.com/en/equipment-services/electrolyzers/small/>`_ It consumes 18 kW at an outflow of 3 m:sup:`3`/h of hydrogen and 60 kW at 10 m:sup:`3`/h.

    This function is only accurate if the water inflow `volume_h2o_in` remains between 6.69 x 10:sup:`-4` L/s and 2.23 x 10:sup:`-3` L/s.
    """

    volume_h2o_in /= 1000  # m^3/s; converting from liters to cubic meters

    ratio_h2_o2 = 2*_constants.rho_h2/_constants.rho_o2  # ratio of hydrogen over oxygen mass outflow rates

    # output volumes
    volume_h2_out = volume_h2o_in * _constants.rho_h2o / (1 + 1/ratio_h2_o2) / _constants.rho_h2  # m^3/s
    volume_o2_out = volume_h2_out * .5  # m^3/s

    # output masses
    mass_h2_out = volume_h2_out * _constants.rho_h2  # kg/s
    mass_o2_out = volume_o2_out * _constants.rho_o2  # kg/s

    linear_fit = np.polyfit([3/3600, 10/3600], [18, 60], 1)  # linear interpolation/extrapolation to estimate power consumed
    power_consumed = np.polyval(linear_fit, volume_h2_out) * 1000  # W

    return mass_h2_out, mass_o2_out, power_consumed


def Shen(volume_h2o_in, E0, K, R, A, output_voltage=False):
    """
    Calculates power consumption and outflows for electrolyzing pure water using the concise model from Shen et al. 2011 (see References section).

    Parameters
    ----------
    volume_h2o_in : float
        Volumetric inflow of water; liters per second.
    E0 : float
        Reversible cell potential; depends on the cell's materials; Volts.
    K : float
        Power conversion coefficient; unity per ohm squared centimeter.
    R : float
        Cell (internal) resistance; ohm squared centimeter.
    A : float
        Membrane stack area; squared centimeter.
    output_voltage : boolean
        Flag to return voltage (V) with other return variables.

    Returns
    -------
    mass_h2_out : float
        Mass outflow of hydrogen; kilograms per second.
    mass_o2_out : float
        Mass outflow of oxygen; kilograms per second.
    power_consumed : float
        Power consumed during electrolysis.
    V : float (optional)
        Operating voltage; V; see `output_voltage`.

    Notes
    -----
    Power calculation comes from the model in [1]_. Essentially, power is assumed to be proportional to the square of the cell voltage, ::math:`V`, internal resistance, ::math:`R`, and cell dissociatio potential, ::math:`E_0`:

    .. math:: P = K ( V - IR - E_0)^2

    ::math:`K` and ::math:`R` are given in units with cm:sup:`2` because electrolysis processes are typically measured with current density rather than current.
    
    References
    ----------
    .. [1] N. Shen, N. Bennett, Y. Ding, and K. Scott, "A concise model for evaluating water electrolysis," International Journal of Hydrogen Energy, vol. 36, pp. 14335-14341, 2011.
    """

    volume_h2o_in /= 1000  # m^3/s; converting from liters to cubic meters
    mass_h2o_in = volume_h2o_in * _constants.rho_h2o  # kg/s

    # molecular flow rates
    mol_h2o = mass_h2o_in / _constants.mol_weight_h2o
    mol_h2 = mol_h2o
    mol_o2 = mol_h2o/2

    # mass outflow rates
    mass_h2_out = mol_h2 * _constants.mol_weight_h2
    mass_o2_out = mol_o2 * _constants.mol_weight_o2

    # power calculation
    I = _constants.F * 2 * mol_h2o / A  # A/cm^2; current density

    a = K
    b = K * (-2*I*R - 2*E0) - I
    c = K * (2*E0*I*R + I**2*R**2 + E0**2) + I*R**2

    V = (-b + (b**2 - 4*a*c)**(1/2)) / (2 * a)  # V; model from reference

    power_consumed = V * I * A  # W

    if output_voltage:
        return mass_h2_out, mass_o2_out, power_consumed, V

    else:
        return mass_h2_out, mass_o2_out, power_consumed

import pyseafuel._constants as _constants
import numpy as np

# ──────────────────────────────────────────────────────────────────────────

def ideal(volume_seawater_in, S, T, water_ratio, efficiency=1, brine_concentration=False):
    """
    Thermodynamic limit for desalinating an inflow of saline water to produce pure water.

    Parameters
    ----------
    volume_seawater_in : float
        Seawater inflow; liters per second.
    S : float
        Seawater inflow salinity; Practical Salinity Units.
    T : float
        Temperature of the seawater inflow; Kelvin.
    water_ratio : float
        Ratio of the inflow separated into pure water; between [0, 1].
    P : float (optional)
        Operating pressure of the inflow; decibars; default = 10.1325 db.
    efficiency : float (optional)
        Efficiency of the desalination process; between [0, 1]; default = 1.
    brine_concentration : boolean (optional)
        Returns brine molar concentration if set to True; default = False.

    Returns
    -------
    volume_h2o_out : float
        Flow of pure water out, in liters per second.
    volume_brine_out : float
        Flow of brine out, in liters per second.
    power_consumed : float
        Power consumed by the desalination process, in Watts.
    c_b : float (optional)
        Brine molar concentration, in moles per liter.

    References
    ----------
    .. [1] L. Wang, C. Violet, R. DuChanois, and M. Elimelech, "Derivation of the Theoretical Minimum Energy of Separation of Desalination Process," Journal of Chemical Education, vol. 97, pp. 4361-4369, 2020.
    """

    # molar concentration of salt in inflow
    ppt = S  # PSU approxiamtely equal to parts per thousand (PPT); which is essentially in g/L;
    c_f = ppt / _constants.mol_weight_nacl / 1000  # mol/L

    pi_f = 2 * _constants.R * T * c_f   # J/L; osmotic pressure of sea water

    # calculating power consumed
    sec = -pi_f / water_ratio * np.log(1 - water_ratio)  # J/L; sec is the specific energy consumption to produce the pure water given the saline inflow
    power_consumed = volume_seawater_in * sec * efficiency  # W; power required to input feed 

    # output flows
    volume_h2o_out = water_ratio * volume_seawater_in  # L/s; output of pure water
    volume_brine_out = (1 - water_ratio) * volume_seawater_in  # L/s; output of brine

    c_b = c_f / (1 - water_ratio)  # brine concentration; moles per liter

    if brine_concentration:
        return volume_h2o_out, volume_brine_out, power_consumed, c_b

    return volume_h2o_out, volume_brine_out, power_consumed


def reverse_osmosis(volume_seawater_in, S, T, water_ratio, stages, brine_concentration=False):
    """
    Multistage reverse osmosis desalinator for desalinating an inflow of saline water to produce pure water.

    Parameters
    ----------
    volume_seawater_in : float
        Seawater inflow; liters per second.
    S : float
        Seawater inflow salinity; Practical Salinity Units.
    T : float
        Temperature of the seawater inflow; Kelvin.
    water_ratio : float
        Ratio of the inflow separated into pure water; between [0, 1].
    stages : int
        Number of stages.
    brine_concentration : boolean (optional)
        Returns brine molar concentration if set to True; default = False.

    Returns
    -------
    volume_h2o_out : float
        Flow of pure water out; liters per second.
    volume_brine_out : float
        Flow of brine out; liters per second.
    power_consumed : float
        Power consumed by the desalination process; Watts.
    c_b : float (optional)
        Brine molar concentration; moles per liter.

    References
    ----------
    .. [1] L. Wang, C. Violet, R. DuChanois, and M. Elimelech, "Derivation of the Theoretical Minimum Energy of Separation of Desalination Process," Journal of Chemical Education, vol. 97, pp. 4361-4369, 2020.
    """

    def _water_ratio_i(water_ratio, stages, i):
        """Water ratio per stage.
        """

        water_ratio_i = water_ratio * i / ((1 - water_ratio) * stages + water_ratio * i)

        return water_ratio_i

    # molar concentration of salt in the inflow
    ppt = S  # PSU approxiamtely equal to parts per thousand (PPT); which is essentially in g/L;
    c_f = ppt / _constants.mol_weight_nacl / 1000  # mol/L

    pi_f = 2 * _constants.R * T * c_f  # J/l; osmotic pressure of sea water

    # calculating specific energy consumption
    sec = 0

    for i in np.arange(1, stages+1):
        sec += (_water_ratio_i(water_ratio, stages, i) - _water_ratio_i(water_ratio, stages, i-1)) / (1 - _water_ratio_i(water_ratio, stages, i))

    sec *= pi_f / water_ratio  # J/L; sec is the specific energy consumption to produce the pure water given the saline inflow

    # power consumed
    power_consumed = volume_seawater_in * sec  # W; power required to input feed 

    # volume outflows
    volume_h2o_out = water_ratio * volume_seawater_in  # L/s; output of pure water
    volume_brine_out = (1 - water_ratio) * volume_sea_water_in  # L/s; output of brine

    c_b = c_f / (1 - water_ratio)  # mol/L; brince concentration

    if brine_concentration:
        return volume_h2o_out, volume_brine_out, power_consumed, c_b

    return volume_h2o_out, volume_brine_out, power_consumed


def electrodialysis(volume_seawater_in, S, T, water_ratio, salt_removal, stages, brine_concentration=False):
    """
    Multistage electrodialysis desalinator for desalinating an inflow of saline water to produce pure water.

    Parameters
    ----------
    volume_seawater_in : float
        Seawater inflow; liters per second.
    S : float
        Seawater inflow salinity; Practical Salinity Units.
    T : float
        Seawater inflow temperature; Kelvin.
    water_ratio : float
        Ratio of the inflow separated into pure water; between [0, 1].
    salt_removal : float
        Percentage of salt removal in terms of concentration for the output flow; between (0, 1).
    stages : int
        Number of stages.
    brine_concentration : boolean (optional)
        Returns brine molar concentration if set to True; default = False.

    Returns
    -------
    volume_h2o_out : float
        Flow of pure water out; liters per second.
    volume_brine_out : float
        Flow of brine out; liters per second.
    power_consumed : float
        Power consumed by the desalination process; Watts.
    c_b : float (optional)
        Brine molar concentration; moles per liter.

    References
    ----------
    .. [1] L. Wang, C. Violet, R. DuChanois, and M. Elimelech, "Derivation of the Theoretical Minimum Energy of Separation of Desalination Process," Journal of Chemical Education, vol. 97, pp. 4361-4369, 2020.
    """
    
    # per stage values
    salt_removal_i = 1 - (1 - salt_removal)**(1/stages)  # salt removal percentage per stage in terms of concentration
    water_ratio_i = water_ratio**(1/stages)  # water ratio per stage

    # Calculating inflow salt molar concentration
    ppt = S  # PSU approxiamtely equal to parts per thousand (PPT); which is essentially in g/L;
    c_f = ppt / _constants.mol_weight_nacl / 1000  # mol/L

    # calculating specific energy consumption
    sec = 0
    
    for i in np.arange(1, stages+1):
        sec += (1 - salt_removal_i)**(i-1)

    sec *= 2 * _constants.R * T * salt_removal_i * c_f * np.log(1 / ( (1 - salt_removal_i) * (1 - water_ratio_i)) - water_ratio_i / (1 - water_ratio_i))

    # calculating power consumption
    power_consumed = volume_seawater_in * sec

    # volume outflows
    volume_h2o_out = water_ratio * volume_seawater_in  # L/s; output of pure water
    volume_brine_out = (1 - water_ratio) * volume_seawater_in  # L/s; output of brine

    # brine concentration
    c_b = c_f * (1 - (1 - salt_removal) * water_ratio) / (1 - water_ratio)  # mol/L; brine molar concentration

    if brine_concentration:
        return volume_h2o_out, volume_brine_out, power_consumed, c_b

    return volume_h2o_out, volume_brine_out, power_consumed

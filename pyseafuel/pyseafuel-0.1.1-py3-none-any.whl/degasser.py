import pyseafuel._constants as _constants

# ──────────────────────────────────────────────────────────────────────────

def bipolar_membrane(volume_seawater_in, outflow_pH=4.5):
    """
    Calculates the outflow and power consumption to extract carbon dioxide gas from sea water.

    Parameters
    ----------
    volume_seawater_in : float
        Sea water inflow; liters per second.
    outflow_pH : float (optional)
        Desired outflow pH of the acidified sea water stream; default = 4.5.

    Returns
    -------
    mass_co2_out : float
        Mass flow rate out of degassed carbon dioxide; kilogram per second.
    power_consumed : float
        Power consumed to operate the electrodialysis device; Watts.

    Notes
    -----
    This function estimates the carbon dioxide extraction flow rate and power consumption from sea water from the data found in Table SI in [1]_. [1]_ outlines and tests a prototype bipolar membrane electrodialysis device that separates the inflow sea water into a basified and acidified stream, extracting carbon dioxide from the acified stream.

    References
    ----------
    .. [1] M. Eisaman, K. Parajuly, A. Tuganov, C. Eldershaw, N. Chang, and K. Littau, "CO:sub:`2` extraction from seawater using bipolar membrane electrodialysis," vol. 5, pp. 7346-7352, 2012.
    """

    def flow_ratio_from_pH(pH):
        """
        Ratio of carbon dioxide out to seawater in. Fitted from data from Table SI from [1]_.
        """

        # fitted values
        a = -1.19546904e4
        b = 3.11106752e2
        c = 3.89901804 - pH

        flow_ratio = (-b - (b**2 - 4*a*c)**.5) / 2 / a  # Lpm/Lpm; co2 out / seawater in
    
        return flow_ratio

    def power_required(mass_co2_out, pH):
        """
        Power consumed extracting carbon dioxide. Fitted from data from Table SI from [1]_.
        """

        # fitted values
        a = 58.29015036
        b = -524.44486215
        c = 1423.21006136
        
        energy_mol = a*pH**2 + b*pH + c  # kJ/mol
        energy_kg = energy_mol * 1000 / _constants.mol_weight_co2  # J/kg
        power = energy_kg * mass_co2_out  # W

        return power

    volume_co2_out = flow_ratio_from_pH(outflow_pH) * volume_seawater_in  # L/s at STP
    mass_co2_out = volume_co2_out * _constants.rho_co2 / 1000  # kg/s; converting to mass flow

    power_consumed = power_required(mass_co2_out, outflow_pH)  # W

    return mass_co2_out, power_consumed

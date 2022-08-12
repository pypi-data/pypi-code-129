import pyseafuel._constants as _constants
import numpy as np

# ──────────────────────────────────────────────────────────────────────────

def carbon_dioxide(ppm_co2, T, S, P=101325, volume=True):
    """
    Calculate the gaseous carbon dioxide dissolved into sea water from the atmosphere at equilibrium.

    Parameters
    ----------
    ppm_co2 : float
        Atmospheric concentration of carbon dioxide in dry air; mole fraction Parts Per Million (micromol/mol).
    T : float
        Seawater temperature; Kelvin.
    S : float
        Seawater salinity; Practical Salinity Units (PSU).
    P : float (optional)
        Pressure at the air-sea interface; Pa; default = 101325 Pa.
    volume : bool (optional)
        Whether or not to calculate dissolved carbon dioxide in mol/L or mol/kg.

    Returns
    -------
    co2 : float
        Dissolved carbon dioxide and carbonic acid in the ocean; mol/L or mol/kg (see 'volume'); defaults to mol/L.

    Notes
    -----
    [CO:sub:`2`] includes dissolved CO:sub:`2` and H:sub:`2`CO:sub:`3`, as they are hard to distinguish in experiments.

    From [1]_:

    .. math:: [CO_2] = K f_{CO_2} e^{(1 - P) v_{CO_2} / RT}

    However, when pressure is close to 1 atm, we can assume the exponential term goes to 1:
    
    .. math:: [CO_2] = K * f_{CO_2} 

    References
    ----------
    .. [1] R. F. Weiss "Carbon Dioxide in Water and Seawater: The Solubility of a Non-ideal Gas," Marine Chemistry, vol. 2, pp. 203-216, 1974.
    """

    if volume:
        # constants for volume basis
        A = [-58.0931, 90.5069, 22.2940]
        B = [0.027766, -0.025888, 0.0050578]

    else:
        # constants for mass basis
        A = [-60.2409, 93.4517, 23.3585]
        B = [0.023517, -0.023656, 0.0047036]
    
    K = np.exp(A[0] + A[1]*(100/T) + A[2]*np.log(T/100) + S*(B[0] + B[1]*(T/100) + B[2]*(T/100)**2)) / 101325  # mol/L Pa or mol/kg Pa

    # calculating molar fractions
    x_co2 = ppm_co2 * 1e-6  # mol co2 / mol dry air; mole fraction
    x_air = 1 - x_co2  # mol air / mol dry air; mole fraction

    # calculating fugacity
    second_virial_coef = (-1636.75 + 12.0408 * T - 3.27957e-2 * T**2 + 3.16528e-5 * T**3) * 1e-6  # m^3 / mol; second virial coefficient for co2
    delta_co2 = (57.7 - 0.118 * T) * 1e-6  # m^3 / mol co2; binary mixture coefficient
    f_co2 = x_co2 * P * np.exp((second_virial_coef + 2 * x_air**2 * delta_co2) * P / _constants.R / T)  # Pa; fugacity

    co2 = K * f_co2

    return co2


def bicarbonate(T, S, co2, pH):
    """
    Calculates the bicarbonate molar concentration of the ocean carbon buffer system at equilibrium.

    Parameters
    ----------
    T : float
        Seawater temperature; Kelvin.
    S : float
        Seawater salinity; Practical Salinity Units.
    co2 : float
        Sum of dissolved carbon dioxide and carbonic acid molar concentration; moles per kilogram of solution.
    pH : float
        Potential of hydrogen.
    
    Returns
    -------
    hco3 : float
        Molar concentration of bicarbonate; moles per kilogram of solution.

    Notes
    -----
    The coefficients come from [1]_.

    The dissolved CO:sub:`2` and H:sub:`2`CO:sub:`3` are hard to distinguish from one another in solution and are typically combined when calculating reaction equilibrium constants of the ocean buffer system [1]_.

    pH is defined as:

    .. math:: pH = - \log(a_{H^+})

    However, here, it is assumed that :math:`a_{H^+} \approx [H^+]`.

    References
    ----------
    .. [1] T. Lueker, A. Dickson, and C. Keeling, "Ocean pCO:sub:`2` calculated from dissolved inorganic carbon, alkalinity, and equations for K:sub:`1` and K:sub:`2`: validation based on laboratory measurements of CO:sub:`2` in gas and seawater at equilibrium," Marine Chemistry, vol. 70, pp. 105-119, 2000.
    """

    # pK1 = 3633.86/T - 61.2172 + 9.67770 * np.log(T) - 0.011555*S + 0.0001152*S**2
    # K1 = 10**(-pK1)

    K1 = 10**(-3633.86/T + 61.2172 - 9.67770*np.log(T) + 0.011555*S - 0.0001152*S**2)

    hco3 = K1 * co2 / 10**(-pH)

    return hco3

def carbonate(T, S, hco3, pH):
    """
    Calculates the carbonate molar concentration of the ocean carbon buffer system at equilibrium.

    Parameters
    ----------
    T : float
        Seawater temperature; Kelvin.
    S : float
        Seawater salinity; Practical Salinity Units.
    hco3 : float
        Bicarbonate molar concentration; moles per kilogram of solution.
    pH : float
        Potential of hydrogen.
    
    Returns
    -------
    co3 : float
        Molar concentration of bicarbonate; moles per kilogram of solution.

    Notes
    -----
    The coefficients come from [1]_.

    pH is defined as:

    .. math:: pH = - \log_{10}(a_{H^+})

    However, here, it is assumed that :math:`a_{H^+} \approx [H^+]`.

    References
    ----------
    .. [1] T. Lueker, A. Dickson, and C. Keeling, "Ocean pCO:sub:`2` calculated from dissolved inorganic carbon, alkalinity, and equations for K:sub:`1` and K:sub:`2`: validation based on laboratory measurements of CO:sub:`2` in gas and seawater at equilibrium," Marine Chemistry, vol. 70, pp. 105-119, 2000.
    """

    # pK2 = 471.78/T + 25.9290 - 3.16967 * np.log(T) - 0.01781 * S + 0.0001122 * S**2
    # K2 = 10**(-pK2)

    K2 = 10**(-471.78/T - 25.9290 + 3.16967*np.log(T) + 0.01781*S - 0.0001122*S**2)

    co3 = K2 * hco3 / 10**(-pH)

    return co3


def dic(co2, hco3, co3):
    """
    The dissolved inorganic carbon molar concentration is the sum of dissolved carbon dioxide, carbonic acid, bicarbonate, and carbonate.

    Parameters
    ----------
    co2 : float 
        Sum of dissolved carbon dioxide and carbonic acid molar concentration; moles per kilogram of solution.
    hco3 : float
        Bicarbonate molar concentration; moles per kilogram of solution.
    co3 : float
        Carbonate molar concentration; moles per kilogram of solution.
    
    Returns
    -------
    dic : float
        Molar concentration of dissolved inorganic carbon; moles per kilogram of solution.

    Notes
    -----
    CO:sub:`2`:sup:`*` is the sum of CO:sub:`2` and H:sub:`2`CO:sub:`3`.
    HCO:sub:`3`:sup:`-` is bicarbonate.
    CO:sub:`3`:sup:`2-` is carbonate.
    """

    return np.sum(co2, hco3, co3)

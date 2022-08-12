import pyseafuel._constants as _constants
import numpy as np
from scipy import integrate, optimize

# ──────────────────────────────────────────────────────────────────────────

def equilibrium(N_co_0, N_co2_0, N_h2_0, P, T):
    """
    Solves for the equilibrium of the hydrogenation of carbon dioxide reaction.

    Parameters
    ----------
    N_co_0 : float
        Initial amount of carbon monoxide; moles.
    N_co2_0 : float
        Initial amount of carbon dioxide; moles.
    N_h2_0 : float
        Initial amount of hydrogen; moles.
    P : float
        Pressure; bars.
    T : float
        Temperature; Kelvin.

    return N_co, N_co2, N_h2, N_h2o, N_ch3oh, xi_3

    Returns
    -------
    N_co : float
        Equilibrium amount of carbon monoxide; moles.
    N_co2 : float
        Equilibrium amount of carbon dioxide; moles.
    N_h2 : float
        Equilibrium amount of hydrogen; moles.
    N_h2o : float
        Equilibrium amount of water; moles.
    xi_3 : float
        Conversion factor of initial carbon dioxide to methanol.

    Notes
    -----
    This numerical solution for the amounts of reactants/products at equilibrium for the hydrogenation of carbon monoxide follows the method laid out in [1]_.

    References
    ----------
    .. [1] J. Terreni, A. Borgschulte, M. Hillestad, and B. Patterson, "Understanding Catalysis-A Simplified Simulation of Catalytic Reactors for CO:sub:`2` Reduction," ChemEngineering, vol. 4, 2020.
    """

    def _sn(N_co_0, N_co2_0, N_h2_0):
        """"Stoichiometric number" of the initial conditions.
        """

        return (N_h2_0 - N_co2_0)/(N_co_0 + N_co2_0)

    def _F(xi, SN, P, T):
        """Equilibrium equation to solve.
        """

        def _Q_2(xi, SN):
            """"Reaction quotient" of the reverse water gas shift reaction.
            """
            # xi[0] = xi_2
            # xi[1] = xi_3
            return xi[0] * (xi[0] + xi[1]) / ( (SN + 1 - xi[0] - 3*xi[1]) * (1 - xi[0] - xi[1]) )

        def _Q_3(xi, SN, P):
            """"Reaction quotient" of direct hydrogenation of carbon dioxide.
            """

            # xi[0] = xi_2
            # xi[1] = xi_3
            Po = 1.01325  # bars; reference pressure for reduced pressure
            return xi[1] * (xi[0] + xi[1]) * (SN + 2 - 2*xi[1])**2 * Po**2 / ( (SN + 1 - xi[0] - 3*xi[1])**3 * (1 - xi[0] - xi[1]) * P**2 )

        def _K_2(T):
            """Kinetic factor at equilibrium for the reverse water gas shift reaction.
            """
            return 1.07e2 * np.exp( -3.91e4 / (_constants.R * T) )

        def _K_3(T):
            """Kinetic factor at equilibrium for the direct hydrogenation of carbon dioxide.
            """
            return 2.56e-11 * np.exp( 5.87e4 / (_constants.R * T) )

        # return np.abs( np.log(K_2(T)) - np.log( Q_2(xi, SN) ) ) + np.abs( np.log(K_3(T)) - np.log( Q_3(xi, SN, P) ) )
        return [_K_2(T) - _Q_2(xi, SN), _K_3(T) - _Q_3(xi, SN, P)]

    SN = _sn(N_co_0, N_co2_0, N_h2_0)

    # solve for equilibrium conversion coefficients
    xi = optimize.fsolve(_F, [0.1, 0.1], args=(SN, P, T))  # initial values of 0.1 seems to work well for convergence

    # moles of reactants/products at equilibrium
    N_co = xi[0] * N_co2_0
    N_co2 = (1 - xi[0] - xi[1]) * N_co2_0
    N_h2 = (SN + 1 - xi[0] - 3*xi[1]) * N_co2_0
    N_h2o = (xi[0] + xi[1]) * N_co2_0
    N_ch3oh = xi[1] * N_co2_0

    xi_3 = xi[1]  # conversion of initial carbon dioxide to methanol

    return N_co, N_co2, N_h2, N_h2o, N_ch3oh, xi_3


def plug_flow(mass_co_in, mass_co2_in, mass_h2_in, P=60, T=270, rho_catalyst=1000, n_tubes=10000, d_tubes=0.02, L_tubes=3, outflow='mass', output=None):
    """
    Plug Flow Reactor (PFR) steady state flow simulation of hydrogenation of carbon dioxide to produce methanol with a Cu/ZnO/Al:sub:`2`O:sub:`3` catalyst.
    
    Parameters
    ----------
    mass_co_in : float
        Mass flow rate in of carbon monoxide; kilograms per second.
    mass_co2_in : float
        Mass flow rate in of carbon dioxide; kilograms per second.
    mass_h2_in : float
        Mass flow rate in of hydrogen gas; kilograms per second.
    P : float (optional)
        Pressure of the reactor; bars; default = 60 bars.
    T : float (optional)
        Temperature of the reactor; Celsius; between [180, 340]; default = 270.
    rho_catalyst : float (optional)
        Density of the catalyst Cu/ZnO/Al:sub:`2`O:sub:`3`; kilograms per cubic meter; default = 1000.
    n_tubes : float (optional)
        Number of tubes of the PFR; default = 10000.
    d_tubes : float (optional)
        Diameter of the PFR tubes; meters; default = 0.02.
    L_tubes : float (optional)
        Length of the tubes; meters; default = 3.
    outflow : string (optional)
        Flow output units; choose between 'mass', 'molar', or 'volume'; kg/s, mol/s, and L/s, respectively; default = 'mass'.
    output : string or None (optional)
        Output flag; if equal to 'total', the entire numerical solution is returned; default = None.

    Returns
    -------
    co_out : float or ndarray
        Carbon monoxide flow rate out; kg/s, mol/s, or L/s.
    co2_out : float or ndarray
        Carbon dioxide flow rate out; kg/s, mol/s, or L/s.
    h2_out : float or ndarray
        Hydrogen gas flow rate out; kg/s, mol/s, or L/s.
    h2o_out : float or ndarray
        Water flow rate out; kg/s, mol/s, or L/s.
    ch3oh_out : float or ndarray
        Methanol flow rate out; kg/s, mol/s, or L/s.
    conversion_factor : float
        Amount of initial carbon dioxide converted to methanol in the reactor.
    x : float or ndarray
        Axial flow coordinate.

    Notes
    -----
    For `output = 'volume'`, it is assumed the outflow temperature is cool enough for the water and methanol to condense.

    References
    ----------
    .. [1] J. Terreni, A. Borgschulte, M. Hillestad, and B. Patterson, "Understanding Catalysis-A Simplified Simulation of Catalytic Reactors for CO:sub:`2` Reduction," ChemEngineering, vol. 4, 2020.

    """

    def _kinetic_factors(a, b, T):
        """Kinetic factors in Arrhenius form.
        """
        return a * np.exp(b/(_constants.R*T))

    def _dN_dx(x, N_dot, rho_catalyst, A_tubes, k, P):
        """Differential equation to solve.
        """

        Po = 1.01325  # bars; reference pressure for reduced pressure

        p = N_dot / np.sum(N_dot) * P / Po  # partial reduced pressures; co, co2, h2, h2o, ch3oh

        # building the reaction rates array
        denom = (1 + k[6]*p[0] + k[7]*p[1]) * (p[2]**.5 + k[8]*p[3])

        r1 = k[3]*k[6]*(p[0]*p[2]**1.5 - p[4]/(p[2]**.5*k[0]))/denom
        r2 = k[4]*k[7]*(p[1]*p[2] - (p[3]*p[0])/k[1])/denom
        r3 = k[5]*k[7]*(p[1]*p[2]**1.5 - (p[4]*p[3])/(p[2]**1.5*k[2]))/denom

        R = np.array([-r1 + r2, -r2 - r3, -2*r1 - r2 - 3*r3, r2 + r3, r1 + r3])

        return rho_catalyst * A_tubes * R


    # Arrhenius Parameters; values in order: K1, K2, K3, k1, k2, k3, K_co, K_co2, K_h2o/K_h2**.5
    a = np.array([2.39e-13, 1.07e2, 2.56e-11, 4.89e7, 9.64e11, 1.09e5, 2.16e-5, 7.05e-7, 6.37e-9])
    b = np.array([9.84e4, -3.91e4, 5.87e4, -1.13e5, -1.53e5, -.875e5, .468e5, .617e5, .840e5])

    T += 273.15  # now in Kelvin
    A_tubes = n_tubes * np.pi * (d_tubes/2)**2  # tube area

    # initial molar flow rates
    N_dot_co_0 = mass_co_in / _constants.mol_weight_co  # mol/s
    N_dot_co2_0 = mass_co2_in / _constants.mol_weight_co2  # mol/s
    N_dot_h2_0 = mass_h2_in / _constants.mol_weight_h2  # mol/s

    # storing in an array
    N_dot_0 = np.array([N_dot_co_0, N_dot_co2_0, N_dot_h2_0, 0, 0])  # co, co2, h2, h2o, ch3oh

    # calculating kinetic factors
    k = _kinetic_factors(a, b, T)

    # solving numerically
    N_dot_sol = integrate.solve_ivp(_dN_dx, (0, L_tubes), N_dot_0, args=(rho_catalyst, A_tubes, k, P), vectorized=True)

    x = N_dot_sol.t  # axial coordinate

    # solved molar flows
    N_dot_co = N_dot_sol.y[0]  # mol/s; carbon monoxide
    N_dot_co2 = N_dot_sol.y[1]  # mol/s; carbon dioxide
    N_dot_h2 = N_dot_sol.y[2]  # mol/s; hydrogen
    N_dot_h2o = N_dot_sol.y[3]  # mol/s; water
    N_dot_ch3oh = N_dot_sol.y[4]  # mol/s; methanol

    conversion_factor = N_dot_ch3oh[-1] / N_dot_co2_0  # initial carbon dioxide to methanol conversion ratio

    if output != 'total':

        # just outputting the end values
        x = x[-1]
        N_dot_co = N_dot_co[-1]
        N_dot_co2 = N_dot_co2[-1]
        N_dot_h2 = N_dot_h2[-1]
        N_dot_h2o = N_dot_h2o[-1]
        N_dot_ch3oh = N_dot_ch3oh[-1]

    # determining output units
    if outflow == 'mass':

        co_out = N_dot_co * _constants.mol_weight_co  # kg/s
        co2_out = N_dot_co2 * _constants.mol_weight_co2  # kg/s
        h2_out = N_dot_h2 * _constants.mol_weight_h2  # kg/s
        h2o_out = N_dot_h2o * _constants.mol_weight_h2o  # kg/s
        ch3oh_out = N_dot_ch3oh * _constants.mol_weight_ch3oh  # kg/s

    elif outflow == 'volume':

        co_out = N_dot_co * _constants.R * 273.15 / 1e5 * 1e3  # L/s; flow at STP
        co2_out = N_dot_co2 * _constants.R * 273.15 / 1e5 * 1e3  # L/s; flow at STP
        h2_out = N_dot_h2 * _constants.R * 273.15 / 1e5 * 1e3  # L/s; flow at STP
        h2o_out = N_dot_h2o * _constants.mol_weight_h2o / _constants.rho_h2o * 1e3  # L/s; assuming the outflow is at a low enough temperature that the water has condensed
        ch3oh_out = N_dot_ch3oh * _constants.mol_weight_ch3oh / _constants.rho_ch3oh * 1e3  # L/s; assuming the outflow is at a low enough temperature that the methanol has condensed

    elif outflow == 'molar':

        co_out = N_dot_co  # mol/s
        co2_out = N_dot_co2  # mol/s
        h2_out = N_dot_h2  # mol/s
        h2o_out = N_dot_h2o  # mol/s
        ch3oh_out = N_dot_ch3oh  # mol/s

    return co_out, co2_out, h2_out, h2o_out, ch3oh_out, conversion_factor, x

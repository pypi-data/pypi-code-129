import pyseafuel
import pyseafuel._constants as _constants

# ──────────────────────────────────────────────────────────────────────────

# def seafuel(sea_water_carbon_dioxide_arm_flow, sea_water_hydrogen_arm_flow, water_ratio, stages, salt_removal, psu, sst, P, T, E0, K, r, A):
# def seafuel(seawater_volume_in_degasser, seawater_volume_in_desalinator, seawater_S, seawater_T, desal_water_ratio, desal_stages, desal_salt_removal, electro_E0, electro_K, electro_R, electro_A, reactor_P, reactor_T, reactor_outflow):
def seafuel(degasser, desalinator, electrolyzer, reactor):
    """

    Parameters
    ----------
    degasser : dict
        Degasser information; must contain the 'type' key. 'type' can equal on of the following: 'bipolar_membrane'.
        'bipolar_membrane' requires 'seawater_in' (seawater inflow) in L/s.
    desalintor : dict
        Desalinator information; must contain the 'type' key. 'type' can equal on of the following: 'electrodialysis'.
        'electrodialysis' requires 'seawater_in' (seawater inflow) in L/s, 'seawater_S' (seawater salinity) in PSU, 'seawater_T' (seawater temperature) in Kelvin, 'water_ratio' (volume ratio of fresh water out over seawater in) from (0, 1), 'salt_removal' (fraction of salt removed from the fresh water outflow) from (0, 1), and 'stages' (number of separation stages).
    electrolyzer : dict
        Electrolyzer information; must contain the 'type' key. 'type' can equal on of the following: 'Shen'.
        'Shen' requires 'E0' (reversible cell potential) in V, 'K' (Shen et al. model power coeffecient) in ohm:sup:`-1` cm:sup:`-2`, 'R' (internal cell resistance) in ohm:sup:`1` cm:sup:`2`, and 'area' (area of the membrane stack) in cm:sup:`2`.
    reactor : dict
        Reactor information; must contain the 'type' key. 'type' can equal on of the following: 'plug_flow_reactor'.
        'plug_flow' requires 'P' (operating pressure of the reactor) in bars and 'T' (operating temperature of the reactor) in Celsius.

    Returns
    -------
    flows : dict
        Dictionary of dictionaries containing the volumetric (L/s) and mass (kg/s) flows for the system.
    power : dict
        Power consumption for each component, and total consumption.
    misc : dict
        Remaining useful non-flow, non-power related information.

    Notes
    -----
    For the input dictionaries, the 'type' value is derived from the function names found in the component's respective submodule.

    The flow diagram for this system follows:

    .. image:: ../diagrams/seafuel.png

    Examples
    --------

    """

    # degasser
    if degasser['type'] == 'bipolar_membrane':
        mass_co2_out, power_degas = pyseafuel.degasser.bipolar_membrane(degasser['seawater_in'])
        # mass_co2_out; kg/s
        # power_degas; W

        # degasser results dictionary
        degasser_flows = {'seawater_in': degasser['seawater_in'], 'co2_out': mass_co2_out}


    # desalinator
    if desalinator['type'] == 'electrodialysis':
        volume_h2o_out, volume_brine_out, power_desal, concentration_brine = pyseafuel.desalinator.electrodialysis(desalinator['seawater_in'], desalinator['seawater_S'], desalinator['seawater_T'], desalinator['water_ratio'], desalinator['salt_removal'], desalinator['stages'], brine_concentration=True)
        # volume_h2o_out; L/s
        # volume_brine_out; L/s
        # power_desal; W
        # concentration_brine; mol/L

        # desalinator results dictionary
        desalinator_flows = {'seawater_in': desalinator['seawater_in'], 'h2o_out': volume_h2o_out, 'brine_out': volume_brine_out}
        desalinator_misc = {'brine_concentration': concentration_brine}


    # electrolyzer
    if electrolyzer['type'] == 'Shen':
        volume_h2o_in = volume_h2o_out
        mass_h2_out, mass_o2_out, power_electro = pyseafuel.electrolyzer.Shen(volume_h2o_in, electrolyzer['E0'], electrolyzer['K'], electrolyzer['R'], electrolyzer['area'])
        # mass_h2_out; kg/s
        # mass_o2_out; kg/s
        # power_electro; W

        # electrolyzer results dictionary
        electrolyzer_flows = {'h2o_in': volume_h2o_in, 'h2_out': mass_h2_out, 'o2_out': mass_o2_out}


    # reactor
    if reactor['type'] == 'plug_flow':
        mass_co2_in = mass_co2_out
        mass_h2_in = mass_h2_out
        volume_co_out, volume_co2_out, volume_h2_out, volume_h2o_out, volume_ch3oh_out, conversion_factor, _ = pyseafuel.reactor.plug_flow(0, mass_co2_in, mass_h2_in, P=reactor['P'], T=reactor['T'], outflow='volume')
        # volume_co_out; L/s
        # volume_co2_out; L/s
        # volume_h2_out; L/s
        # volume_h2o_out; L/s
        # volume_ch3oh_out; L/s
        # conversion_factor;

        # flow input ratio
        mol_h2_in = mass_h2_out / _constants.mol_weight_h2
        mol_co2_in = mass_co2_out / _constants.mol_weight_co2
        reactor_input_ratio = mol_h2_in / mol_co2_in
        
        # reactor results dictionary
        reactor_flows = {'co2_in': mass_co2_in, 'h2_in': mass_h2_in, 'co_out': volume_co_out, 'co2_out': volume_co2_out, 'h2_out': volume_h2_out, 'h2o_out': volume_h2o_out, 'ch3oh_out': volume_ch3oh_out}
        reactor_misc = {'input_ratio': reactor_input_ratio, 'conversion_factor': conversion_factor}


    # return dictionaries
    
    # flows
    flows = {'degasser': degasser_flows, 'desalinator': desalinator_flows, 'electrolyzer': electrolyzer_flows, 'reactor': reactor_flows}

    # power
    power_total = power_degas + power_desal + power_electro
    power = {'degasser': power_degas, 'desalinator': power_desal, 'electrolyzer': power_electro, 'total': power_total}

    # miscellaneous
    misc = {'desalinator': desalinator_misc, 'reactor': reactor_misc}

    return flows, power, misc

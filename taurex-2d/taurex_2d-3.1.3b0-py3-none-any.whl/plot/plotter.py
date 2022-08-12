import h5py
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np
import taurex.plot.corner as corner
import matplotlib as mpl
from taurex.constants import *
from taurex_2d.util.util import decode_string_array
from taurex_2d.util.util import terminatorIndex, slice2D
import os
from pathlib import Path
import warnings

# some global matplotlib vars
mpl.rcParams['axes.linewidth'] = 1  #set the value globally
mpl.rcParams['text.antialiased'] = True
mpl.rcParams['errorbar.capsize'] = 2

# rc('text', usetex=True) # use tex in plots
#rc('font', **{ 'family' : 'serif','serif':['Palatino'], 'size'   : 11})
def merge_ranges(ranges, other_ranges):
    new_range = []
    for idx in range(min(len(ranges),len(other_ranges))):
        new_range.append([min(other_ranges[idx][0], ranges[idx][0]), max(other_ranges[idx][1], ranges[idx][1])])
    for rest in range(idx+1, len(ranges)):
        new_range.append(ranges[rest])
    for rest in range(idx+1, len(other_ranges)):
        new_range.append(other_ranges[rest])
    return new_range

class Plotter(object):
    phi = 1.618

    modelAxis = {
        'TransmissionModel' : '$(R_p/R_*)^2$',
        'Transmission2DModel' : '$(R_p/R_*)^2$',
        'EmissionModel' : '$F_p/F_*$',
        'DirectImageModel' : '$F_p$'
    }

    def __init__(self,filename=None,model=None,title=None,prefix=None,cmap='Paired',out_folder='.',select_params=None,legend=None,save=False,r_factor=1):
        self.unit = 1e6
        self.nslices = None
        self.r_factor = r_factor
        if filename:
            self.fd = h5py.File(filename,'r')
            self.model = self.fd['ModelParameters']
            self.R = RJUP*np.float(self.model['Planet']['planet_radius'][...])/self.unit * self.r_factor
            self.nlayers = np.int(self.model['Pressure']['nlayers'][...])
            self.active_gases = self.activeGases
            if 'nslices' in self.model.keys():
                self.nslices = np.int(self.model['nslices'][...])
                self.beta_deg = np.float(self.model['beta'][...])
                self.beta  = np.radians(self.beta_deg)
            try:
                self.profiles = self.forward_output()['Profiles']
                self.z = self.profiles['altitude_profile'][...]/self.unit
                self.r = self.R + self.z
                self.temp_profile = self.profiles['temp_profile'][...]
                self.pressure_profile = self.profiles['pressure_profile'][...]
                self.mix_profile = self.profiles['active_mix_profile'][...]
            except:
                pass
        elif model:
            self.fd = None
            self.model = model
            self.R = RJUP*model.planet.radius/self.unit * self.r_factor
            self.nlayers = model.nLayers
            if '_nslices' in model.__dict__.keys():
                self.nslices = model.nslices
                self.beta_deg = model.beta
                self.beta = np.radians(model.beta)
            self.z = model.altitudeProfile/self.unit
            self.r = self.R + self.z
            self.temp_profile = model.temperatureProfile
            self.pressure_profile = model.pressureProfile
            self.mix_profile = model.chemistry.activeGasMixProfile
            self.active_gases = model.chemistry.activeGases
        else:
            raise Warning("No file nor model given.")
        self.title = title
        self.cmap = mpl.cm.get_cmap(cmap)
        self.prefix=prefix
        if self.prefix is None:
            self.prefix = "output"
        self.out_folder=out_folder
        self.save=save

        if not os.path.exists(self.out_folder):
            os.makedirs(self.out_folder)
        self.select_params=select_params
        self.legend=legend

    @property
    def num_solutions(self,fd_position='Output'):
        return len([(int(k[8:]),v) for k,v in self.fd[fd_position]['Solutions'].items() if 'solution' in k])

    def solution_iter(self,fd_position='Output'):
        for idx,solution in [(int(k[8:]),v) for k,v in self.fd[fd_position]['Solutions'].items() if 'solution' in k]:
            yield idx,solution

    def forward_output(self):
        return self.fd['Output']

    def compute_ranges(self):
        solution_ranges = []

        mu_derived = None
        for idx,sol in self.solution_iter():

            mu_derived = self.get_mu_parameters(sol)

            fitting_names = self.fittingNames

            fit_params = sol['fit_params']
            param_list = []
            for fit_names in self.fittingNames:
                param_values = fit_params[fit_names]
                sigma_m = param_values['sigma_m'][()]
                sigma_p = param_values['sigma_p'][()]
                val = param_values['value'][()]

                param_list.append([val,val- 5.0*sigma_m,val+5.0*sigma_p])

            if mu_derived is not None:
                sigma_m = mu_derived['sigma_m'][()]
                sigma_p = mu_derived['sigma_p'][()]
                val = mu_derived['value'][()]
                param_list.append([val, val- 5.0*sigma_m,val+5.0*sigma_p])

            solution_ranges.append(param_list)

        fitting_boundary_low = self.fittingBoundaryLow
        fitting_boundary_high = self.fittingBoundaryHigh

        if mu_derived is not None:
            fitting_boundary_low = np.concatenate((fitting_boundary_low, [-1e99]))
            fitting_boundary_high = np.concatenate((fitting_boundary_high, [1e99]))

        range_all = np.array(solution_ranges)

        range_min = np.min(range_all[:,:,1],axis=0)
        range_max = np.max(range_all[:,:,2],axis=0)

        range_min = np.where(range_min < fitting_boundary_low, fitting_boundary_low,range_min)
        range_max = np.where(range_max > fitting_boundary_high, fitting_boundary_high,range_max)

        return list(zip(range_min,range_max))

    @property
    def activeGases(self):
        return decode_string_array(self.fd['ModelParameters']['Chemistry']['active_gases'])

    @property
    def inactiveGases(self):
        return decode_string_array(self.fd['ModelParameters']['Chemistry']['inactive_gases'])


    @property
    def is2D(self):
        return "nslices" in self.fd['ModelParameters'].keys()

    def slice_path(self, slice_idx):
        if not self.is2D:
            return self.out_folder
        path = self.out_folder
        if slice_idx > 0:
            path = os.path.join(path, "terminator")
        elif slice_idx == -1:
            path = os.path.join(path, "day")
        elif slice_idx == 0 and len(self.slices) > 0:
            path = os.path.join(path, "night")
        Path(path).mkdir(parents=True, exist_ok=True)
        return path

    def plot_2Dmaps(self, **kwargs):
        if self.is_retrieval:
            for solution_idx, solution_val in self.solution_iter():
                self.profiles = solution_val['Profiles']
                self.z = self.profiles['altitude_profile'][...]/self.unit
                self.r = self.R + self.z
                self.temp_profile = self.profiles['temp_profile'][...]
                self.pressure_profile = self.profiles['pressure_profile'][...]
                self.mix_profile = self.profiles['active_mix_profile'][...]
                self.active_gases = (self.model['Chemistry']['active_gases'][...]).flatten()
                try:
                    self.beta_deg = solution_val["fit_params"]["beta"]["value"][...]
                except:
                    pass
                self.plot_2Dmap("%s"%solution_idx, **kwargs)
        else:
            self.plot_2Dmap(**kwargs)

    def plot_2Dmap(self, idx="", figsize=(4,3)):
        """Plot a 2D map of the rays, the pressure, the temperature, and the VMRs."""
        if self.nslices is None:
            return # HDF5 doesn't have angular coordinate information (nslices)
        min_z = 0
        if self.r_factor == 0:
            min_z = self.R
        min_a = np.degrees(np.arcsin(min_z/max(self.r)))
        try:
            plot_paths = True
            self.model['Path']['point_rad_0'] # fail if not exist
            fig, ax = plt.subplots(figsize=figsize)
            ax = plt.subplot(111, projection='polar')
            ## Plot paths going through layers
            for i in range(self.nlayers):
                radii = self.R+self.model['Path']['point_rad_%d'%i][...]/self.unit
                angles = self.model['Path']['point_ang_%d'%i][...]
                # angles -= 90
                rot_a = np.degrees(np.arcsin(min_z/radii))

                angles *= 90/(90-rot_a)
                angles = np.radians(angles+90)
                ax.plot(angles, radii, linewidth=.3, marker='.', markersize=.6, label=i)
        except KeyError:
            plot_paths = False

        alpha_space = np.linspace(90-self.beta_deg/2,90+self.beta_deg/2,self.nslices-1)

        def save2DPlot(profile="map", grid=False):
            """Subfunction (saving each 2D plot) so that we can use local variables."""
            ax.set_rmax(max(self.r))
            ax.set_rmin(min_z)

            # transform alpha to match "zoom"
            alpha_ticks = alpha_space[np.where(alpha_space>min_a)]
            alpha_ticks = alpha_ticks[np.where(alpha_ticks<180-min_a)]
            alpha_ticks -= 90
            alpha_ticks *= 90/(90-min_a)
            alpha_ticks += 90
            ax.set_thetagrids(alpha_ticks)
            ax.set_rgrids(self.r, angle=-90, fmt="%.1f")

            plt.rc('ytick', labelsize=5)
            ax.grid(True, linewidth=.1)
            if not grid:
                ax.set_thetagrids([90-self.beta_deg/2,90,90+self.beta_deg/2])
                ax.set_xticklabels(['',r'$\beta= %g^\circ$'%(self.beta_deg),''])
                ax.set_rgrids([self.r[1],self.r[-1]])
                ax.set_yticklabels([0, f'{self.z[-1]:.0f}\nMm'])
            else:
                ax.set_yticklabels([])
                ax.set_xticklabels([])
            ax.set_thetamax(180)
            if self.save:
                fig.savefig(os.path.join(self.out_folder, f'{self.prefix}_{profile}{idx}.pdf'),bbox_inches='tight',dpi=140)
                plt.close("all") #comment for interactive use
            else:
                ax.set_title(profile)
                plt.show()

        if plot_paths:
            save2DPlot("paths", grid=True)

        def plotPolar(profile, color="GnBu", norm=colors.LogNorm, vmin=None, vmax=None, p_levels=None):
            """2D map of the pressure, the temperature, and the VMRs (:attr:`profile` being the property to plot)."""
            alpha_night = np.linspace(0,90-self.beta_deg/2,50)
            alpha_day = np.linspace(90+self.beta_deg/2,180,50)
            shape = alpha_day.shape+(profile.shape[1],)
            profile_day = np.zeros(shape)
            profile_night = np.zeros(shape)

            # profile = profile.copy()
            # if profile[0].min() > profile[-1].min():
            #     profile = profile[::-1] # put hottest side on the left

            profile_day[:] = profile[-1,:]
            profile_night[:] = profile[0,:]
            profile = np.concatenate((profile_night, profile[1:-1], profile_day))
            alpha_ticks = np.concatenate((alpha_night, alpha_space, alpha_day))
            X,Y = np.meshgrid(np.deg2rad(alpha_ticks),self.r)
            if p_levels is not None:
                zp = self.pressure_profile
                # zp = self.pressure_profile.copy()[::-1]
                zp_day = np.zeros(shape)
                zp_night = np.zeros(shape)
                zp_day[:] = zp[-1,:]
                zp_night[:] = zp[0,:]
                zp = np.concatenate((zp_night, zp[1:-1], zp_day))
                alpha_middles = np.deg2rad(alpha_ticks)[:-1] + np.diff(np.deg2rad(alpha_ticks))/2
                x,y = np.meshgrid(alpha_middles, self.r[:-1]+np.diff(self.r)/2)
                ax.contour(x,y,zp.T, colors="black", linewidths=.2,
                locator=mpl.ticker.FixedLocator(p_levels),
                )

            if vmin is None:
                vmin = profile.min()
            else:
                vmin = max(vmin, profile.min())
            if vmax is None:
                vmax = profile.max()
            else:
                vmax = min(vmax, profile.max())

            # vmin=650
            # vmax=3000

            c = ax.pcolormesh(X, Y, profile.T,
                    cmap=color, vmin=vmin, vmax=vmax)
            cbar = plt.colorbar(c, ax=ax, extend='both')
            cbar.ax.tick_params(labelsize=8)
            plt.tight_layout()

        fig, ax = plt.subplots(figsize=figsize)
        ax = plt.subplot(111, projection='polar')
        plotPolar(self.temp_profile, "hot", norm=colors.Normalize, p_levels=[1e-4, 1, 100, 10**4])
        ax.set_title("Temperature (K)")
        save2DPlot("temp")

        # fig, ax = plt.subplots(figsize=figsize)
        # ax = plt.subplot(111, projection='polar')
        # plotPolar(self.pressure_profile, "GnBu", vmin=1e-6)
        # ax.set_title("Pressure (Pa)")
        # save2DPlot("pressure")

        for idx, gas in enumerate(self.active_gases):
            fig, ax = plt.subplots(figsize=figsize)
            ax = plt.subplot(111, projection='polar')
            plotPolar(self.mix_profile[idx], "GnBu", vmin=1e-8, p_levels=[1e-4, 1, 100, 10**4])
            try:
                save2DPlot("mix_"+gas)
            except:
                save2DPlot("mix_"+gas.decode('ascii'))

    def plot_fit_xprofile(self):
        for solution_idx, solution_val in self.solution_iter():
            slice_idx = self.slice_idx

            fig = plt.figure(figsize=(7,7/self.phi))
            ax = fig.add_subplot(111)
            num_moles = len(self.activeGases+self.inactiveGases)

            profiles = solution_val['Profiles']
            pressure_profile = profiles['pressure_profile'][:]/1e5
            active_profile = profiles['active_mix_profile'][...]
            active_profile_std = profiles['active_mix_profile_std'][...]

            inactive_profile = profiles['inactive_mix_profile'][...]
            inactive_profile_std = profiles['inactive_mix_profile_std'][...]

            if slice_idx == 1:
                slice_idx = terminatorIndex(pressure_profile)
            pressure_profile = slice2D(pressure_profile, slice_idx)

            cols_mol = {}
            for mol_idx,mol_name in enumerate(self.activeGases):
                cols_mol[mol_name] = self.cmap(mol_idx/num_moles)

                prof = active_profile[mol_idx]
                prof_std = active_profile_std[mol_idx]

                prof = slice2D(prof, slice_idx)
                prof_std = slice2D(prof_std, slice_idx)

                plt.plot(prof,pressure_profile,color=cols_mol[mol_name], label=mol_name)

                plt.fill_betweenx(pressure_profile, prof + prof_std, prof,
                                color=self.cmap(mol_idx / num_moles), alpha=0.5)
                plt.fill_betweenx(pressure_profile, prof,
                                np.power(10, (np.log10(prof) - (
                                            np.log10(prof + prof_std) - np.log10(prof)))),
                                color=self.cmap(mol_idx / num_moles), alpha=0.5)

            for mol_idx,mol_name in enumerate(self.inactiveGases):
                inactive_idx = len(self.activeGases) + mol_idx
                cols_mol[mol_name] = self.cmap(inactive_idx/num_moles)


                prof = inactive_profile[mol_idx]
                prof_std = inactive_profile_std[mol_idx]

                prof = slice2D(prof, slice_idx)
                prof_std = slice2D(prof_std, slice_idx)

                plt.plot(prof,pressure_profile,color=cols_mol[mol_name], label=mol_name)

                plt.fill_betweenx(pressure_profile, prof + prof_std, prof,
                                color=self.cmap(inactive_idx / num_moles), alpha=0.5)
                plt.fill_betweenx(pressure_profile, prof,
                                np.power(10, (np.log10(prof) - (
                                            np.log10(prof + prof_std) - np.log10(prof)))),
                                color=self.cmap(inactive_idx / num_moles), alpha=0.5)

        plt.yscale('log')
        plt.gca().invert_yaxis()
        plt.xscale('log')
        plt.xlim(1e-12, 3)
        plt.xlabel('Mixing ratio')
        plt.ylabel('Pressure (bar)')
        plt.tight_layout()
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1, prop={'size':11}, frameon=False)
        if self.title:
            plt.title(self.title, fontsize=14)
        if self.save:
            plt.savefig(os.path.join(self.slice_path(self.slice_idx), '%s_fit_mixratio.pdf' % (self.prefix)))
            plt.close('all')

    def plot_forward_xprofile(self):
        slice_idx = self.slice_idx
        fig = plt.figure(figsize=(7,7/self.phi))
        ax = fig.add_subplot(111)
        num_moles = len(self.activeGases+self.inactiveGases)

        solution_val = self.forward_output()

        profiles = solution_val['Profiles']
        pressure_profile = profiles['pressure_profile'][:]/1e5
        if slice_idx == 1:
            slice_idx = terminatorIndex(pressure_profile)
        pressure_profile = slice2D(pressure_profile, slice_idx)
        active_profile = profiles['active_mix_profile'][...]

        inactive_profile = profiles['inactive_mix_profile'][...]

        cols_mol = {}
        for mol_idx,mol_name in enumerate(self.activeGases):
            cols_mol[mol_name] = self.cmap(mol_idx/num_moles)

            prof = active_profile[mol_idx]
            prof = slice2D(prof, slice_idx)

            plt.plot(prof,pressure_profile,color=cols_mol[mol_name], label=mol_name)

        for mol_idx,mol_name in enumerate(self.inactiveGases):
            inactive_idx = len(self.activeGases) + mol_idx
            cols_mol[mol_name] = self.cmap(inactive_idx/num_moles)

            prof = inactive_profile[mol_idx]
            prof = slice2D(prof, slice_idx)

            plt.plot(prof,pressure_profile,color=cols_mol[mol_name], label=mol_name)

        plt.yscale('log')
        plt.gca().invert_yaxis()
        plt.xscale('log')
        plt.xlim(1e-12, 3)
        plt.xlabel('Mixing ratio')
        plt.ylabel('Pressure (bar)')
        plt.tight_layout()
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
        ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1, prop={'size':11}, frameon=False)
        if self.title:
            plt.title(self.title, fontsize=14)
        if self.save:
            plt.savefig(os.path.join(self.slice_path(self.slice_idx), '%s_fit_mixratio.pdf' % (self.prefix)))
        plt.close('all')

    def plot_fitted_tp(self):
        # fitted model
        fig = plt.figure(figsize=(5,3.5))
        ax = fig.add_subplot(111)

        for solution_idx, solution_val in self.solution_iter():
            slice_idx = self.slice_idx
            if self.num_solutions > 1:
                label = 'Fitted profile (%i)' % (solution_idx)
            else:
                label = 'Fitted profile'
            temp_prof = solution_val['Profiles']['temp_profile'][:]
            temp_prof_std = solution_val['Profiles']['temp_profile_std'][:]
            pres_prof = solution_val['Profiles']['pressure_profile'][:]/1e5

            if slice_idx == 1:
                slice_idx = terminatorIndex(pres_prof)
            pres_prof = slice2D(pres_prof, slice_idx)
            temp_prof = slice2D(temp_prof, slice_idx)

            temp_prof_std = slice2D(temp_prof_std, slice_idx)
            plt.plot(temp_prof, pres_prof, color=self.cmap(float(solution_idx)/self.num_solutions), label=label)
            plt.fill_betweenx(pres_prof,  temp_prof-temp_prof_std,  temp_prof+temp_prof_std, color=self.cmap(float(solution_idx)/self.num_solutions), alpha=0.5)

        plt.yscale('log')
        plt.gca().invert_yaxis()
        plt.xlabel('Temperature (K)')
        plt.ylabel('Pressure (bar)')
        plt.tight_layout()
        legend = plt.legend(loc='upper left', ncol=1, prop={'size':11})
        legend.get_frame().set_facecolor('white')
        legend.get_frame().set_edgecolor('white')

        legend.get_frame().set_alpha(0.8)
        if self.title:
            plt.title(self.title, fontsize=14)
        if self.save:
            plt.savefig(os.path.join(self.slice_path(self.slice_idx), '%s_tp_profile.pdf' % (self.prefix)))
        plt.close()

    def plot_forward_tp(self):
        fig = plt.figure(figsize=(5,3.5))
        ax = fig.add_subplot(111)

        solution_val = self.forward_output()

        temp_prof = solution_val['Profiles']['temp_profile'][:]
        pres_prof = solution_val['Profiles']['pressure_profile'][:]/1e5

        slice_idx = self.slice_idx
        if slice_idx == 1:
            slice_idx = terminatorIndex(pres_prof)
        pres_prof = slice2D(pres_prof, slice_idx)
        temp_prof = slice2D(temp_prof, slice_idx)

        plt.plot(temp_prof, pres_prof)

        plt.yscale('log')
        plt.ylim(1e-6)
        plt.gca().invert_yaxis()
        plt.xlabel('Temperature (K)')
        plt.ylabel('Pressure (bar)')
        plt.tight_layout()
        legend = plt.legend(loc='upper left', ncol=1, prop={'size':11})
        legend.get_frame().set_facecolor('white')
        legend.get_frame().set_edgecolor('white')

        legend.get_frame().set_alpha(0.8)
        if self.title:
            plt.title(self.title, fontsize=14)
        if self.save:
            plt.savefig(os.path.join(self.slice_path(self.slice_idx), '%s_tp_profile.pdf' % (self.prefix)))
        plt.close()

    def get_mu_parameters(self, solution):
        if 'mu_derived' not in solution['fit_params'].keys():
            return None
        else:
            return solution['fit_params']['mu_derived']


    def plotting_posteriors(self, figs=[], ranges=None, M=0, nModel=1):
        ''' Plotting posteriors of model M'''
        if not self.is_retrieval:
            raise Exception('HDF5 was not generated from retrieval, no posteriors found')

        for solution_idx, solution_val in self.solution_iter():
            mu_derived = self.get_mu_parameters(solution_val)

            tracedata = solution_val['tracedata']
            weights = solution_val['weights']

            figure_past = None

            if solution_idx > 0 or M>0:
                figure_past = figs[solution_idx + M*self.num_solutions - 1]

            latex_names = self.fittingLatex

            if mu_derived is not None:
                latex_names.append('$\mu$ (derived)')
                tracedata = np.column_stack((tracedata, mu_derived['trace']))

            if self.select_params is not None:
                res = []
                if mu_derived is not None:
                    res = [-1]
                for p in self.select_params:
                    res += [i for i, x in enumerate(self.fittingNames) if p in x]
                tracedata = tracedata[:,res]
                latex_names = [latex_names[i] for i in res]
                ranges = [ranges[i] for i in res]

            color_idx = np.float(solution_idx + M*self.num_solutions)/(self.num_solutions*nModel)

            # print('color: {}'.format(color_idx))
            ### https://matplotlib.org/users/customizing.html
            plt.rc('xtick', labelsize=10) #size of individual labels
            plt.rc('ytick', labelsize=10)
            plt.rc('axes.formatter', limits=( -4, 5 )) #scientific notation..

            fig =  corner.corner(tracedata,
                                    weights=weights,
                                    labels=latex_names,
                                    label_kwargs=dict(fontsize=20),
                                    smooth=True,
                                    scale_hist=True,
                                    quantiles=[0.16, 0.5, 0.84],
                                    show_titles=True,
                                    title_kwargs=dict(fontsize=12),
                                    range=ranges,
                                    #quantiles=[0.16, 0.5],
                                    ret=True,
                                    fill_contours=True,
                                    color=self.cmap(float(color_idx)),
                                    top_ticks=False,
                                    bins=30,
                                    fig = figure_past)
            if self.title:
                fig.gca().annotate(self.title, xy=(0.5, 1.0), xycoords="figure fraction",
                    xytext=(0, -5), textcoords="offset points",
                    ha="center", va="top", fontsize=14)

            figs.append(fig)
        return ranges

    def plot_posteriors(self):
        figs = []
        ranges = self.compute_ranges()
        self.plotting_posteriors(figs, ranges)
        if self.save:
            plt.savefig(os.path.join(self.out_folder, '%s_posteriors.pdf' % (self.prefix)))
        self.posterior_figure_handles = figs
        self.posterior_figure_ranges  = ranges
        plt.close()

    @property
    def modelType(self):
        try:
            return self.fd['ModelParameters']['model_type'][()].decode('ascii')
        except:
            return self.fd['ModelParameters']['model_type'][()]

    def count_contributions(self,spectra):
        pass


    def plotting_fitted_spectrum(self, resolution=None, M=-1):
        ''' Plotting fitted spectrum of model M'''
        obs_spectrum = self.fd['Observed']['spectrum'][...]
        error = self.fd['Observed']['errorbars'][...]
        wlgrid = self.fd['Observed']['wlgrid'][...]
        bin_widths = self.fd['Observed']['binwidths'][...]

        if M>=0:
            obs_label = 'Observed %i'%M
        else:
            obs_label = 'Observed'

        plt.errorbar(wlgrid,obs_spectrum, error, lw=1, color='black', alpha=0.4, ls='none', zorder=0, label=obs_label)

        N = self.num_solutions
        for solution_idx, solution_val in self.solution_iter():
            if N > 1 or M >= 0:
                label = 'Fitted model %i (sol %i)' % (M, solution_idx)
            else:
                label = 'Fitted model'

            try:
                binned_grid = solution_val['Spectra']['binned_wlgrid'][...]
            except KeyError:
                binned_grid = solution_val['Spectra']['bin_wlgrid'][...]

            native_grid = solution_val['Spectra']['native_wngrid'][...]


            plt.scatter(wlgrid, obs_spectrum, marker='d',zorder=1,**{'s': 10, 'edgecolors': 'grey','c' : self.cmap(float(solution_idx)/N) })

            self._generic_plot(binned_grid,native_grid,solution_val['Spectra'],resolution=resolution,color=self.cmap(float(solution_idx)/N),label=label)


        plt.xlim(np.min(wlgrid)-0.05*np.min(wlgrid), np.max(wlgrid)+0.05*np.max(wlgrid))
        # plt.ylim(0.0,0.006)
        plt.xlabel(r'Wavelength ($\mu$m)')
        plt.ylabel(self.modelAxis[self.modelType])

        if np.max(wlgrid) - np.min(wlgrid) > 5:
            plt.xscale('log')
            plt.tick_params(axis='x', which='minor')
            #ax.xaxis.set_minor_formatter(mpl.ticker.FormatStrFormatter("%i"))
            #ax.xaxis.set_major_formatter(mpl.ticker.FormatStrFormatter("%i"))
        plt.legend(loc='best', ncol=2, frameon=False, prop={'size':11})
        if self.title:
            plt.title(self.title, fontsize=14)
        plt.tight_layout()

    def plot_fitted_spectrum(self, resolution=None):
        fig = plt.figure(figsize=(10.6, 7.0))
        self.plotting_fitted_spectrum(resolution)
        if self.save:
            plt.savefig(os.path.join(self.out_folder, '%s_spectrum.pdf'  % (self.prefix)))
        plt.close()

    def plot_forward_spectrum(self,resolution=None):
        fig = plt.figure(figsize=(5.3, 3.5))

        spectra_out = self.forward_output()['Spectra']

        native_grid = spectra_out['native_wngrid'][...]

        try:
            wlgrid = spectra_out['binned_wlgrid'][...]
        except KeyError:
            wlgrid = spectra_out['native_wlgrid'][...]


        self._generic_plot(wlgrid,native_grid,spectra_out,resolution=resolution,alpha=1)
        plt.xlim(np.min(wlgrid)-0.05*np.min(wlgrid), np.max(wlgrid)+0.05*np.max(wlgrid))
        # plt.ylim(0.0,0.006)
        plt.xlabel(r'Wavelength ($\mu$m)')
        plt.ylabel(self.modelAxis[self.modelType])

        if np.max(wlgrid) - np.min(wlgrid) > 5:
            plt.xscale('log')
            plt.tick_params(axis='x', which='minor')
            #ax.xaxis.set_minor_formatter(mpl.ticker.FormatStrFormatter("%i"))
            #ax.xaxis.set_major_formatter(mpl.ticker.FormatStrFormatter("%i"))
        plt.legend(loc='best', ncol=2, frameon=False, prop={'size':11})
        if self.title:
            plt.title(self.title, fontsize=14)
        plt.tight_layout()
        if self.save:
            plt.savefig(os.path.join(self.out_folder, '%s_forward_spectrum.pdf'  % (self.prefix)))
        plt.close()

    def plot_fitted_contrib(self,full=False,resolution=None):
        # fitted model

        N = self.num_solutions
        for solution_idx, solution_val in self.solution_iter():

            fig=plt.figure(figsize=(5.3*2, 3.5*2))
            ax = fig.add_subplot(111)



            obs_spectrum = self.fd['Observed']['spectrum'][:]
            error = self.fd['Observed']['errorbars'][...]
            wlgrid = self.fd['Observed']['wlgrid'][...]
            plot_wlgrid = wlgrid
            bin_widths = self.fd['Observed']['binwidths'][...]

            plt.errorbar(wlgrid,obs_spectrum, error, lw=1, color='black', alpha=0.4, ls='none', zorder=0, label='Observed')
            self._plot_contrib(solution_val,wlgrid,ax,full=full,resolution=resolution)


            #plt.tight_layout()
            if self.save:
                plt.savefig(os.path.join(self.out_folder, '%s_spectrum_contrib_sol%i.pdf'  % (self.prefix,solution_idx)))
            plt.close()

        plt.close('all')

    def plot_forward_contrib(self,full=False,resolution=None):
        fig=plt.figure(figsize=(5.3*2, 3.5*2))
        ax = fig.add_subplot(111)


        spectra_out = self.forward_output()['Spectra']

        native_grid = spectra_out['native_wngrid'][...]

        try:
            wlgrid = spectra_out['binned_wlgrid'][...]
        except KeyError:
            wlgrid = spectra_out['native_wlgrid'][...]

        self._generic_plot(wlgrid,native_grid,spectra_out,resolution=resolution,alpha=0.5)
        self._plot_contrib(self.forward_output(),wlgrid,ax,full=full,resolution=resolution)


        #plt.tight_layout()
        if self.save:
            plt.savefig(os.path.join(self.out_folder, '%s_spectrum_contrib_forward.pdf'  % (self.prefix)))
        plt.close()


    def _plot_contrib(self,output,wlgrid,ax,full=False,resolution=None):


        if full:
            wlgrid = self.full_contrib_plot(output['Spectra'],wlgrid,resolution=resolution)
        else:
            wlgrid = self.simple_contrib_plot(output['Spectra'],wlgrid,resolution=resolution)

        plt.xlim(np.min(wlgrid)-0.05*np.min(wlgrid), np.max(wlgrid)+0.05*np.max(wlgrid))
        # plt.ylim(0.0,0.006)
        plt.xlabel('Wavelength ($\mu$m)')
        plt.ylabel(self.modelAxis[self.modelType])

        if np.max(wlgrid) - np.min(wlgrid) > 5:
            plt.xscale('log')
            plt.tick_params(axis='x', which='minor')
            #ax.xaxis.set_minor_formatter(mpl.ticker.FormatStrFormatter("%i"))
            #ax.xaxis.set_major_formatter(mpl.ticker.FormatStrFormatter("%i"))
        #plt.legend(loc='best', ncol=2, frameon=False, prop={'size':11})
        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.1,
                        box.width, box.height * 0.9])
        # Put a legend below current axis
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08),
                fancybox=True, shadow=True, ncol=5)
        if self.title:
            plt.title(self.title, fontsize=14)

    def full_contrib_plot(self,spectra,wlgrid,resolution=None):
        native_grid = spectra['native_wngrid'][...]
        for contrib_name,contrib_dict in spectra['Contributions'].items():

            first_name = contrib_name

            for component_name,component_value in contrib_dict.items():
                if isinstance(component_value,h5py.Dataset):
                        continue
                total_label = '{}-{}'.format(contrib_name,component_name)
                self._generic_plot(wlgrid,native_grid,component_value,resolution,label=total_label)
        return wlgrid
    def simple_contrib_plot(self,spectra,wlgrid,resolution=None):


        binner = None
        native_grid = spectra['native_wngrid'][...]


        for contrib_name,contrib_dict in spectra['Contributions'].items():
            first_name = contrib_name
            if first_name == 'Absorption':
                for component_name,component_value in contrib_dict.items():
                    if isinstance(component_value,h5py.Dataset):
                        continue
                    total_label = '{}-{}'.format(contrib_name,component_name)
                    self._generic_plot(wlgrid,native_grid,component_value,resolution,label=total_label)
            else:
                self._generic_plot(wlgrid,native_grid,contrib_dict,resolution)

        return wlgrid


    def _generic_plot(self,wlgrid,native_grid,spectra,resolution,color=None,error=False,alpha=1.0,label=None):


        binned_error = None
        if resolution is not None:
            from taurex.binning import FluxBinner
            from taurex.util.util import create_grid_res,wnwidth_to_wlwidth
            _grid = create_grid_res(resolution,wlgrid.min()*0.9,wlgrid.max()*1.1)
            bin_wlgrid = _grid[:,0]

            bin_wngrid = 10000/_grid[:,0]

            bin_sort = bin_wngrid.argsort()

            bin_wlgrid = bin_wlgrid[bin_sort]
            bin_wngrid = bin_wngrid[bin_sort]

            bin_wnwidth = wnwidth_to_wlwidth(bin_wlgrid,_grid[bin_sort,1])
            wlgrid = _grid[bin_sort,0]
            binner = FluxBinner(bin_wngrid,bin_wnwidth)
            native_spectra = spectra['native_spectrum'][...]
            binned_spectrum = binner.bindown(native_grid,native_spectra)[1]
            try:
                native_error = spectra['native_std']
            except KeyError:
                native_error = None
            if native_error is not None:
                binned_error = binner.bindown(native_grid,native_error)[1]

        else:
            try:
                binned_spectrum = spectra['binned_spectrum'][...]
            except KeyError:
                try:
                    binned_spectrum = spectra['bin_spectrum'][...]
                except KeyError:
                    binned_spectrum = spectra['native_spectrum'][...]
            try:
                binned_error = spectra['binned_std'][...]
            except KeyError:
                binned_error = None
        plt.plot(wlgrid, binned_spectrum, label=label,alpha=alpha)
        if binned_error is not None:
            plt.fill_between(wlgrid, binned_spectrum-binned_error,
                                binned_spectrum+binned_error,
                                alpha=0.5, zorder=-2, color=color, edgecolor='none')

            # 2 sigma
            plt.fill_between(wlgrid, binned_spectrum-2*binned_error,
                                binned_spectrum+2*binned_error,
                                alpha=0.2, zorder=-3, color=color, edgecolor='none')


    def plot_forward_tau(self):

        forward_output =self.forward_output()

        contribution = forward_output['Spectra']['native_tau'][...]
        #contribution = self.pickle_file['solutions'][solution_idx]['contrib_func']

        pressure = forward_output['Profiles']['pressure_profile'][:]
        wavelength = forward_output['Spectra']['native_wlgrid'][:]

        self._plot_tau(contribution,pressure,wavelength)

        if self.save:
            plt.savefig(os.path.join(self.slice_path(self.slice_idx), '%s_tau_forward.pdf' % (self.prefix)))

        plt.close()


    def plot_fitted_tau(self):
        N = self.num_solutions
        for solution_idx, solution_val in self.solution_iter():

            contribution = solution_val['Spectra']['native_tau'][...]
            #contribution = self.pickle_file['solutions'][solution_idx]['contrib_func']

            pressure = solution_val['Profiles']['pressure_profile'][:]
            wavelength = solution_val['Spectra']['native_wlgrid'][:]

            self._plot_tau(contribution,pressure,wavelength)

            if self.save:
                plt.savefig(os.path.join(self.slice_path(self.slice_idx), '%s_tau_sol%i.pdf' % (self.prefix,solution_idx)))

            plt.close()

    def _plot_tau(self,contribution,pressure,wavelength):
        slice_idx = self.slice_idx
        if slice_idx == 1:
            slice_idx = terminatorIndex(pressure)
        pressure = slice2D(pressure, slice_idx) # take slice at terminator as reference
        grid = plt.GridSpec(1, 4, wspace=0.4, hspace=0.3)
        fig = plt.figure('Contribution function')
        ax1 = plt.subplot(grid[0, :3])
        plt.imshow(contribution, aspect='auto')

        ### mapping of the pressure array onto the ticks:
        y_labels = np.array([pow(10, 6), pow(10, 4), pow(10, 2), pow(10, 0), pow(10, -2), pow(10, -4)])
        y_ticks = np.zeros(len(y_labels))
        for i in range(len(y_ticks)):
            y_ticks[i] = (np.abs(pressure - y_labels[i])).argmin()  ## To find the corresponding index
        plt.yticks(y_ticks, ['$10^{%.f}$' % y for y in np.log10(y_labels) - 5])

        ### mapping of the wavelength array onto the ticks:
        x_label0 = np.ceil(np.min(wavelength) * 10) / 10.
        x_label5 = np.round(np.max(wavelength) * 10) / 10.
        x_label1 = np.round(
            pow(10, (np.log10(x_label5) - np.log10(x_label0)) * 1 / 5. + np.log10(x_label0)) * 10) / 10.0
        x_label2 = np.round(
            pow(10, (np.log10(x_label5) - np.log10(x_label0)) * 2 / 5. + np.log10(x_label0)) * 10) / 10.0
        x_label3 = np.round(
            pow(10, (np.log10(x_label5) - np.log10(x_label0)) * 3 / 5. + np.log10(x_label0)) * 10) / 10.
        x_label4 = np.round(
            pow(10, (np.log10(x_label5) - np.log10(x_label0)) * 4 / 5. + np.log10(x_label0)) * 10) / 10.

        x_labels = np.array([x_label0, x_label1, x_label2, x_label3, x_label4, x_label5])
        x_ticks = np.zeros(len(x_labels))
        for i in range(len(x_ticks)):
            x_ticks[i] = (np.abs(wavelength - x_labels[i])).argmin()  ## To find the corresponding index
        plt.xticks(x_ticks, x_labels)
        plt.gca().invert_yaxis()
        plt.gca().invert_xaxis()
        plt.xlabel("Wavelength ($\mu m$)")
        plt.ylabel("Pressure (Bar)")

        ax2 = plt.subplot(grid[0, 3])

        contribution_collapsed = np.average(contribution, axis=1)
        # contribution_collapsed = np.amax(contribution_hr, axis=1) ## good for emission
        contribution_sum = np.zeros(len(contribution_collapsed))
        for i in range(len(contribution_collapsed) - 1):
            contribution_sum[i + 1] = contribution_sum[i] + contribution_collapsed[i + 1]

        plt.plot(contribution_collapsed, pressure * pow(10, -5))

        plt.yscale('log')
        plt.gca().invert_yaxis()
        plt.gca().yaxis.tick_right()
        plt.xlabel("Contribution")


    @property
    def fittingNames(self):
        from taurex.util.util import decode_string_array
        if not self.is_retrieval:
            raise Exception('HDF5 was not generated from retrieval, no fitting names found')
        return decode_string_array(self.fd['Optimizer']['fit_parameter_names'])

    @property
    def fittingLatex(self):
        from taurex.util.util import decode_string_array
        if not self.is_retrieval:
            raise Exception('HDF5 was not generated from retrieval, no fitting latex found')
        return decode_string_array(self.fd['Optimizer']['fit_parameter_latex'])

    @property
    def fittingBoundaryLow(self):
        if not self.is_retrieval:
            raise Exception('HDF5 was not generated from retrieval, no fitting boundary found')
        return self.fd['Optimizer']['fit_boundary_low'][:]

    @property
    def fittingBoundaryHigh(self):
        if not self.is_retrieval:
            raise Exception('HDF5 was not generated from retrieval, no fitting boundary found')
        return self.fd['Optimizer']['fit_boundary_high'][:]


    @property
    def is_retrieval(self):
        try:
            if self.fd:
                self.fd['Output']
                self.fd['Optimizer']
                self.fd['Output']['Solutions']
                return True
        except KeyError:
            return False
        return False

    @property
    def is_lightcurve(self):
        try:
            self.fd['Lightcurve']
            return True
        except KeyError:
            return False

class Comparison:
    def __init__(self, plots=None,title=None,prefix=None,cmap='Paired',out_folder='.'):
        self.plots = np.array([x for x in plots if x is not None])
        if len(self.plots) <= 1:
            warnings.warn("No plots to compare ("+str(len(plots))+")")
        self.title = title
        self.cmap = mpl.cm.get_cmap(cmap)
        self.prefix=prefix
        if self.prefix is None:
            self.prefix = "output"
        self.out_folder=out_folder

        if not os.path.exists(self.out_folder):
            os.makedirs(self.out_folder)


    def plot_fitted_spectrum(self, resolution=None):
        fig = plt.figure(figsize=(10.6, 7.0))
        for idx, plot in enumerate(self.plots):
            plot.plotting_fitted_spectrum(resolution, idx)
        plt.savefig(os.path.join(self.out_folder, '%s_spectrum.pdf'  % (self.prefix)))
        plt.close()

    def plot_posteriors(self, resolution=None):
        fig = plt.figure(figsize=(10.6, 7.0))
        figs = []
        old_ranges = None
        for idx, plot in enumerate(self.plots):
            ranges = plot.compute_ranges()
            if old_ranges:
                ranges = merge_ranges(ranges, old_ranges)
            old_ranges = ranges
            print("Parameters of %s: %s"%(plot.legend, plot.fittingNames))
        for idx, plot in enumerate(self.plots):
            try:
                plot.plotting_posteriors(figs, ranges, idx, len(self.plots))
            except ValueError as e:
                raise ValueError("%s. You may want to try to select parameters to plot with the '-f' option, compatible with other plots (checkout above output), among: %s" %(e, plot.fittingNames))
        plt.savefig(os.path.join(self.out_folder, '%s_posteriors.pdf' % (self.prefix)))
        self.posterior_figure_handles = figs
        self.posterior_figure_ranges  = ranges
        plt.close()

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Taurex-Plotter')
    parser.add_argument("-i", "--input",dest='input_files',nargs='+',type=str,required=True,help="Input hdf5 file from taurex")
    parser.add_argument("-P","--plot-posteriors",dest="posterior",default=False,help="Plot fitting posteriors",action='store_true')
    parser.add_argument("-x","--plot-xprofile",dest="xprofile",default=False,help="Plot molecular profiles",action='store_true')
    parser.add_argument("-t","--plot-tpprofile",dest="tpprofile",default=False,help="Plot Temperature profiles",action='store_true')
    parser.add_argument("-d","--plot-tau",dest="tau",default=False,help="Plot optical depth contribution",action="store_true")
    parser.add_argument("-s","--plot-spectrum",dest="spectrum",default=False,help="Plot spectrum",action='store_true')
    parser.add_argument("-c","--plot-contrib",dest="contrib",default=False,help="Plot contrib",action='store_true')
    parser.add_argument("-C","--full-contrib",dest="full_contrib",default=False,help="Plot detailed contribs",action="store_true")
    parser.add_argument("-2D","--plot-2D",dest="plot_2D",default=False,help="Plot 2D TP profiles",action="store_true")
    parser.add_argument("-rad", "--radius-factor", dest="r_factor", default=1., type=float, help="Radius factor. Should be between 0 and 1 (to make atmosphere bigger).")
    parser.add_argument("-a","--all",dest="all",default=False,help="Plot everythiong",action='store_true')
    parser.add_argument("-T","--title",dest="title",type=str,help="Title of plots")
    parser.add_argument("-o","--output-dir",dest="output_dir",type=str,required=True,help="output directory to store plots")
    parser.add_argument("-p","--prefix",dest="prefix",type=str,help="File prefix for outputs")
    parser.add_argument("-m","--color-map",dest="cmap",type=str,default="Paired",help="Matplotlib colormap to use")
    parser.add_argument("-R","--resolution",dest="resolution",type=float,default=None,help="Resolution to bin spectra to")
    parser.add_argument("-f","--fit-params",dest="select_params",nargs='+',type=str,default=None,help="Select fit params to plot in posteriors")
    parser.add_argument("-l","--legends",dest="legends",nargs='+',type=str,default=None,help="Set model name for legends")
    args=parser.parse_args()

    plot_xprofile = args.xprofile or args.all
    plot_tp_profile = args.tpprofile or args.all
    plot_spectrum = args.spectrum or args.all
    plot_contrib = args.contrib or args.all
    plot_fullcontrib = args.full_contrib or args.all
    plot_posteriors = args.posterior or args.all
    plot_tau = args.tau or args.all
    plot_2D = args.plot_2D or args.all

    if len(args.input_files) > 1:
        print("Plotting %s"%args.input_files)
        # Superimpose multiple plots
        plots = []
        if args.legends is None:
            args.legends = args.input_files
        for idx, file in enumerate(args.input_files):
            plot=Plotter(file,cmap=args.cmap, save=True,
                        title=args.title,prefix=args.prefix,out_folder=args.output_dir,select_params=args.select_params, legend=args.legends[idx])
            plots.append(plot)

        comparison = Comparison(plots,cmap=args.cmap,
                        title=args.title,prefix=args.prefix,out_folder=args.output_dir)

        if plot_spectrum:
            if plot.is_retrieval:
                comparison.plot_fitted_spectrum(resolution=args.resolution)
            else:
                comparison.plot_forward_spectrum(resolution=args.resolution)

        if plot_posteriors:
            if plot.is_retrieval:
                comparison.plot_posteriors()

        return

    file = args.input_files[0] # only one plot
    plot=Plotter(file,cmap=args.cmap, save=True,
                    title=args.title,prefix=args.prefix,out_folder=args.output_dir, r_factor=args.r_factor)

    plot.plot_2D = plot_2D

    plot.slices = [0]
    if plot.plot_2D and plot.is2D:
        plot.slices = [0, 1, -1] # we don't know the size of the pressure_profile yet, so we will calculate the terminator index later

    if plot_posteriors:
        if plot.is_retrieval:
            plot.plot_posteriors()

    for slice_idx in plot.slices:
        plot.slice_idx = slice_idx
        if plot_xprofile:
            if plot.is_retrieval:
                plot.plot_fit_xprofile()
            else:
                plot.plot_forward_xprofile()
        if plot_tp_profile:
            if plot.is_retrieval:
                plot.plot_fitted_tp()
            else:
                plot.plot_forward_tp()
        if plot_tau:
            if plot.is_retrieval:
                plot.plot_fitted_tau()
            else:
                plot.plot_forward_tau()

    if plot_spectrum:
        if plot.is_retrieval:
            plot.plot_fitted_spectrum(resolution=args.resolution)
        else:
            plot.plot_forward_spectrum(resolution=args.resolution)
    if plot_contrib:
        if plot.is_retrieval:
            plot.plot_fitted_contrib(full=plot_fullcontrib,resolution=args.resolution)
        else:
            plot.plot_forward_contrib(full=plot_fullcontrib,resolution=args.resolution)
    if plot_2D:
        plot.plot_2Dmaps()

if __name__ == "__main__":
    main()





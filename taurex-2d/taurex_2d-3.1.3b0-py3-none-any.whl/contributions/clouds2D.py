from taurex.contributions import Contribution
from taurex_2d.contributions.contribution import SimpleContribution
import numpy as np
from taurex.core import fitparam


class Clouds2DContribution(SimpleContribution, Contribution):
    """
    Optically thick cloud deck up to a certain height, based on a pressure on the day side and another on the night side, with a linear transition between the two.
    NOT TESTED. USE AT YOUR OWN RISK

    These have the form:

    .. math::
            \\tau(\\lambda,z) =
                \\begin{cases}
                \\infty       & \\quad \\text{if } P(z) >= P_{a}\\\\
                0            & \\quad \\text{if } P(z) < P_{a}
                \\end{cases}

    Where :math:`P_{a}` is the pressure at the top of the cloud-deck within slice a


    Parameters
    ----------
    clouds_day_pressure: float
        Pressure at top of cloud deck on day side

    clouds_night_pressure: float
        Pressure at top of cloud deck on night side

    """
    def __init__(self, clouds_day_pressure=1e3, clouds_night_pressure=1e3):
        super().__init__('Clouds2D')
        self._cloud_day_pressure = clouds_day_pressure
        self._cloud_night_pressure = clouds_night_pressure

    @property
    def order(self):
        return 3

    def contribute(self, model, start_layer, end_layer, density_offset, layer,
                   density, tau, path_length=None):
        if (self.sigma_xsec.ndim == 3): #2D model
            for a in range(self.sigma_xsec.shape[0]):
                tau[layer] += self.sigma_xsec[a,layer, :]
        else:
            tau[layer] += self.sigma_xsec[layer, :]

    def prepare_each(self, model, wngrid):
        """
        Returns an absorbing cross-section that is infinitely absorbing
        up to a certain height

        Parameters
        ----------
        model: :class:`~taurex.model.model.ForwardModel`
            Forward model

        wngrid: :obj:`array`
            Wavenumber grid

        Yields
        ------
        component: :obj:`tuple` of type (str, :obj:`array`)
            ``Clouds`` and opacity array.
        """

        contrib = np.zeros(shape=(model.pressureProfile.shape+wngrid.shape))
        cloud_pressure = np.zeros(shape=(model.pressureProfile.shape[0]))
        angles = model.alpha*np.arange(model.nslices-2)-model.beta/2+model.alpha/2

        cloud_pressure[0] = self.cloudsNightPressure
        cloud_pressure[-1] = self.cloudsDayPressure

        # Interpolation between day and night
        if model.beta != 0:
            cloud_pressure[1:-1] = self.cloudsNightPressure + (self.cloudsDayPressure - self.cloudsNightPressure) * (angles / model.beta + 1/2)


        cloud_filtr = model.pressureProfile >= cloud_pressure[:,None]
        contrib[cloud_filtr, :] = np.inf
        self._contrib = contrib
        yield 'Clouds', self._contrib

    @fitparam(param_name='clouds_day_pressure',
              param_latex='$Pday_\mathrm{clouds}$',
              default_mode='log',
              default_fit=False, default_bounds=[1e-3, 1e6])
    def cloudsDayPressure(self):
        """
        Cloud day top pressure in Pascal
        """
        return self._cloud_day_pressure

    @cloudsDayPressure.setter
    def cloudsDayPressure(self, value):
        self._cloud_day_pressure = value

    @fitparam(param_name='clouds_night_pressure',
              param_latex='$Pnight_\mathrm{clouds}$',
              default_mode='log',
              default_fit=False, default_bounds=[1e-3, 1e6])
    def cloudsNightPressure(self):
        """
        Cloud night top pressure in Pascal
        """
        return self._cloud_night_pressure

    @cloudsNightPressure.setter
    def cloudsNightPressure(self, value):
        self._cloud_night_pressure = value

    def write(self, output):
        contrib = super().write(output)
        contrib.write_scalar('clouds_day_pressure', self._cloud_day_pressure)
        contrib.write_scalar('clouds_night_pressure', self._cloud_night_pressure)
        return contrib

    @classmethod
    def input_keywords(self):
        return ['Clouds2D']
"""
Various one-off functions that are imported to the trm.utils
top level.
"""

import numpy as np
from scipy import interpolate
from scipy.optimize import brentq

from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation
import astropy.units as u

__all__ = (
    'centroid', 'splfit', 'style_mpl_axes',
    'timcorr'
)

def centroid(xpos, fwhm, y, emission, e=None, nmax=None):
    """computes weighted centroid(s) of a feature(s) in a 1D array.

    The centroid(s) is(are) located by locating the maximum after
    cross-correlation with a gaussian. The positions are returned in
    terms of pixels with the centre of the first pixel marking 0.0.

    Arguments::

      xpos : float|array-like
         initial position(s), with centre of the first pixel defined
         as 0.0. This(these) must initially be within the range 1 to
         length-2, i.e. more than 1 from either end of the part of the
         array being looked at (see `nmax`). The routine fails if it
         cannot locate an extremum of the cross-correlation within
         3*fwhm from this position at the most.

      fwhm : float
         the full width at half maximum in pixels of the gaussian
         which must be > 0, and should probably be at least 2
         pixels. Values comparable to the widths of features are a
         start.

      emission : bool
         True for positive features (peaks), False for negative
         features (troughs).  (Emission / absorption in astronomical
         parlance)

      y : array
         values containing the feature(s) to be centroided. Need at
         lest 3 pixels.

      e : array|None
         1-sigma uncertainties on the y values. Used to estimate the
         uncertainty in the centroids.

      nmax : int|None
         if not None, then only the part of the array from round(xpos)-nmax to
         round(xpos)+nmax will be used.

    Returns:

      (xcen,xerr) or xcen if xpos is a single value, or a list of
      (xcen,xerr) or xcen values if xpos is a list. xerr values only
      returned if the array e is supplied.

    Raises ValueError exceptions if there are problems with the inputs
    or if it fails to determine the centroid for any input position.

    """

    # check inputs
    if len(y) < 3:
        raise ValueError('length of y array < 3')
    if fwhm < 2:
        raise ValueError(f'fwhm = {fwhm} < 2')
    if e is not None and len(e) != len(y):
        raise ValueError('length of e array does not match the y array')
    if nmax is not None and nmax < 1:
        raise ValueError('nmax must be None or > 0')

    def comperr(xd, y, e, sigma):
        """Computes uncertainty in final position from median"""
        xdsq = np.power(xd,2)
        vc   = np.sum(xdsq*np.exp(-xdsq)*np.power(e,2))
        ddc  = np.sum(y*(xdsq-1)*np.exp(-xdsq/2))
        return sigma*np.sqrt(vc)/abs(ddc)

    def dcorr(xd, y):
        """Returns the derivative of correlation with gaussian. We want
        this to be zero.

        xd -- xd offsets from centre of gaussian, scaled by sigma
        y  -- the corresponding y values
        """
        return np.sum(y*xd*np.exp(-np.power(xd,2)/2))

    def bfunc(xpos, x, y, sigma):
        """Function for the root finder brentq"""
        return dcorr((x - xpos)/sigma, y)

    # OK, let's start.
    sigma = fwhm/2.3548

    # pixel centre values
    x = np.arange(len(y),dtype=float)

    if not isinstance(xpos, list):
        xpos = list(xpos)

    vals = []
    for xp in xpos:
        if xp < 1.0 or xp > len(y)-2:
            raise ValueError(f'xpos = {xp} is out of range 1 to {len(y)-2}')

        if nmax is None:
            # full array
             n1, n2 = 0, len(y)
        else:
            # sub array
            ixp = round(xp)
            n1 = max(0,ixp-nmax)
            n2 = min(len(y),ixp+nmax+1)

        # sub-arrays
        xsub = x[n1:n2]
        ysub = y[n1:n2]
        if e is not None:
            esub = e[n1:n2]

        # compute derivative of x-corr
        xd = (xsub - xp)/sigma
        dc1 = dcorr(xd, ysub)

        if dc1 == 0:
            # unlikely, but xpos might be
            # correct from the off
            if e is None:
                vals.append(xpos)
                xerr = None
            else:
                xerr = comperr(xd, ysub, esub, sigma)
                vals.append((xpos,xerr))
            continue

        # Usual case: try to bracket the peak by looking for closest
        # switch in sign of the derivative of the x-corr.
        x1 = xp
        x2 = xp
        dc2 = dc1
        found_switch = False

        # move in direction defined by sign of gradient.
        if (dc1 > 0.0 and emission) or (dc1 < 0.0 and not emission):
            cshift =  0.25
        else:
            cshift = -0.25

        shift = cshift
        done = False
        while abs(shift) <= 3.0:
            x2 = xp + fwhm*shift
            xd = (xsub - x2)/sigma
            dc2 = dcorr(xd, ysub)
            if dc2 == 0:
                if e is None:
                    vals.append(x2)
                else:
                    xerr = comperr(xd, ysub, esub, sigma)
                    vals.append((x2,xerr))
                done = True
                break

            if (dc1 > 0 and dc2 < 0) or (dc1 < 0 and dc2 > 0):
                found_switch = True
                break
            shift += cshift

        if done:
            # lucked out
            continue

        if not found_switch:
            raise ValueError(
                f'could not find peak within 3*fwhm of initial position xpos = {xp}'
            )

        # reorder if necessary
        if x1 > x2:
            x1,x2 = x2,x1
            dc1,dc2 = dc2,dc1

        if x1 < n1 or x2 < n1+1 or x1 > n2-2 or x2 > n2-1:
            raise ValueError(
                f'bracketting limits = {x1},{x2} out of ranges {n1}--{n2-2}, {n1+1}--{n2-1}.'
            )

        # now find root using Brent's method
        xm,r = brentq(bfunc, x1, x2, args=(xsub,ysub,sigma), full_output=True)
        if not r.converged:
            raise ValueError('brentq failed to converge')

        if e is not None:
            xd = (xsub - xm)/sigma
            xerr = comperr(xd, ysub, esub, sigma)
            vals.append((xm,xerr))
        else:
            vals.append(xm)

    if len(vals) > 1:
        return vals
    else:
        return vals[0]

def splfit(x, y, ye, nspline, thresh, slow=True):
    """This uses scipy.interpolate to fit a cubic spline to data with
    rejection.  The spline knots are regularly spaced in x and
    rejection cycles are used to kick out points more than thresh
    sigma away from the fit, one at a time.

    Arguments::

       x : array
         the X values

       y : array
         the Y values

       ye : array
         uncertainties in Y, used to weight fit. Any points with
         ye <= 0 are ignored.

       nspline : int
         the number of splines

       thresh : float
         the rejection threshold i.e. number of RMS to use.

       slow : bool
         True for worst-point-at-a-time rejection (secure, but slow);
         False for lots

    Returns (sfit,nrej,rms,ok,sp)::

       sfit : array
         the final fit

       nrej : int
         number of points rejected

       rms : float
         RMS of sigma-normalised residuals (i.e. = 1 in ideal case
         where scatter matches errors)

       ok : array (boolean)
         a mask to show which points were used in the final fit.
         True = point was used

       sp : tuple
         final spline fitted, as returned by scipy.interpolate.splrep
         See that for more details.

    """

    ok   = ye > 0.
    nrej = 1

    while nrej:

        xg  = x[ok]
        yg  = y[ok]
        yeg = ye[ok]

        # space knots (which must be interior knots)
        knots   = np.arange(xg[0], xg[-1], (xg[-1]-xg[0])/nspline)[1:]

        # Fit the spline
        sp = interpolate.splrep(xg, yg, 1./yeg, task=-1, t=knots)

        # Calculate the fit (to all points)
        sfit = interpolate.splev(x, sp)

        resid = np.abs((y - sfit)/ye)
        rms = np.sqrt((resid[ok]**2).sum()/(len(yg)-nspline))

        if slow:
            worst = resid[ok].max()
            if worst > rms*thresh:
                ok = ok & (resid != worst)
                nrej = 1
            else:
                nrej = 0
        else:
            nok = len(yg)
            ok  = ok & (resid < rms*thresh)
            nnok = len(y[ok])
            nrej = nok - nnok

    nrej = len(x) - len(x[ok])
    return (sfit,nrej,rms,ok,sp)

def style_mpl_axes(axes):
    """I don't like the default matplotlib axes as I prefer to have ticks
    marks going into the axes, and for all 4 axes to have them (PGPLOT
    style). This routine applies fixes to accomplish this.

    Arguments::

      axes : :class:`~matplotlib.axes.Axes`
         the Axes object which will be updated.

    """
    axes.tick_params(axis="x", direction="in")
    axes.tick_params(axis="y", direction="in")
    axes.tick_params(bottom=True, top=True, left=True, right=True)

def timcorr(ts, position, telescope, intime="MJD(UTC)", outime="BMJD(TDB)"):
    """Applies time conversions (e.g. UTC to TDB) and light travel time
    corrections (e.g. to heliocentre or barycentre) to a set of times.


    Arguments::

        ts : array
           the times, in days. Multiple different formats
           accepted. See `intime`.

        position : str | astropy.coordinates.SkyCoord
          RA/Dec string (hours/degrees e.g. "20:23:04,5
          -00:02:56.3") suitable for creating an
          astropy.coordinates.SkyCoord object, or a pre-built SkyCoord

        telescope : str | astropy.coordinates.EarthLocation
          string recognised for creating an
          astropy.coordinates.EarthLocation object, or a pre-built
          EarthLocation. Examples: 'lapalma', 'paranal'.

        intime : str
          type of input time. Possibilities::

            JD(UTC) : Julian Day, UTC time.
            MJD(UTC) : Modified Julian Day, UTC time.

        outime : str
          type of time returned. Possibilities::

            BMJD(TDB) : Barycentric MJD, TDB time.
            BJD(TDB) : Barycentric JD, TDB time.

    """
    INTIMES = ('JD(UTC)', 'MJD(UTC)',)
    if intime not in INTIMES:
        raise ValueError(
            f'intime = {intime} not recognised.\n'
            'Possible values = {INTIMES}'
        )
    OUTIMES = ('BMJD(TDB)','BJD(TDB)',)
    if outime not in OUTIMES:
        raise ValueError(
            f'outime = {outime} not recognised.\n'
            'Possible values = {OUTIMES}'
        )

    if not isinstance(position, SkyCoord):
        position = SkyCoord(position, unit=(u.hourangle, u.deg))

    if not isinstance(telescope, EarthLocation):
        telescope = EarthLocation.of_site(telescope)
        
    if intime == 'JD(UTC)' or intime == 'HJD(UTC)':
        times = Time(ts, format='jd', scale='utc', location=telescope)
    elif intime == 'MJD(UTC)' or intime == 'HMJD(UTC)':
        times = Time(ts, format='mjd', scale='utc', location=telescope)

    if intime.startswith('H'):
        # heliocentric correction: subtract to get UTC times
        ltt_helio = times.light_travel_time(
            position, kind='heliocentric'
        )
        times = times - ltt_helio

    if outime == 'BMJD(TDB)':
        # Barycentric correction: add to get to barycentre
        ltt_bary = times.light_travel_time(
            position, kind='barycentric'
        )
        times = (times.tdb + ltt_bary).mjd
        
    elif outime == 'BJD(TDB)':
        # Barycentric correction: add to get to barycentre
        ltt_bary = times.light_travel_time(
            position, kind='barycentric'
        )
        times = (times.tdb + ltt_bary).jd

    return times


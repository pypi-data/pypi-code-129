class ApplyZernike(eqx.Module):
    """
    NEW DOCTRING:
        TO DO
        
    OLD DOCSTRING:
    Adds an array of phase values to the input wavefront calculated from the OPD
     
    Parameters
    ----------
    nterms: int, equinox.static_field
        The number of zernike terms to apply, ignoring the first two radial
        terms: Piston, Tip, Tilt
        
    basis: jax.numpy.ndarray, equinox.static_field
        Arrays holding the pre-calculated zernike basis terms
        
    coefficients: jax.numpy.ndarray
        Array of shape (nterns) of coefficients to be applied to each 
        Zernike term
    """
    npix: int = eqx.static_field()
    names: list = eqx.static_field()
    basis: np.ndarray = eqx.static_field()
    coefficients: np.ndarray
    
    def __init__(self, npix, coefficients, indexes=None):
        self.npix = int(npix)
        self.coefficients = np.array(coefficients)
        
        # Load basis
        indexes = np.arange(len(coefficients)) if indexes is None else indexes
        
        # Check indexes
        if np.max(indexes) >= 22:
            raise ValueError("Zernike indexes above 22 not currently supported")
            
        # Get full basis
        full_basis = np.array(np.nan_to_num(
                zernike_basis(nterms=np.max(indexes)+1, npix=int(npix))))
        
        # Get basis
        self.basis = np.array([full_basis[indx] for indx in indexes])
        
        # Names - Helper
        all_names = ['Piston', 'Tilt X', 'Tilt Y',
                     'Focus', 'Astigmatism 45', 'Astigmatism 0',
                     'Coma Y', 'Coma X',
                     'Trefoil Y', 'Trefoil X',
                     'Spherical', '2nd Astig 0', '2nd Astig 45',
                     'Tetrafoil 0', 'Tetrafoil 22.5',
                     '2nd coma X', '2nd coma Y', '3rd Astig X', '3rd Astig Y',
                     'Pentafoil X', 'Pentafoil Y', '5th order spherical']
        
        # Load in names
        self.names = [all_names[indx] for indx in indexes]

    def __call__(self, params_dict):
        """
        
        """
        # Get relevant parameters
        WF = params_dict["Wavefront"]
        wavefront = WF.wavefront
        wavel = WF.wavel

        # Get zernike phase
        zernike_opd = self.get_opd(self.basis, self.coefficients)
        zernike_phase = self.opd_to_phase(zernike_opd, wavel)
        
        # Add phase to wavefront
        phase_out = np.angle(wavefront) + zernike_phase
        
        # Recombine into wavefront
        wavefront_out = np.abs(wavefront) * np.exp(1j*phase_out)

        # Update Wavefront Object
        WF = eqx.tree_at(lambda WF: WF.wavefront,  WF, wavefront_out)
        params_dict["Wavefront"] = WF
        return params_dict
    
    def opd_to_phase(self, opd, wavel):
        """
        
        """
        return 2*np.pi*opd/wavel
    
    def get_opd(self, basis, coefficients):
        """
        
        """
        return np.dot(basis.T, coefficients)
    
    
class Interpolator(eqx.Module):
    """
    
    """
    npix_out: int = eqx.static_field()
    pixelscale_out: float
    
    def __init__(self, npix_out, pixelscale_out):
        self.npix_out = int(npix_out)
        self.pixelscale_out = np.array(pixelscale_out).astype(float)

    def __call__(self, params_dict):
        """
        NOTE: Poppy pads all arrays by 2 pixels before interpolating to reduce 
        edge effects - We will not do that here, chosing instead to have
        all layers as minimal as possible, and have guidelines around best 
        practice to get the best results
        """
        # Get relevant parameters
        WF = params_dict["Wavefront"]
        wavefront = WF.wavefront
        pixelscale = WF.pixelscale
        
        # Get coords arrays
        npix_in = wavefront.shape[0]
        xs_in = pixelscale * np.arange(-npix_in//2, npix_in//2, dtype=float)
        xs_out = np.arange(-self.npix_out//2, self.npix_out//2, dtype=float)
        
        XX, YY = np.meshgrid(xs_out, xs_out)
        XX_out = (self.pixelscale_out * XX).flatten()
        YY_out = (self.pixelscale_out * YY).flatten()
        
        # Interp Mag and Phase
        mag = interp2d(XX_out, YY_out, xs_in, xs_in, 
                    np.abs(wavefront)).reshape([self.npix_out, self.npix_out])
        phase = interp2d(XX_out, YY_out, xs_in, xs_in, 
                 np.angle(wavefront)).reshape([self.npix_out, self.npix_out])
        
        # Recombine
        wavefront_out = mag * np.exp(1j*phase)
        
        # Enforce conservation of energy:
        pixscale_ratio = pixelscale / self.pixelscale_out
        wavefront_out *= 1. / pixscale_ratio
        
        # Update Wavefront Object
        WF = eqx.tree_at(lambda WF: WF.wavefront,  WF, wavefront_out)
        WF = eqx.tree_at(lambda WF: WF.pixelscale, WF, self.pixelscale_out)
        params_dict["Wavefront"] = WF
        return params_dict
    
    
    
class Interpolator(eqx.Module):
    """
    Note this has strange behvaiour with hessian calcuations (gives nans)
    """
    npix_out: int = eqx.static_field()
    pixelscale_out: float
    
    def __init__(self, npix_out, pixelscale_out):
        self.npix_out = int(npix_out)
        self.pixelscale_out = np.array(pixelscale_out).astype(float)

    def __call__(self, params_dict):
        """
        NOTE: Poppy pads all arrays by 2 pixels before interpolating to reduce 
        edge effects - We will not do that here, chosing instead to have
        all layers as minimal as possible, and have guidelines around best 
        practice to get the best results
        """
        # Get relevant parameters
        WF = params_dict["Wavefront"]
        wavefront = WF.wavefront
        pixelscale = WF.pixelscale
        
        # Get coords arrays
        npix_in = wavefront.shape[0]
        ratio = self.pixelscale_out/pixelscale
        shift = (npix_in - ratio*self.npix_out)/2
        xs = ratio*(np.arange(self.npix_out)) + shift
        YY, XX = np.meshgrid(xs, xs)
        coords = np.array([XX, YY])
        
        # Interp mag and phase
        mag   = map_coordinates(np.abs(wavefront),   coords, order=1)
        phase = map_coordinates(np.angle(wavefront), coords, order=1)
        
        # Recombine
        wavefront_out = mag * np.exp(1j*phase)
        
        # Enforce conservation of energy:
        pixscale_ratio = pixelscale / self.pixelscale_out
        wavefront_out *= 1. / pixscale_ratio
        
        # Update Wavefront Object
        WF = eqx.tree_at(lambda WF: WF.wavefront,  WF, wavefront_out)
        WF = eqx.tree_at(lambda WF: WF.pixelscale, WF, self.pixelscale_out)
        params_dict["Wavefront"] = WF
        return params_dict